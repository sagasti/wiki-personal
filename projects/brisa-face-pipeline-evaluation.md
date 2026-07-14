---
title: "Brisa Face Pipeline Evaluation — Abril 2026"
created: "2026-04-22"
updated: "2026-07-14"
type: "project"
related: [[runpod]], [[brisa]], [[lora-inventory-and-dual-identity]]
---

# Brisa Face Pipeline Evaluation — Abril 2026

## Objetivo
Encontrar la mejor pipeline de generación de caras/cuerpos para el personaje "Brisa" (redhead, pixie cut, freckles, hazel eyes) en ComfyUI.

## Estado 2026-07-13/14
- Preferencia estable (USER): stills **JGG + FaceID → CRPony refine**; video Wan dual MoE (single-noise = horrible).
- **Cloud NSFW no confiable:** OpenArt MCP / Gemini Imagen-Veo / Grok Imagine filtran o flaggean. Adulto real → Comfy local o [[runpod]] H200.
- Modelos del pipeline **ya en network volume** RunPod (`s3://f4uirc6q1f/ComfyUI/models/…`): Juggernaut XL XI 7.1GB, CRPony v160, FaceID SDXL + LoRA, SDXL VAE. Detalle en [[runpod]].
- Sesión Desktop: se intentó batch en pod; Jorge: **“detenelo, seguimos mañana”** — pod stopped. Próximo: `pod.py start` con OK + generar.

## Pipelines Evaluados

### ✅ JuggernautXL + FaceID SDXL + Pony/CRPony Refine (GANADOR ACTUAL)
- **Checkpoint**: juggernautXL_juggXIByRundiffusion.safetensors
- **IP-Adapter**: FaceID SDXL (ip-adapter-faceid_sdxl*.bin + lora)
- **Refine**: Pony V6 XL / **CyberRealisticPony v160**, denoise ~0.2
- **CFG**: 4.5 (low) — menos caricaturesco
- **Resolución**: 768x1344 (portrait) / 1024x1334 (H200)
- **Resultados**: 5 imágenes exitosas (face, body, lingerie, nude, studio)
- **Veredicto**: Mejor pipeline hasta ahora. Mantiene identidad facial, genera cuerpo completo.

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
3. **Pony refine denoise 0.2**: Sweet spot para refinar sin perder identidad. 0.4 demasiado agresivo.
4. **Prompt negativo útil**: "stylized, digital art, 3d render" + positivo "raw unretouched photo"
5. **Resolución vertical**: 768x1344 mejor para fullbody que 1024x1024

## Próximos Pasos
- [ ] Probar FaceID SDXL con Pony refine en H200 (mayor resolución, más calidad)
- [ ] Entrenar LoRA de Brisa con dataset curado (104 imgs approved)
- [ ] Comparar LoRA vs FaceID para consistencia de identidad
- [ ] Armar pipeline prod definitivo en RunPod H200


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
