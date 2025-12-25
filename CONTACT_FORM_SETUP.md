# Contact Form Setup

The contact page includes a form that sends messages directly via email using Formspree, a free form backend service for static sites.

## How It Works

When a user submits the contact form:
1. The form data is sent to Formspree's servers via AJAX
2. Formspree validates the data and sends an email to the configured address
3. The user sees a success message without leaving the page
4. No email client opens - everything happens in the background

## Setup Instructions

### Step 1: Create a Free Formspree Account

1. Go to [https://formspree.io/register](https://formspree.io/register)
2. Sign up for a free account (free tier allows 50 submissions/month)
3. Verify your email address

### Step 2: Create a New Form

1. Log into Formspree
2. Click "New Form" or "+" button
3. Give your form a name (e.g., "MetaCurious Contact Form")
4. Set the email address where you want to receive submissions
   - Enter the email address where you want to receive contact form messages (e.g., `info@metacurious.ca`)
5. Click "Create Form"

### Step 3: Get Your Form Endpoint

After creating the form, Formspree will provide you with a unique endpoint URL that looks like:
```
https://formspree.io/f/YOUR_FORM_ID
```

Copy this URL - you'll need it in the next step.

### Step 4: Update the Contact Form

Edit the file `layouts/contact/single.html` and find the form element:

**Find this line:**
```html
<form id="contact-form" class="contact-form">
```

**Replace it with:**
```html
<form id="contact-form" class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID">
```

Replace `YOUR_FORM_ID` with your actual Formspree form ID from Step 3.

### Step 5: Test the Form

1. Deploy your changes (commit and push)
2. Go to your contact page
3. Fill out and submit the form
4. You should see a success message
5. Check your email for the submission

## Formspree Features

- **Email notifications**: Receive submissions instantly via email
- **Spam protection**: Built-in spam filtering with reCAPTCHA option
- **Auto-responders**: Send automatic confirmation emails to users
- **Webhook integration**: Integrate with other services
- **Dashboard**: View all submissions in the Formspree dashboard
- **Custom redirect**: Redirect users after successful submission
- **AJAX support**: Submit forms without page reload (already configured)

## Alternative: Web3Forms

If you prefer not to create an account, you can use Web3Forms:

1. Go to [https://web3forms.com](https://web3forms.com)
2. Enter your email address
3. You'll receive an access key via email
4. Add the access key as a hidden field in the form (edit `layouts/contact/single.html`):

```html
<form id="contact-form" class="contact-form">
  <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY">
  <!-- existing form fields -->
</form>
```

5. Update the JavaScript in `layouts/contact/single.html` to use Web3Forms endpoint. Find the line with `form.getAttribute('action')` and ensure it returns the Web3Forms URL:
```javascript
const formAction = form.getAttribute('action') || 'https://api.web3forms.com/submit';
```

## Troubleshooting

### Form submissions not received
- Verify your Formspree form ID is correct in the HTML
- Check your email spam/junk folder
- Verify the email address in Formspree settings matches your desired recipient
- Check Formspree dashboard for submission logs

### Error message when submitting
- Check browser console (F12) for JavaScript errors
- Verify internet connection
- Ensure form fields have correct `name` attributes (name, email, message)
- Verify the Formspree endpoint URL is correct

### Formspree free tier limits
- Free tier: 50 submissions/month
- Paid tier: Unlimited submissions starting at $10/month
- For higher volume, consider upgrading or switching to Web3Forms (unlimited free tier)

### Form shows loading but never completes
- Check for ad blockers or privacy extensions that may block Formspree
- Verify CORS isn't being blocked by browser extensions
- Try in an incognito/private browsing window

## Email Template

Formspree will send emails with the following information:
- **From**: formspree@formspree.io (or your verified domain)
- **Reply-To**: The email address entered in the form
- **Subject**: Contact Form: [Name]
- **Body**: Contains name, email, and message fields

You can customize the email template and subject in Formspree's dashboard under form settings.

## Privacy & Security

- Formspree is GDPR compliant
- All data is transmitted over HTTPS
- Form submissions are encrypted in transit
- You can enable reCAPTCHA for additional spam protection
- Optional: Add honeypot field for additional spam filtering

## Pricing

- **Free**: 50 submissions/month
- **Gold**: $10/month - Unlimited submissions, custom redirect, file uploads
- **Platinum**: $40/month - Everything in Gold + advanced features

For most personal/small business sites, the free tier is sufficient.

## GitHub Actions Workflow (Optional)

The existing `.github/workflows/contact-form.yml` file is no longer needed with Formspree. You can:
- Keep it for reference
- Delete it to clean up the repository
- Use it for alternative implementations (e.g., GitHub Issues integration)

## Support

For questions about Formspree:
- Documentation: [https://help.formspree.io](https://help.formspree.io)
- Support: [https://formspree.io/contact](https://formspree.io/contact)
- FAQ: [https://help.formspree.io/hc/en-us/categories/360002400634](https://help.formspree.io/hc/en-us/categories/360002400634)

## Quick Start Summary

1. Sign up at formspree.io (free account)
2. Create a new form and set your email address
3. Copy the form endpoint URL (e.g., `https://formspree.io/f/abcd1234`)
4. Edit `layouts/contact/single.html` - find the `<form>` tag and add `action="YOUR_FORMSPREE_URL"`
5. Commit, push, and test!

That's it - your contact form will now send emails directly without opening an email client.
