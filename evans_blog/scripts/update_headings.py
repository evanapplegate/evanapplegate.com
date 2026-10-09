import os
import re

def update_headings(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Check if the first line starts with one or more '#'
    lines = content.split('\n')
    if lines and re.match(r'^#{1,3}\s', lines[0]):
        # Replace the first heading with level 1 heading
        lines[0] = re.sub(r'^#{1,3}\s', '# ', lines[0])
        
        # Replace all other headings with level 2 headings
        for i in range(1, len(lines)):
            if re.match(r'^#{1,6}\s', lines[i]):
                lines[i] = re.sub(r'^#{1,6}\s', '## ', lines[i])
        
        # Join the lines back together
        updated_content = '\n'.join(lines)
        
        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)
        return True
    return False

def main():
    posts_dir = 'posts'
    updated_files = 0
    
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(posts_dir, filename)
            if update_headings(file_path):
                updated_files += 1
                print(f"Updated headings in {filename}")
    
    print(f"\nTotal files updated: {updated_files}")

if __name__ == "__main__":
    main()
