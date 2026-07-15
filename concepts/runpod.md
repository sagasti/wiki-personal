---
title: "RunPod GPU Setup"
created: "2026-04-26"
updated: "2026-07-15"
type: "concept"
tags: ["#reference", "#devops", "#ai"]
date: "2026-04-26"
source: "MEMORY.md rotation; Desktop 20260713_174939_5f4b63 → 20260714_142753_b2cf3c"
valid_until: "2026-08-12"
related: [[brisa-face-pipeline-evaluation]], [[runpod-s3-forklift-access]], [[brisa]], [[brisa-video-production]]
---

# RunPod GPU Setup

## Pod comfyui-luz-h200 (on-demand)

> **2026-07:** el pod **se recrea on-demand** (skill `comfy-ui` / `runpod` / `pod.py`). No asumir IP/Pod ID fijos de entradas viejas. Verificar con skill antes de usar. **Nunca levantar sin OK de Jorge** (caro). H200 ~$4.39/h. **Post-job: SIEMPRE preguntar si apaga** — no `stop --force` automático (Jorge 15/7).

- **Name actual (scripts):** `comfyui-luz-h200` (histórico: brisa-comfyui-h200)
- **Pod ID reciente (puede cambiar):** `1n0whm7wacau00` (sesión 13–15/7; re-chequear con `pod.py status`)
- **GPU:** H200 143GB VRAM
- **SSH:** host `103.196.86.23`, **puerto público cambia en cada start** (ej. 10985 → 17264 → 18700 → 19210). Key local `~/.ssh/id_rsa`; en pod a veces también template key. Usar `StrictHostKeyChecking=no` si rota host key.
- **Network Volume:** f4uirc6q1f (us-nc-1) — estable; se llenó ~700GB durante uploads 13/7 → limpiar caches regenerables (`.hf_cache/`, downloads) **sin** tocar LoRAs/training_runs
- **ComfyUI URL:** https://comfy.sagasti.com (cloudflared a veces 530) · proxy RunPod confiable: `https://<podId>-8089.proxy.runpod.net`
- **Autostart:** Template `t9hgwtx2xb` → ComfyUI + nginx + cloudflared (~2–4 min a 8188 listo)
- **2026-07-15 ~02:50:** batch erótico 6/6 + prod limpia → `pod.py stop --force` → **EXITED** (no factura). Reanudar solo con OK Jorge.
- **Train Wan:** apagar Comfy (OOM). Scripts I2V: `/workspace/scripts/bere/wan_i2v_api_builder.py`

## Modelos SDXL en network volume (staged 2026-07-13/14)

Prefijo S3: `s3://f4uirc6q1f/ComfyUI/models/` (endpoint `https://s3api-us-nc-1.runpod.io`, region `us-nc-1`). Subida multi-GB **preferible con pod EXITED** vía `aws s3 cp` (SCP multi-GB inestable; Civitai corta ~1.5GB).

| Archivo | Path en volume | Notas |
|---------|----------------|--------|
| Juggernaut XL XI | `checkpoints/juggernautXL_juggXIByRundiffusion.safetensors` | **7.1 GB** — OK 2026-07-13 |
| CyberRealistic Pony v160 | `checkpoints/Pony/cyberrealisticPony_v160.safetensors` | ~5.1 GB — **UNet Diffusers only** (0 VAE/CLIP en el file) |
| FaceID SDXL | `ipadapter/ip-adapter-faceid_sdxl.bin` | + plusv2 ya presente |
| FaceID LoRA | `loras/…/ip-adapter-faceid_sdxl_lora.safetensors` | ~372 MB |
| SDXL VAE | `vae/SDXL/sdxl_vae.safetensors` | ~335 MB |
| CLIP-G | `text_encoders/clip_g.safetensors` | ~1.3 GB — DualCLIP con CRPony (subido 14/7) |
| LoRA stills | `loras/brisa_sdxl/brisa_stills.safetensors` (+ alias PRODUCTION) | prod 15/7 |
| LoRA video | `loras/identity/brisa_video.safetensors` (+ alias wan22 PRODUCTION) | all6 / prod 15/7 |

**Pipeline stills Brisa (prod):** Jugg + `brisa_stills` + FaceID light → CRPony d=0.4 DualCLIP. Ver [[brisa-video-production]] + [[brisa-face-pipeline-evaluation]].

## Pod ideogram-nc1 (experimental)
- **Pod ID:** 8jx9xeju7h2fsi
- **Image:** runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04
- **JUPYTER_PASSWORD:** ideogram2026
- **Status:** Stopped 14/6 por Jorge. Volume `f4uirc6q1f` intacto.
- **Uso:** Exploración de Ideogram, no ComfyUI.

## Cron
- `runpod-gpu-monitor-brisa`: cada 15m, chequea pod gt7xw3blwtrthx, notifica si GPU disponible
- `comfyui-local-autostop`: cada 10m, para ComfyUI local si idle >10 min
- `runpod-autostop`: **PAUSED desde 5/5** — Jorge preguntó 14/6 pero no reactivó

## Regla crítica
- **NUNCA levantar sin preguntar a Jorge** (caro)

## Template
- `comfyui-luz-auto` (t9hgwtx2xb) — auto-fix torch CUDA mismatch, Brisa SSH key inyectada

## Notas
- Pod ID y SSH cambian con cada restart/recreate. Verificar antes de usar.
- `valid_until` renovado 2026-07-12 → 2026-08-12 (pod on-demand; revalidar ID/SSH al usar).

---
*Promovido desde MEMORY.md el 2026-04-26 (mantenimiento semanal)*


## Update 2026-05-11

## Configuration
- **Endpoint**: `s3api-us-nc-1.runpod.io`
- **Region**: `us-nc-1`
- **Bucket**: `f4uirc6q1f`
- **Access Key format**: `google-oauth2|<numeric_id>` (contains `|`)
- **Path-style access**: required (not virtual-hosted)

## GUI Client Incompatibility
The `|` character in the Access Key breaks AWS v4 signature generation in all GUI S3 clients tested:
- ForkLift: hardcoded to `s3.amazonaws.com`, no custom endpoint/region fields
- Cyberduck: fails on `|` in access key
- Transmit: fails on `|` in access key

Only **AWS CLI v1** handles the `|` correctly.

## API Pagination Bug
RunPod's S3-compatible API has broken pagination — `aws s3 sync` and `aws s3 ls` return incomplete results or hang. Files must be downloaded individually with `aws s3 cp`.

## Workaround: Local Mirror
Sync datasets locally to `~/RunPod-Storage/datasets/` using AWS CLI, then browse with Finder/ForkLift as a normal folder.

Known dataset paths under `s3://f4uirc6q1f/datasets/`:
- `bere_curated/`
- `cabel_curated/`
- `bere_final/`
- `jorge_sagasti_final/`
