# Brisa Character — Archived Pipeline (OpenClaw Era)

> **⚠️ ARCHIVED:** These are legacy workflows and images from the OpenClaw era (pre-migration).
> Current work uses the assets in `brisa-character-assets/` and the Z-Image Turbo pipeline.
> Kept for historical reference — the pipeline definitions are proven and may be re-implemented as Hermes skills.

## Character Definition
- **Face ref:** `brisa_face_ref_v2.jpg` — short copper red bob, hazel-green eyes, freckles
- **Face weight:** 1.8 (best identity transfer with IP-Adapter FaceID)
- **Sampler:** DPM++ 3M SDE Karras, 50 steps (quality), 40 steps (refine)

## Pipeline Variants

### Pipeline A: JuggernautXL + FaceID (baseline)
- **Workflow:** `01_character_sheet.py`
- **Steps:** 40, DPM++ 2M Karras
- **Post:** none
- **Pros:** fast, correct face
- **Cons:** skin looks smooth/plastic

### Pipeline B: JuggernautXL + FaceID + Upscale + Sharpen
- **Workflow:** `03_upscale_sharpen.py`
- **Steps:** 40, DPM++ 2M Karras → 4x-UltraSharp (2x) → ImageSharpen
- **Output:** `character-sheet/` (24-31MB, 1536×2048)
- **Pros:** more detail, correct face
- **Cons:** skin still somewhat smooth

### Pipeline C: JuggernautXL + FaceID + img2img refine (2-pass)
- **Workflow:** `05_quality_2pass.py`
- **Steps:** 50 DPM++ 3M SDE → img2img refine (denoise 0.25, 30 steps)
- **Output:** `quality-tests/brisa_quality_*`
- **Pros:** better skin texture, correct face ✅ Jorge liked this
- **Cons:** slower (~10 min/image)

### Pipeline D: CyberRealisticPony v1.6 (no FaceID)
- **Workflow:** `06_pony_nofaceid.py`
- **Model:** UNETLoader + DualCLIPLoader + VAELoader (Pony has no embedded CLIP/VAE)
- **Steps:** 50 DPM++ 3M SDE → img2img refine
- **Output:** `quality-tests/pony_*`
- **Pros:** best skin texture (visible pores, subsurface scattering) ✅
- **Cons:** no face identity — different person each time

### Pipeline E: JuggernautXL + FaceID → Pony refine (2-model)
- **Workflow:** `07_2model_pipeline_d04.py` (denoise 0.4)
- **Steps:** Juggernaut 50 steps → Pony img2img (denoise 0.4, 40 steps)
- **Output:** `2model-pipeline/brisa_2model_*`
- **Pros:** best skin + face identity ✅ Jorge liked the face close-up
- **Cons:** denoise 0.4 changes face too much in body shots

### Pipeline F: JuggernautXL + FaceID → Pony refine (denoise 0.2)
- **Workflow:** `08_2model_pipeline_d02.py`
- **Steps:** Juggernaut 50 steps → Pony img2img (denoise 0.2, 30 steps)
- **Status:** generating...
- **Goal:** preserve face identity better while still getting Pony skin quality

## Pony Model Setup
CyberRealisticPony v1.6 has **no embedded CLIP or VAE** — requires:
- `UNETLoader` → `models/unet/cyberrealisticPony_v160.safetensors` (symlink from checkpoints)
- `DualCLIPLoader` (type: sdxl) → `models/clip/text_encoder/model.fp16.safetensors` + `text_encoder_2/model.fp16.safetensors`
- `VAELoader` → `models/vae/SDXL/sdxl_vae.safetensors`

## Known Issues
- **IP-Adapter FaceID Plus V2 SDXL:** BROKEN — architecture mismatch (dim 1280 vs 1664)
- **FaceDetailer:** requires CLIPSeg custom node (git clone fails on this Mac)
- **Conda CLI tqdm bug:** long generations don't save — use ComfyUI.app instead
- **Nano Banana Pro:** filters nude content

## Negative Prompts
- **SDXL:** `cartoon, anime, illustration, deformed, ugly, bad anatomy, bad proportions, extra limbs, extra fingers, mutated hands, smooth skin, plastic skin, airbrushed, oversmooth, blurry`
- **Pony:** `score_6, score_5, score_4,` + same as SDXL

## Next Steps
1. Evaluate Pipeline F (denoise 0.2) results
2. Fix CLIPSeg for FaceDetailer
3. Train LoRA on RunPod H200
4. I2V with Kling for video
