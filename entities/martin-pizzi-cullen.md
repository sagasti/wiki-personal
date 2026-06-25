---
title: "Martín Pizzi Cullen"
created: "2026-06-23"
updated: "2026-06-23"
type: "entity"
tags: ["#person", "#luz-estudio", "#lora"]
related: [[jorge-sagasti]]
---

# Martín Pizzi Cullen

Persona del círculo social de Jorge (aparece en muchas fotos con Emiliano Sagasti, Fabián Picón,
Ignacio Socas — amigos de toda la vida; fotos desde 1981, colegio EAM, hasta hoy). Señor mayor,
pelado, perilla/candado gris, a veces anteojos.

## LoRA de identidad (Luz Estudio, 2026-06-23)

Jorge pidió entrenar un **LoRA de identidad de Martín** (mismo pipeline que Brisa/Bere/cabel).
- **Trigger word**: `mpcullen`
- **Dataset**: 43 imgs curadas (18 cuerpo entero/solo — incl. 15 fondo verde chroma — + 25 crops de cara).
- **Receta**: Flux.2 Klein 9B + LoKr + lr 5e-4, 4500 steps (la RECETA DEFINITIVA del proyecto).
- **Fuentes**: 255 fotos face-tagged en el Photos.app de Jorge (1981→2026) + carpeta `~/Desktop/martin-pizzi`.
- **Workdir**: `~/dev/comfy-ui/datasets/martin_pizzi/` (`dataset/` candidatas, `final/` las 43, scripts del pipeline).

Cómo se armó el dataset (pipeline reusable para personas reales): export por nombre con **osxphotos**
+ **InsightFace** (buffalo_l) para clustering de identidad y crops limpios. Detalle del pipeline y los
gotchas en [[building-person-lora-datasets-from-photos]].
