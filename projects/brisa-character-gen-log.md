---
title: "Brisa Character Generation Log"
created: "2026-04-19"
updated: "2026-04-19"
type: "project"
---

# Brisa Character Generation Log

## Character Definition
- **Name**: Brisa
- **Type**: Consistent NSFW character (face + body) for images and video
- **Face**: Redhead, short red hair (pixie cut, messy), freckles across nose and cheeks, subtle wrinkles, fine lines around eyes, realistic skin texture, pores visible, hazel eyes (brown-green), natural makeup
- **Body**: TBD (tattoo to be added later)
- **Goal**: Iterate locally on Mac MPS → curate best images → train FLUX LoRA on RunPod H200 → produce high-quality media with LoRA

## Platforms
- **Local (Mac MPS)**: 36GB unified memory. ComfyUI en `/Volumes/Extra/ComfyUI/` corre con **conda env `comfy-ui`** (port 8188). Arranque: `conda activate comfy-ui && python main.py --listen 127.0.0.1 --port 8188 --use-split-cross-attention`. Models en `/Volumes/Extra/ComfyUI/models/`. ComfyUI.app (port 8000) descartado. Venv legacy en `/Volumes/Extra/ComfyUI/venv/` — no usar.
- **RunPod H200**: Pod "comfyui-luz" (70arq467blfpta). SSH: root@103.196.86.136 -p 41601. Proxy: https://70arq467blfpta-8188.proxy.runpod.net

## Available Models

### Local (Mac MPS)
| Model | Path | Type | Size | Notes |
|-------|------|------|------|-------|
| CyberRealistic Z-Image Turbo v4 | unet/cyberrealisticZImage_v40.safetensors | Lumina2/ZImage UNET | 11GB | Needs Qwen3 4B TE + FLUX VAE. WORKING |
| Qwen3 4B Q8_0 GGUF | text_encoders/qwen3_4b_q8_0.gguf | Z-Image text encoder | 4GB | CLIPLoaderGGUF type=lumina2 |
| JuggernautXL v11 | checkpoints/juggernautXL_juggXIByRundiffusion.safetensors | SDXL full | ~6.5GB | Working, used for initial tests |
| CyberRealistic Pony v16 (UNET only) | checkpoints/Pony/cyberrealisticPony_v160.safetensors | SDXL UNET | 4.8GB | INCOMPLETE - no CLIP, causes errors |
| FLUX1 Dev fp8 | unet/FLUX1/flux1-dev-fp8.safetensors | FLUX UNET | ~11GB | Original FLUX, SFW |
| FLUX1 Krea Dev fp8 | unet/FLUX1/flux1-krea-dev_fp8_scaled.safetensors | FLUX UNET | ~11GB | Krea variant |
| V2 Flux Klein 4 (LoRA) | loras/V2_flux_klein_4.safetensors | FLUX LoRA | 158MB | Klein LoRA |
| berchu_lora_40 | loras/berchu_lora_40.safetensors | LoRA | - | Trigger: "Berchu" |
| cabelous_lora_40 | loras/cabelous_lora_40.safetensors | LoRA | - | Trigger: "Cabelous" |

### Pending Downloads (in progress)
- FluxTrait Klein 9b V1 Q8 (GGUF) - portrait & detailed skin specialist
- 2 more .crdownload files in checkpoints/

### RunPod H200
- Hunyuan Video bf16 + Q8
- WAN 2.2 14B fp8
- LTX 2.3 22B dev fp8
- FLUX 1 Krea Dev fp8
- Qwen Image Edit fp8
- SD 1.5

---

## Generation Runs

### Run 001 - CRPony Face Tests (FAILED)
- **Date**: 2026-04-19 ~16:30
- **Platform**: Local Mac MPS, port 8188
- **Model**: CyberRealistic Pony v16 (cyberrealisticPony_v160.safetensors)
- **Error**: `clip input is invalid: None` - checkpoint is UNET only (4.8GB), missing CLIP text encoder and VAE
- **Result**: All 3 prompts failed
- **Lesson**: HF download was incomplete checkpoint. Need full SDXL (~6.5GB) or use UNETLoader+CLIPLoader+VAELoader separately

### Run 002 - JuggernautXL Face Tests (SUCCESS)
- **Date**: 2026-04-19 ~16:35-16:41
- **Platform**: Local Mac MPS, port 8188
- **Model**: JuggernautXL v11 (juggernautXL_juggXIByRundiffusion.safetensors)
- **Type**: SDXL full checkpoint (CheckpointLoaderSimple)
- **Settings**:
  - Size: 896x1152
  - Steps: 30
  - CFG: 5.0
  - Sampler: dpmpp_sde_gpu
  - Scheduler: karras
  - Denoise: 1.0
- **Prompt prefix**: `score_9, score_8_up, score_7_up, photorealistic, masterpiece, 1girl, solo, redhead, short red hair, pixie cut, messy short hair, freckles, light skin freckles across nose and cheeks, subtle wrinkles, fine lines around eyes, realistic skin texture, pores visible, hazel eyes, brown-green eyes, detailed eyes, natural makeup`
- **Negative**: `score_6, score_5, score_4, blurry, cartoon, anime, painting, deformed, bad anatomy, bad hands, extra fingers, smooth skin, plastic skin, airbrushed, worst quality, low quality`

#### 002a - Front closeup
- **Seed**: 42
- **Prompt**: [base] + `, face portrait, closeup, looking at viewer, soft lighting, studio lighting, shallow depth of field`
- **Output**: CRPony_face_front_00001_.png (1.2MB)
- **Filename prefix**: CRPony_face_front
- **Prompt ID**: 500e1daa-f71...
- **Verdict**: Pending review

#### 002b - 3/4 view
- **Seed**: 142
- **Prompt**: [base] + `, face portrait, 3/4 view, looking slightly left, dramatic lighting, rim light, cinematic`
- **Output**: CRPony_face_34_00001_.png (1.2MB)
- **Filename prefix**: CRPony_face_34
- **Prompt ID**: 8290bc43-31f...
- **Verdict**: Pending review

#### 002c - Profile
- **Seed**: 242
- **Prompt**: [base] + `, face profile, side view, natural light, window light, subtle shadows, contemplative expression`
- **Output**: CRPony_face_profile_00001_.png (1.1MB)
- **Filename prefix**: CRPony_face_profile
- **Prompt ID**: 439181b0-bda...
- **Verdict**: Pending review

---

## Workflow Templates

### SDXL Checkpoint (CheckpointLoaderSimple)
```json
{
  "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "<MODEL>"}},
  "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 896, "height": 1152, "batch_size": 1}},
  "6": {"class_type": "CLIPTextEncode", "inputs": {"text": "<POSITIVE>", "clip": ["4", 1]}},
  "7": {"class_type": "CLIPTextEncode", "inputs": {"text": "<NEGATIVE>", "clip": ["4", 1]}},
  "3": {"class_type": "KSampler", "inputs": {
    "seed": "<SEED>", "steps": 30, "cfg": 5.0,
    "sampler_name": "dpmpp_sde_gpu", "scheduler": "karras", "denoise": 1.0,
    "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["5", 0]
  }},
  "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
  "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "<PREFIX>", "images": ["8", 0]}}
}
```

### FLUX GGUF (UnetLoaderGGUF + DualCLIPLoaderGGUF)
```json
{
  "10": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "<GGUF_FILE>"}},
  "11": {"class_type": "DualCLIPLoaderGGUF", "inputs": {"clip_name1": "t5/t5xxl_fp8_e4m3fn.safetensors", "clip_name2": "clip_l.safetensors", "type": "flux"}},
  "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 896, "height": 1152, "batch_size": 1}},
  "6": {"class_type": "CLIPTextEncode", "inputs": {"text": "<POSITIVE>", "clip": ["11", 0]}},
  "7": {"class_type": "CLIPTextEncode", "inputs": {"text": "<NEGATIVE>", "clip": ["11", 0]}},
  "3": {"class_type": "KSampler", "inputs": {
    "seed": "<SEED>", "steps": 20, "cfg": 3.5,
    "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0,
    "model": ["10", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["5", 0]
  }},
  "12": {"class_type": "VAELoader", "inputs": {"vae_name": "FLUX1/ae.safetensors"}},
  "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["12", 0]}},
  "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "<PREFIX>", "images": ["8", 0]}}
}
```

---

### Run 003 - Z-Image Turbo + Skin Comparison (IN PROGRESS)
- **Date**: 2026-04-19 ~18:55
- **Platform**: Local Mac MPS, port 8188
- **Improved skin prompt additions**: `skin imperfections, subtle skin texture, micro details, skin microtexture, skin microtexture visible`
- **Improved negative additions**: `oversmoothed, wax skin, doll skin`
- **Settings**: Same as Run 002 (896x1152, 30 steps, dpmpp_sde_gpu, karras) unless noted

#### 003a - Z-Image Turbo face front
- **Model**: cyberrealisticZImage_v40.safetensors, CFG 5.0, seed 42
- **Prefix**: ZI_face_front, Prompt ID: 6f60f5dc-06a...

#### 003b - Z-Image Turbo face 3/4
- **Model**: cyberrealisticZImage_v40.safetensors, CFG 5.0, seed 142
- **Prefix**: ZI_face_34, Prompt ID: ff980d3e-e07...

#### 003c - Z-Image Turbo face profile
- **Model**: cyberrealisticZImage_v40.safetensors, CFG 5.0, seed 242
- **Prefix**: ZI_face_profile, Prompt ID: ee90d3cb-05a...

#### 003d - JuggernautXL face front (enhanced skin prompt)
- **Model**: juggernautXL, CFG 5.0, seed 42
- **Prefix**: JGG_face_front_skin, Prompt ID: fa3b18f7-ead...
- **Purpose**: Compare same model with improved skin prompt vs Run 002a

#### 003e - JuggernautXL face front (CFG 7)
- **Model**: juggernautXL, CFG 7.0, seed 42
- **Prefix**: JGG_face_front_cfg7, Prompt ID: 80dc56e0-7cb...
- **Purpose**: Test higher CFG for more skin detail adherence

#### 003f - Z-Image Turbo upper body skin
- **Model**: cyberrealisticZImage_v40.safetensors, CFG 5.0, seed 342
- **Prompt**: [base] + `, upper body, bare shoulders, collarbone, looking at viewer, soft natural lighting, skin detail, skin microtexture, pores visible on chest, subtle chest freckles`
- **Prefix**: ZI_upper_skin, Prompt ID: 01e060e0-58b...
- **Purpose**: Test skin quality on body (shoulders/chest)

---

### Run 004 - Z-Image Turbo FLUX format (FAILED)
- **Date**: 2026-04-19 ~19:00
- **Model**: cyberrealisticZImage_v40.safetensors (moved to unet/)
- **Attempt 1**: CheckpointLoaderSimple → `clip input is invalid: None` (it's UNET only, not full checkpoint)
- **Attempt 2**: UNETLoader + DualCLIPLoader + VAELoader, weight_dtype=fp8_e4m3fn → `Float8_e4m3fn to MPS backend not supported`
- **Attempt 3**: UNETLoader weight_dtype=default → `RuntimeError: normalized_shape=[2560] vs input size[1,256,4096]` (Z-Image is not standard FLUX arch, UNETLoader assumes FLUX)
- **Verdict**: Z-Image Turbo v4 safetensors NOT compatible with Mac MPS. Needs GGUF conversion or different loader.

### Run 005 - FluxTrait Klein Q8 GGUF + Flux NSFW Unlocked (PARTIAL)
- **Date**: 2026-04-19 ~19:35
- **FluxTrait Klein Q8 GGUF**: FAILED - `Mixing scaled FP8 with GGUF is not supported` when using umt5_xxl_fp8_e4m3fn_scaled. Also `clip missing: text_projection.weight` and shape mismatch with standard T5+CLIP_L. Flux.2 Klein needs specific CLIP setup not available in current DualCLIPLoaderGGUF.
- **Flux NSFW Unlocked v3 FP16**: SUCCESS with UNETLoader (default dtype) + DualCLIPLoader (T5 fp8 + CLIP_L, type=flux) + VAELoader (FLUX1/ae.safetensors)

#### 005e - Flux NSFW Unlocked test (SUCCESS)
- **Model**: fluxNSFWUNLOCKED_v30FP16.safetensors, UNETLoader default, seed 42
- **Prefix**: FNU_test, Output: FNU_test_00001_.png (930KB)
- **Workflow**: UNETLoader(default) + DualCLIPLoader(t5/t5xxl_fp8_e4m3fn + clip_l, flux) + VAELoader(FLUX1/ae.safetensors)

### Run 006 - Flux NSFW Unlocked Full Set (IN PROGRESS)
- **Date**: 2026-04-19 ~21:15
- **Model**: fluxNSFWUNLOCKED_v30FP16.safetensors
- **Workflow**: Same as 005e
- **Settings**: 896x1152, 20 steps, CFG 3.5, euler/simple
- **Issue**: Output looks caricaturized, skin too plastic. CFG 3.5 too high for FLUX.

#### 006a - FNU_face_front (seed 42)
#### 006b - FNU_face_34 (seed 142)
#### 006c - FNU_face_profile (seed 242)
#### 006d - FNU_upper_skin (seed 342)

### Run 007 - Z-Image Fix + Skin Realism Tests (IN PROGRESS)
- **Date**: 2026-04-19 ~20:30

#### 007a - Z-Image with Qwen3 4B (SUCCESS!)
- **Problem**: Z-Image is Lumina2 arch, NOT FLUX. DualCLIPLoader type=flux gives shape mismatch (4096 vs 12288)
- **Fix**: Downloaded Qwen3 4B Q8_0 GGUF (4GB) from worstplayer/Z-Image_Qwen_3_4b_text_encoder_GGUF
- **Correct workflow**: UNETLoader(Z-Image) + CLIPLoaderGGUF(qwen3_4b_q8_0.gguf, type=lumina2) + VAELoader(FLUX1/ae.safetensors)
- **Output**: ZImage_test_00001_.png (970KB, 1024x1024) — ~6min on MPS
- **Lesson**: Z-Image needs Qwen3 4B TE, never DualCLIPLoader type=flux

#### 007b - FNU Skin Realism Tests (QUEUED)
- **Model**: fluxNSFWUNLOCKED_v30FP16
- **Prompt additions**: "detailed skin texture, skin pores visible, subsurface scattering, realistic skin, natural skin tone, photorealistic, raw photo, unretouched"
- **Tests**:
  - FNU_skin_cfg2_normal_25s: CFG 2.0, scheduler normal, 25 steps, seed 42
  - FNU_skin_cfg15_normal_25s: CFG 1.5, scheduler normal, 25 steps, seed 42
  - FNU_skin_cfg25_normal_30s: CFG 2.5, scheduler normal, 30 steps, seed 42

### Key Lessons
- **MPS does not support fp8 dtypes** - UNETLoader with fp8_e4m3fn/fast/e5m2 fails on Mac
- **Z-Image is Lumina2 arch, NOT FLUX** - Needs CLIPLoaderGGUF type=lumina2 + Qwen3 4B GGUF TE. DualCLIPLoader type=flux = shape mismatch crash
- **GGUF + FP8 scaled CLIP = incompatible** - Cannot mix DualCLIPLoaderGGUF with umt5_xxl_fp8_e4m3fn_scaled
- **Flux.2 Klein (FluxTrait) needs specific CLIP** - Standard T5+CLIP_L or UMT5 don't work
- **UNETLoader weight_dtype=default works for FP16 FLUX on MPS** - Flux NSFW Unlocked v3 FP16 confirmed working
- **SDXL checkpoints (CheckpointLoaderSimple)** work fine on MPS (JuggernautXL confirmed)
- **Working FLUX on MPS**: UNETLoader(default) + DualCLIPLoader(t5 fp8 + clip_l, flux) + VAELoader(flux ae)
- **FLUX CFG too high = plastic skin** - CFG 3.5 gives caricature look. Try 1.5-2.5 with scheduler normal
- **Skin realism prompt terms**: "detailed skin texture, skin pores, subsurface scattering, realistic skin, natural skin tone, photorealistic, raw photo, unretouched"

### Current Ranking (Jorge's assessment)
1. **FNU (FluxNSFW Unlocked v3)** — winning but needs lower CFG for skin realism
2. **CRPony (CyberRealistic Pony v16)** — also good, needs proper UNET+CLIP+VAE setup

---

## Next Steps
1. Wait for Run 007b skin tests to complete, compare CFG variants
2. Iterate best model with refined prompts for Brisa character
3. Try Z-Image with Brisa prompts (now that it works!)
4. Define body (add tattoo)
5. Curate best 6-8 images for LoRA training
6. Train FLUX LoRA on RunPod H200
7. Production: FLUX + LoRA for images, Hunyuan Video + LoRA for video
