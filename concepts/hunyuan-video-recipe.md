---
title: "Hunyuan Video Recipe"
created: "2026-04-26"
updated: "2026-04-26"
type: "concept"
tags: ["#reference", "#ai", "#comfyui", "#video"]
date: "2026-04-26"
source: "MEMORY.md rotation (weekly maintenance)"
---

# Hunyuan Video Recipe

## Configuración clave
- **ModelSamplingFlux:** max_shift=2.05, base_shift=0.95 → **CLAVE para motion**
- **CFG:** 6.0
- **Scheduler:** simple
- **Negative prompt:** "static still image no motion"
- **LoRA:** berchu_40 al 85%

## Advertencias
- **Sin ModelSamplingFlux = sin movimiento**
- **CFG alto + LoRA = ruido** → si hay LoRA, bajar CFG a ~1.0
- **bf16 full** ~2h para 257 frames en H200

## Ver también
- [[runpod]] — GPU setup
- [[comfyui]] — Setup local

---
*Promovido desde MEMORY.md el 2026-04-26 (mantenimiento semanal)*
