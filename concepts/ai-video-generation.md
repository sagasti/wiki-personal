---
title: "AI Video Generation"
created: "2026-04-29"
updated: "2026-04-29"
type: "concept"
tags: ["#concept", "#ai", "#video", "#generation", "#luz-estudio"]
related: [[ai-video-study-plan]], [[hunyuan-video-recipe]], [[did-video]], [[higgsfield-ai]], [[video-rating-system]], [[luz-estudio]]
---

# AI Video Generation

Umbrella sobre el stack de generación de video con IA que Jorge usa para Reels personales y para servicios B2B de [[luz-estudio]]. Cubre tres categorías: talking avatar (lipsync sobre foto), text-to-video local (ComfyUI), y cloud APIs.

## Stack actual

| Tool | Tipo | Cuándo se usa |
|---|---|---|
| [[did-video]] (D-ID) | Talking avatar | Lipsync sobre foto, casos puntuales |
| [[hunyuan-video-recipe]] (ComfyUI + Hunyuan) | Text-to-video local | Producción pesada en [[runpod]] H200, control total |
| [[higgsfield-ai]] | Cloud API | Reels rápidos, menor control pero mucho más rápido |

## Páginas relacionadas

- [[ai-video-study-plan]] — plan de estudios sobre el área
- [[video-rating-system]] — rating de outputs generados
- [[hunyuan-video-recipe]] — recipe técnico de Hunyuan en ComfyUI
- [[higgsfield-ai]] — cloud API
- [[did-video]] — talking avatars
- [[luz-estudio]] — empresa donde se monetiza este stack
- [[comfyui]] — herramienta base

## Direcciones de exploración

- Wan / I2V para movimiento controlado
- Higgsfield para producción rápida con presets
- Hunyuan para piezas largas con identidad consistente (combinable con [[lora]])

## Estado

Página stub creada por audit (29-04-2026). Pendiente: comparativa cost/calidad/tiempo de cada stack, casos reales de uso en clientes de Luz Estudio, decisión por proyecto.
