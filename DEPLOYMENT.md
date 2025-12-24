# GitHub Pages Setup Instructions

This document describes the steps needed to enable GitHub Pages deployment for this Hugo site, including PR preview deployments.

## Steps to Enable GitHub Pages

1. **Go to Repository Settings**
   - Navigate to the repository on GitHub
   - Click on "Settings" tab

2. **Configure GitHub Pages**
   - In the left sidebar, click on "Pages"
   - Under "Source", select "Deploy from a branch"
   - Select the "gh-pages" branch and "/" (root) folder
   - Save the configuration

3. **Trigger First Deployment**
   - The workflow is configured to run on:
     - Push to `main` branch
     - Manual trigger via "workflow_dispatch"
   
   - To manually trigger (if needed):
     - Go to "Actions" tab
     - Select "Deploy Hugo site to GitHub Pages" workflow
     - Click "Run workflow"

4. **Access Your Site**
   - Once deployed, the site will be available at:
     - `https://<username>.github.io/<repository>/`
     - For this repository: `https://derekroberts.github.io/hugo/`

## PR Preview Deployments

This repository includes automatic PR preview deployments. When you open a pull request:

1. **Automatic Build & Deploy**
   - The workflow automatically builds the Hugo site with your PR changes
   - Deploys the preview to a PR-specific path: `/pr-{number}/`
   - Posts a comment on the PR with the preview URL

2. **Preview URL Format**
   - `https://<username>.github.io/<repository>/pr-<PR_NUMBER>/`
   - Example: `https://derekroberts.github.io/hugo/pr-5/`

3. **Automatic Updates**
   - The preview is automatically updated whenever you push new commits to the PR
   - The existing PR comment is updated (not duplicated)

4. **Automatic Cleanup**
   - When the PR is closed or merged, the preview deployment is automatically removed
   - A cleanup comment is posted on the PR

### How It Works

- PR previews are deployed to the `gh-pages` branch in subdirectories
- Each PR gets its own isolated preview environment
- The main production site remains unaffected on the root path
- Previews are built with PR-specific baseURL for correct asset loading

## Important Notes

- The workflow requires GitHub Pages to be enabled with "gh-pages" branch as the source
- The first deployment may take a few minutes
- Subsequent deployments are triggered automatically on push to main branch
- The workflow uses Hugo v0.146.0 (extended version)
- PR previews require write permissions to the repository

## Custom Domain (Optional)

To use a custom domain like `metacurious.ca`:

1. Add a `CNAME` file in the `static/` directory with your domain
2. Configure DNS settings with your domain provider:
   - Add a CNAME record pointing to `<username>.github.io`
   - Or add A records pointing to GitHub Pages IPs
3. In GitHub repository settings → Pages, add your custom domain
4. Enable "Enforce HTTPS" (recommended)

## Merging to Main Branch

Once this pull request is merged to the `main` branch, the GitHub Actions workflow will automatically:
1. Build the Hugo site
2. Deploy to GitHub Pages
3. Make the site available at the configured URL

## Troubleshooting

If deployment fails:
- Check the Actions tab for error logs
- Ensure GitHub Pages is enabled in repository settings
- Verify the workflow file syntax is correct
- Make sure the repository has Pages enabled (may require public repository or GitHub Pro)
- For PR previews, ensure the workflow has write permissions to contents and pull requests
