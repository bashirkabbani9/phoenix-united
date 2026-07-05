# Phoenix United FC — Development Programme Landing Page

Live marketing landing page for the **Phoenix United FC** (Dubai) football + degree
development programme. Static, single self-contained HTML file — hosted on GitHub Pages,
served on the client's custom domain.

## What's here

| File | Purpose |
|------|---------|
| `index.html` | **The live site.** Fully self-contained (all images/CSS/JS inlined). This is what GitHub Pages serves. Generated — do not edit by hand. |
| `phoenix-united-landing.template.html` | **The editable source.** Hand-authored markup/CSS with `__TOKEN__` placeholders for images. Edit this. |
| `build.py` | Inlines the `_web/` images into the template → produces `index.html`. |
| `_web/` | Optimised images used by the build (crest, renders, team, partner crests, Arabic artwork). |
| `CNAME` | The custom domain GitHub Pages serves (added during deploy). |

> Confidential brand source docs (`.pptx` / `.pdf` / `.docx`) and the `_assets/` extraction
> scratch are git-ignored and never published.

## Editing workflow

```bash
# 1. edit the source
#    phoenix-united-landing.template.html   (copy/layout/styles)
#    _web/                                   (swap an image, keep the same filename)

# 2. rebuild the live file
python3 build.py

# 3. publish
git add -A
git commit -m "describe the change"
git push
```

GitHub Pages redeploys automatically within ~1 minute of the push, and the client sees the
update on the live domain.

## Brand rules (locked)

- **Colours (only these five):** black `#0D0D0D`, gold `#C9A84C`, midnight blue `#0D1B2A`,
  sandy/cream `#E8DFC8`, white `#FFFFFF`. No other colours, no gradients.
- **Type:** Arial family + the commissioned Arabic calligraphy artwork (never typed).
- **Primary CTA:** "Start Your Pathway".
- **Never use:** world-class, elite, passionate, holistic, journey, second chance, etc.
- **Pricing:** gated — no figures; funnel to an evaluation call.

## Open items

- Wire the apply form to a real inbox / WhatsApp / email endpoint (currently front-end only).
- Confirm team-portrait name↔face accuracy with the client.
- Swap interim AI-render imagery for the real 2026 photoshoot when available.
