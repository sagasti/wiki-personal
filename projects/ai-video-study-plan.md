---
title: "Plan de Estudios — AI Video Generation"
created: "2026-04-19"
updated: "2026-04-21"
type: "project"
---

# Plan de Estudios — AI Video Generation

_Objetivo: dominar generación de video con IA para poder crear cualquier cosa que nos pidan, y enseñarle a Jorge._

---

## Módulo 1: Fundamentos (Semana 1)

### 1.1 ComfyUI Avanzado
- [ ] Nodes esenciales: KSampler, VAEDecode, CLIPTextEncode, SaveImage
- [ ] Custom nodes: Video Helper Suite, ComfyUI Manager, KJ Nodes
- [ ] Workflows: cargar, modificar, debuggear (red nodes, missing models)
- [ ] Latent space: qué es, cómo funciona, por qué importa
- [ ] Model loading: diffusion_models vs checkpoints, FP8 vs BF16 vs GGUF
- [ ] VRAM management: SageAttention, Teacache, layer offloading, Tiled VAE Decode

### 1.2 Modelos de Video — Overview
- [ ] Hunyuan Video: 13B, T2V + I2V, prompt rewrite, camera motion
- [ ] WAN 2.1/2.2: 1.3B y 14B, T2V + I2V, workhorse local
- [ ] LTX 2/2.3: 22B, T2V + I2V + audio, 2-pass generation, distilled LoRA
- [ ] Comparativa: cuándo usar cada uno (calidad vs velocidad vs VRAM)

### 1.3 Parámetros Críticos
- [ ] CFG: rangos por modelo (Hunyuan 6-10, LTX 3-5, WAN 5-8)
- [ ] Steps: calidad vs tiempo (20-30 standard, 6 con fast LoRA)
- [ ] Frames: FPS × segundos + 1 (ej: 24×5+1 = 121)
- [ ] Resolución: múltiplo de 32, máx 720p nativo → upscale
- [ ] Samplers: flowmatch (LTX/Hunyuan), euler_ancestral (WAN)
- [ ] Schedulers: normal, karras, exponential — cuándo cada uno

---

## Módulo 2: Generación de Video (Semana 2)

### 2.1 Text-to-Video (T2V)
- [ ] Prompt engineering para video: describir movimiento, no solo escena estática
- [ ] Camera motion en prompts (ver Módulo 4)
- [ ] Sujeto + cámara + entorno = evitar "estatua congelada"
- [ ] Prompt scheduling para videos largos
- [ ] Negative prompts efectivos para video

### 2.2 Image-to-Video (I2V)
- [ ] Preparar imagen de entrada: resolución, aspect ratio
- [ ] CFG bajo para I2V (3.0, no 7.0 — la imagen ya es ground truth)
- [ ] Steps altos para motion suave (60-80)
- [ ] FPS alto (50) para fluidez
- [ ] Florence2 para auto-captioning de imágenes

### 2.3 Video-to-Video (V2V)
- [ ] Driving video + máscara
- [ ] ControlNets: Canny, Depth, Pose
- [ ] Primera pasada baja res → upscale latent → segunda pasada refina

### 2.4 Upscaling y Post-procesamiento
- [ ] Latent upscale 2X (LTX)
- [ ] Topaz Video AI para upscale final
- [ ] RTX Super Resolution (NVIDIA)
- [ ] Frame interpolation para fluidez
- [ ] FFmpeg: formatos, CRF, movflags +faststart

---

## Módulo 3: LoRA Training (Semana 3)

### 3.1 Dataset Preparation
- [ ] Capturar video: 20-30 clips, 3-8 seg c/u
- [ ] Cortar con DaVinci Resolve (blade tool, export individual)
- [ ] Solo clips donde aparece el sujeto — nada de otros personajes
- [ ] Captioning: descripción visual + audio entre comillas
- [ ] Gemini Pro para auto-captioning → corregir a mano
- [ ] Character sheet: 8 ángulos del personaje en grilla

### 3.2 Training con AI Toolkit (Ostris)
- [ ] Setup: Node.js v22 + Python 3.12 + venv
- [ ] UI: puerto 8675, auth token
- [ ] Config: modelo LTX 2.3, Low VRAM, FP8 quantize, rank 32
- [ ] Steps = clips × 200-250 (ej: 30 clips → 6000-7500 steps)
- [ ] 2 fases: High Noise (captura) → Balance (refinamiento)
- [ ] Auto Frame Count, Cache Text Embeddings, Do Differential Guidance
- [ ] Resolución: 512 fase 1, +768 fase 2 (1024 con H200)

### 3.3 Tipos de LoRA
- [ ] Standard LoRA: más flexible, para characters/estilos
- [ ] IC LoRA: image condition, para animación específica
- [ ] ID LoRA: identity only, más específico pero menos flexible
- [ ] Distilled LoRA: acelera generación, mejora audio

### 3.4 Evaluación y Deploy
- [ ] Probar LoRA en ComfyUI con workflow T2V
- [ ] Verificar consistencia en distintas escenas
- [ ] Ajustar weight (0.7-1.0)
- [ ] Exportar para ComfyUI y LTX Studio

---

## Módulo 4: Camera & Cinematography (Semana 4)

### 4.1 Camera Motion Dictionary
- [ ] Dolly in/out: "camera slowly dollies forward/backward"
- [ ] Pan left/right: "camera pans left, revealing [subject]"
- [ ] Tilt up/down: "camera tilts up from [bottom] to reveal [top]"
- [ ] Orbit: "camera travels in half circle around subject"
- [ ] Tracking: "camera tracks alongside walking subject"
- [ ] Crane up/down: "camera lifts vertically, revealing environment"
- [ ] Drone: "high altitude flyover, drone ascends while panning down"
- [ ] Snap zoom: "extremely fast abrupt zoom into [target]"
- [ ] Rack focus: "focus shifts from foreground to background"
- [ ] 360 spin: "camera rotates completely around centered subject"
- [ ] POV: "first person view, subtle head motion and footsteps"
- [ ] Vertigo/Zolly: "dolly with opposite zoom"
- [ ] Dutch angle: "camera tilted diagonally, tension"
- [ ] Handheld: "subtle shake, imperfect framing, documentary"

### 4.2 First Frame / Last Frame
- [ ] LTX 2.3: lock start y end frame para control total
- [ ] Evitar sorpresas: definir exactamente dónde empieza y termina
- [ ] Looping: last frame = first frame para loops perfectos

### 4.3 Storyboarding con LTX Studio
- [ ] Script → storyboard visual automático
- [ ] Character sheet como referencia para consistencia
- [ ] Editar shots, camera angles, micro detalles
- [ ] Generar video desde storyboard
- [ ] Retake: regenerar solo un segmento

---

## Módulo 5: VFX y Composición (Semana 5)

### 5.1 AI VFX Workflow (Inner Reflections)
- [ ] OneVAE: inpainting/outpainting + ControlNets
- [ ] Gary's model: reference images, identity preservation
- [ ] Model merge: lo mejor de ambos
- [ ] Máscara blanco/negro: blanco = generar, negro = mantener
- [ ] Driving video: footage modificado + ControlNet

### 5.2 ControlNets para VFX
- [ ] Canny: preservar edges exactos
- [ ] Depth: Z-depth (blanco = cerca, negro = lejos)
- [ ] Pose: OpenPose skeleton para movimiento humano
- [ ] Camera tracking: puntos de tracking → reproduce movimiento

### 5.3 Composición
- [ ] Clean plates: remover objetos del footage
- [ ] Roto en After Effects/DaVinci → máscara
- [ ] Blend generado + original con máscara
- [ ] Interacción: reflejos, sombras, iluminación match

---

## Módulo 6: Producción para Ciudadanías BC (Semana 6)

### 6.1 Reels de Bere
- [ ] Character sheet de Bere (8 ángulos, photo-realistic)
- [ ] Script templates para Reels (myth-busting, testimonios, info)
- [ ] Camera moves: dolly + "Bere camina hacia cámara"
- [ ] Audio: diálogo limpio con LTX 2.3
- [ ] Vertical (9:16) para Instagram/TikTok

### 6.2 Posts con VFX
- [ ] Pasaporte español flotando con partículas doradas
- [ ] Bere frente a la Sagrada Familia (depth + reference)
- [ ] Bandera española con movimiento de tela
- [ ] Transiciones entre escenas (first/last frame)

### 6.3 Pipeline Completo
- [ ] Idea → script → storyboard → generar → editar → postear
- [ ] Automatizar con ComfyUI API + Buffer
- [ ] Batch generation: variaciones del mismo shot
- [ ] A/B testing en redes

---

## Práctica Nocturna (en Mac de Jorge)

**Regla:** Noche = generación (no compite con GPU de día)

| Sesión | Qué hacer | Resolución | Tiempo est. |
|---|---|---|---|
| 1 | ComfyUI local: verificar, instalar nodes | - | 30 min |
| 2 | Hunyuan T2V: 3 prompts de prueba | 480p, 73f | 20 min/gen |
| 3 | LTX 2.3 T2V: mismos prompts, comparar | 480p, 121f | 15 min/gen |
| 4 | WAN 2.1 I2V: animar imagen existente | 480p, 97f | 10 min/gen |
| 5 | Camera motion: probar 5 movimientos | 480p, 73f | 15 min/gen |
| 6 | LTX 2-pass: baja res → upscale | 480p→960p | 30 min/gen |
| 7 | VFX: máscara + depth + canny | 480p, 73f | 40 min/gen |
| 8 | Character sheet: generar de Bere | 1024px img | 5 min/gen |

---

## Entregables

1. **Skill `ai-video`** — SKILL.md con todo el conocimiento
2. **Workflows ComfyUI** — JSON files para cada caso de uso
3. **Prompt templates** — cámara, sujetos, estilos
4. **Guía de LoRA training** — paso a paso con screenshots
5. **Recetas Ciudadanías BC** — scripts + prompts + workflows listos
