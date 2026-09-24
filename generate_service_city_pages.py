#!/usr/bin/env python3
"""Generate 10 service pages per city (13 cities = 130 pages).
Each page composes substantial service-specific copy with that city's
climate/housing/quirk data, truthful Napa-base disclosure, license number,
Service schema, and links back to the city hub."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

CITIES = [
 dict(slug="napa", name="Napa", county="Napa County", image="vineyard-hero.jpg",
  climate="hot, dry summer afternoons and damp, chilly winters",
  housing="a mix of older downtown bungalows and newer subdivisions toward Browns Valley",
  quirk="smoke season puts sudden demands on blowers and filtration"),
 dict(slug="sonoma", name="Sonoma", county="Sonoma County", image="family-hero-2.jpg",
  climate="valley heat that builds all afternoon",
  housing="Plaza-era historic homes and mid-century ranches",
  quirk="decades of patched ductwork are common in older homes"),
 dict(slug="st-helena", name="St. Helena", county="Napa County", image="napa-vineyard-2.jpg",
  climate="up-valley summers that run hotter than Napa proper",
  housing="Main Street cottages and multi-zone estate properties",
  quirk="guest houses and wine storage add zones that can fail quietly"),
 dict(slug="yountville", name="Yountville", county="Napa County", image="vineyard-hero.jpg",
  climate="warm valley summers and cool winter nights",
  housing="close-set cottages and newer homes near the golf course",
  quirk="small lots make equipment placement and noise a real design decision"),
 dict(slug="calistoga", name="Calistoga", county="Napa County", image="napa-vineyard-2.jpg",
  climate="the hottest summer afternoons in Napa Valley",
  housing="vintage cottages and resort-era homes",
  quirk="piecemeal HVAC work from past decades is the rule, not the exception"),
 dict(slug="petaluma", name="Petaluma", county="Sonoma County", image="family-hero-1.jpg",
  climate="fog-cooled summers and damp, chilly winters",
  housing="west-side Victorians and craftsman homes",
  quirk="marine moisture quietly corrodes burners, venting, and cabinets"),
 dict(slug="healdsburg", name="Healdsburg", county="Sonoma County", image="vineyard-hero.jpg",
  climate="north-county summers that push past 100 degrees",
  housing="plaza-area older homes and newer hillside builds",
  quirk="guest units and additions often run their own mini-splits"),
 dict(slug="sebastopol", name="Sebastopol", county="Sonoma County", image="family-hero-3.jpg",
  climate="fog-belt cool summers and damp winters",
  housing="older farmhouses and 70s-era homes",
  quirk="damp shade is hard on heat exchangers and venting"),
 dict(slug="vacaville", name="Vacaville", county="Solano County", image="hvac-tech.jpg",
  climate="inland Solano heat that runs past 100 degrees for weeks",
  housing="large tract neighborhoods built with builder-grade equipment",
  quirk="systems here fail from summer load, not just age"),
 dict(slug="fairfield", name="Fairfield", county="Solano County", image="heat-pump-unit.jpg",
  climate="hot summers with steady Suisun winds",
  housing="older downtown neighborhoods and newer Cordelia developments",
  quirk="wind-blown dust packs outdoor condenser coils"),
 dict(slug="glen-ellen", name="Glen Ellen", county="Sonoma County", image="napa-vineyard-2.jpg",
  climate="shaded, gentler summers in the Valley of the Moon",
  housing="creekside cottages and hillside homes in the trees",
  quirk="leaf litter and damp shade take a toll on outdoor units"),
 dict(slug="kenwood", name="Kenwood", county="Sonoma County", image="vineyard-hero.jpg",
  climate="warm but manageable valley summers",
  housing="vineyard properties and tucked-away ranch houses",
  quirk="mixed patchworks of central systems, mini-splits, and wall units are common"),
 dict(slug="windsor", name="Windsor", county="Sonoma County", image="family-hero-1.jpg",
  climate="hot north-county summers",
  housing="whole neighborhoods built in the same two boom decades",
  quirk="original systems are hitting end-of-life in waves"),
]

SERVICES = [
 dict(slug="ac-repair", name="Air Conditioning Repair", short="A/C repair",
  paras=[
   "When an air conditioner quits in {name}, it usually picks a bad week — {climate} mean cooling failures here are comfort emergencies, not inconveniences. Our repair visits start with diagnosis, not replacement talk: we test the system end to end, find the actual fault, and give you the repair price in writing before any work begins.",
   "The common culprits we repair across {housing} include failed capacitors and contactors, refrigerant leaks, seized condenser fan motors, clogged condensate lines, and electrical faults at the disconnect. In {name} specifically, {quirk} — so we check for that pattern on every call.",
   "Repair versus replace is your call, not ours to push. If a repair only buys a season on a system near end-of-life, we say so in plain language and price both paths. Same-day service is available for {name} cooling emergencies — call or text and a real person answers."],
  bullets=["Written diagnosis and price before any repair begins",
   "Same-day emergency response for cooling failures",
   "Honest repair-versus-replace numbers, never pressure"],
  extra="What a {name} repair visit looks like: we confirm the symptom with you, test the electrical and refrigerant sides of the system, isolate the actual failed part, and hand you a written price before any repair. Most common failures are fixed the same visit because our trucks carry the parts that fail most often in {county}. If a part has to be ordered, we tell you the timeline up front — no vague 'we'll call you.'",
  faqs=[("How fast can you get to {name} for an A/C repair?",
   "Same-day emergency response is available for {name}. Call or text (707) 531-9216 — Mon-Sat 7am-7pm, and emergencies move to the front of the line."),
   ("Do you charge to diagnose an A/C problem in {name}?",
   "We quote our current diagnostic pricing when you call, and the diagnosis always comes with a written explanation of the fault and the repair price before any work starts."),
   ("Should I repair or replace my A/C in {name}?",
   "It depends on the system's age, the cost of the repair, and its efficiency. If a repair only buys a season on a unit near end-of-life, we tell you plainly and price both paths — you decide, with real numbers in front of you."),
   ("Do you repair all A/C brands in {name}?",
   "Yes. We service and repair all major residential air-conditioning brands across {name} and the rest of {county}, whoever installed it.")]),
 dict(slug="ac-installation", name="A/C Installation & Replacement", short="A/C installation",
  paras=[
   "A new air conditioner in {name} should be sized to the house, not copied from the label of the old one. With {climate}, an undersized system runs itself to death and an oversized one short-cycles without ever dehumidifying properly. We start every {name} installation quote with a real load assessment of your home.",
   "Around {housing}, we regularly find ductwork that undoes good equipment — leaks, crushed runs, and undersized returns. Because {quirk}, we inspect the whole airflow path before quoting, so the new system actually delivers its rated comfort and efficiency.",
   "Every installation includes permits where required, clean workmanship, and a walkthrough of your new system in plain language. As a triple-licensed contractor (C-20 HVAC, C-10 Electrical), we handle any electrical circuit work in the same job — no second contractor to schedule."],
  bullets=["Load-based sizing, never label-copying",
   "Full duct and airflow inspection before any quote",
   "HVAC and electrical handled under one roof"],
  extra="A right-sized system in {name} pays you back every month it runs. We factor in your insulation, windows, and the way {climate} loads a home before recommending a size and efficiency level — then we quote the equipment plainly, note any rebates or incentives that currently apply, and put the whole project, timeline included, in writing. Installation day ends with a walkthrough so you actually know how to run your new system.",
  faqs=[("How much does A/C installation cost in {name}?",
   "Most residential installations run $6,000-$15,000 depending on home size, ductwork condition, and system type. Every {name} quote starts with a free in-home assessment — call (707) 531-9216."),
   ("Do I need to replace ducts when replacing my A/C in {name}?",
   "Not always. We inspect your ducts first; if they're sound, we say so. If they leak enough to waste the new system's efficiency, we show you and price the fix separately so you can decide."),
   ("How long does an A/C installation take in {name}?",
   "Most straightforward replacements are completed in a single day. Jobs that involve ductwork, electrical, or a switch to a heat pump can run longer — your written quote states the timeline before we begin."),
   ("Are there rebates for a new A/C in {name}?",
   "Sometimes — utility and state incentives change through the year. We tell you exactly what applies to your {name} project at quote time, rather than promising savings that may not exist.")]),
 dict(slug="furnace-repair", name="Furnace Repair", short="furnace repair",
  paras=[
   "A dead furnace on a cold night doesn't wait for business hours, and in {name} — where {climate} — heating failures are safety issues as much as comfort ones. We repair all major furnace brands, and every repair visit includes verifying the safety controls and checking carbon monoxide in the living space with proper test instruments.",
   "Across {housing}, the furnace problems we see most are failed ignitors and flame sensors, cracked or corroded components in older heat exchangers, tired blower motors, and short-cycling from clogged filters or failing limit switches. Because {quirk}, we look beyond the immediate fault to what caused it.",
   "You get the diagnosis and the repair price in writing before we touch a wrench. If the honest answer is that your furnace is near the end, we tell you that too — including what California's 2027 rules mean for your replacement options."],
  bullets=["Safety-first: CO checks with test instruments on every repair",
   "All major brands; written diagnosis before work begins",
   "Straight talk when repair no longer makes sense"],
  extra="Heat is a safety system, not just a comfort one, so a {name} furnace repair is never only about getting warm air moving again. We verify the burner, the safety controls, and carbon monoxide in the living space with real instruments before we consider the job done. Because {quirk}, we also look at what caused the failure — a clogged filter, a failing motor, a venting issue — so the same problem doesn't put you back in the cold next month.",
  faqs=[("My furnace in {name} is blowing cold air — what's wrong?",
   "Common causes range from a failed ignitor or flame sensor to a limit switch or thermostat fault. We diagnose it properly and give you the fix in writing — call (707) 531-9216."),
   ("Is a cracked heat exchanger dangerous?",
   "Yes — it can allow carbon monoxide into your home's air. That's why examining the heat exchanger and checking CO levels are part of every JVG furnace visit in {name}."),
   ("How fast can you repair a furnace in {name}?",
   "No-heat calls are treated as priorities, with same-day response available in {name}. Call or text (707) 531-9216 — a real person answers, Mon-Sat 7am-7pm."),
   ("My furnace is old — is it worth repairing in {name}?",
   "We give you the honest number. If a repair makes sense, we do it; if your furnace is near end-of-life, we explain your options — including what California's 2027 rules mean for your replacement choices — with no pressure.")]),
 dict(slug="heating-installation", name="Heating Installation", short="heating installation",
  paras=[
   "Installing new heat in {name} today means one big decision first: another gas furnace while they remain available, or a heat pump that meets California's 2027 zero-emission rules. We quote both honestly for {name} homes, with real numbers, so you decide with the facts.",
   "Heating loads across {housing} vary more than most owners expect — insulation, window age, and duct condition often matter more than square footage. With {climate}, right-sizing is the difference between even, quiet warmth and a system that blasts and stalls. We measure before we quote.",
   "Installation day is clean and complete: permits where required, old equipment hauled away, safety controls verified, and a plain-language walkthrough. Electrical circuits for new equipment are handled by our own C-10 license — one crew, one point of responsibility."],
  bullets=["Gas and heat-pump options quoted side by side",
   "Measured heating loads, not square-footage guesses",
   "Permits, haul-away, and electrical in one job"],
  extra="The 2027 decision is real, but it isn't a reason to panic-buy in {name}. We lay out both paths — a modern gas furnace while they remain available, or a heat pump that meets the zero-emission rules — with real numbers, real timelines, and any incentives that currently apply, so you choose on facts instead of pressure. Whatever you pick, we size it to your actual home in {county}, not the label on the old unit.",
  faqs=[("Can I still install a gas furnace in {name}?",
   "Yes — until California's 2027 zero-emission rules take effect, new gas furnaces remain available. We'll give you honest numbers for both gas and heat pump options so you can choose."),
   ("How long does a heating installation take in {name}?",
   "Most straightforward replacements are done in a day; jobs with duct or electrical work can run longer. Your written quote includes the timeline before we start."),
   ("Gas furnace or heat pump for my {name} home?",
   "Both work well in {name}. A heat pump is all-electric and 2027-ready but may need panel work; a gas furnace is often a lower upfront cost while available. We quote both side by side so the choice is yours."),
   ("Do you handle the permits for heating installation in {name}?",
   "Yes — we pull the required permits, haul away the old equipment, verify the safety controls, and handle any electrical under our own C-10 license. One crew, one point of responsibility.")]),
 dict(slug="heat-pumps", name="Heat Pump Installation", short="heat pumps",
  paras=[
   "Heat pumps are the future of comfort in {name} — one system that cools through {climate} and heats efficiently through the winter, all electric, and fully in line with California's 2027 appliance rules. We've installed them across the valley and answer every question without the sales pitch.",
   "The honest {name} caveats: homes among {housing} sometimes need electrical panel work to go all-electric, and duct condition matters for any central system. As a C-10 licensed electrical contractor, we assess your panel in the same visit and quote everything as one job — no surprises on change orders.",
   "Modern cold-climate heat pumps handle temperatures far below anything {name} sees; local winters are easy work. Ask us about current federal and state incentives when you're ready — programs change, and we'll tell you exactly what applies to your project."],
  bullets=["2027-ready: meets California's zero-emission standards",
   "Panel and electrical assessed up front, under our C-10 license",
   "Straight answers on sizing, ducts, and incentives"],
  extra="One heat pump replaces both your furnace and your air conditioner — it cools through {climate} and heats efficiently all winter, all electric. For {name} homes, the honest questions are whether your panel has room and whether your ducts are sound, and we answer both during the assessment rather than after the sale. Because we hold a C-10 electrical license, any panel or circuit work is quoted as part of the same job, so you get one price and one crew, not a surprise second contractor.",
  faqs=[("Do heat pumps work in {name} winters?",
   "Easily. Modern heat pumps heat efficiently well below freezing — {name} winters are well within their comfortable range."),
   ("Will my electrical panel handle a heat pump in {name}?",
   "Many homes are ready; some older panels need an upgrade. We check your panel during the assessment and, because we hold a C-10 electrical license, we can do any needed work as part of the same job."),
   ("Are there rebates for heat pumps in {name}?",
   "Often yes — federal, state, and utility incentives exist but change through the year. We tell you exactly which ones apply to your {name} project at quote time, in writing."),
   ("Is a heat pump worth it in {name}?",
   "For most {name} homes, yes — it's one efficient system for heating and cooling, it meets California's 2027 direction, and it removes gas-combustion risk. We'll show you the real numbers for your home so you can judge for yourself.")]),
 dict(slug="maintenance-inspection", name="$69.99 Preventative Maintenance Inspection", short="maintenance inspection",
  paras=[
   "Our $69.99 preventative maintenance inspection is the simplest way for a {name} homeowner to know exactly where their system stands. It is a visual and operational inspection only — no repairs, cleaning, or component replacements are included in this visit, and nothing is ever sold at the door.",
   "The 11 points cover your blower motor and fan, ignition system, safety controls and limit switches, accessible gas piping, venting, carbon monoxide levels in the living space, heat exchanger, condenser coil, accessible electrical connections, thermostat, and a full furnace cycle test. In {name}, where {quirk}, this look catches the local failure patterns early.",
   "You get a written assessment in plain language: what's healthy, what needs attention, and what it would cost — then you decide. With {climate}, the best time to know is before the season that tests your system, not during it."],
  bullets=["11 points, visual and operational — no repairs included",
   "Written plain-language assessment, yours to keep",
   "CO and safety checks with proper instruments, every visit"],
  extra="Think of it as a physical for your system before the season that tests it. For $69.99, a {name} homeowner gets an honest, documented picture of where their heating and cooling stand — what's healthy, what's wearing, and what it would cost to address — with zero pressure and nothing sold at the door. In {name}, where {quirk}, catching a small issue in this visit is often the difference between a cheap fix now and an emergency call during the next heat wave or cold snap.",
  faqs=[("What does the $69.99 inspection include in {name}?",
   "An 11-point visual and operational inspection — blower, ignition, safety controls, gas piping, venting, CO levels, heat exchanger, condenser coil, electrical connections, thermostat, and a furnace cycle test — with a written assessment. No repairs, cleaning, or replacements are included."),
   ("Is the $69.99 inspection a sales visit?",
   "No. Nothing is sold at the door. You get the written findings and prices for anything that needs attention, and every decision after that is yours."),
   ("When should I book an inspection in {name}?",
   "The best time is before the season that stresses your system — cooling ahead of {name}'s summer heat, heating ahead of winter. Booking off-season also means easier scheduling."),
   ("Do you cover both heating and cooling in the {name} inspection?",
   "The 11-point inspection focuses on your furnace and its safety systems, and includes a look at the condenser coil and airflow. Ask us about your specific system when you book and we'll tell you exactly what the visit covers for your {name} home.")]),
 dict(slug="electrical", name="Electrical: Panels, Circuits & Lighting", short="electrical work",
  paras=[
   "JVG holds a C-10 electrical contractor license alongside our HVAC license — which means {name} homeowners don't need a second contractor for panel upgrades, new circuits, or lighting. One family team, one schedule, one point of responsibility.",
   "Electrical capacity is quietly becoming the big question in {name}: heat pumps, EV chargers, and induction ranges all want panel room that homes among {housing} often don't have. We assess panels honestly — plenty pass; the ones that don't get a clear, written upgrade path.",
   "All work is permitted where required and done to code. If your electrical project connects to a comfort project — a heat pump circuit, a new condenser disconnect — we fold it into one job instead of two bills."],
  bullets=["C-10 licensed: panels, circuits, lighting, disconnects",
   "Panel capacity assessments for heat pumps and EV chargers",
   "Permitted, code-compliant work — in writing"],
  extra="Homes among {housing} were often wired for a different era's demands, and in {name} the modern additions — heat pumps, EV chargers, induction ranges — all compete for panel capacity that may not be there. We assess honestly: plenty of panels pass, and the ones that don't get a clear, written upgrade path with real numbers. Every job is permitted where required and done to code, and if your electrical work connects to a comfort project we fold it into one job instead of two bills.",
  faqs=[("Do I need a panel upgrade for a heat pump in {name}?",
   "Sometimes. Many panels have room; older ones may not. We assess yours up front and give you a written answer with real numbers — no scare tactics."),
   ("Are you licensed for electrical work in {name}?",
   "Yes — JVG holds a C-10 Electrical license under CSL #1103018, alongside our C-20 HVAC and B General Contractor classifications. You can verify it on the CSLB license lookup."),
   ("Can you install an EV charger in {name}?",
   "Yes. As a C-10 licensed electrical contractor we install EV chargers and the circuits they need, and we'll tell you up front whether your panel can support one."),
   ("Do you do electrical work beyond HVAC in {name}?",
   "We do — panels, dedicated circuits, lighting, and disconnects for {name} homes. It's the same family team and the same written-price honesty as our HVAC work.")]),
 dict(slug="ductless-mini-splits", name="Ductless Mini-Split Service", short="mini-splits",
  paras=[
   "Ductless mini-splits solve the rooms that central systems can't reach — the converted garage, the addition, the guest unit, the upstairs office that bakes every afternoon. In {name}, where {quirk}, mini-splits are often the practical answer we recommend.",
   "We install, repair, and service ductless systems across {housing}. Installation is about placement done right: head units where air actually circulates, line sets routed cleanly, condensate handled properly, and the outdoor unit positioned for airflow and long life through {climate}.",
   "Mini-splits are also heat pumps — efficient heating and cooling in one, and compliant with California's 2027 direction. For many {name} projects, a single-zone mini-split is the least invasive path to comfort in a problem room."],
  bullets=["Install, repair, and service for all major mini-split brands",
   "Clean placement: line sets, condensate, and airflow done right",
   "Single rooms to multi-zone whole-home setups"],
  extra="A mini-split is often the least invasive fix for a stubborn room in {name} — no ductwork to tear open, just a clean install done right. The details are what separate a good mini-split from a noisy, dripping one: head units placed where air actually circulates, line sets routed neatly, condensate handled properly, and the outdoor unit sited to survive {climate}. We handle single-zone problem rooms and multi-zone whole-home systems alike, and because they're heat pumps, they align with California's 2027 direction too.",
  faqs=[("How much does a mini-split cost in {name}?",
   "Single-zone installations typically run considerably less than full central replacements; multi-zone systems scale with the number of rooms. We quote after a free assessment — call (707) 531-9216."),
   ("Do mini-splits heat as well as cool?",
   "Yes — they're heat pumps. One wall unit both heats and cools its zone efficiently, which suits {name}'s climate well."),
   ("Where do mini-splits make the most sense in {name}?",
   "Converted garages, additions, guest units, and rooms a central system can't keep comfortable — common needs in {name} homes among {housing}."),
   ("Do you repair existing mini-splits in {name}?",
   "Yes — we install, service, and repair all major ductless brands in {name}, not just new installations.")]),
 dict(slug="emergency-hvac", name="Same-Day Emergency HVAC", short="emergency service",
  paras=[
   "When cooling dies during a heat wave or heat quits on a cold night, waiting three days isn't an option. JVG offers same-day emergency response for {name} — call or text (707) 531-9216 and a real person answers, Mon-Sat 7am to 7pm. Emergencies move to the front of the line.",
   "With {climate}, we know which failures can't wait: homes with elderly family members, infants, or medical needs get priority, period. Our trucks carry the common failure parts — capacitors, contactors, ignitors, flame sensors, fan motors — so most emergency calls end with the system running the same visit.",
   "Emergency work gets the same honesty as scheduled work: diagnosis explained, price in writing before repair, and no crisis upselling. Being a Napa-based family team, we're straight with you about arrival windows for {name} — and we keep them."],
  bullets=["Same-day response, emergencies to the front of the line",
   "Trucks stocked with the common failure parts",
   "No crisis upselling — written prices even under pressure"],
  extra="Emergencies are exactly when honesty matters most, and it's when some companies lean hardest on scared homeowners. Not us. A {name} emergency call gets the same diagnosis-first, written-price approach as a scheduled visit — no crisis upselling, no invented problems. Our trucks carry the parts that fail most in {county}, so most emergency calls end with the system running the same visit, and we're straight about arrival windows for {name} rather than leaving you waiting all day.",
  faqs=[("Do you really offer same-day HVAC service in {name}?",
   "Yes, for emergencies — call or text (707) 531-9216, Mon-Sat 7am-7pm. We're honest about arrival windows for {name} and we keep them."),
   ("What counts as an HVAC emergency?",
   "No cooling during extreme heat, no heat in cold weather, suspected gas or carbon monoxide issues, and failures affecting vulnerable family members. When in doubt, call — a person, not a menu, will answer."),
   ("Who gets priority for emergency service in {name}?",
   "Homes with elderly family members, infants, or medical needs move to the front of the line, period — followed by no-heat and no-cooling calls during extreme weather."),
   ("Will an emergency call cost more in {name}?",
   "You'll always get the price in writing before we repair, even under pressure. We quote our current rates honestly when you call — no surprise crisis pricing.")]),
 dict(slug="indoor-air-quality", name="Indoor Air Quality & Smoke Season", short="indoor air quality",
  paras=[
   "Air quality stopped being an abstract topic in {name} the first time the sky turned orange. When smoke season arrives, your HVAC system becomes the front line for the air your family breathes — and its readiness is testable in advance.",
   "Good indoor air in {name} rests on three things: a healthy blower moving enough air, filtration matched to the moment (higher-rated filters for smoke days), and a duct path that isn't pulling attic or crawlspace air into the house. Since {quirk}, we pay particular attention to the local pattern during inspections.",
   "Our $69.99 maintenance inspection covers the blower and airflow fundamentals; from there, honest upgrades — better filtration, sealing obvious duct leaks, or a mini-split for a sensitive room — are priced in writing. Clean air isn't a luxury; it's part of your family's safety and comfort."],
  bullets=["Smoke-season readiness: blower, filtration, and airflow",
   "Filter guidance matched to {county} conditions",
   "Honest, written options — never fear-based selling"],
  extra="You can't control the sky over {name}, but you can control the air inside your home — and your HVAC system is the tool that does it. We approach indoor air quality without the fear-selling: a healthy blower, the right filter for the moment, and a duct path that isn't pulling attic or crawlspace air into your living space. Since {quirk}, we pay attention to the local pattern, and any upgrade we suggest — better filtration, sealing obvious leaks, a mini-split for a sensitive room — comes priced in writing so you decide.",
  faqs=[("What filter should I use during smoke season in {name}?",
   "A higher-rated (MERV 13 where the system supports it) filter during smoke events, swapped back after — and check it monthly during smoke season, not quarterly. We'll confirm what your blower can handle."),
   ("Can my A/C run during heavy smoke in {name}?",
   "Yes — run it with windows closed and a good filter; the system recirculates and filters indoor air. What matters is a healthy blower and the right filter, which is exactly what we check."),
   ("How do I prepare my {name} home's air for smoke season?",
   "Start with a blower and airflow check, keep a supply of the right filters on hand, and seal obvious duct leaks. Our $69.99 inspection covers the fundamentals and gives you a written picture before the smoke arrives."),
   ("Do I need an expensive air purifier in {name}?",
   "Often not. For most {name} homes, a healthy blower and the correct filter do the heavy lifting. We'll tell you honestly whether added filtration is worth it for your situation.")]),
]

TPL = """---
layout: default
title: "{svc_name} in {city}, CA | JVG Cooling & Heating Solutions"
description: "{svc_short_cap} in {city}, {county} from JVG — a Napa Valley family team with 25 years of experience. Honest written pricing, licensed CSL #1103018. Call or text (707) 531-9216."
permalink: /service-areas/{city_slug}/{svc_slug}/
---

{{% include hero.html
   eyebrow="{city} · {county}"
   headline_a="{svc_name},"
   headline_b="done honestly in {city}."
   image="/assets/images/{image}"
   image_alt="{svc_name} service in {city}, California"
   hide_chip="true"
   lede="A Napa Valley family team serving {city} — 25 years of experience, written pricing, and a real person on the phone." %}}

<article class="jvg-article">
  <header class="jvg-article__head">
    <p class="jvg-article__eyebrow"><a href="{{{{ '/service-areas/{city_slug}/' | relative_url }}}}">JVG in {city}</a> · {svc_name}</p>
    <h1>{svc_name} in {city}</h1>
    <p class="jvg-article__meta">Family-operated · 25 years of experience · Lic. #1103018 (C-20 HVAC · C-10 Electrical · B General)</p>
  </header>
{paras}
  <p>{extra}</p>

  <h2>Why {city} homeowners call JVG</h2>
  <ul>
{bullets}
  </ul>

  <h2>{city} questions, honest answers</h2>
{faqs}
  <p><em>Straight with you: we don't keep an office in {city} — we're a family team based in Napa Valley serving {city} on scheduled routes, with same-day priority for emergencies. Our arrival windows already include the drive.</em></p>

  <div class="jvg-article__related">
    <h2>More JVG services in {city}</h2>
    <ul>
{related}
    </ul>
  </div>

  <div class="jvg-article__cta">
    <h2>Talk to the family about {svc_short} in {city}</h2>
    <p>Call or text — Mon–Sat, 7am–7pm. A real person answers, and every price comes in writing.</p>
    <p><a class="jvg-article__btn" href="tel:{{{{ site.phone }}}}">Call {{{{ site.phone_display }}}}</a></p>
    <p class="jvg-article__fine">Start simple: the $69.99 preventative maintenance inspection — 11 points, written assessment, no repairs sold at the door.</p>
  </div>
</article>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{svc_name}",
  "provider": {{
    "@type": "HVACBusiness",
    "name": "JVG Cooling & Heating Solutions",
    "telephone": "+17075319216",
    "url": "https://jvghvac.com"
  }},
  "areaServed": {{ "@type": "City", "name": "{city}, CA" }}
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{faq_schema}
  ]
}}
</script>

{{% include offer.html %}}
"""

def js_escape(t):
    return t.replace("\\", "\\\\").replace('"', '\\"')

count = 0
for c in CITIES:
    for s in SERVICES:
        fill = dict(name=c["name"], county=c["county"], climate=c["climate"],
                    housing=c["housing"], quirk=c["quirk"])
        paras = "\n".join("  <p>%s</p>" % p.format(**fill) for p in s["paras"])
        extra = s["extra"].format(**fill)
        bullets = "\n".join("    <li>%s</li>" % b.format(**fill) for b in s["bullets"])
        faqs = "\n".join(
            '  <h3>%s</h3>\n  <p>%s</p>' % (q.format(**fill), a.format(**fill))
            for q, a in s["faqs"])
        # FAQPage structured data from the same Q&A
        faq_items = []
        for q, a in s["faqs"]:
            faq_items.append(
                '    {\n'
                '      "@type": "Question",\n'
                '      "name": "%s",\n'
                '      "acceptedAnswer": { "@type": "Answer", "text": "%s" }\n'
                '    }' % (js_escape(q.format(**fill)), js_escape(a.format(**fill))))
        faq_schema = ",\n".join(faq_items)
        # Internal links to the other services in this same city
        related = "\n".join(
            '      <li><a href="{{ \'/service-areas/%s/%s/\' | relative_url }}">%s in %s</a></li>'
            % (c["slug"], o["slug"], o["name"], c["name"])
            for o in SERVICES if o["slug"] != s["slug"])
        page = TPL.format(svc_name=s["name"], svc_short=s["short"],
                          svc_short_cap=s["short"][0].upper() + s["short"][1:],
                          city=c["name"], county=c["county"],
                          city_slug=c["slug"], svc_slug=s["slug"], image=c["image"],
                          paras=paras, extra=extra, bullets=bullets, faqs=faqs,
                          faq_schema=faq_schema, related=related)
        fn = os.path.join(HERE, "svc-%s-%s.html" % (c["slug"], s["slug"]))
        with open(fn, "w") as f:
            f.write(page)
        count += 1
print("wrote", count, "pages")
