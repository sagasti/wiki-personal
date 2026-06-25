# Brisa Character — Catálogo Completo de Generaciones

_Cada entrada tiene: archivo, path, pipeline, parámetros, y workflow para reproducir._

## ⭐ Avatar oficial actual (2026-06-04)
`brisa-avatar-oficial.png` — pixie cut pelirrojo, pecas, ojos avellana, tomando **mate** en una cocina. Elegida por Jorge como foto de perfil de la cuenta `ia@openpass.com.ar` (Brisa, asistente de I+D) en Google Chat. Seed `426598910` (gen `1777406748`). Copia en `~/dev/openpass-qa-management/brisa-avatar.png`.

## Face Reference
| Archivo | Path | Descripción |
|---------|------|-------------|
| brisa_face_ref_v2.jpg | `/Volumes/Extra/ComfyUI/input/brisa_face_ref_v2.jpg` | Cara referencia elegida por Jorge (cobrizo, ojos verde-avellana, pecas) |

---

## Pipeline A: JuggernautXL + FaceID (básico)
**Workflow:** `workflows/01_character_sheet.py`
**Params:** JuggernautXL, FACEID preset, weight=1.8, lora_strength=1.0, euler, 25 steps, 768×768/1024

| Archivo | Path | Fecha | Size |
|---------|------|-------|------|
| brisa_faceid_body_00001_.png | output/ | 2026-04-19 14:51 | 737K |
| brisa_face_portrait_00001_.png | output/ | 2026-04-19 15:05 | 662K |
| brisa_fid_w12_l10_00001_.png | output/ | 2026-04-19 15:02 | 707K |
| brisa_fid_w15_l10_00001_.png | output/ | 2026-04-19 15:02 | 702K |
| brisa_fid_w18_l10_00001_.png | output/ | 2026-04-19 15:03 | 703K |

**Params variación:** weight 1.2 / 1.5 / 1.8, seed=42/123/777

---

## Pipeline A2: Character Sheet (euler, 25 steps)
**Workflow:** `workflows/01_character_sheet.py`
**Params:** mismo Pipeline A, 8 vistas (4 cara + 4 cuerpo)

| Archivo | Path | Fecha | Size | Vista |
|---------|------|-------|------|-------|
| brisa_sheet_face_front_00001_.png | output/ | 2026-04-19 15:23 | 632K | cara frente |
| brisa_sheet_face_profile_00001_.png | output/ | 2026-04-19 15:20 | 607K | cara perfil |
| brisa_sheet_face_34_00001_.png | output/ | 2026-04-19 15:21 | 634K | cara 3/4 |
| brisa_sheet_face_smile_00001_.png | output/ | 2026-04-19 15:21 | 609K | cara sonrisa |
| brisa_sheet_body_front_00001_.png | output/ | 2026-04-19 15:22 | 666K | cuerpo frente |
| brisa_sheet_body_back_00001_.png | output/ | 2026-04-19 15:22 | 726K | cuerpo espalda |
| brisa_sheet_body_34_00001_.png | output/ | 2026-04-19 15:23 | 645K | cuerpo 3/4 |
| brisa_sheet_body_seated_00001_.png | output/ | 2026-04-19 15:23 | 700K | cuerpo sentada |

---

## Pipeline B: HQ (DPM++ 2M Karras, 40 steps)
**Workflow:** `workflows/04_scenarios.py` (mismo formato)
**Params:** JuggernautXL, FACEID, weight=1.8, dpmpp_2m, karras, 40 steps
**Negativo extra:** smooth skin, plastic skin, airbrushed, oversmooth

| Archivo | Path | Fecha | Size | Vista |
|---------|------|-------|------|-------|
| brisa_hq_face_front_00001_.png | output/ | 2026-04-19 15:28 | 647K | cara frente |
| brisa_hq_face_profile_00001_.png | output/ | 2026-04-19 15:28 | 623K | cara perfil |
| brisa_hq_face_34_00001_.png | output/ | 2026-04-19 15:29 | 627K | cara 3/4 |
| brisa_hq_face_smile_00001_.png | output/ | 2026-04-19 15:30 | 596K | cara sonrisa |
| brisa_hq_body_front_00001_.png | output/ | 2026-04-19 15:30 | 700K | cuerpo frente |
| brisa_hq_body_back_00001_.png | output/ | 2026-04-19 15:31 | 593K | cuerpo espalda |
| brisa_hq_body_34_00001_.png | output/ | 2026-04-19 15:32 | 675K | cuerpo 3/4 |
| brisa_hq_body_seated_00001_.png | output/ | 2026-04-19 15:33 | 745K | cuerpo sentada |

---

## Pipeline C: Upscale + Sharpen
**Workflow:** `workflows/03_upscale_sharpen.py`
**Params:** Pipeline B → 4x-UltraSharp (2x) → ImageSharpen(radius=2, sigma=1.0, alpha=0.5)
**Resolución:** 1536×1536 (cara) / 1536×2048 (cuerpo)

| Archivo | Path | Fecha | Size |
|---------|------|-------|------|
| brisa_detail_face_front_00001_.png | output/ | 2026-04-19 16:01 | 24M |
| brisa_detail_face_profile_00001_.png | output/ | 2026-04-19 16:02 | 21M |
| brisa_detail_face_34_00001_.png | output/ | 2026-04-19 16:03 | 24M |
| brisa_detail_face_smile_00001_.png | output/ | 2026-04-19 16:03 | 23M |
| brisa_detail_body_front_00001_.png | output/ | 2026-04-19 16:04 | 31M |
| brisa_detail_body_back_00001_.png | output/ | 2026-04-19 16:06 | 28M |
| brisa_detail_body_34_00001_.png | output/ | 2026-04-19 16:06 | 30M |
| brisa_detail_body_seated_00001_.png | output/ | 2026-04-19 16:07 | 31M |

---

## Pipeline D: Scenarios (upscaled)
**Workflow:** `workflows/04_scenarios.py`
**Params:** Pipeline B + upscale + sharpen, distintos escenarios

| Archivo | Path | Fecha | Size | Escenario |
|---------|------|-------|------|-----------|
| brisa_flow_lingerie_bed_00001_.png | output/ | 2026-04-19 16:17 | 31M | lingerie en cama |
| brisa_flow_bikini_beach_00001_.png | output/ | 2026-04-19 16:18 | 27M | bikini en playa |
| brisa_flow_dress_urban_00001_.png | output/ | 2026-04-19 16:19 | 28M | vestido rojo urbano |
| brisa_flow_nude_studio_00001_.png | output/ | 2026-04-19 16:20 | 31M | nude studio dinámico |
| brisa_flow_topless_jeans_00001_.png | output/ | 2026-04-19 16:21 | 31M | topless + jeans |
| brisa_flow_nude_reclined_00001_.png | output/ | 2026-04-19 16:22 | 26M | nude reclinada |

---

## Pipeline E: Quality 2-pass (JuggernautXL + FaceID + img2img refine)
**Workflow:** `workflows/05_quality_2pass.py`
**Params:** Pass 1: JuggernautXL, FACEID, weight=1.8, dpmpp_3m_sde, karras, 50 steps → Pass 2: img2img refine, denoise=0.25, 30 steps → ImageSharpen(radius=2, sigma=1.0, alpha=0.4)
**Negativo:** + "smooth skin, plastic skin, airbrushed, oversmooth"

| Archivo | Path | Fecha | Size | Vista |
|---------|------|-------|------|-------|
| brisa_quality_face_front_00001_.png | output/ | 2026-04-20 09:22 | 966K | cara |
| brisa_quality_body_front_00001_.png | output/ | 2026-04-20 09:24 | 1.1M | cuerpo |
| brisa_quality_lingerie_00001_.png | output/ | 2026-04-20 09:25 | 1.2M | lingerie |
| brisa_quality_nude_studio_00001_.png | output/ | 2026-04-20 09:27 | 1.2M | nude studio |

**✅ Jorge liked the face from this pipeline**

---

## Pipeline F: CyberRealisticPony v1.6 (sin FaceID)
**Workflow:** `workflows/06_pony_nofaceid.py`
**Params:** UNETLoader(cyberrealisticPony) + DualCLIPLoader(sdxl) + VAELoader(SDXL), dpmpp_3m_sde, karras, 50 steps → img2img refine denoise=0.25
**Score tags:** score_9, score_8_up, score_7_up, realistic, photorealistic

| Archivo | Path | Fecha | Size |
|---------|------|-------|------|
| pony_full_test_00001_.png | output/ | 2026-04-20 10:29 | 822K |

**Nota:** Mejor piel pero sin identidad de cara

---

## Pipeline G: 2-model (JuggernautXL+FaceID → Pony refine, denoise=0.4)
**Workflow:** `workflows/07_2model_pipeline_d04.py`
**Params:** Pass 1: JuggernautXL + FaceID (50 steps) → Pass 2: Pony img2img (denoise=0.4, 40 steps) → sharpen

| Archivo | Path | Fecha | Size | Vista |
|---------|------|-------|------|-------|
| brisa_2model_face_00001_.png | output/ | 2026-04-20 10:44 | 1.1M | cara |
| brisa_2model_body_00001_.png | output/ | 2026-04-20 10:46 | 1.3M | cuerpo |
| brisa_2model_lingerie_00001_.png | output/ | 2026-04-20 10:47 | 1.4M | lingerie |
| brisa_2model_nude_studio_00001_.png | output/ | 2026-04-20 10:50 | 1.3M | nude studio |

**✅ Jorge liked the face close-up. Body shots lose face identity at denoise 0.4**

---

## Pipeline H: 2-model (denoise=0.2)
**Workflow:** `workflows/08_2model_pipeline_d02.py`
**Params:** Pass 1: JuggernautXL + FaceID (50 steps) → Pass 2: Pony img2img (denoise=0.2, 30 steps) → sharpen

| Archivo | Path | Fecha | Size | Vista |
|---------|------|-------|------|-------|
| brisa_2model_d02_body_00001_.png | output/ | 2026-04-20 14:02 | 1.2M | cuerpo |
| brisa_2model_d02_lingerie_00001_.png | output/ | 2026-04-20 14:04 | 1.3M | lingerie |
| brisa_2model_d02_nude_studio_00001_.png | output/ | 2026-04-20 14:06 | 1.2M | nude studio |

**Goal:** Preserve face identity better while getting Pony skin quality

---

## Pipeline I: Low CFG (4.5) + Pony refine
**Workflow:** `workflows/09_lowcfg.py` (generated from /tmp/gen_lowcfg.py)
**Params:** CFG 4.5, JuggernautXL/URPM + FaceID → Pony refine denoise=0.2
**Negativo extra:** stylized, digital art, 3d render

| Archivo | Path | Fecha | Size | Modelo |
|---------|------|-------|------|--------|
| brisa_lowcfg_face_jugg_lowcfg_00001_.png | output/ | 2026-04-20 14:10 | 984K | Juggernaut |
| brisa_lowcfg_body_jugg_lowcfg_00001_.png | output/ | 2026-04-20 14:12 | 1.1M | Juggernaut |

---

## Jorge's manual tests (ComfyUI GUI)

| Archivo | Path | Fecha | Size | Notas |
|---------|------|-------|------|-------|
| FNU_test_00001_.png | output/ | 2026-04-19 21:10 | 930K | FaceID Nude test |
| FNU_face_front_00001_.png | output/ | 2026-04-19 21:57 | 874K | FNU cara frente |
| FNU_face_34_00001_.png | output/ | 2026-04-19 22:09 | 365K | FNU cara 3/4 |
| FNU_face_profile_00001_.png | output/ | 2026-04-19 22:18 | 1.0M | FNU cara perfil |
| FNU_upper_skin_00001_.png | output/ | 2026-04-19 22:28 | 733K | FNU upper + skin |
| FNU_skin_cfg2_normal_25s_00001_.png | output/ | 2026-04-19 22:53 | 867K | FNU skin cfg2 |
| FNU_skin_cfg15_normal_25s_00001_.png | output/ | 2026-04-19 23:05 | 987K | FNU skin cfg15 |
| FNU_skin_cfg25_normal_30s_00001_.png | output/ | 2026-04-19 23:17 | 853K | FNU skin cfg25 |
| FNUv2_face_front_cfg35_00001_.png | output/ | 2026-04-20 12:39 | 799K | FNUv2 cfg35 |
| FNUv2_face_front_cfg25_00001_.png | output/ | 2026-04-20 13:54 | 858K | FNUv2 cfg25 |
| CRPony_face_front_00001_.png | output/ | 2026-04-19 16:35 | 1.2M | CyberRealisticPony |
| CRPony_face_34_00001_.png | output/ | 2026-04-19 16:38 | 1.2M | CRPony 3/4 |
| CRPony_face_profile_00001_.png | output/ | 2026-04-19 16:41 | 1.1M | CRPony perfil |
| ZImage_test_00001_.png | output/ | 2026-04-19 20:38 | 970K | ZImage test |
| ZImage_test_00002_.png | output/ | 2026-04-19 20:45 | 1.1M | ZImage test 2 |
| JGG_face_front_skin_00001_.png | output/ | 2026-04-19 19:05 | 1.5M | Juggernaut skin |
| JGG_face_front_cfg7_00001_.png | output/ | 2026-04-19 19:09 | 1.5M | Juggernaut cfg7 |
| PM_face_front_00001_.png | output/ | 2026-04-20 15:51 | 779K | PornMerge cara |
| PM_body_front_00001_.png | output/ | 2026-04-20 15:54 | 1.1M | PornMerge cuerpo |
| PM_face_front_lowcfg_00001_.png | output/ | 2026-04-20 15:55 | 747K | PornMerge low cfg |
| PM_nude_fullbody_00001_.png | output/ | 2026-04-20 16:14 | 1.4M | PornMerge nude |
| PM_nude_fullbody_v2_00001_.png | output/ | 2026-04-20 16:17 | 1.4M | PornMerge nude v2 |
| OPT_D_RV60_PM_nude_00001_.png | output/ | 2026-04-20 17:51 | 1.1M | Optimized RV60+PM |
| test_00001_.png | output/ | 2026-04-20 17:08 | 858K | test |
| q5_s07_00001_.png | output/ | 2026-04-20 17:22 | 964K | q5 s07 |

---

## Modelos disponibles

| Modelo | Path | Tipo | Notas |
|-------|------|------|-------|
| JuggernautXL | checkpoints/juggernautXL_juggXIByRundiffusion.safetensors | SDXL completo | Base principal |
| CyberRealisticPony v1.6 | checkpoints/Pony/cyberrealisticPony_v160.safetensors | Solo UNet | Necesita DualCLIPLoader + VAELoader |
| uberRealisticPornMerge v23 | checkpoints/uberRealisticPornMerge_v23Final.safetensors | SDXL completo | NSFW fotorealista |
| crystalClearXL | checkpoints/crystalClearXL_ccxl.safetensors | SDXL completo | |
| photon_v1 | checkpoints/photon_v1.safetensors | SDXL completo | |
| SDXL base 1.0 | checkpoints/sd_xl_base_1.0.safetensors | SDXL completo | |
| SDXL refiner 1.0 | checkpoints/sd_xl_refiner_1.0.safetensors | SDXL refiner | |
| Bere_openart | loras/Bere_openart.safetensors | FLUX LoRA | Trigger: `Bere_openart` |
| Cabel_openart | loras/Cabel_openart.safetensors | FLUX LoRA | Trigger: `Cabel_openart` |
| ip-adapter-faceid_sdxl | ipadapter/ip-adapter-faceid_sdxl.bin | IP-Adapter | FACEID preset |
| ip-adapter-faceid-plusv2_sdxl | ipadapter/ip-adapter-faceid-plusv2_sdxl.bin | IP-Adapter | BROKEN (dim mismatch) |
| CLIP ViT-H | clip_vision/CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors | CLIP Vision | Para FaceID |
| 4x-UltraSharp | upscale_models/4x-UltraSharp.pth | Upscaler | ESRGAN |
| SDXL VAE | vae/SDXL/sdxl_vae.safetensors | VAE | Para Pony |
| text_encoder (CLIP-L) | clip/text_encoder/model.fp16.safetensors | CLIP | Para Pony DualCLIPLoader |
| text_encoder_2 (CLIP-G) | clip/text_encoder_2/model.fp16.safetensors | CLIP | Para Pony DualCLIPLoader |

---

## Parámetros comunes

| Parámetro | Valores usados |
|-----------|---------------|
| FaceID weight | 1.2, 1.5, **1.8** (default) |
| FaceID lora_strength | 0.8, **1.0** (default) |
| Sampler | euler, dpmpp_2m, **dpmpp_3m_sde** (best) |
| Scheduler | **karras** |
| Steps | 25, 40, **50** (quality) |
| CFG | 7.0 (default), **4.5** (low, less caricature) |
| Pony denoise | 0.2, 0.25, **0.4** |
| Upscale | 4x-UltraSharp, 2x |
| Sharpen | radius=2, sigma=1.0, alpha=0.3-0.5 |
