---
title: "Bere LoRA Training Recipe"
created: "2026-05-03"
updated: "2026-05-03"
type: "project"
tags: ["#lora", "#bere", "#z-image", "#musubi-tuner", "#training"]
sources: ["hermes-session/20260502_223713_750db8"]
hermes_session: "20260502_223713_750db8"
confidence: "medium"
---

# Bere LoRA Training Recipe

## Training Configuration

- **Tool**: musubi-tuner (Z-Image training)
- **Base model**: Z-Image (`z_image_bf16.safetensors`)
- **Text encoder**: Qwen3 4B (bf16) — loaded from `qwen_3_4b.safetensors`
- **VAE**: `ae.safetensors`
- **Dataset**: 76 items (38 images × 2 repeats)
- **Cache dir**: `/workspace/datasets/bere_final_cache`
- **Epochs**: 20 | **Steps**: 1520 | **Batch size**: 1
- **Final loss**: ~0.36 | **Training time**: ~26 min
- **Output**: `bere_zimage.safetensors` (134MB)
- **Output path**: `/workspace/training_runs/bere_zimage_musubi_v1/`

## Musubi-tuner Cache Files

Two caches per image:
- Latent: `{id}_{W}x{H}_zi.safetensors`
- Text encoder: `{id}_zi_te.safetensors`

## Technical Notes

- `zimage_cache_text_encoder_outputs.py` does **NOT** accept `--dit` or `--mixed_precision` flags (causes unrecognized args error)
- Same recipe as [[brisa]] LoRA training
- Dataset source: [[bere-lora-dataset-source]]
- Architecture: [[z-image-model-architecture]]
