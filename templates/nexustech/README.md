# NexusTech — High-Converting Client Landing Page Template

A clean, modern, mobile-responsive template website designed for fast client turnaround on Upwork, Fiverr, Contra, or direct outreach.

## Features
- **Modern Responsive Design**: Tailwind CSS utility styling with fluid breakpoints (Mobile, Tablet, Desktop).
- **Dark & Light Mode**: Built-in toggle with automatic `localStorage` persistence.
- **Conversion-Ready Sections**:
  - Hero with call-to-actions & live metrics
  - 6-service offerings grid with hover animations
  - Featured portfolio showcase cards
  - About studio & trust metrics
  - Verified client testimonials
  - Interactive Contact Form with instant validation and success feedback
- **Zero Build Step**: Pure HTML5, CSS3, and JavaScript — works instantly in any browser.

## How to Preview Locally
Run this command from inside this folder:
```bash
python3 -m http.server 8080
```
Then open your browser to `http://localhost:8080`.

## Connecting Real Form Submissions (Free)
To send form inquiries straight to your or the client's email inbox without writing backend code:
1. Go to [Web3Forms](https://web3forms.com) (free, no sign-up needed) or [Formspree](https://formspree.io).
2. Get your free Access Key.
3. In `index.html`, add:
   ```html
   <input type="hidden" name="access_key" value="YOUR-ACCESS-KEY-HERE">
   ```
   and change the form action to `action="https://api.web3forms.com/submit" method="POST"`.

## Deploying in 60 Seconds
- **Vercel / Netlify**: Drag-and-drop this entire folder into the Netlify dashboard for an instant live URL (`https://your-site.netlify.app`).
- **GitHub Pages**: Push this directory to a GitHub repository and enable Pages in repository settings.
