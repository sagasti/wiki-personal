---
title: "ciudadanias-bc cartel design pipeline"
created: "2026-05-06"
updated: "2026-05-06"
type: "decision"
tags: ["#ciudadanias-bc", "#bere", "#design", "#decision", "#cartel"]
sources: ["hermes-session/20260506_184142_cea83c"]
hermes_session: "20260506_184142_cea83c"
confidence: "medium"
---

# ciudadanias-bc cartel design pipeline

## Cartel Design Pipeline for Ciudadanías BC

**Decision:** Use HTML rendered via PIL to PNG instead of AI image generators for cartels with text.

**Rationale:** AI image generators (e.g., image-gen models) produce misspelled/garbled text in Spanish. HTML+PIL gives pixel-perfect text rendering.

## Bere's Cartel Design Preferences

- **Format:** Square (1:1) — consistent with her reel preference
- **Background:** No all-white; needs color and visual interest
- **National identity:** Include the country's flag; use accent colors matching the country (e.g., more red for Portugal 🇵🇹)
- **Contact info:** Show phone number and web URL as bare values, without labels like "Teléfono:" or "Web:"
- **Process:** Highly iterative; expects multiple revision rounds

## Pipeline

1. Write HTML with inline styles
2. Render to image via PIL (`imgkit` or similar)
3. Save to `~/wiki/projects/ciudadanias-bc-cartel-<service>.png`

See also: [[berenice-carbajo]], [[ciudadanias-bc]], [[ciudadanias-bc-portuguesa-services]]
