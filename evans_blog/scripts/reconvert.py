import os
import re
from bs4 import BeautifulSoup
import html

def clean_text(text):
    """Clean text by replacing common HTML entities."""
    if text:
        text = html.unescape(text)
        text = text.replace('\xa0', ' ')  # Replace non-breaking spaces
    return text

def html_to_markdown(html_content):
    """Convert HTML to Markdown."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract text and apply markdown formatting
    markdown_lines = []
    
    # Process headings, paragraphs, links, and lists
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'a', 'strong', 'em', 'blockquote']):
        if element.name == 'h1':
            markdown_lines.append(f"# {clean_text(element.get_text().strip())}\n")
        elif element.name == 'h2':
            markdown_lines.append(f"## {clean_text(element.get_text().strip())}\n")
        elif element.name == 'h3':
            markdown_lines.append(f"## {clean_text(element.get_text().strip())}\n")  # Note: h3 becomes h2 as requested
        elif element.name == 'h4':
            markdown_lines.append(f"## {clean_text(element.get_text().strip())}\n")  # Note: h4 becomes h2 as requested
        elif element.name == 'h5':
            markdown_lines.append(f"## {clean_text(element.get_text().strip())}\n")  # Note: h5 becomes h2 as requested
        elif element.name == 'h6':
            markdown_lines.append(f"## {clean_text(element.get_text().strip())}\n")  # Note: h6 becomes h2 as requested
        elif element.name == 'p' and element.parent.name not in ['li']:
            # Process links within paragraphs
            content = process_links_and_formatting(element)
            if content.strip():
                markdown_lines.append(f"{content}\n\n")
        elif element.name == 'ul' and element.parent.name not in ['li']:
            # Skip ul here, we'll process li elements individually
            pass
        elif element.name == 'ol' and element.parent.name not in ['li']:
            # Skip ol here, we'll process li elements individually
            pass
        elif element.name == 'li':
            # For list items, check if parent is ol or ul
            content = process_links_and_formatting(element)
            
            if element.parent.name == 'ol':
                # Use 1. for ordered lists
                markdown_lines.append(f"1. {content}\n")
            else:
                # Use - for unordered lists
                markdown_lines.append(f"- {content}\n")
        elif element.name == 'blockquote' and element.parent.name not in ['li', 'blockquote']:
            content = process_links_and_formatting(element)
            markdown_lines.append(f"> {content}\n\n")
            
    return '\n'.join(markdown_lines)

def process_links_and_formatting(element):
    """Process links and formatting within an element."""
    result = ""
    
    # Process the element's children
    for child in element.children:
        if child.name == 'a':
            # Handle links
            href = child.get('href', '')
            text = clean_text(child.get_text().strip())
            result += f"[{text}]({href})"
        elif child.name == 'strong' or child.name == 'b':
            # Handle bold text
            text = clean_text(child.get_text().strip())
            result += f"**{text}**"
        elif child.name == 'em' or child.name == 'i':
            # Handle italic text
            text = clean_text(child.get_text().strip())
            result += f"*{text}*"
        elif child.name is None:
            # Plain text
            result += clean_text(child.string) if child.string else ""
        elif isinstance(child, str):
            # Plain text (another case)
            result += clean_text(child)
        else:
            # Recursively process nested elements
            result += process_links_and_formatting(child)
    
    return result

def convert_file(html_file_path, md_file_path):
    """Convert an HTML file to Markdown and save it."""
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Extract title for H1 if not present
    soup = BeautifulSoup(html_content, 'html.parser')
    h1 = soup.find('h1')
    
    markdown_content = html_to_markdown(html_content)
    
    # If no h1 was found in the content, create a title from filename
    if not h1 and not markdown_content.strip().startswith("# "):
        title = os.path.basename(html_file_path).replace('.html', '').replace('_', ' ').title()
        markdown_content = f"# {title}\n\n{markdown_content}"
    
    # Save markdown content
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    
    print(f"Converted {html_file_path} to {md_file_path}")

def convert_all_html_files():
    """Convert all HTML files in the html_files directory to Markdown."""
    html_dir = 'html_files'
    md_dir = 'posts'
    
    # Create the markdown directory if it doesn't exist
    os.makedirs(md_dir, exist_ok=True)
    
    for filename in os.listdir(html_dir):
        if filename.endswith('.html'):
            html_file_path = os.path.join(html_dir, filename)
            md_file_path = os.path.join(md_dir, filename.replace('.html', '.md'))
            convert_file(html_file_path, md_file_path)

if __name__ == "__main__":
    convert_all_html_files()
    print("Conversion complete!")
    
    # After conversion, run the update_posts.py script to update blog.js with H1 titles
    print("Updating blog.js with post titles...")
    os.system('python update_posts.py')
    print("Done!")
