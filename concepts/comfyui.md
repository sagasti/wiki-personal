---
title: "ComfyUI"
created: "2026-04-29"
updated: "2026-05-03"
type: "concept"
tags: ["#concept", "#ai", "#image-generation", "#video-generation", "#workflow"]
related: [[comfyui]], [[comfyui-face-gen-tests]], [[hunyuan-video-recipe]], [[brisa-face-pipeline-evaluation]], [[runpod]]
---

# ComfyUI

Workflow-based UI para diffusion models. Permite armar pipelines visuales con nodos para generación de imágenes y video. Es la herramienta central del pipeline de generación de [[brisa]] y de los proyectos de [[ai-video-generation]].

## Por qué Jorge lo usa

- Control granular sobre cada paso del pipeline (ksampler, VAE, conditioning, refining, upscaling)
- Soporta SDXL, FLUX, Z-Image, Hunyuan Video, Wan, etc.
- Workflows reproducibles como JSON

## Stack en uso

- **Local**: ver [[comfyui]] (conda env `comfy-ui`, port 8188)
- **Cloud GPU**: en [[runpod]] H200 — usado para entrenamiento de [[lora]] y generación pesada
- **Tests de caras**: ver [[comfyui-face-gen-tests]] y [[brisa-face-pipeline-evaluation]]
- **Video**: workflow [[hunyuan-video-recipe]]

## Páginas relacionadas

- [[comfyui]] — setup local
- [[brisa-face-pipeline-evaluation]] — pipeline ganador para Brisa
- [[hunyuan-video-recipe]] — recipe de video
- [[runpod]] — pod cloud
- [[lora]] — fine-tuning con LoRAs

## R2 Storage + HuggingFace
- **HF account:** sagasti
- **FLUX.1-dev:** gated access enabled
- **R2:** Cloudflare R2 for output storage

## Estado

Página stub creada por audit (29-04-2026). Pendiente: documentar nodos custom usados, models disponibles, troubleshooting común.


---

## Setup local



## Configuración
- **Solo conda env** `comfy-ui` puerto 8188
- **ComfyUI.app borrada** 24/4/2026
- **Models en:** `/Volumes/Extra/ComfyUI/models/`

## Start command
```bash
conda run -n comfy-ui python /Volumes/Extra/ComfyUI/main.py --listen 127.0.0.1 --port 8188 --use-split-cross-attention
```

## Issues resueltos
- tqdm broken pipe issue → ya no ocurre (24/4)

## Ver también
- [[brisa-tools]] — Herramientas y config local de Brisa
- [[hermes-configuration]] — Config general de Hermes

*Promovido desde MEMORY.md el 2026-04-26 (mantenimiento semanal)*


## Update 2026-05-03

When building a ComfyUI workflow for [[z-image-model-architecture]], the model must be loaded with **UNETLoader** instead of `CheckpointLoaderSimple`.

Available ZImage model files:
- `cyberrealisticZImage_v40.safetensors`
- `fluxtraitFLUX2KleinFLUXZ_klein9bV2.safetensors`
- `z_image_bf16.safetensors`

Performance note: ZImage generation on local CPU without a dedicated GPU is very slow.
