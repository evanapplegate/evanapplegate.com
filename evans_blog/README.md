# Evans Blog

A simple flat-file blog system using Markdown files that can be deployed directly to GitHub Pages. Claude wrote all this so good luck maintaining it, Evan!

## Structure
- Markdown (.md) files in the `posts` directory contain individual blog posts
- HTML files in the `html_files` directory (original versions)
- Images in the `images` directory
- `index.html` provides navigation and displays posts
- `styles.css` contains all styling
- `blog.js` handles post loading and navigation

Last updated: 2025-04-05

## Adding New Posts
1. Create a new Markdown file in the `posts` directory (e.g., `new-post.md`)
2. Add your blog post content to the file using Markdown syntax
3. Use update_posts.py to add the new post to the posts array in `blog.js`

## Adding Images
1. Place your image files in the `images` directory
2. Reference them in your Markdown posts using:
   ```markdown
   ![Image description](/images/filename.jpg)
   ```
3. For more control (sizing, etc.), use HTML:
   ```html
   <img src="/images/filename.jpg" alt="Image description" width="500">
   ```

## GitHub Pages Deployment
1. Push this repository to GitHub
2. Go to repository settings > Pages
3. Select the main branch as the source
4. Your blog will be available at `https://[username].github.io/[repo-name]/`

## Local Development
You can test locally by running a simple HTTP server:

```bash
# Using Python
python -m http.server

# Or using Node.js
npx serve
```

## Markdown Reference
Basic Markdown syntax for your blog posts:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

[Link text](https://example.com)

- Bullet point
- Another bullet point

1. Numbered item
2. Another numbered item

![Image alt text](/images/image.jpg)

> Blockquote
