---
title: "Z-Image model architecture"
created: "2026-05-02"
updated: "2026-05-02"
type: "concept"
tags: ["#z-image", "#architecture", "#qwen3", "#text-encoder", "#vae", "#musubi-tuner", "#training"]
sources: ["hermes-session/20260502_184215_60fd9d"]
hermes_session: "20260502_184215_60fd9d"
confidence: "medium"
---

# Z-Image model architecture

## Z-Image Architecture Details

- **Model ID**: `Tongyi-MAI/Z-Image` (HuggingFace)
- **Text Encoder**: Qwen3-4B (`Qwen3ForCausalLM` from transformers)
- **Tokenizer**: `Qwen2Tokenizer.from_pretrained("Tongyi-MAI/Z-Image", subfolder="tokenizer")`
- **VAE**: AutoencoderKL loaded from ComfyUI `.safetensors` format, keys auto-converted to diffusers format
- **Default VAE dtype**: `torch.float32` (overridable via `--vae_dtype`)

### musubi-tuner integration
- `zimage_cache_latents.py` accepts only: `--dataset_config`, `--vae`, `--vae_dtype`, `--device`, `--batch_size`, `--num_workers`, `--skip_existing`, `--keep_cache`, `--debug_mode`
- Flags like `--dit`, `--cache_directory`, `--mixed_precision`, `--sdpa` are **not valid** for this script
- Training pipeline caches latents internally — separate cache step is not required

### Related
- [[comfyui]] — VAE and diffusion model files sourced from ComfyUI models directory
- [[lora]] — LoRA training via musubi-tuner on Z-Image
