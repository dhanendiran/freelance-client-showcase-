#!/usr/bin/env python3
"""
Quick Proposal & Cold Pitch Generator for Freelance Jobs
Run: python3 quick_proposal.py
"""

import sys

def main():
    print("=" * 60)
    print("⚡ FREELANCE FAST-CASH PROPOSAL & PITCH GENERATOR")
    print("=" * 60)
    print("1. Upwork / Freelancer Landing Page Proposal")
    print("2. Upwork Figma-to-Code Proposal")
    print("3. Upwork CSS/Responsive Bug Fix Proposal")
    print("4. Local Business Cold Email Pitch")
    print("5. Local Business Instagram / Facebook DM")
    print("=" * 60)
    
    choice = input("Select an option (1-5): ").strip()
    live_link = input("Your live demo link (e.g. https://your-site.netlify.app): ").strip() or "https://your-site.netlify.app"
    
    if choice == "1":
        client_need = input("Client's main need (e.g., redesign, lead capture): ").strip() or "high-converting landing page"
        print("\n" + "-" * 50)
        print("📋 COPY & PASTE THIS PROPOSAL INTO UPWORK:")
        print("-" * 50)
        print(f"""I can build your modern, mobile-responsive landing page for your {client_need} and deliver the complete live version within 24–48 hours.

Here are two live landing pages I've recently built with clean HTML5 & Tailwind CSS:
• Local Business / Clinic: {live_link}/templates/apex-dental/index.html
• Modern SaaS & Tech: {live_link}/templates/nexustech/index.html
• GitHub Profile: https://github.com/dhanendiran

What you get:
1. 100% pixel-perfect responsive design across iPhone, Android, and Desktop
2. Lead capture / contact form connected directly to your email
3. Fast loading speeds (< 1.2s page load) with zero bloat
4. Free deployment to Vercel, Netlify, or your preferred hosting server

Do you already have copy/text ready, or would you like me to structure the page sections first?

I can start right now and deliver your preview draft today!

Best,
Dhanendiran""")

    elif choice == "4":
        biz_name = input("Business Name: ").strip() or "Business"
        biz_type = input("Business Type (e.g. Dentist, Roofer, Gym): ").strip() or "Service"
        city = input("City Name: ").strip() or "your area"
        print("\n" + "-" * 50)
        print("📋 COPY & PASTE THIS COLD EMAIL:")
        print("-" * 50)
        print(f"""Subject: Quick question regarding your website + mobile preview

Hi {biz_name} team,

I was searching for top-rated {biz_type}s in {city} and came across your business on Google.

I noticed that your current website isn't fully optimized for mobile devices, which makes it harder for potential customers browsing from their phones to quickly tap-to-call or book an appointment.

Because you have great reviews, I went ahead and drafted a modern, mobile-friendly website concept for you:

👉 Live Preview: {live_link}/templates/apex-dental/index.html

Features included:
- Instant mobile tap-to-call button
- Fast appointment / quote request form
- Showcase for your customer reviews and services
- Loads in under 1 second on phones

If you'd like to use this design for your business, I can customize it with your exact branding, phone number, and services for a flat $200. No monthly maintenance fees or lock-ins.

If you're interested, let me know and I'll send over the details. If not, no worries at all and keep up the great work!

Best regards,
Dhanendiran M.
Web Developer & Designer""")

    else:
        print("\nCheck UPWORK_FIVERR_PROPOSALS.md or COLD_EMAIL_LEADS_AND_SCRIPTS.md for all scripts!")

if __name__ == "__main__":
    main()
