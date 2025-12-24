# Metacurious Hugo Site

This repository contains the Hugo-based website for Metacurious, migrated from Wix.

## Overview

Metacurious is now built with [Hugo](https://gohugo.io/), a fast and modern static site generator, and is hosted on [GitHub Pages](https://pages.github.com/).

## Site Structure

- `content/` - Markdown content files
- `layouts/` - Custom HTML templates
- `static/` - Static assets (images, CSS, JS)
- `themes/PaperMod/` - Hugo theme (via git submodule)
- `hugo.toml` - Hugo configuration file
- `.github/workflows/hugo.yml` - GitHub Actions workflow for deployment
- `.github/workflows/contact-form.yml` - GitHub Actions workflow for contact form emails

## Features

### Contact Form

The site includes a contact form at `/contact/` with the following features:
- Name, Email, and Message input fields
- Client-side form validation
- Multiple submission options (mailto fallback, optional GitHub Issues integration)
- Responsive design matching the site theme

For detailed setup instructions, see [CONTACT_FORM_SETUP.md](CONTACT_FORM_SETUP.md).

## Local Development

### Prerequisites

- Hugo v0.146.0 or higher (extended version)

### Build and Serve

```bash
# Build the site
hugo

# Serve locally with live reload
hugo server -D

# Build for production
hugo --minify
```

## Deployment

The site automatically deploys to GitHub Pages via GitHub Actions when changes are pushed to the `main` branch.

### Setup GitHub Pages

1. Go to repository Settings → Pages
2. Set Source to "GitHub Actions"
3. The workflow will automatically build and deploy on push to main

## Theme

This site uses the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, which provides:
- Clean, minimalist design
- Dark/light mode support
- Fast performance
- Mobile-responsive layout

## Content Management

Content is written in Markdown format. To add new content:

```bash
# Create a new blog post
hugo new content/blog/my-post.md

# Create a new page
hugo new content/my-page.md
```

## License

Apache License 2.0 - See LICENSE file for details

