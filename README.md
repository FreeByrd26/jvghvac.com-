# JVG Cooling & Heating Solutions — Website

Static Jekyll site for **JVG Cooling & Heating Solutions**, a family-operated HVAC and electrical contractor serving **Napa Valley and Sonoma County**.

**Deployed on:** GitHub Pages (via GitHub Actions)
**Live URL:** https://freebyrd26.github.io/jvghvac.com-/
**Custom domain:** _(pending — update `_config.yml` `url`/`baseurl` and `CNAME` once `jvghvac.com` DNS is live)_

---

## Local development

```bash
cd site
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000`.

---

## Edit-friendly content

All site-wide variables (phone, license, slogan, offer price, hours) live in `_config.yml`. Update once, propagates everywhere.

```yaml
phone: "+17075319216"
phone_display: "(707) 531-9216"
offer_price: "69.99"
slogan: "Family Operated Business Providing Comfort and Solutions"
```

---

## Structure

```
site/
├── _config.yml             # Site config (phone, slogan, offer price, etc.)
├── _layouts/
│   └── default.html        # Wraps every page (menu + bg + footer)
├── _includes/              # Reusable blocks
│   ├── menu.html
│   ├── footer.html
│   ├── floating-bg.html
│   ├── schema.html         # JSON-LD for AI/SEO
│   ├── hero.html
│   ├── trust-bar.html
│   ├── services.html
│   ├── about.html
│   ├── why.html
│   ├── offer.html          # maintenance & diagnostic offer
│   ├── service-areas.html
│   └── faq.html
├── assets/
│   ├── css/style.css
│   └── images/
│       ├── vineyard-hero.jpg
│       └── jvg-tech-at-work.jpg
├── index.html              # Home
├── about.html
├── services.html
├── preventative-maintenance.html  # Maintenance & diagnostic landing page
├── heat-pumps.html
├── air-conditioning.html
├── heating.html
├── electrical.html
├── service-areas.html
├── contact.html
├── 404.html
├── robots.txt
└── CNAME                   # Custom domain (pending)
```

---

## Deployment

Pushing to `main` triggers `.github/workflows/` which builds the Jekyll site
and deploys it to GitHub Pages automatically — no manual steps.

To enable the custom domain `jvghvac.com`:

1. Point DNS at GitHub Pages (A/AAAA records, or a `CNAME` to `freebyrd26.github.io`).
2. Put `jvghvac.com` in the `CNAME` file.
3. In `_config.yml`, set `url: https://jvghvac.com` and `baseurl: ""`.
4. Commit and push — Pages will issue the HTTPS certificate.

---

## Brand facts

- **Family-operated** since **2001** — Father & son, the Garcia family
- **License:** Contractors License No. 1103018 · C-20 HVAC · C-10 Electrical · B General Contractor
- **Phone:** (707) 531-9216
- **Email:** JVGHVAC@gmail.com
- **Service area:** Napa Valley, Sonoma County
- **Lead-gen offer:** $69.99 preventative maintenance & diagnostic
