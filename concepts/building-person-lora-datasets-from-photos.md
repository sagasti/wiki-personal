---
title: "Armar datasets de LoRA de personas reales desde Photos.app"
created: "2026-06-23"
updated: "2026-06-23"
type: "concept"
tags: ["#luz-estudio", "#lora", "#dataset", "#osxphotos", "#insightface"]
related: [[martin-pizzi-cullen]], [[jorge-sagasti]]
---

# Pipeline: dataset de LoRA de identidad desde Photos.app

Probado armando el LoRA de [[martin-pizzi-cullen]] (2026-06-23). Reusable para cualquier persona real
que esté en el Photos.app de Jorge. Vive en `~/dev/comfy-ui/datasets/<persona>/` con scripts.

## Pasos
1. **Sourcing — osxphotos** (instalado, `/opt/homebrew/bin/osxphotos`). Si la persona está face-tagged en
   Photos: `osxphotos export <dir> --person "Nombre Completo" --only-photos --convert-to-jpeg --filename "{uuid}" --update`.
   `--update` es idempotente (incremental, agarra solo nuevas). Listar personas: `osxphotos persons`.
2. **NO olvidar las carpetas manuales** (ej. `~/Desktop/<persona>`): pueden tener fotos que NO están en Photos
   (WhatsApp, etc). Procesarlas TAMBIÉN, dedup contra Photos por average-hash (aHash, hamming ≤4).
   *(Costó: en Martín casi pierdo 57 fotos buenas —incl. cuerpo entero— por no ingerir el Desktop.)*
3. **Identidad — InsightFace buffalo_l** (CPU alcanza para ~300 imgs, ~5 min). Detectar TODAS las caras de cada
   foto, embeddings, **clustering DBSCAN cosine**. Como todas las fotos contienen al sujeto, **el cluster más
   grande (presente en casi todas las fotos) es él**. Mostrar reps de los top clusters → que Jorge confirme cuál.
4. **Crops** con los bbox de InsightFace (limpios): solo/dominante (cara ≥2.2× la 2da) → foto **entera** (cuerpo);
   grupal → **cabeza+torso** (expandir bbox ~2.8× ancho, -0.75fh arriba, +2.9fh abajo). Filtrar por tamaño de
   cara (≥140-200px) + nitidez (Laplacian var) + det_score.
5. **Curación**: selector HTML clickable ordenado por calidad → exporta lista → `final/`.
6. Caption sin rasgos + train con la RECETA DEFINITIVA (Flux.2 Klein + LoKr + lr 5e-4). Ver lessons_learned del repo.

## ⛔ Gotchas
- **Las coordenadas de cara de Photos (osxphotos `face_rect`/`mwg_rs_area`/tags) son POCO CONFIABLES**: el tag
  "Martín" muchas veces caía sobre OTRA cara (incl. una mujer), y `face_rect` está en el espacio del thumbnail de
  detección → mal escalado en fotos high-res. **No usar las coords de Photos. Usar InsightFace** (bbox propio +
  identidad por embedding). Photos solo sirve para SABER que la persona está en la foto, no DÓNDE.
- **insightface NO instala en Python 3.14** (homebrew default, sin wheels). Hacer venv con **python 3.12**:
  `/opt/homebrew/opt/python@3.12/bin/python3.12 -m venv .venv_face` + `pip install insightface onnxruntime
  opencv-python-headless scikit-learn`. (osxphotos sí corre en el 3.14 del sistema.)
- **Material social = caras chicas**: las fotos grupales (cenas) dan caras de ~50-200px → crops blandos. Para un
  LoRA bueno conviene **conseguir fotos dedicadas del sujeto solo** (cuerpo entero, primeros planos, fondo limpio).
  Las de fondo verde chroma de Martín fueron oro — al captionar, **describir el fondo** ("green screen") para que
  el modelo no ate el fondo a la identidad.
