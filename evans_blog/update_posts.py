import os
import re

def extract_h1_from_markdown(file_path):
    """Extract the first H1 heading from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Look for the first # heading (H1)
        match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        # Fallback to filename
        return os.path.basename(file_path).replace('.md', '').replace('_', ' ').title()
    except Exception as e:
        print(f"Error extracting title from {file_path}: {e}")
        return os.path.basename(file_path).replace('.md', '').replace('_', ' ').title()

def update_blog_js():
    """Update blog.js with titles from the first H1 in each Markdown file."""
    posts_dir = 'posts'
    blog_js_path = 'blog.js'
    
    # Scan the posts directory for markdown files
    posts = []
    
    for filename in sorted(os.listdir(posts_dir)):
        if filename.endswith('.md'):
            file_path = os.path.join(posts_dir, filename)
            
            # Special case for genasys.md - keep custom title
            if filename == 'genasys.md':
                title = 'Have you heard about our painfully loud speaker as a service?'
            else:
                # Extract title from Markdown H1
                title = extract_h1_from_markdown(file_path)
                print(f"Found title in {filename}: {title}")
            
            # Create entry for this post
            posts.append({
                'title': title,
                'file': f'posts/{filename}'
            })
    
    # Create posts array text
    posts_str = []
    for post in posts:
        escaped_title = post['title'].replace("'", "\\'")
        posts_str.append(f"    {{ title: '{escaped_title}', file: '{post['file']}' }}")
    
    posts_text = ',\n'.join(posts_str)
    
    # Read the current blog.js file
    with open(blog_js_path, 'r') as file:
        content = file.read()
    
    # Replace only the posts array using regex
    pattern = r'const posts = \[\s*\{.*?\}\s*\];'
    replacement = f"const posts = [\n{posts_text}\n  ];"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write the updated content back to blog.js
    with open(blog_js_path, 'w') as file:
        file.write(new_content)
    
    print(f"Updated blog.js with {len(posts)} posts.")

if __name__ == "__main__":
    update_blog_js()
