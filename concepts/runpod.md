---
title: "RunPod GPU Setup"
created: "2026-04-26"
updated: "2026-06-14"
type: "concept"
tags: ["#reference", "#devops", "#ai"]
date: "2026-04-26"
source: "MEMORY.md rotation (weekly maintenance)"
valid_until: "2026-05-26"
---

# RunPod GPU Setup

## Pod Activo
- **Name:** brisa-comfyui-h200
- **Pod ID:** gt7xw3blwtrthx
- **GPU:** H200 143GB VRAM
- **SSH:** verificar con `runpod` skill (cambia cada restart). Key `/opt/data/.ssh/id_ed25519` funciona en pods creados con template `t9hgwtx2xb` (después del 13/6).
- **Network Volume:** f4uirc6q1f (300GB, us-nc-1)
- **ComfyUI URL:** https://comfy.sagasti.com (Basic auth `api:$COMFYUI_API_PASSWORD`)
- **Autostart:** Template `t9hgwtx2xb` arranca ComfyUI + nginx + cloudflared tunnel automáticamente (~45s).

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
- `valid_until` set a 1 mes — revisar si el pod sigue activo.

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
