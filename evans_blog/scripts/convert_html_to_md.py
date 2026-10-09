#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup
import html
import glob
import sys

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
            markdown_lines.append(f"### {clean_text(element.get_text().strip())}\n")
        elif element.name == 'h4':
            markdown_lines.append(f"#### {clean_text(element.get_text().strip())}\n")
        elif element.name == 'h5':
            markdown_lines.append(f"##### {clean_text(element.get_text().strip())}\n")
        elif element.name == 'h6':
            markdown_lines.append(f"###### {clean_text(element.get_text().strip())}\n")
        elif element.name == 'p' and element.parent.name not in ['li']:
            # Process links within paragraphs
            content = process_links_and_formatting(element)
            if content.strip():
                markdown_lines.append(f"{content}\n")
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
            markdown_lines.append(f"> {content}\n")
            
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
    
    return result

def convert_file(html_file_path, md_file_path):
    """Convert an HTML file to Markdown and save it."""
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Extract title for H1
    match = re.search(r'<title>(.*?)</title>', html_content)
    title = match.group(1) if match else os.path.basename(html_file_path).replace('.html', '')
    
    # If title is not in the content, add it as H1
    markdown_content = html_to_markdown(html_content)
    if not markdown_content.strip().startswith('# '):
        markdown_content = f"# {title}\n\n{markdown_content}"
    
    # Save markdown content
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    
    print(f"Converted {html_file_path} to {md_file_path}")

def convert_all_html_files(directory):
    """Convert all HTML files in the directory to Markdown."""
    posts_dir = os.path.join(directory, 'posts')
    
    # Create the markdown directory if it doesn't exist
    os.makedirs(posts_dir, exist_ok=True)
    
    # Get all HTML files except index.html
    html_files = glob.glob(os.path.join(directory, '*.html'))
    html_files = [f for f in html_files if os.path.basename(f) != 'index.html']
    
    for html_file in html_files:
        base_name = os.path.basename(html_file)
        md_file = os.path.join(posts_dir, base_name.replace('.html', '.md'))
        convert_file(html_file, md_file)

if __name__ == "__main__":
    import glob
    import sys
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()
    
    convert_all_html_files(directory)
    print("Conversion complete!")
