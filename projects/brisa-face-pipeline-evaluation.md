---
title: "Brisa Face Pipeline Evaluation — Abril 2026"
created: "2026-04-22"
updated: "2026-07-15"
type: "project"
related: [[runpod]], [[brisa]], [[lora-inventory-and-dual-identity]], [[brisa-video-production]], [[wan22-issues]]
---

# Brisa Face Pipeline Evaluation — Abril 2026

## Objetivo
Encontrar la mejor pipeline de generación de caras/cuerpos para el personaje "Brisa" (redhead, pixie cut, freckles, hazel eyes) en ComfyUI.

## Estado producción 2026-07-15
- **Canónico:** [[brisa-video-production]] — nombres `brisa_stills` / `brisa_video`, Desktop `~/Desktop/brisa_prod/`.
- **Stills NSFW (USER + A/B 2026-07-14):** Juggernaut XL + **`brisa_stills` @1.0** + FaceID light (0.85, cara canónica) → **CRPony d=0.4 DualCLIP** (`clip_l`+`clip_g`) + SDXL VAE. Ganó a d=0.25 y a FLUX+ReActor (A/B seeds `42424201`–`04`).
- **CRPony v160 = UNet Diffusers only** → `UNETLoader` + DualCLIP + VAE SDXL externo; **no** `CheckpointLoaderSimple`.
- **Video:** still **distinta por escena** → Wan 2.2 dual MoE + **`brisa_video` @1.0** (alias histórico all6). Single-noise = horrible.
- **Cloud NSFW no confiable:** OpenArt / Gemini / Grok → Comfy local o [[runpod]] H200.
- **Dataset stills train:** `/Volumes/Extra/ComfyUI/brisa/datasets/brisa_sdxl_v1/` (100 PNG+txt, trigger `brisa,`, QC Jorge OK).
- **Pod:** apagado post-batch erótico 6/6 (2026-07-15 ~02:50). No levantar sin OK.

## Pipelines Evaluados

### ✅ JuggernautXL + brisa_stills + FaceID light → CRPony d=0.4 DualCLIP (PROD 2026-07)
- **Base**: juggernautXL_juggXIByRundiffusion.safetensors
- **Identity**: LoRA `brisa_stills` @1.0 + FaceID SDXL light (w≈0.85–1.35 en tests; prod light 0.85)
- **Refine**: CyberRealisticPony v160 via **UNETLoader**, denoise **0.4**, DualCLIP + SDXL VAE
- **Veredicto prod:** identidad + body + skin usable; batch variety + erotic I2V deliverables en `brisa_prod/`

### 🟡 JuggernautXL + FaceID only → Pony (pre-LoRA SDXL, 2026-04→07-14)
- **Checkpoint**: juggernautXL_juggXIByRundiffusion.safetensors
- **IP-Adapter**: FaceID SDXL (ip-adapter-faceid_sdxl*.bin + lora)
- **Refine**: Pony V6 XL / **CyberRealisticPony v160**, denoise histórico ~0.2; **A/B 14/7: d=0.4 DualCLIP gana**
- **Limitaciones (pre-stills LoRA):** FaceID no nativo, two-pass mueve cara, peor consistencia de serie
- **Veredicto**: Ganador pre-`brisa_stills`; ahora plan B / fallback si falta el LoRA

### ❌ PhotoMaker v1 + JuggernautXL
- **Modelo**: photomaker-v1.bin (891MB)
- **Trigger word**: "photomaker" en prompt
- **Problema principal**: Con ref de cara, PhotoMaker sobre-enfoca la cara y genera solo portrait/crop facial
- **Intentos fallidos**:
  - PM_face_front (CFG 7) → solo cara
  - PM_body_front (CFG 7, prompt "full body nude") → solo cara a pesar del prompt
  - PM_face_front_lowcfg (CFG 4.5) → solo cara
  - PM_nude_fullbody (768x1344, CFG 4.5, "wide angle full body shot, head to toes visible") → deforme
  - PM_nude_fullbody_v2 (idem, prompt ajustado) → deforme
- **Veredicto**: Descartado. No genera fullbody, y al forzarlo genera deformaciones.

### ❌ FLUX.1-dev + FNUv2
- **Problema**: No existe IP-Adapter FaceID para FLUX
- **Resultado**: Imágenes deformes, sin identidad facial
- **Veredicto**: Descartado hasta que haya IP-Adapter FaceID para FLUX

### ❌ URPM + IP-Adapter
- **Problema**: URPM es SD1.5 (512×512), incompatible con FaceID SDXL y Pony refine SDXL
- **Veredicto**: Descartado por incompatibilidad de arquitectura

## Lecciones Aprendidas

1. **PhotoMaker vs FaceID**: PhotoMaker está diseñado para face swap/portrait, no para fullbody. FaceID SDXL preserva identidad sin zoom-in facial.
2. **CFG bajo (4.5)**: Mejor que CFG 7 para rostros — menos sobre-enfoque, menos caricaturesco.
3. **Pony refine denoise (2026-07-14):** con DualCLIP + FaceID/stills, **d=0.4 gana a 0.25** (y al path FLUX+ReActor). La lección vieja “0.2 sweet / 0.4 agresivo” queda **superada** en el stack prod actual.
4. **Prompt negativo útil**: "stylized, digital art, 3d render" + positivo "raw unretouched photo"
5. **Resolución vertical**: 768x1344 / 720×1280 video mejor para fullbody que 1024x1024
6. **CRPony v160**: archivo UNet-only Diffusers — siempre DualCLIP + VAE externo
7. **Video**: never single-noise; always dual MoE + still distinta por escena + LoRA `brisa_video`
8. **Al elegir stack/LoRA**: borrar intermedios; keepers en `brisa_prod/`

## Próximos Pasos
- [x] FaceID + Pony refine en H200
- [x] LoRA stills SDXL (`brisa_stills` desde `brisa_sdxl_v1` ~100)
- [x] LoRA video Wan (`brisa_video` / all6)
- [x] Pipeline prod + batch erótico 6/6 en Desktop
- [ ] Iterar calidad / nuevos packs solo si Jorge pide (pod off)


---

## Configuración ganadora actual (Z-Image v4.0, 2pass)


## Pipeline: Z-Image v4.0 2pass

**Date**: 2026-04-21
**Verdict**: Best face/skin quality after extensive testing

### Config
- **UNET**: cyberrealisticZImage_v40.safetensors (CyberRealistic Z-Image v4.0)
- **Text Encoder**: Qwen3-4B-Q8_0.gguf (type: lumina2)
- **VAE**: ae.safetensors (FLUX1/Z-Image)
- **AuraFlow Shift**: **4.0** (tested 3.0, 4.0, 5.0 — 4.0 best balance)
- **CFG**: **1.0**
- **Resolution**: 1024×1334
- **Sampler**: dpmpp_2m_sde

### 2pass Recipe
1. **1st pass**: 9 steps, beta scheduler, add_noise=enable, return_with_leftover_noise=enable
2. **2nd pass**: 9 steps, sgm_uniform scheduler, add_noise=disable, start_at_step=0

### Skin Prompt Reinforcement
"visible pores, skin grain texture, dermatological detail, no smoothing no airbrushing"

### Negative
ConditioningZeroOut (no explicit negative prompt)

### Key Findings
- Shift 3.0: good but less skin detail
- Shift 4.0: **winner** — best skin pore detail without artifacts
- Shift 5.0: too much, artifacts/deformations
- CFG 1.0: most natural, least caricature-like
- FLUX: descartado (censorship NSFW refusals)
- URPM: descartado (SD1.5, 512×512)
- PhotoMaker: descartado (over-focuses on face, can't generate body)

### Pod (RunPod H200)
- Pod ID: c7pdhtx92ttrhe
- SSH: root@103.196.86.21 -p 49191
- Proxy: https://comfi-ui.luz.center
- ComfyUI: localhost:8188
- All models in /workspace/ComfyUI/models/

### Comparison with JGG+FaceID+Pony pipeline
- Z-Image: best skin/face quality, but NO face identity (no FaceID for Z-Image/Lumina2)
- JGG+FaceID+Pony: best identity preservation + good quality, **recommended for Brisa**
- Use Z-Image for generic faces, JGG+FaceID+Pony for character consistency
