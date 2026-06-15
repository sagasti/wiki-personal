---
title: "Luz Estudio Workspace"
created: "2026-05-07"
updated: "2026-06-09"
type: "project"
tags: ["#project", "#luz-estudio", "#ai-video", "#comfyui", "#runpod", "#workspace", "#discontinuado"]
related: [[luz-estudio]], [[runpod]], [[comfyui]], [[hunyuan-video-recipe]], [[ai-video-generation]], [[lora]]
confidence: high
---

# Luz Estudio Workspace

> ⚠️ **DISCONTINUADO (2026-06-09)**: el negocio **Luz Estudio** (servicios comerciales de video IA) se
> terminó — Jorge no lo continúa. El workspace `~/dev/luz-estudio` se **renombró a `~/dev/comfy-ui`** y el
> agente/slug pasó a llamarse `comfy-ui`, acotado a **administrar ComfyUI** (pods RunPod, workflows, LoRAs
> — esto sí sigue, le sirve a [[brisa]]). La infra `luz.center` (VPS Hetzner `luz-prod-01` + n8n + bot
> Telegram) está en **teardown**, delegado a la sesión `infra` (dueña del VPS). ⚠️ Ese VPS también hostea
> `admin.ciudadaniasbc.com` (app LIVE de Bere) → teardown quirúrgico, no nukear el box. Ver
> [[luz-center-infra]].

Repo `~/dev/comfy-ui` (ex `~/dev/luz-estudio`) — workspace de Claude Code para administrar ComfyUI. Lo de abajo es el stack productivo histórico de cuando era Luz Estudio.

## Stack productivo

| Pieza | Detalle |
|---|---|
| **GPU primaria** | NVIDIA H200 (143 GB VRAM) en [[runpod]] cloud Community |
| **Pod productivo** | `comfyui-luz` |
| **Software** | ComfyUI v0.19.1 + custom nodes (MatAnyone, VideoHelperSuite, GGUF, KJNodes, LTXVideo) |
| **URL pública** | `https://comfi-ui.luz.center` (Cloudflare Tunnel + nginx auth) |
| **Storage** | RunPod network volume **200 GB** en US-NC-1 — todo persiste entre pods |
| **Local dev** | Mac M3 Max (36 GB) con ComfyUI en `/Volumes/Extra/ComfyUI/` + **conda env `comfy-ui`** (Python 3.12.13, torch 2.11, MPS, 187 packages). Arranque: `conda activate comfy-ui && python main.py --listen 127.0.0.1 --port 8188 --use-split-cross-attention`. Hay un `venv/` legacy en el mismo dir pero **no se usa** (subset 121 packages). ComfyUI.app descartado. |

## Modelos disponibles en network volume

- **Wan 2.2 T2V** (fp8) ← preferido para T2V
- **HunyuanVideo** (bf16) ← ver [[hunyuan-video-recipe]]
- **LTX 2.3** (fp8)
- **Qwen Image Edit**
- **Flux**

## Skills locales del workspace

`.claude/skills/`:

- **`video-creator`** — pipeline ComfyUI completo: Wan 2.2 / HunyuanVideo / LTX, training+inference de LoRAs, manejo de workflows, background swap, color grading
- **`runpod-manager`** — pods (create/start/stop/terminate via GraphQL), S3 del network volume, Cloudflare Tunnel

Triggers de auto-load:
- `video-creator`: "generar video", "t2v", "i2v", "train a LoRA", "background swap", menciones a Wan/HunyuanVideo/LTX/ComfyUI
- `runpod-manager`: "levantar pod", "apagar pod", "tunnel", "cloudflare"

## Preferencias FIJAS (calidad > velocidad)

Aplicar SIEMPRE estas reglas, son criterio explícito de Jorge:

- bf16 sobre fp8 cuantizado cuando la VRAM alcance
- 30+ steps sobre LoRAs de aceleración
- BiRefNet portrait sobre u2net para segmentación de personas
- Videos de fondo largos (20-30s) para evitar loops visibles
- MatAnyone sobre rembg per-frame (consistencia temporal)
- Color grading post para composites realistas
- Wan 2.2 full sobre Wan 2.1 GGUF cuando esté en RunPod
- Ante duda en tradeoff → mayor calidad y avisar

## Workflow típico

```bash
cd ~/dev/luz-estudio
claude

# 1. Levantar pod si no está corriendo
# > "levantá un pod H200 y corré el autostart"
# (runpod-manager hace curl GraphQL, espera SSH, ejecuta autostart.sh)

# 2. Generar video
# > "armame un workflow Wan 2.2 para X"
# (video-creator consulta references/workflows.md)

# 3. Apagar pod al cerrar — paga por hora
```

## Referencias internas

- `references/lessons_learned.md` — bugs ya resueltos + workarounds
- `references/workflows.md` — library de JSON workflows listos
- `.secrets/credentials.md` — gitignoreado, RunPod/Cloudflare/SSH keys

## Servicios comerciales que monta este workspace

(Lista en [[luz-estudio]] entity page — acá solo recordatorio operativo)

- T2V con LoRAs custom de personas/marcas
- Background replacement (cambio de fondo manteniendo subject + audio)
- Animación de personajes consistentes (LoRA de identidad)
- Múltiples ángulos desde una sola foto (Qwen Image Edit)
- Upscaling de video (SeedVR2 + GAN x4)
- Eventualmente: API endpoint serverless

## Sesión activa pinneada

- **Title:** "Luz Estudio" (Claude Code Desktop) — la sesión de mayor turn count del catálogo (~294 turns acumulados al cierre del export del repo)
- **cwd:** `/Users/jorge/dev/luz-estudio`

Ver [[jorge-active-projects]] para el catálogo completo y [[luz-estudio]] para el plano comercial/empresa.
