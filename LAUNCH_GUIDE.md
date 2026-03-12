# High Country Finish and Repair CO — Launch Guide

## 1. Adding Your Photos

Drop photos into the `images/` folder, then update the HTML:

**Hero background:**
```html
<!-- Find this in index.html: -->
<div class="hero-bg-img" id="hero-bg"></div>
<!-- Change to: -->
<div class="hero-bg-img" style="background-image:url('images/hero.jpg')"></div>
```

**Gallery photos** — replace each `gallery-placeholder` div:
```html
<!-- Replace: -->
<div class="gallery-placeholder">...</div>
<!-- With: -->
<img class="gallery-img" src="images/wrap1.jpg" alt="Vehicle wrap Denver"/>
```

**Photo naming suggestions:**
- `hero.jpg` — your best-looking full vehicle wrap (landscape, 1920x1080+)
- `wrap1.jpg`, `wrap2.jpg` — vehicle wrap shots
- `sign1.jpg`, `sign2.jpg` — lobby/building sign shots
- `window1.jpg` — window tint/frosting shot
- `wall1.jpg` — wall graphic shot
- `about.jpg` — you or your team working (optional)

**Gallery data-cat tags** (for filter buttons):
- `data-cat="wrap"` — vehicle wraps & spot graphics
- `data-cat="sign"` — any sign work
- `data-cat="window"` — window tint/frosting
- `data-cat="wall"` — wall graphics

---

## 2. Set Up the Contact Form (Formspree — Free)

The form currently falls back to mailto. To get proper form submissions to your email:

1. Go to **https://formspree.io** → sign up free
2. Create a new form, set email to `highcountryfinishandrepairco@gmail.com`
3. Copy your Form ID (looks like `xpzgkwrb`)
4. In `index.html`, find:
   ```html
   action="https://formspree.io/f/YOUR_FORM_ID"
   ```
   Replace `YOUR_FORM_ID` with your actual ID.

Free tier: 50 submissions/month. Paid: $10/mo unlimited.

---

## 3. Hosting (Recommended: Netlify — Free)

1. Go to **https://netlify.com** → sign up free
2. Drag and drop the `vinyl-website` folder onto the Netlify dashboard
3. Your site goes live instantly at a random URL like `amazing-site-123.netlify.app`
4. Connect your custom domain (step 4 below)

Netlify also handles the Formspree alternative — you can use **Netlify Forms** instead (built-in, free 100/mo):
- Add `netlify` attribute to the form tag
- Remove the Formspree action
- Submissions appear in your Netlify dashboard

---

## 4. Domain Name

Recommended domains (check availability):
- `highcountryfinish.com`
- `highcountryfinishandrepairco.com`
- `hcfinishco.com`

Buy from **Namecheap.com** (~$12/yr) or **Cloudflare Registrar** (cheapest, at-cost).

Once you have a domain, point it to Netlify in the domain DNS settings — Netlify has a 2-minute walkthrough.

---

## 5. Google Business Profile (Gets You on Maps)

This is FREE and critical for local search.

1. Go to **https://business.google.com**
2. Sign in with your Google account
3. Search for "High Country Finish and Repair CO" — if it doesn't exist, click "Add your business"
4. Fill in:
   - Business name: **High Country Finish and Repair CO**
   - Category: **Sign Shop** (primary), add **Window Tinting Service**, **Auto Wrapping Service**
   - Phone: **303-882-4656**
   - Service area: Denver + list the specific cities
   - Website: (add once your site is live)
   - Hours of operation
5. Verify by postcard or phone (Google mails a card with a PIN)
6. Add all your portfolio photos to the Google listing — this is huge for conversions

---

## 6. Other Free Listings to Create

In order of priority:

| Platform | URL | Notes |
|---|---|---|
| **Google Business** | business.google.com | #1 priority — do this first |
| **Yelp for Business** | biz.yelp.com | Free, helps local SEO |
| **Facebook Business** | business.facebook.com | Create a page, post your work |
| **Instagram** | instagram.com | @highcountryfinish or similar — post every job |
| **Thumbtack** | thumbtack.com/pro | Good for residential leads |
| **Angi (Angie's List)** | angi.com | Good for commercial leads |
| **BBB** | bbb.org | Credibility, especially for commercial clients |
| **Houzz** | houzz.com/pro | Good for residential window frosting/wall graphics |

---

## 7. SEO Checklist (Already Built In)

The site already has:
- ✅ Meta title and description with local keywords
- ✅ Schema-ready structure
- ✅ Canonical URL (update to your real domain)
- ✅ Mobile-first responsive design
- ✅ Fast loading (no heavy frameworks)
- ✅ Semantic HTML headings
- ✅ Alt text placeholders on images
- ✅ Local city mentions throughout content

**After launch, also do:**
- Submit sitemap to Google Search Console (free)
- Get 5+ Google reviews ASAP (ask every satisfied customer)
- Post your Google Business profile photos weekly for first month

---

## 8. Stats to Update

In the hero section, update these numbers to be accurate:
```html
<div class="hs-num">500+</div>  <!-- installs completed -->
<div class="hs-num">10+</div>   <!-- years experience -->
```

---

## Summary Checklist

- [ ] Add hero + portfolio photos
- [ ] Update hero stats (500+ installs, years experience)
- [ ] Sign up for Formspree and add form ID
- [ ] Deploy to Netlify
- [ ] Buy domain name
- [ ] Connect domain to Netlify
- [ ] Set up Google Business Profile
- [ ] Create Yelp, Facebook, Instagram accounts
- [ ] Get first 5 Google reviews
