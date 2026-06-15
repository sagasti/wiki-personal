---
title: "Brisa — Evaluación de Imágenes"
created: "2026-04-20"
updated: "2026-04-29"
type: "project"
---

# Brisa — Evaluación de Imágenes

Jorge evalúa cada imagen y yo anoto su feedback.
Veredictos: ✅ gusta | ❌ no | ⚠️ parcial | ⏳ pendiente

---

## #01 — Pipeline E: JGG + FaceID → CRPony d=0.4 — FACE
- **Archivo:** `2model-pipeline/brisa_2model_face_00001_.png`
- **Pipeline:** JuggernautXL + IP-Adapter FaceID (w=1.8) → CRPony refine denoise 0.4, 40 steps
- **Veredicto:** ⏳
- **Notas Jorge:**

## #02 — Pipeline E: JGG + FaceID → CRPony d=0.4 — BODY
- **Archivo:** `2model-pipeline/brisa_2model_body_00001_.png`
- **Pipeline:** mismo que #01
- **Veredicto:** ⏳
- **Notas Jorge:**

## #03 — Pipeline E: JGG + FaceID → CRPony d=0.4 — LINGERIE
- **Archivo:** `2model-pipeline/brisa_2model_lingerie_00001_.png`
- **Pipeline:** mismo que #01
- **Veredicto:** ⏳
- **Notas Jorge:**

## #04 — Pipeline E: JGG + FaceID → CRPony d=0.4 — NUDE STUDIO
- **Archivo:** `2model-pipeline/brisa_2model_nude_studio_00001_.png`
- **Pipeline:** mismo que #01
- **Veredicto:** ⏳
- **Notas Jorge:**

## #05 — Pipeline C: JGG + FaceID → refine d=0.25 — FACE
- **Archivo:** `quality-tests/brisa_quality_face_front_00001_.png`
- **Pipeline:** JuggernautXL + FaceID → img2img refine denoise 0.25, 30 steps
- **Veredicto:** ⏳
- **Notas Jorge:**

## #06 — Pipeline C: JGG + FaceID → refine d=0.25 — BODY
- **Archivo:** `quality-tests/brisa_quality_body_front_00001_.png`
- **Pipeline:** mismo que #05
- **Veredicto:** ⏳
- **Notas Jorge:**

## #07 — Pipeline C: JGG + FaceID → refine d=0.25 — NUDE STUDIO
- **Archivo:** `quality-tests/brisa_quality_nude_studio_00001_.png`
- **Pipeline:** mismo que #05
- **Veredicto:** ⏳
- **Notas Jorge:**

## #08 — Pipeline F: JGG + FaceID → CRPony d=0.2, CFG 4.5 — FACE
- **Archivo:** `brisa_lowcfg_face_jugg_lowcfg_00001_.png`
- **Pipeline:** JGG + FaceID → CRPony refine denoise 0.2, CFG 4.5
- **Veredicto:** ⏳
- **Notas Jorge:**

## #09 — Pipeline F: JGG + FaceID → CRPony d=0.2, CFG 4.5 — BODY
- **Archivo:** `brisa_lowcfg_body_jugg_lowcfg_00001_.png`
- **Pipeline:** mismo que #08
- **Veredicto:** ⏳
- **Notas Jorge:**

## #10 — PhotoMaker + JGG, CFG 7 — FACE FRONT
- **Archivo:** `PM_face_front_00001_.png`
- **Pipeline:** JuggernautXL + PhotoMaker v1, CFG 7, 50 steps
- **Veredicto:** ⏳
- **Notas Jorge:**

## #11 — PhotoMaker + JGG, CFG 4.5 — FACE FRONT
- **Archivo:** `PM_face_front_lowcfg_00001_.png`
- **Pipeline:** JuggernautXL + PhotoMaker v1, CFG 4.5, 50 steps
- **Veredicto:** ⏳
- **Notas Jorge:**

## #12 — PhotoMaker + JGG, CFG 7 — BODY FRONT (prompt nude, salió vestida)
- **Archivo:** `PM_body_front_00001_.png`
- **Pipeline:** JGG + PhotoMaker v1, CFG 7, prompt "full body nude"
- **Veredicto:** ⏳
- **Notas Jorge:** JGG censura nude, generó con ropa

## #13 — Opción D: Realistic Vision v6.0 B1 + PhotoMaker, CFG 4.5 — NUDE
- **Archivo:** `OPT_D_RV60_PM_nude_00001_.png`
- **Pipeline:** Realistic Vision v6.0 B1 + PhotoMaker v1, CFG 4.5, 50 steps
- **Veredicto:** ⏳
- **Notas Jorge:**

## #14 — Opción B: CRPony v160 + PhotoMaker, CFG 4.5 — NUDE
- **Archivo:** `OPT_B_CRPony_PM_nude_00001_.png`
- **Pipeline:** CyberRealisticPony v1.6 + PhotoMaker v1, CFG 4.5, 50 steps
- **Veredicto:** ⏳
- **Notas Jorge:**

## #15 — Opción C: JGG + PhotoMaker → CRPony refine d=0.7 — NUDE
- **Archivo:** `OPT_C_2pass_JGG_PM_PonyRefine_00001_.png`
- **Pipeline:** JGG + PhotoMaker (50s) → CRPony refine denoise 0.7 (30s)
- **Veredicto:** ⏳
- **Notas Jorge:**

## #16 — Opción E: CyberRealistic Final + PhotoMaker, CFG 4.5 — NUDE
- **Archivo:** `OPT_E_CyberRealistic_PM_nude_00001_.png`
- **Pipeline:** CyberRealistic Final + PhotoMaker v1, CFG 4.5, 50 steps
- **Veredicto:** ⏳
- **Notas Jorge:**

---

## Resumen de decisiones

| # | Pipeline | Veredicto | Key insight |
|---|---|---|---|
| 01 | E: JGG+FaceID→CRPony d=0.4 face | ⏳ | |
| 02 | E: JGG+FaceID→CRPony d=0.4 body | ⏳ | |
| 03 | E: JGG+FaceID→CRPony d=0.4 lingerie | ⏳ | |
| 04 | E: JGG+FaceID→CRPony d=0.4 nude | ⏳ | |
| 05 | C: JGG+FaceID→refine d=0.25 face | ⏳ | |
| 06 | C: JGG+FaceID→refine d=0.25 body | ⏳ | |
| 07 | C: JGG+FaceID→refine d=0.25 nude | ⏳ | |
| 08 | F: JGG+FaceID→CRPony d=0.2 face | ⏳ | |
| 09 | F: JGG+FaceID→CRPony d=0.2 body | ⏳ | |
| 10 | PM+JGG CFG7 face | ⏳ | |
| 11 | PM+JGG CFG4.5 face | ⏳ | |
| 12 | PM+JGG CFG7 body (vestida) | ⏳ | |
| 13 | D: RV6+PM nude | ⏳ | |
| 14 | B: CRPony+PM nude | ⏳ | |
| 15 | C: JGG+PM→CRPony d=0.7 nude | ⏳ | |
| 16 | E: CyberRealistic+PM nude | ⏳ | |


---

## Histórico — Comparativa OpenClaw vs Hermes inicial


> **Historical comparison** (2026-04-19/20): OpenClaw-era pipelines vs initial Hermes tests.
> OpenClaw has since been fully migrated to Hermes. The pipeline techniques described here
> (FaceID, 2-pass, 2-model) are being re-implemented as Hermes skills.

## Dos sistemas comparados

| | **OpenClaw (viejo)** | **Hermes (nuevo, 19/4)** |
|---|---|---|
| **Modelo base** | JuggernautXL v11 (SDXL) | JuggernautXL v11 (SDXL) + FLUX + Z-Image |
| **Face identity** | ✅ IP-Adapter FaceID (weight 1.8) + ref image | ❌ Sin FaceID, solo prompt |
| **2-pass refine** | ✅ img2img con denoise 0.25 | ❌ Single pass |
| **2-model pipeline** | ✅ Juggernaut → Pony refine (d=0.4 y d=0.2) | ❌ No implementado |
| **Pony skin quality** | ✅ Usado como refine pass | ✅ Usado como modelo principal (CRPony) |
| **FLUX** | ❌ No probado | ❌ Probado, deformado (prompts incorrectos) |
| **Upscale+Sharpen** | ✅ 4x-UltraSharp + ImageSharpen | ❌ No implementado |
| **Sampler** | dpmpp_3m_sde + Karras | dpmpp_sde_gpu (SDXL) / euler (FLUX) |
| **Steps** | 50 (base) + 30 (refine) | 20-30 (single pass) |
| **Prompts** | Lenguaje natural + "8k uhd, dslr quality, raw photo" | Score tags (SDXL OK) / lenguaje natural (FLUX) |
| **Negative prompt** | ✅ Detallado y efectivo | ✅ SDXL sí / FLUX vacío (correcto) |
| **Scripts reproducibles** | ✅ 8 scripts Python con todo hardcoded | ❌ Workflows ad-hoc, no scripts |
| **Documentación** | ✅ README con 6 pipelines A-F | ⚠️ Wiki con análisis pero sin pipelines definidos |
| **Cara ref** | ✅ brisa_face_ref_v2.jpg | ❌ No hay |

---

## Pipelines OpenClaw (6 variantes documentadas)

### Pipeline A: JuggernautXL + FaceID (baseline)
- 40 steps, DPM++ 2M Karras
- ✅ Rápido, cara correcta
- ❌ Skin smooth/plastic

### Pipeline B: JuggernautXL + FaceID + Upscale + Sharpen
- 40 steps → 4x-UltraSharp (2x) → ImageSharpen
- ✅ Más detalle, cara correcta
- ❌ Skin still somewhat smooth

### Pipeline C: JuggernautXL + FaceID + img2img refine (2-pass) ⭐
- 50 steps DPM++ 3M SDE → img2img refine (denoise 0.25, 30 steps)
- ✅ Mejor skin texture, cara correcta
- ✅ **Jorge liked this**
- ❌ Más lento (~10 min/image)

### Pipeline D: CyberRealisticPony v1.6 (no FaceID)
- 50 steps DPM++ 3M SDE → img2img refine
- ✅ Best skin texture (visible pores, subsurface scattering)
- ❌ No face identity — different person each time

### Pipeline E: JuggernautXL + FaceID → Pony refine (2-model, d=0.4) ⭐
- Juggernaut 50 steps → Pony img2img (denoise 0.4, 40 steps)
- ✅ Best skin + face identity
- ✅ **Jorge liked the face close-up**
- ❌ denoise 0.4 changes face too much in body shots

### Pipeline F: JuggernautXL + FaceID → Pony refine (2-model, d=0.2)
- Juggernaut 50 steps → Pony img2img (denoise 0.2, 30 steps)
- 🔄 En progreso al momento de evaluación
- Goal: preserve face identity better while still getting Pony skin quality

---

## Pipelines Hermes (19/4 tests)

### CRPony (SDXL, score tags)
- JuggernautXL, CFG 5, dpmpp_sde_gpu, 30 steps
- ✅ Mejor resultado del batch nuevo
- ⚠️ Sin FaceID → no es "Brisa", es una mujer random con features parecidos

### JGG (SDXL, score tags + skin detail)
- JuggernautXL, CFG 5 y 7, dpmpp_sde_gpu, 30 steps
- ✅ Bueno, más skin detail tags
- ⚠️ Sin FaceID → misma limitación

### ZImage (Lumina2)
- CyberRealisticZImage v4, CFG 4, euler, 20 steps
- ❌ Prompt genérico → otra persona
- ❌ Solo 20 steps

### FNU (FluxNSFW v3)
- FluxNSFW v3 FP16, CFG 1.5-3.5, euler, 20-30 steps
- ❌ Muy deforme en todas las variantes
- ❌ Score tags no funcionan en FLUX
- ❌ Sin FaceID

### FNUv2 (FluxNSFW v3, prompts corregidos) — ENCOLADO
- FLUX con lenguaje natural, sin score tags, CFG 1.5-3.5
- 🔄 Pendiente de evaluación

---

## Veredicto

**OpenClaw gana claramente en calidad y consistencia por 3 razones clave:**

1. **IP-Adapter FaceID** — La diferencia fundamental. Sin esto, no hay identidad de personaje. Todos los tests Hermes generan una mujer distinta cada vez.

2. **2-pass / 2-model pipeline** — El refine pass (Pony o img2img) es lo que da la skin quality. Single-pass no llega.

3. **Scripts reproducibles** — Los 8 scripts Python con seeds, prompts, y parámetros hardcoded permiten volver a cualquier resultado exacto.

**Lo que Hermes tiene a favor:**
- Más modelos probados (FLUX, Z-Image)
- Documentación analítica en wiki
- Mejor entendimiento de qué NO funciona (score tags en FLUX, CFG alto en FLUX)

**Recomendación:**
- Migrar los scripts a Hermes (ya copiados a `~/wiki/projects/brisa-character-archive/`)
- Implementar Pipeline E/F (2-model) como skill de Hermes
- Agregar IP-Adapter FaceID a los tests FLUX
- Probar FLUX + FaceID + Pony refine como Pipeline G

---

## FNUv2 Results (FLUX + natural language prompts) — 20/4/2026

**Veredicto: ❌ FLUX (FluxNSFW v3) no funciona para Brisa**

| Archivo | CFG | Steps | Resultado |
|---------|-----|-------|-----------|
| FNUv2_face_front_cfg35 | 3.5 | 25 | ❌ Deforme, no le gusta a Jorge |
| FNUv2_face_front_cfg25 | 2.5 | 25 | ❌ En progreso, cancelado |
| FNUv2_face_front_cfg15 | 1.5 | 25 | ❌ Cancelado |
| FNUv2_brisa_cfg35 | 3.5 | 25 | ❌ Cancelado |
| FNUv2_skin_detail_cfg35 | 3.5 | 30 | ❌ Cancelado |

**Razones del fracaso FLUX:**
1. **No hay IP-Adapter FaceID para FLUX** — Solo existe para SDXL. Sin esto, no hay identidad de personaje
2. **FluxNSFW v3 FP16** produce caras deformes incluso con CFG correcto y prompts en lenguaje natural
3. **FLUX en MPS (Mac)** es inestable — se cuelga, OOM, lento
4. Score tags no funcionan (confirmado), pero incluso sin ellos los resultados son malos

**Conclusión: FLUX descartado para Brisa local.** Probar en RunPod H200 con bf16 full si se quiere insistir, pero sin FaceID no hay identidad.

**Path forward: SDXL (JuggernautXL + FaceID + Pony refine) es el camino.**

---

## PhotoMaker v1 Results — 20/4/2026

**Veredicto: ❌ PhotoMaker no funciona para fullbody, solo genera portraits**

| Archivo | CFG | Resolución | Prompt | Resultado |
|---------|-----|------------|--------|-----------|
| PM_face_front_00001_ | 7 | 768x1344 | "photomaker portrait" | ❌ Solo cara (esperado) |
| PM_body_front_00001_ | 7 | 768x1344 | "photomaker full body nude" | ❌ Solo cara a pesar del prompt |
| PM_face_front_lowcfg_00001_ | 4.5 | 768x1344 | "photomaker portrait" | ❌ Solo cara |
| PM_nude_fullbody_00001_ | 4.5 | 768x1344 | "wide angle full body shot, head to toes visible" | ❌ Deforme |
| PM_nude_fullbody_v2_00001_ | 4.5 | 768x1344 | idem + ajustes | ❌ Deforme |

**Razones del fracaso PhotoMaker:**
1. **Sobre-enfoque facial**: Con ref de cara, PhotoMaker amplía la cara y genera solo crop/portrait
2. **No respeta prompt de fullbody**: Incluso con "full body nude, head to toes visible" genera solo cara
3. **Al forzar fullbody**: Genera deformaciones (proporciones incorrectas, artefactos)
4. **CFG bajo no ayuda**: CFG 4.5 mejora un poco vs 7 pero no resuelve el zoom-in

**Conclusión: PhotoMaker descartado para fullbody.** Útil solo para face swap/portrait.

---

## Resumen Final de Pipelines (22/4/2026)

| Pipeline | Face Identity | Fullbody | Calidad | Estado |
|----------|--------------|----------|---------|--------|
| JGG + FaceID + Pony refine (d=0.2) | ✅ | ✅ | ⭐⭐⭐ | **GANADOR** |
| JGG + FaceID + Pony refine (d=0.4) | ⚠️ | ✅ | ⭐⭐ | OK, pierde cara en body shots |
| PhotoMaker v1 | ✅ (cara) | ❌ | ⭐ | Descartado |
| FLUX FNUv2 | ❌ | ❌ | ⭐ | Descartado |
| URPM + IPAdapter | ❌ | ❌ | — | Incompatible SD1.5/SDXL |

**Pipeline ganador: JuggernautXL + FaceID SDXL + Pony V6 XL refine (denoise 0.2)**
