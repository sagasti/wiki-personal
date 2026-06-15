---
title: "bere-lora-dataset-source"
created: "2026-05-02"
updated: "2026-05-02"
type: "project"
tags: ["#bere", "#lora", "#dataset", "#apple-photos", "#flux", "#runpod"]
sources: ["hermes-session/20260502_184215_60fd9d"]
hermes_session: "20260502_184215_60fd9d"
confidence: "medium"
---

# bere-lora-dataset-source

## Bere LoRA Dataset Source

### Apple Photos Inventory
- **Total photos of Bere**: 286
- **Local (not iCloud-only)**: 2 (most are iCloud-only, need download before export)
- **Portraits**: 147 (subset suitable for face LoRA training)
- **Date range**: 2024-08-27 through 2026-03-22

### RunPod Status
- No Bere dataset exists on RunPod (`/workspace/datasets/` and `/workspace/brisa/datasets/` only contain Brisa data)
- Bere-related files on RunPod: reference image at `/workspace/scripts/legacy/bere_ref.jpeg`, output grids in `/workspace/ComfyUI/output/`

### Local LoRA Assets
- Existing LoRA: `Bere_openart_flux.safetensors` in `/Volumes/Extra/ComfyUI/models/loras/`
- Dataset dir on local: `/Volumes/Extra/ComfyUI/output/bere/` (contains test outputs, not training set)

### Pipeline
1. Export best portraits from Apple Photos → local disk
2. Generate captions
3. Upload to RunPod
4. Train FLUX LoRA on H200

### Related
- Person: [[berenice-carbajo]]
- Infrastructure: [[runpod]], [[comfyui]], [[lora]]
