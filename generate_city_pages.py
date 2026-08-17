#!/usr/bin/env python3
"""Generate one unique, substantial service-area page per city (13 total).
Truthful framing (one Napa-based family team, no fake local offices),
unique local copy per page, Service schema with areaServed."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

CITIES = [
 dict(slug="napa", name="Napa", county="Napa County",
  image="vineyard-hero.jpg", alt="Napa Valley vineyards near the city of Napa",
  hb="in our hometown.",
  lede="Napa is home base — where this family lives, works, and answers the phone.",
  intro=[
   "Napa is where JVG started and where the family still lives, so nobody knows the city's homes better — from the older bungalows and Victorians around downtown and Old Town to the newer subdivisions out toward Browns Valley and north Napa. Those older homes often hide undersized ducts, tired floor furnaces, and panels that need a hard look before any system upgrade; the newer ones usually need honest maintenance more than replacement.",
   "Napa's climate works systems from both ends: hot, dry summer afternoons that push A/C hard, cool nights and damp winters that keep furnaces busy, and smoke season, when a healthy blower and a good filter suddenly matter more than anything. We size and service equipment for that whole picture — not just the week you call.",
   "Because we're local, same-day emergency response in Napa itself is as realistic as it gets. Call or text, and one of us — not a call center — picks up."],
  bullets=["Older downtown homes: duct, panel, and floor-furnace evaluations before any upgrade",
   "Smoke-season readiness: blower health, filtration, and airflow checks",
   "Same-day emergency response right in town"]),
 dict(slug="sonoma", name="Sonoma", county="Sonoma County",
  image="family-hero-2.jpg", alt="A family at home near Sonoma",
  hb="around the Plaza.",
  lede="Historic homes, valley heat, and a family team that treats Sonoma like a neighbor.",
  intro=[
   "Sonoma's mix is unlike anywhere else we work: adobe-era and early-1900s homes near the Plaza with quirky retrofits, ranch houses from the 60s and 70s, and newer builds toward the east side. Older Sonoma homes often carry decades of patched ductwork and add-on wall heaters — the first honest step is usually an inspection, not a sales pitch.",
   "Sonoma Valley traps summer heat, and afternoon highs run well past what many older A/C systems were sized for. We see plenty of systems short-cycling their way to an early death because they were never matched to the house. When replacement time comes, heat pumps handle Sonoma's mild winters easily and meet California's 2027 rules.",
   "We're over the Mayacamas from our Napa base often — Sonoma calls get grouped so we arrive on time and you're not paying for windshield hours."],
  bullets=["Honest assessments for Plaza-area and mid-century homes with patched systems",
   "Right-sizing A/C and heat pumps for Sonoma Valley summer heat",
   "2027 planning: heat pump options that fit older construction"]),
 dict(slug="st-helena", name="St. Helena", county="Napa County",
  image="napa-vineyard-2.jpg", alt="Vineyards and hills around St. Helena",
  hb="up the valley.",
  lede="Estate homes and Main Street cottages deserve the same honest work.",
  intro=[
   "St. Helena homes range from Main Street cottages to estate properties with multiple zones, wine storage, and guest houses — and both ends of that range are regulars on our schedule. Multi-zone systems fail quietly: one bad damper or a tired zone board and half the house goes uncomfortable while the equipment looks fine. We diagnose the whole system, not just the loudest symptom.",
   "Up-valley summers run hotter than Napa proper, and shaded estate equipment often outlives sun-baked units by years — placement matters, and we factor it into every replacement quote. For wine country properties, steady temperatures aren't a luxury; they protect the house and everything in it.",
   "We're 25 minutes up Highway 29 from our Napa base, and St. Helena appointments are scheduled with that drive built in — when we give you a window, we mean it."],
  bullets=["Multi-zone diagnosis for estate and guest-house systems",
   "Replacement quotes that account for up-valley heat and equipment placement",
   "Scheduled windows that respect your time — no all-day waiting"]),
 dict(slug="yountville", name="Yountville", county="Napa County",
  image="vineyard-hero.jpg", alt="Vineyard rows near Yountville",
  hb="in Yountville.",
  lede="Small town, high standards — comfort work that matches them.",
  intro=[
   "Yountville may be small, but its homes work hard — cottages and bungalows that host family and guests year-round, plus newer homes near the golf course with systems now hitting their first replacement cycle. In a town known for hospitality, a guest room that won't cool in July gets noticed.",
   "Many Yountville homes sit on smaller lots where outdoor unit placement, noise, and airflow clearance are real constraints. Quiet, correctly-placed equipment is a design decision — we make it deliberately, not by default.",
   "Minutes from our Napa base, Yountville gets true same-day response for emergencies. Call or text and a Garcia answers."],
  bullets=["Quiet equipment placement for close-set cottage lots",
   "First-replacement-cycle guidance for 15-to-20-year-old systems",
   "True same-day emergency response from nearby Napa"]),
 dict(slug="calistoga", name="Calistoga", county="Napa County",
  image="napa-vineyard-2.jpg", alt="Hills above Calistoga at the top of Napa Valley",
  hb="at the top of the valley.",
  lede="The hottest town in the valley is the worst place for a weak A/C.",
  intro=[
   "Calistoga sits at the hot end of Napa Valley — summer afternoons here routinely run several degrees above Napa proper, and A/C systems that coast elsewhere get worked to their limits. If your system struggled last July, it isn't going to age out of the problem; a $69.99 inspection tells you exactly where it stands before the next heat wave.",
   "The town's older cottages and resort-era homes often mix vintage construction with decades of piecemeal HVAC work. We're comfortable in old houses: we inspect what's actually there, explain it in plain language, and never sell repairs at the door.",
   "Heat pumps deserve a special mention in Calistoga: one system that handles brutal summers and mild winters, ready for California's 2027 rules — and we've installed them across the valley."],
  bullets=["Pre-summer inspections tuned to the valley's hottest microclimate",
   "Vintage-home experience: honest work on older construction",
   "Heat pump planning ahead of the 2027 gas phase-out"]),
 dict(slug="petaluma", name="Petaluma", county="Sonoma County",
  image="family-hero-1.jpg", alt="A family comfortable at home near Petaluma",
  hb="in river town.",
  lede="Fog-cooled summers, damp winters — Petaluma comfort is a heating story.",
  intro=[
   "Petaluma lives in the coastal fog influence, which flips the usual script: summers are milder than the inland valleys, and it's the damp, chilly winters that test a home. Victorians and craftsman homes on the west side often run furnaces that predate their owners — beautiful houses, tired heat. A visual and operational inspection is the honest starting point.",
   "That marine air also means moisture: we pay attention to venting, corrosion, and combustion safety in ways inland techs sometimes skip. Carbon monoxide checks with proper instruments are part of every inspection we do.",
   "For replacements, Petaluma's mild profile is ideal heat pump territory — efficient in exactly the temperature band this town lives in, and compliant with the 2027 rules."],
  bullets=["Furnace and venting inspections for older west-side homes",
   "Moisture-aware service: corrosion, venting, and CO checks standard",
   "Heat pumps that fit Petaluma's mild coastal climate perfectly"]),
 dict(slug="healdsburg", name="Healdsburg", county="Sonoma County",
  image="vineyard-hero.jpg", alt="Vineyards outside Healdsburg",
  hb="in Healdsburg.",
  lede="North county heat with wine country standards.",
  intro=[
   "Healdsburg summers are genuinely hot — north of the fog line, afternoons push triple digits more often than most of Sonoma County, and cooling systems carry the load. Between the plaza-area older homes and the newer hillside builds, we see two very different problems: vintage systems past their design life, and modern systems that were installed fast and sized wrong.",
   "Wine country properties around Healdsburg often add complexity — guest units, cellars, additions with their own mini-splits. We service ducted and ductless systems alike, and our written assessments cover the property as a system, not a collection of boxes.",
   "It's a drive from Napa, so we batch Healdsburg work into scheduled windows — you get a real arrival time, and emergencies still jump the line."],
  bullets=["Cooling-first inspections for north county's hotter summers",
   "Ducted and ductless (mini-split) service for main homes and additions",
   "Written plain-language assessments for whole properties"]),
 dict(slug="sebastopol", name="Sebastopol", county="Sonoma County",
  image="family-hero-3.jpg", alt="A family at home near Sebastopol",
  hb="in apple country.",
  lede="Fog-belt homes need heating done right — and air kept clean.",
  intro=[
   "Sebastopol sits in the fog belt, where damp air and shaded properties keep homes cool most of the year — which means furnaces and heat systems do the heavy lifting while A/C is often an afterthought. Older farmhouses and 70s-era homes around town frequently run heating equipment well past its safe, efficient prime.",
   "Damp climates are hard on equipment in quiet ways: corroded burners, rusted heat exchangers, venting trouble. That's why every inspection we do here includes examining the heat exchanger for visible cracks and corrosion and checking carbon monoxide in the living space with test instruments — safety first, in plain language.",
   "Smoke season doesn't skip Sebastopol either; a healthy system with good filtration is your indoor air defense when it rolls in."],
  bullets=["Heating-first inspections for the fog belt's damp climate",
   "Heat exchanger and CO safety checks with proper instruments, every visit",
   "Indoor air readiness for smoke season"]),
 dict(slug="vacaville", name="Vacaville", county="Solano County",
  image="hvac-tech.jpg", alt="Technician inspecting an air conditioner in Vacaville",
  hb="in Vacaville.",
  lede="Real inland heat, hardworking A/C — and a family team that shows up.",
  intro=[
   "Vacaville summers are the real thing: inland Solano heat that runs past 100° and keeps air conditioners working from morning to night for weeks straight. Systems here don't fail from age alone — they fail from load. The homes in Vacaville's big tract neighborhoods were often built with builder-grade equipment on the smallest passing size, and fifteen summers later, it shows.",
   "That's exactly what our $69.99 preventative maintenance inspection is for: a visual and operational check of the whole system — condenser coil, electrical connections, thermostat, safety controls — with a written assessment before the next heat wave finds the weak spot. No repairs sold at the door; you decide what happens next.",
   "Vacaville is part of our regular service loop from Napa. Scheduled work gets a real window, and summer emergencies move to the front of the line."],
  bullets=["Load-focused A/C inspections built for 100° summers",
   "Builder-grade system evaluations in tract-home neighborhoods",
   "Scheduled service windows plus emergency priority in summer"]),
 dict(slug="fairfield", name="Fairfield", county="Solano County",
  image="heat-pump-unit.jpg", alt="A heat pump unit at a Fairfield home",
  hb="in Fairfield.",
  lede="Hot summers, steady winds, and honest HVAC for Solano families.",
  intro=[
   "Fairfield homes deal with a tough combination: hot inland summers and the steady Suisun winds that drive dust and debris straight into outdoor condenser coils. A clogged coil makes your A/C work harder, cool worse, and die younger — which is why coil inspection for visible damage, debris buildup, and restricted airflow is one of the 11 points on our maintenance inspection.",
   "From older neighborhoods near downtown to newer developments toward Cordelia and Green Valley, we service every generation of equipment — and for military families around Travis, we keep scheduling flexible and communication simple: call or text, and a real person answers.",
   "When replacement time comes, Fairfield's climate suits heat pumps well — one system for hot summers and mild winters, in line with California's 2027 appliance rules."],
  bullets=["Condenser coil checks for wind-blown dust and debris",
   "Flexible scheduling and straight communication for busy households",
   "Heat pump guidance ahead of the 2027 rules"]),
 dict(slug="glen-ellen", name="Glen Ellen", county="Sonoma County",
  image="napa-vineyard-2.jpg", alt="Wooded hills of the Valley of the Moon near Glen Ellen",
  hb="in the Valley of the Moon.",
  lede="Wooded properties, older homes, and comfort that works off the beaten path.",
  intro=[
   "Glen Ellen homes hide in the trees — creekside cottages, hillside cabins, and older houses in the Valley of the Moon, many with systems that were added or extended over decades. Shade keeps summer loads gentler than the open valley, but leaf litter, debris, and damp shade take their own toll on outdoor equipment and venting.",
   "Rural properties mean practical details matter: access, clearances around equipment, and electrical capacity in homes that may still run older panels. As a triple-licensed contractor (C-20 HVAC, C-10 Electrical), we can assess and handle both sides in one visit instead of leaving you to coordinate two trades.",
   "We schedule Glen Ellen and Kenwood together on service loops, so you get a firm window — and the same written, plain-language assessment every JVG customer gets."],
  bullets=["Debris and shade-aware checks for wooded properties",
   "HVAC and electrical assessed together under one license",
   "Firm scheduling windows on our valley service loop"]),
 dict(slug="kenwood", name="Kenwood", county="Sonoma County",
  image="vineyard-hero.jpg", alt="Vineyards near Kenwood in Sonoma Valley",
  hb="in Kenwood.",
  lede="Small community, full service — nobody's too far off our loop.",
  intro=[
   "Kenwood is exactly the kind of place big HVAC outfits skip: a small community between Sonoma and Santa Rosa where a service call means a real drive. We build Kenwood into our Sonoma Valley loop deliberately — small towns deserve the same response as big ones.",
   "The homes here range from vineyard properties to tucked-away ranch houses, many with a patchwork of systems: an aging central furnace, a mini-split added for a studio, a wall unit somebody meant to replace years ago. Our inspection covers what's actually installed and tells you, in writing, what's worth keeping.",
   "Valley of the Moon summers are warm but manageable — which makes Kenwood ideal territory for heat pumps when replacement time comes, ahead of California's 2027 changes."],
  bullets=["Reliable service for a town the big outfits drive past",
   "Mixed-system properties assessed as one honest picture",
   "Heat pump readiness for 2027"]),
 dict(slug="windsor", name="Windsor", county="Sonoma County",
  image="family-hero-1.jpg", alt="A family at home in Windsor",
  hb="in Windsor.",
  lede="Newer homes, first replacements, and maintenance that keeps them honest.",
  intro=[
   "Windsor grew fast, and a huge share of its homes were built in the same two decades — which means their original HVAC systems are now hitting end-of-life in waves. If your neighbors are all replacing systems, yours is on the same clock. The smart move is knowing your system's real condition before it picks the hottest week of the year to quit.",
   "North county summers run hot in Windsor, and builder-grade equipment installed during the boom years wasn't always sized generously. Our $69.99 inspection gives you the written facts: what's healthy, what's wearing, and what a replacement would actually involve — no pressure, no scare tactics.",
   "For those replacements, heat pumps are the forward-compatible choice under California's 2027 rules, and Windsor's climate suits them well."],
  bullets=["End-of-life assessments for boom-era original systems",
   "Straight answers on repair-versus-replace — in writing",
   "2027-ready heat pump replacements sized correctly"]),
]

SERVICES_LI = """      <ul>
        <li>$69.99 preventative maintenance inspection (visual &amp; operational — no repairs included)</li>
        <li>Air conditioning repair &amp; installation</li>
        <li>Furnace &amp; heating repair and installation</li>
        <li>Heat pump installation &amp; replacement (2027-ready)</li>
        <li>Ductless / mini-split service</li>
        <li>Electrical: panel upgrades, circuits &amp; lighting (C-10)</li>
        <li>Same-day emergency response</li>
      </ul>"""

TPL = """---
layout: default
title: "HVAC in {name}, CA | Heating, A/C & Heat Pumps | JVG Cooling & Heating"
description: "Family-operated HVAC serving {name} ({county}) from our Napa Valley base — heating, air conditioning, heat pumps, and licensed C-10 electrical. $69.99 preventative maintenance inspection. Lic. #1103018."
permalink: /service-areas/{slug}/
---

{{% include hero.html
   eyebrow="Serving {name} · {county}"
   headline_a="Heating &amp; cooling,"
   headline_b="{hb}"
   image="/assets/images/{image}"
   image_alt="{alt}"
   hide_chip="true"
   lede="{lede}" %}}

<article class="jvg-article">
  <header class="jvg-article__head">
    <p class="jvg-article__eyebrow">JVG in {name}</p>
    <h1>HVAC service in {name}, done the family way.</h1>
    <p class="jvg-article__meta">One Napa-based family team · 25 years of experience · Lic. #1103018 (C-20 HVAC · C-10 Electrical · B General)</p>
  </header>
{paras}
  <h2>What we do in {name}</h2>
{services}
  <h2>Worth knowing in {name}</h2>
  <ul>
{bullets}
  </ul>
  <p><em>One honest note: we don't have an office in {name} — we're a family team based in Napa Valley that serves {name} on scheduled routes, with emergency priority. When we quote an arrival window, we've already accounted for the drive.</em></p>

  <div class="jvg-article__cta">
    <h2>Book your $69.99 inspection in {name}</h2>
    <p>A visual and operational inspection of your system — 11 points, written assessment in plain language, and no repairs, cleaning, or component replacements sold at the door.</p>
    <p><a class="jvg-article__btn" href="tel:{{ site.phone }}">Call {{ site.phone_display }}</a></p>
    <p class="jvg-article__fine">Mon–Sat 7am–7pm · Call or text · A real person answers</p>
  </div>
</article>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "HVAC repair, maintenance inspection, and installation",
  "provider": {{
    "@type": "HVACBusiness",
    "name": "JVG Cooling & Heating Solutions",
    "telephone": "+17075319216",
    "url": "https://jvghvac.com"
  }},
  "areaServed": {{ "@type": "City", "name": "{name}, CA" }},
  "offers": {{ "@type": "Offer", "name": "Preventative Maintenance Inspection (No Repairs Included)", "price": "69.99", "priceCurrency": "USD" }}
}}
</script>

{{% include offer.html %}}
{{% include faq.html %}}
"""

for c in CITIES:
    paras = "\n".join(f"  <p>{p}</p>" for p in c["intro"])
    bullets = "\n".join(f"    <li>{b}</li>" for b in c["bullets"])
    page = TPL.format(name=c["name"], county=c["county"], slug=c["slug"], hb=c["hb"],
                      image=c["image"], alt=c["alt"], lede=c["lede"],
                      paras=paras, services=SERVICES_LI, bullets=bullets)
    fn = os.path.join(HERE, f"area-{c['slug']}.html")
    with open(fn, "w") as f:
        f.write(page)
    print("wrote", os.path.basename(fn))
print("done:", len(CITIES))
