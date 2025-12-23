# GitHub Pages Setup Instructions

This document describes the steps needed to enable GitHub Pages deployment for this Hugo site.

## ⚠️ IMPORTANT: GitHub Pages Must Be Enabled

**The site will NOT be accessible until GitHub Pages is enabled in the repository settings!**

The GitHub Actions workflow will fail with an error at the "Setup Pages" step if GitHub Pages is not enabled. You must complete the setup steps below before the site can be deployed.

## Steps to Enable GitHub Pages

1. **Go to Repository Settings**
   - Navigate to the repository on GitHub
   - Click on "Settings" tab

2. **Configure GitHub Pages**
   - In the left sidebar, click on "Pages"
   - Under "Source", select "GitHub Actions"
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

## Important Notes

- The workflow requires GitHub Pages to be enabled with "GitHub Actions" as the source
- The first deployment may take a few minutes
- Subsequent deployments are triggered automatically on push to main branch
- The workflow uses Hugo v0.146.0 (extended version)

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
