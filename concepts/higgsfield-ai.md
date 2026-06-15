---
title: "Higgsfield AI"
created: "2026-04-19"
updated: "2026-05-17"
type: "concept"
tags: ["#concept", "#ai-video", "#cloud-api"]
related: [[RunPod]], [[comfyui]]
---

# Higgsfield AI

- **Qué es:** Cloud API para image/video generation (async REST)
- **Modelos:** Kling 2.1 Pro I2V, Seedance 1.0 Pro I2V, DoP (Dance of Pixels), Soul T2I
- **Workflow:** generar base image local → animar vía API → Reel
- **Ventajas:** no necesita pod, Kling/Seedance no disponibles local, pay-per-use
- **Unknowns:** pricing, LoRA support, video duration limits
- **Docs:** https://docs.higgsfield.ai/how-to/introduction
- **Estado:** registrado y testeado
- **Account:** jorge@sagasti.com (Plus, 1000cr/mo)
- **Soul IDs:**
  - Jorge soul_2: `334f6664`
  - Jorge soul_cinematic: `6fc434cc`
  - Bere soul_cinematic: `88b5d94d`
  - Bere soul_2: `0e51cf22` ⚠️ contaminated
- **Soul Cinematic gotcha:** `--medias` param unsolved (complex JSON). Ver skill `media-generation-apis`.
