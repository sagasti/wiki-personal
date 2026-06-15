---
title: "Luz Estudio"
created: "2026-04-29"
updated: "2026-05-07"
type: "entity"
tags: ["#organization", "#jorge", "#video", "#ai-video", "#b2b"]
related: [[jorge-sagasti]], [[ai-video-generation]], [[did-video]], [[higgsfield-ai]], [[hunyuan-video-recipe]], [[luz-estudio-workspace]]
---

# Luz Estudio

Empresa propia de Jorge para servicios de video con IA. Modelo B2B servicio puntual (no SaaS), targeting agencias publicitarias argentinas.

## Stack productivo

| Pieza | Tecnología | Cuándo se usa |
|---|---|---|
| Talking avatar / lipsync | [[did-video]] (D-ID) | Proyectos con foto + audio, casos puntuales |
| Cloud API rápida | [[higgsfield-ai]] | Reels rápidos con presets, menor control |
| Local heavy production | ComfyUI + [[hunyuan-video-recipe]] | Producción pesada, control total, [[runpod]] H200 |

Ver umbrella en [[ai-video-generation]].

## Posicionamiento

- B2B, no SaaS
- Servicio puntual, no contrato continuo
- Target: agencias publicitarias argentinas
- Diferencial: combinar 3 stacks (cloud rápido + local heavy + talking avatars) según el brief

## Workspace técnico

La infra de producción (pods H200, ComfyUI, network volume 200GB, modelos, skills) vive en repo aparte: ver [[luz-estudio-workspace]]. Esa página tiene los detalles de stack, preferencias de calidad y skills de Claude Code.

## Estado

Página stub creada por audit (29-04-2026). Workspace técnico documentado el 2026-05-07. Pendiente: clientes activos, casos terminados, pipeline comercial, pricing, contratos.
