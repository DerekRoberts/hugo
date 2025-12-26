# MetaCurious Website

Hugo-based website for MetaCurious, coaching emerging leaders for more equitable communities.

## Overview

This site is built with [Hugo](https://gohugo.io/), a fast static site generator, and automatically deploys to GitHub Pages when changes are pushed to the `main` branch.

## Quick Start

### Viewing the Site

The live site is available at: `https://derekroberts.github.io/hugo/`

### Making Content Changes

Content files are in the `content/` directory:
- `content/_index.md` - Homepage
- `content/about-the-coach.md` - About page
- `content/services.md` - Services page
- `content/contact.md` - Contact page

Simply edit these Markdown files and push changes. The site will automatically rebuild and deploy.

### Adding New Content

```bash
# Create a new page
hugo new content/my-page.md

# Create a new blog post (if blog section exists)
hugo new content/blog/my-post.md
```

## Contact Form Setup

The contact form requires a Formspree endpoint to be configured.

📋 **Quick Setup Guide**: [SETUP_CONTACT_FORM.md](SETUP_CONTACT_FORM.md)

## Local Development

To preview changes locally before pushing:

### Prerequisites

- [Hugo v0.146.0 or higher](https://gohugo.io/installation/) (extended version required)

### Running Locally

```bash
# Install theme dependencies (first time only)
git submodule update --init --recursive

# Start local server with live reload
hugo server -D

# Site will be available at http://localhost:1313/
```

### Building for Production

```bash
# Build the site
hugo --minify
```

The built site will be in the `public/` directory (this directory is git-ignored).

## Site Structure

- `content/` - Markdown content files (edit these to update site content)
- `layouts/` - HTML templates (custom styling and structure)
- `static/` - Static assets (images, favicon)
- `assets/` - CSS and other processed assets
- `hugo.toml` - Site configuration (title, menu, theme settings)
- `themes/PaperMod/` - Hugo theme (via git submodule)

## Theme

This site uses the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, which provides:
- Clean, minimalist design
- Dark/light mode toggle
- Mobile-responsive layout
- Fast performance

## Deployment

Deployment is automatic via GitHub Actions:
- Push changes to `main` branch
- GitHub Actions builds and deploys to GitHub Pages
- Site updates within 1-2 minutes

No manual deployment steps required.

## License

Apache License 2.0 - See LICENSE file for details
