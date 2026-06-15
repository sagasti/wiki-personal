---
title: "LoRA (Low-Rank Adaptation)"
created: "2026-04-29"
updated: "2026-05-04"
type: "concept"
tags: ["#concept", "#fine-tuning", "#ai", "#image-generation", "#technique"]
related: [[brisa-lora-tags]], [[brisa-face-pipeline-evaluation]], [[comfyui]], [[runpod]]
---

# LoRA — Low-Rank Adaptation

Técnica de fine-tuning eficiente para modelos grandes. En vez de re-entrenar todos los parámetros, agrega un par de matrices de bajo rango (A·B) que se aprenden y se inyectan en las layers de atención del modelo base. Resultado: archivo chico (10-200 MB), entrena en horas en una GPU, no necesita VRAM para hostear el modelo completo durante el train.

Es la técnica central del pipeline de personalización de [[brisa]] sobre FLUX y Z-Image.

## Por qué Jorge lo usa

- Personalización de identidad facial sin re-entrenar el base model
- 100+ imágenes son suficientes para una buena LoRA de personaje (vs millones para fine-tuning)
- Stack en producción: dataset de [[brisa]] curado a 104 imágenes (1024x1334), tags via [[brisa-lora-tags]]
- Inferencia: simplemente cargás la LoRA encima del base en [[comfyui]]

## Stack en uso

| Pieza | Tool / Path |
|---|---|
| Training framework | Kohya sd-scripts en /workspace/sd-scripts/ (RunPod) |
| GPU | H200 143GB en [[runpod]] |
| Base models targeteados | FLUX.1-dev, Z-Image v4.0 |
| Dataset | 104 imágenes curadas con OpenRouter+gemini-2.5-flash |
| Tags / captions | Ver [[brisa-lora-tags]] |

## Hallazgos relevantes

- PhotoMaker como alternativa: descartado (sobre-enfoca cara, no genera fullbody)
- IP-Adapter FaceID con FLUX: descartado (no soporta correctamente)
- LoRA pura sigue siendo el approach más confiable para identidad de personaje
- **PuLID for FLUX** (`pulid_flux_v0.9.1.safetensors`): instalado en `/Volumes/Extra/ComfyUI/models/pulid/`. Alternativa a FaceID para FLUX — pendiente testing.
- **Multi-character con IPAdapter**: `ComfyUI_IPAdapter_plus` incluye `ipadapter_regional_conditioning.json` y `ipadapter_combine_embeds.json` para generar 2+ personajes en una imagen. Ver [[technical-lessons]] para limitaciones de dual LoRA stacking.
- **Dual LoRA stacking**: blending de caras, no funciona para 2 personajes distintos. Ver [[technical-lessons]].

## Páginas relacionadas

- [[brisa-lora-tags]] — sistema de tags del dataset
- [[brisa-face-pipeline-evaluation]] — pipeline donde la LoRA se aplica
- [[comfyui]] — UI para inferencia con LoRA
- [[runpod]] — infra de training

## Estado

Página stub creada por audit (29-04-2026). Pendiente: documentar parámetros de training reales, learning rate, network rank/alpha, samples de output, métricas de identidad.


## Update 2026-05-02

Reusable caption format for [[lora]] training datasets, applied consistently across Brisa and Bere datasets.

**Structure:**
```
<trigger_word>, <shot_type>, <angle>, <setting/location>, <lighting>, <expression>, <physical details>, <clothing/accessories>, <companions/objects>, shot on 35mm film, Kodak Portra 400, natural grain
```

**Key rules:**
- Every caption starts with the trigger word (e.g. `bere` or `brisa`)
- Weighted trigger variant allowed: `(bere:1.2)` or `(brisa:1.25)`
- Shot types: close-up, close-up selfie, medium shot, full shot
- Angles: front view, three-quarter angle, profile view, slight low angle
- All captions end with consistent film style: `shot on 35mm film, Kodak Portra 400, natural grain`
- Captions generated via vision analysis of each photo (not generic)
- One `.txt` caption file per image, matching basename

**Tools:** Vision analysis (e.g. `vision_analyze`) to auto-describe each photo, then format into structured caption.
