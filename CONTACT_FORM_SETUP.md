# Contact Form Setup

The contact page includes a form that allows visitors to send messages. The form has two submission mechanisms:

## Current Implementation: mailto Fallback

The contact form currently uses a **mailto link** as its primary submission method. When a user clicks "Send the form":
1. The form attempts to create a GitHub issue (requires authentication)
2. If that fails, it falls back to opening the user's email client with pre-filled data
3. The form fields are cleared and a success message is displayed

This is a reliable, zero-configuration approach that works immediately.

## Optional: GitHub Issues + Email Workflow

For a more automated experience, you can configure the repository to automatically send emails when contact form submissions are received as GitHub issues.

### Prerequisites

To enable automated email sending, you need:
- A Gmail account (or other SMTP email service)
- GitHub repository with Issues enabled
- The following GitHub Secrets configured

### GitHub Secrets Configuration

Add the following secrets to your repository:

1. **`CONTACT_EMAIL`** - The email address where contact form submissions should be sent
   - Example: `info@metacurious.ca`

2. **`EMAIL_USERNAME`** - The email account username for SMTP authentication
   - For Gmail: your full email address (e.g., `your-email@gmail.com`)

3. **`EMAIL_PASSWORD`** - The email account password or app-specific password
   - For Gmail: Use an [App Password](https://support.google.com/accounts/answer/185833)
   - **Important**: For Gmail, you must use an App Password, not your regular password

### Setting Up GitHub Secrets

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret with its name and value
5. Save the secrets

### How It Works

The workflow in `.github/workflows/contact-form.yml`:

1. **Trigger**: Runs when a new issue is opened with the `contact-form` label
2. **Parse**: Extracts name, email, and message from the issue body
3. **Send Email**: Uses the configured SMTP server to send an email notification
4. **Close**: Closes the issue automatically after processing

### Gmail Configuration

If using Gmail, follow these steps:

1. **Enable 2-Step Verification**
   - Go to your Google Account settings
   - Security → 2-Step Verification → Turn On

2. **Create App Password**
   - Go to Security → 2-Step Verification → App passwords
   - Select "Mail" and "Other (Custom name)"
   - Name it "Hugo Contact Form"
   - Copy the 16-character password

3. **Add to GitHub Secrets**
   - Use this app password for `EMAIL_PASSWORD`
   - Use your full Gmail address for `EMAIL_USERNAME`

### Alternative: Using a Form Service

Instead of the GitHub Issues approach, you can use a third-party form service:

#### Option 1: Formspree

1. Sign up at [formspree.io](https://formspree.io)
2. Create a new form
3. Update the form's `action` attribute in `layouts/contact/single.html`:
   ```html
   <form id="contact-form" class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

#### Option 2: Web3Forms

1. Get a free access key at [web3forms.com](https://web3forms.com)
2. Add a hidden field to the form:
   ```html
   <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY">
   ```

#### Option 3: Netlify Forms

If deploying to Netlify, add the `netlify` attribute:
```html
<form id="contact-form" class="contact-form" netlify>
```

## Testing

To test the contact form:

1. Navigate to `/contact/` on your site
2. Fill in the Name, Email, and Message fields
3. Click "Send the form"
4. Your email client should open with pre-filled content

## Troubleshooting

### Mailto doesn't open
- Check your browser settings for default email client
- Try using a different browser
- Ensure you have an email client installed

### GitHub Workflow not running
- Verify the issue has the `contact-form` label
- Check that all GitHub secrets are properly configured
- Review the Actions tab for error messages

### Email not being sent
- Verify SMTP credentials in GitHub Secrets
- For Gmail, ensure you're using an App Password
- Check the workflow logs in GitHub Actions

## Security Notes

- Never commit email credentials to the repository
- Always use GitHub Secrets for sensitive data
- Use App Passwords instead of main account passwords
- The mailto fallback exposes the contact email in the page source

## Support

For questions or issues, please refer to the [Hugo documentation](https://gohugo.io/documentation/) or open an issue in this repository.
