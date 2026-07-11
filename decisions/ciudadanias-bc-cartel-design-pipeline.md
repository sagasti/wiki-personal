---
title: "ciudadanias-bc cartel design pipeline"
created: "2026-05-06"
updated: "2026-07-09"
type: "decision"
tags: ["#ciudadanias-bc", "#bere", "#design", "#decision", "#cartel", "#ideogram"]
sources: ["hermes-session/20260506_184142_cea83c", "hermes-session/20260621_201756_f86828b8"]
confidence: "high"
---

# ciudadanias-bc cartel design pipeline

## Pipelines activos

### A) Texto denso / precios / legal (preferido cuando el copy es crítico)
**Decision:** HTML/PIL programático → PNG.  
**Rationale:** generadores de imagen alucinan español (Tramitó/Tramita, typos). PIL = texto exacto.

### B) Placas/stories de marca (desde 2026-06-14)
**Decision:** Ideogram REST (`ideogram_post.py` / skill `ciudadanias-bc-ig`) + Pillow para logo y footer.  
Ideogram hace fondo + headline/tagline; Pillow estampa logo BC (arriba) y `@ciudadaniasbc · ciudadaniasbc.com` (abajo). Preferir `--magic OFF` y revisar voseo **Tramitá**.

## Preferencias de Bere (diseño)

- **Venta:** fondos con color vibrante (bandera/degradado), tarjeta blanca interna; **nunca** todo blanco/minimalista aburrido.
- **Informar:** claros/suaves (celeste, beige, nude).
- **Formato:** 1:1 posts; **9:16** stories.
- Bandera como badge, no fondo dominante; acentos dorado + azul oscuro.
- Contacto: `11 7639-9809` + `ciudadaniasbc.com` (con “s”).
- Proceso iterativo: varias variantes y feedback de Bere.

## Push de calidad 2026-07-09

Jorge retransmitió que Bere comparaba avisos con ChatGPT (“los hace mejor / más de diseño / distintos al resto de la ciudad”). Brisa respondió subiendo el bar:

- Estilo **editorial / luxury magazine**: card elevada, gradiente con profundidad, no beige genérico.
- Muestras pitch 9:16 (italiana + española) enviadas a WhatsApp **CIUDADANÍAS BC**.
- Oferta de iterar con feedback de Bere o con ejemplo de ChatGPT.
- Guardar feedback de Bere en el skill/reference de patrones (loop de mejora del skill).

## Outputs

- Carteles PIL: `~/wiki-personal/projects/ciudadanias-bc-cartel-<service>.png` o assets en `projects/ciudadanias-bc-assets/`
- Muestras Ideogram pitch 2026-07-09: `ciudadaniasbc_pitch_italiana_20260709.png` / `ciudadaniasbc_pitch_espanola_20260709.png` (enviadas por WA). Futuros assets: guardar en wiki-personal, no en `~/wiki`.

See also: [[berenice-carbajo]], [[ciudadanias-bc]], [[ciudadanias-bc-portuguesa-services]]
