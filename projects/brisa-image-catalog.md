---
title: "Brisa — Catálogo de Imágenes Generadas"
created: "2026-04-20"
updated: "2026-04-21"
type: "project"
---

# Brisa — Catálogo de Imágenes Generadas

**Personaje:** Brisa — redhead, pixie cut (short copper red bob), freckles, hazel-green eyes, slim athletic build
**Ref image:** `brisa_face_ref_v2.jpg`
**Fecha:** 2026-04-19 / 2026-04-20

---

## Cómo leer este documento

Cada entrada tiene:
- **Archivo** — nombre del PNG
- **Pipeline** — qué modelos y técnica se usó
- **Params** — CFG, steps, denoise, sampler
- **Res** — resolución
- **Veredicto** — ✅ gusta / ❌ no gusta / ⏳ pendiente evaluar
- **Notas** — observaciones

---

## Legacy (OpenClaw era)

### Pipeline A: JuggernautXL + FaceID (baseline)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `character-sheet/brisa_sheet_*.png` (8 poses) | CFG ?, 40s, DPM++ 2M Karras | 896×1152 | ❌ | Skin smooth/plastic, correct face |

### Pipeline C: JGG + FaceID → img2img refine (2-pass)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `quality-tests/brisa_quality_face_front_00001_.png` | CFG ?, 50s + refine d=0.25 30s | ? | ✅ | Better skin texture, correct face |
| `quality-tests/brisa_quality_body_front_00001_.png` | same | ? | ⏳ | |
| `quality-tests/brisa_quality_lingerie_00001_.png` | same | ? | ⏳ | |
| `quality-tests/brisa_quality_nude_studio_00001_.png` | same | ? | ⏳ | |
| `quality-tests/pony_full_test_00001_.png` | CRPony, no FaceID | ? | ❌ | Best skin but different person each time |

### Pipeline E: JGG + FaceID → Pony refine d=0.4 (2-model) ★ MEJOR HISTÓRICO
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `2model-pipeline/brisa_2model_face_00001_.png` | JGG 50s → CRPony refine d=0.4 40s | ? | ✅✅ | Best skin + face identity. Jorge liked face close-up |
| `2model-pipeline/brisa_2model_body_00001_.png` | same | ? | ⏳ | d=0.4 changes face too much in body shots |
| `2model-pipeline/brisa_2model_lingerie_00001_.png` | same | ? | ⏳ | |
| `2model-pipeline/brisa_2model_nude_studio_00001_.png` | same | ? | ⏳ | |

### Pipeline F: JGG + FaceID → Pony refine d=0.2
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `brisa_lowcfg_face_jugg_lowcfg_00001_.png` | JGG CFG 4.5 → CRPony d=0.2 | ? | ⏳ | Preserves face better |
| `brisa_lowcfg_body_jugg_lowcfg_00001_.png` | same | ? | ⏳ | |

### Scenarios (upscaled 4x, ~28-32MB each)
| Archivo | Pipeline | Veredicto | Notas |
|---|---|---|---|
| `scenarios/brisa_flow_bikini_beach_00001_.png` | Pipeline E + upscale | ⏳ | |
| `scenarios/brisa_flow_dress_urban_00001_.png` | same | ⏳ | |
| `scenarios/brisa_flow_lingerie_bed_00001_.png` | same | ⏳ | |
| `scenarios/brisa_flow_nude_reclined_00001_.png` | same | ⏳ | |
| `scenarios/brisa_flow_nude_studio_00001_.png` | same | ⏳ | |
| `scenarios/brisa_flow_topless_jeans_00001_.png` | same | ⏳ | |

---

## Hermes (2026-04-19) — Primer batch: modelo comparison sin FaceID/PhotoMaker

### JGG (JuggernautXL v11)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `JGG_face_front_cfg7_00001_.png` | CFG 7, 50s, euler_ancestral | 896×1152 | ⏳ | Sin FaceID, sin identidad |
| `JGG_face_front_skin_00001_.png` | skin realism prompt | 896×1152 | ⏳ | |

### CRPony (CyberRealisticPony v1.6)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `CRPony_face_front_00001_.png` | CFG 7, 50s | 896×1152 | ⏳ | |
| `CRPony_face_34_00001_.png` | same | 896×1152 | ⏳ | |
| `CRPony_face_profile_00001_.png` | same | 896×1152 | ⏳ | |

### FNU (FluxNudeUncovered — FLUX, descartado)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `FNU_face_front_00001_.png` | FLUX | ? | ❌ | FLUX descartado: sin FaceID, deforme |
| `FNU_face_34_00001_.png` | same | ? | ❌ | |
| `FNU_face_profile_00001_.png` | same | ? | ❌ | |
| `FNU_skin_cfg15_normal_25s_00001_.png` | CFG 1.5 | ? | ❌ | |
| `FNU_skin_cfg25_normal_30s_00001_.png` | CFG 2.5 | ? | ❌ | |
| `FNU_skin_cfg2_normal_25s_00001_.png` | CFG 2 | ? | ❌ | |
| `FNU_test_00001_.png` | ? | ? | ❌ | |
| `FNU_upper_skin_00001_.png` | ? | ? | ❌ | |

### FNUv2 (FLUX corrective, descartado)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `FNUv2_face_front_cfg25_00001_.png` | CFG 2.5, natural lang prompt | ? | ❌ | Still deforme |
| `FNUv2_face_front_cfg35_00001_.png` | CFG 3.5 | ? | ❌ | |

### ZImage (Lumina2 arch, descartado)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `ZImage_test_00001_.png` | ? | ? | ❌ | |
| `ZImage_test_00002_.png` | ? | ? | ❌ | |

---

## Hermes (2026-04-20) — PhotoMaker tests

### PhotoMaker + JuggernautXL (sin nude)
| Archivo | Params | Res | Veredicto | Notas |
|---|---|---|---|---|
| `PM_face_front_00001_.png` | JGG + PM, CFG 7, 50s | 768×768 | ⏳ | |
| `PM_body_front_00001_.png` | JGG + PM, CFG 7, "full body nude" | 768×1024 | ❌ | Generó con ropa, JGG censura nudity |
| `PM_face_front_lowcfg_00001_.png` | JGG + PM, CFG 4.5, 50s | 768×768 | ⏳ | |
| `PM_nude_fullbody_00001_.png` | JGG + PM, CFG 4.5, 768×1344, wide angle | 768×1344 | ❌ | Still clothed, PhotoMaker zoom in on face |
| `PM_nude_fullbody_v2_00001_.png` | same, different seed | 768×1344 | ❌ | Same issues |

---

## Hermes (2026-04-20) — Nude pipeline comparison ⏳ GENERATING

**Prompt positivo (común a todos):**
> wide angle full body shot, nude woman standing, head to toes visible, entire body in frame, short copper red bob hair, hazel green eyes, freckles, slim athletic build, standing facing camera, arms relaxed at sides, full frontal nude, bare breasts, bare legs, bare feet visible, fine skin pores, visible skin micro-texture, natural skin imperfections, subsurface scattering, neutral grey background, soft studio lighting, photorealistic, raw unretouched photo, 8k uhd, dslr quality

**Prompt negativo (común):**
> cartoon, anime, illustration, painting, deformed, ugly, bad anatomy, bad proportions, extra limbs, extra fingers, mutated hands, smooth skin, plastic skin, airbrushed, oversmooth, stylized, digital art, 3d render, blurry, clothed, clothing, dressed

| Opción | Archivo | Pipeline | Params | Res | Veredicto | Notas |
|---|---|---|---|---|---|---|
| B | `OPT_B_CRPony_PM_nude_00001_.png` | CRPony v160 + PhotoMaker | CFG 4.5, 50s | 768×1344 | ⏳ | Pony debería generar nude |
| C | `OPT_C_2pass_JGG_PM_PonyRefine_00001_.png` | JGG + PM → CRPony refine d=0.7 | Pass1: CFG 4.5 50s, Pass2: CFG 4.5 30s d=0.7 | 768×1344 | ⏳ | 2-pass, Pony refine con denoise alto para quitar ropa |
| D | `OPT_D_RV60_PM_nude_00001_.png` | Realistic Vision v6.0 B1 + PhotoMaker | CFG 4.5, 50s | 768×1344 | ⏳ | RV6 conocido para realismo |
| E | `OPT_E_CyberRealistic_PM_nude_00001_.png` | CyberRealistic Final + PhotoMaker | CFG 4.5, 50s | 768×1344 | ⏳ | CyberRealistic sin Pony merge |

---

## Modelos disponibles

| Modelo | Path | Tipo | Notas |
|---|---|---|---|
| JuggernautXL v11 | `juggernautXL_juggXIByRundiffusion.safetensors` | SDXL | Buen realismo, censura nude |
| CRPony v1.6 | `Pony/cyberrealisticPony_v160.safetensors` | SDXL (Pony) | NSFW OK, no embedded CLIP/VAE |
| Realistic Vision v6.0 B1 | `realisticVisionV60B1_v60B1VAE.safetensors` | SDXL | 2GB, realismo extremo |
| CyberRealistic Final | `cyberrealistic_final.safetensors` | SDXL | 4GB, realismo extremo |
| PhotoMaker v1 | `photomaker/photomaker-v1.bin` | — | Identity transfer, trigger word "photomaker" |
| IP-Adapter FaceID SDXL | `ipadapter/ip-adapter-faceid_sdxl.bin` | — | Identity transfer, face weight 1.8 |

---

## Decisiones tomadas

- **FLUX descartado** — sin IP-Adapter FaceID para FLUX, no hay forma de mantener identidad
- **URPM descartado** — es SD1.5 (512×512), incompatible con FaceID SDXL y Pony refine SDXL
- **JGG censura nude** — genera ropa a pesar de prompt explícito
- **PhotoMaker zoom-in** — con ref de cara, tiende a generar solo face/upper body
- **Pipeline E histórico** (JGG + FaceID → Pony refine d=0.4) = mejor resultado hasta ahora
