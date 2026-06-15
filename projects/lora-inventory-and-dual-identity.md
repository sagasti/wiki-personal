---
title: "LoRA Inventory & Dual Identity Findings"
created: "2026-05-02"
updated: "2026-05-02"
type: "project"
---

# LoRA Inventory & Dual Identity Findings

## Local LoRAs (Mac `/Volumes/Extra/ComfyUI/models/loras/`)

### FLUX LoRAs (for images)
| File | Size | Tensors | Trigger | Trained with | Notes |
|------|------|---------|---------|-------------|-------|
| `flux/berchu.safetensors` | 164MB | 988 | **Berchu** | ai-toolkit v0.1.0 | Steps 2000, 15 epochs |
| `flux/cabelious.safetensors` | 164MB | 988 | **Cabelous** | ai-toolkit v0.1.0 | Steps 2000, 24 epochs |
| `Bere_openart_flux.safetensors` | 86MB | 684 | unknown | OpenArt | No metadata |
| `Cabel_openart_flux.safetensors` | 86MB | 684 | unknown | OpenArt | No metadata |

### HunyuanVideo LoRAs (for video)
| File | Size | Tensors | Architecture |
|------|------|---------|-------------|
| `hunyuan/berchu_lora_40.safetensors` | 308MB | 640 | `double_blocks.img_attn` |
| `hunyuan/cabelious_lora_40.safetensors` | 308MB | 640 | `double_blocks.img_attn` |
| (also: _22, _30, _50, _60 variants) | | | |

### BRISA production LoRAs
- `BRISA_PRODUCTION_step03000.safetensors` (134MB)
- `brisa_v2_ckpt_03000.safetensors` (134MB)
- `brisa_zimage.safetensors` (134MB)

## Key Findings

### Dual Identity LoRA Stacking — DOES NOT WORK
When you stack two identity LoRAs (e.g., Bere + Cabelious) on the same model, they **blend into a single face**. The model cannot assign each LoRA identity to a different person/region. Both LoRAs modify the same model weights.

**Solutions for 2 people in 1 image:**
1. Generate with 1 LoRA (e.g., Bere) → face-swap the other person (Jorge)
2. Generate base scene without LoRAs → face-swap both
3. Generate each person separately → composite in Photoshop

### Lighting — CRITICAL for face visibility
- **Back lighting / rim lighting (moon behind)** = silhouettes, faces invisible
- **Front lighting / warm light** = faces visible, LoRAs work correctly
- Always use explicit "faces well-lit", "front lighting", "warm light on face" in prompts

### Individual LoRA Verification
- Both `flux/berchu.safetensors` and `flux/cabelious.safetensors` **work correctly** with FLUX.1-dev-fp8 on RunPod H200
- Trigger words confirmed: **"Berchu"** and **"Cabelous"**
- OpenArt LoRAs also FLUX-compatible but lower rank (684 vs 988 tensors)

## RunPod Setup
- FLUX checkpoint: `flux/flux1-dev-fp8.safetensors`
- Text encoders: `t5xxl_fp8_e4m3fn.safetensors` + `clip_l.safetensors`
- VAE: `ae.safetensors`
- Use `CheckpointLoaderSimple` (not UNETLoader) for FLUX on this pod
- LoRAs uploaded to `identity/` subfolder

## Date
2026-05-02
