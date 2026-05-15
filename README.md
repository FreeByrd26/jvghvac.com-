# JVG Cooling & Heating Solutions — Website

Static Jekyll site for **JVG Cooling & Heating Solutions**, a family-operated HVAC and electrical contractor serving **Napa Valley and Sonoma County**.

**Deployed on:** GitHub Pages
**Domain:** _(pending — update `_config.yml` `url` and `CNAME` once confirmed)_

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

All site-wide variables (phone, license, slogan, $69.99 offer price, hours) live in `_config.yml`. Update once, propagates everywhere.

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
├── _config.yml             # Site config (phone, slogan, $69.99, etc.)
├── _layouts/
│   └── default.html        # Wraps every page (menu + bg + footer)
├── _includes/              # Reusable blocks
│   ├── menu.html
│   ├── footer.html
│   ├── floating-bg.html
│   ├── schema.html         # JSON-LD for AI/SEO
│   ├── hero.html           # (Batch B)
│   ├── trust-bar.html      # (Batch B)
│   ├── services.html       # (Batch B)
│   ├── about.html          # (Batch B)
│   ├── why.html            # (Batch C)
│   ├── offer.html          # (Batch C) — $69.99 11-point
│   ├── service-areas.html  # (Batch C)
│   └── faq.html            # (Batch C)
├── assets/
│   ├── css/style.css       # (Batch D) — all blocks consolidated
│   └── images/
├── index.html              # Home (Batch E)
├── about.md                # (Batch E)
├── services.md             # (Batch E)
├── preventative-maintenance.md  # (Batch E) — $69.99 landing
├── heat-pumps.md           # (Batch E) — 2027 angle
├── air-conditioning.md     # (Batch E)
├── heating.md              # (Batch E)
├── electrical.md           # (Batch E)
├── service-areas.md        # (Batch E)
├── contact.md              # (Batch E)
├── 404.html
├── robots.txt
└── CNAME                   # Custom domain (pending)
```

---

## Deployment

1. Push this directory to GitHub.
2. Repo Settings → Pages → Source: **Deploy from a branch** → `main` / `/site` folder (or move files to repo root if preferred).
3. Add custom domain when ready.

---

## Brand facts

- **Family-operated** since **2001** — Father & son, the Garcia family
- **License:** Contractors License No. 1103018 · C-20 HVAC · C-10 Electrical · B General Contractor
- **Phone:** (707) 531-9216
- **Email:** JVGHVAC@gmail.com
- **Service area:** Napa Valley, Sonoma County
- **Lead-gen offer:** $69.99 11-point preventative maintenance tune-up
- **Hablamos Español**
