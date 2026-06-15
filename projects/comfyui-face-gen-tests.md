---
title: "ComfyUI Face Generation Tests — 19/4/2026"
created: "2026-04-20"
updated: "2026-04-20"
type: "project"
---

# ComfyUI Face Generation Tests — 19/4/2026

## Subject: "Brisa" — redhead, pixie cut, freckles, hazel eyes

---

## Batch 1: CRPony (JuggernautXL v11) ✅ MEJOR RESULTADO

| Archivo | CFG | Steps | Sampler | Size | Nota |
|---------|-----|-------|---------|------|------|
| CRPony_face_front | 5.0 | 30 | dpmpp_sde_gpu | 896×1152 | ✅ Bueno |
| CRPony_face_34 | 5.0 | 30 | dpmpp_sde_gpu | 896×1152 | ✅ Bueno |
| CRPony_face_profile | 5.0 | 30 | dpmpp_sde_gpu | 896×1152 | ✅ Bueno |

**Prompt positivo:**
```
score_9, score_8_up, score_7_up, photorealistic, masterpiece, 1girl, solo, redhead, short red hair, pixie cut, messy short hair, freckles, light skin freckles across nose and cheeks, subtle wrinkles, fine lines around eyes, realistic skin texture, pores visible, hazel eyes, brown-green eyes, detailed eyes, natural makeup, face portrait, closeup, looking at viewer, soft lighting, studio lighting, shallow depth of field
```

**Prompt negativo:**
```
score_6, score_5, score_4, blurry, cartoon, anime, painting, deformed, bad anatomy, bad hands, extra fingers, smooth skin, plastic skin, airbrushed, worst quality, low quality
```

**Checkpoint:** `juggernautXL_juggXIByRundiffusion.safetensors`

---

## Batch 2: JGG (JuggernautXL v11) ✅ BUENO

| Archivo | CFG | Steps | Sampler | Size | Nota |
|---------|-----|-------|---------|------|------|
| JGG_face_front_skin | 5.0 | 30 | dpmpp_sde_gpu | 896×1152 | ✅ Bueno, skin detail extra |
| JGG_face_front_cfg7 | 7.0 | 30 | dpmpp_sde_gpu | 896×1152 | ✅ Bueno pero más estilizado |

**Prompt positivo (skin variant — más énfasis en textura):**
```
score_9, score_8_up, score_7_up, photorealistic, masterpiece, 1girl, solo, redhead, short red hair, pixie cut, messy short hair, freckles, light skin freckles across nose and cheeks, subtle wrinkles, fine lines around eyes, realistic skin texture, pores visible, skin imperfections, subtle skin texture, micro details, hazel eyes, brown-green eyes, detailed eyes, natural makeup, face portrait, closeup, looking at viewer, soft lighting, studio lighting, shallow depth of field, detailed skin, skin microtexture, skin imperfections, subtle skin texture, micro details
```

**Prompt negativo (enhanced):**
```
score_6, score_5, score_4, blurry, cartoon, anime, painting, deformed, bad anatomy, bad hands, extra fingers, smooth skin, plastic skin, airbrushed, oversmoothed, wax skin, doll skin, worst quality, low quality
```

**Checkpoint:** `juggernautXL_juggXIByRundiffusion.safetensors`

---

## Batch 3: ZImage (CyberRealistic Z-Image v4) ❌ DEGRADADO

| Archivo | CFG | Steps | Sampler | Size | Nota |
|---------|-----|-------|---------|------|------|
| ZImage_test_00001 | 4.0 | 20 | euler | 1024×1024 | ❌ Otra mujer, no Brisa |
| ZImage_test_00002 | 4.0 | 20 | euler | 1024×1024 | ❌ Otra mujer |

**Prompt positivo (simple):**
```
a beautiful woman, portrait, detailed face, high quality
```

**Problemas:**
- Prompt genérico → no genera a "Brisa", genera mujer random
- Solo 20 steps
- Arquitectura Lumina2 (CLIPLoaderGGUF type=lumina2) — correcto
- TE: qwen3_4b_q8_0.gguf, VAE: FLUX1/ae.safetensors

**Checkpoint:** `cyberrealisticZImage_v40.safetensors`

---

## Batch 4: FNU (FluxNSFW v3 FP16) ❌ MUY DEFORME

| Archivo | CFG | Steps | Sampler | Size | Nota |
|---------|-----|-------|---------|------|------|
| FNU_test | 3.5 | 20 | euler | 896×1152 | ❌ Deforme |
| FNU_face_front | 3.5 | 20 | euler | 896×1152 | ❌ Deforme |
| FNU_face_34 | 3.5 | 20 | euler | 896×1152 | ❌ Deforme |
| FNU_face_profile | 3.5 | 20 | euler | 896×1152 | ❌ Deforme |
| FNU_upper_skin | 3.5 | 20 | euler | 896×1152 | ❌ Deforme |
| FNU_skin_cfg2 | 2.0 | 25 | euler | 1024×1024 | ❌ Prompt distinto, still bad |
| FNU_skin_cfg15 | 1.5 | 25 | euler | 1024×1024 | ❌ Nombre dice cfg15 pero real=1.5 |
| FNU_skin_cfg25 | 2.5 | 30 | euler | 1024×1024 | ❌ Nombre dice cfg25 pero real=2.5 |

**Prompt positivo (caras — mismo que JGG):**
```
score_9, score_8_up, score_7_up, photorealistic, masterpiece, 1girl, solo, redhead, short red hair, pixie cut, messy short hair, freckles, light skin freckles across nose and cheeks, subtle wrinkles, fine lines around eyes, realistic skin texture, pores visible, skin imperfections, subtle skin texture, micro details, hazel eyes, brown-green eyes, detailed eyes, natural makeup, face portrait, closeup, looking at viewer, soft lighting, studio lighting, shallow depth of field, detailed skin, skin microtexture
```

**Prompt positivo (skin tests — prompt distinto!):**
```
brisa, young woman, detailed skin texture, skin pores visible, subsurface scattering, realistic skin, natural skin tone, photorealistic, raw photo, unretouched, portrait, beautiful face, high quality
```

**Problemas:**
- `score_9, score_8_up` etc. son tags de Pony Diffusion — **NO funcionan en FLUX**
- FLUX no usa negative prompts de la misma forma que SDXL
- Solo 20 steps para caras (poco)
- Sampler euler — FLUX suele ir mejor con euler_simple o euler_beta
- DualCLIPLoader type=flux ✅ correcto
- TE: t5xxl_fp8 + clip_l, VAE: FLUX1/ae ✅

**Checkpoint:** `fluxNSFWUNLOCKED_v30FP16.safetensors`

---

## Lecciones aprendidas

1. **JuggernautXL (SDXL)** = mejor para caras fotorrealistas con CFG 5-7, dpmpp_sde_gpu, 30 steps
2. **Score tags** (score_9, score_8_up...) son específicos de Pony/SDXL — **no usar en FLUX ni Z-Image**
3. **FLUX** necesita prompts en lenguaje natural, sin negative prompt fuerte, CFG 1-4, steps 20-30
4. **Z-Image** (Lumina2) necesita CLIPLoaderGGUF type=lumina2, prompts simples en lenguaje natural
5. **Los nombres de archivo FNU mienten** — cfg15 real era 1.5, cfg25 real era 2.5 (desync entre nombre y parámetro real)
6. **Negative prompts** solo útiles en SDXL, en FLUX se ignoran o empeoran
