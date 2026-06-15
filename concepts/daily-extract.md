---
title: "Daily Extract — Contexto Valioso"
created: "2026-04-21"
updated: "2026-04-21"
type: "concept"
---

# Daily Extract — Contexto Valioso

_Extraído de logs diarios (2026-04-09 a 2026-04-21), originalmente del workspace anterior._

## Personas adicionales
- **Fabito (Fabián Picón)** — amigo de Jorge, visitó Malibú 17/04
- **Pablo Emmerich** — corre Opencode sessions (Google Meet)
- **Pedro Lentini** — Technical Talks MCP Vast BHub
- **Andrés Cuñer** — trabaja en alarmas N8N → APIs en OpenPass, interactúa con @ia
- **Indira Muniz (Contractia)** — insiste en KYE meeting (sales pitch, 2da vez)
- **Vivi + Martín** — fueron a Candlelight Charly García + cena 10/04

## ia Google Chat Agent (separado de Brisa)
- **ia@openpass.com.ar** = bot independiente, GLM 5.1 vía n8n
- Jorge NO quiere que Brisa responda como ia
- Workflow: `5fLASZ8B9D3UcQJD`, webhook: `https://n8n.ai.openpass.com.ar/webhook/ia-chat-assistant`
- LLM Gateway: `https://llm.ai.openpass.com.ar/v1` (GLM 5.1, cred `qYE9RoCQsVcyglRU`)
- IyD space: `spaces/AAAAYfVv2wE`
- DMs a ia como persona NO accesibles vía Chat API — solo bot

## Infraestructura
- Node IP: 192.168.1.213 (cambió 17/04)
- GitLab token "git macbook pro" expiró en gitlab.openpass.com.ar — necesita renovación
- Jorge prefiere LLM Gateway interno sobre OpenRouter
- Expreso San Vicente (Línea 51): San Vicente 4:50 AM, Constitución 6:40 AM, Malibú ~7:45-8:00 AM. WhatsApp +54 9 11 4986-9237

## TTS lessons
- `plugins.allow` ROMPE bundled plugins (talk-voice) — NO usar
- `auto: "tagged"` BUG en parser (falla con streaming)
- `auto: "inbound"` = correcto (voz inbound, texto outbound)
- Aoede suena bien en es-AR

## ComfyUI lessons (local)
- IP-Adapter FaceID Plus V2 SDXL = ROTO (dim mismatch 2048,1280 vs 2048,1664)
- CyberRealisticPony v1.6 = mejor skin pero no compatible con FaceID
- SDXL = caricaturesco sin LoRA
- ComfyUI.app (8000) > conda (8188) para generación local

## RunPod / AI Toolkit
- AI Toolkit (Ostris v0.9.4) en `/workspace/ai-toolkit/`, puerto 8675
- Entrena LoRAs para FLUX, WAN 2.1/2.2, LTX-2/2.3
- Nginx: 8089→8188 (ComfyUI), 8666→8675 (AI Toolkit), auth user `api`
- ffmpeg NO en runpod/pytorch image — instalar
- VHS_VideoCombine no instalado → SaveImage + ffmpeg post-process

## D-ID / Ciudadanías BC
- D-ID Talks (Photo Avatar) funciona — Bere lo aprobó
- D-ID Clips (Presenter Alyssa) funciona pero menos customizable
- D-ID Agent conversacional — Jorge no le gustó, mediocre
- D-ID Art Nouveau Brisa avatar — D-ID no detecta cara (too stylized)
- Client key: `ck_KTcwMv4NGcYEty7zAo9Qv` (ciudadaniasbc.com)
- Plan: API Launch, 730 credits, ElevenLabs NO disponible
- Pendiente: re-hacer video de Bere con foto real (no AI frame)

## Higgsfield AI
- Cloud API: Kling 2.1, Seedance 1.0, DoP, Soul T2I
- No registrado aún. Alternativa a RunPod para modelos específicos.
