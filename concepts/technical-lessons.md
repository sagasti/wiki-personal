---
title: "Technical lessons (índice)"
created: "2026-07-12"
updated: "2026-07-18"
type: "concept"
tags: ["#ops", "#lessons", "#index", "#brisa"]
related: [[hermes-whatsapp-bridge-failure-mode]], [[hermes-cli-send-command-gap]], [[brisa-tools]], [[runpod]], [[comfyui]], [[hermes-gemini-google-alias-native-client]], [[brisa-video-production]]
sources: ["MEMORY.md weekly maintenance 2026-07-12", "Telegram 2026-07-12/13", "Telegram 2026-07-17"]
confidence: high
---

# Technical lessons (índice)

Hub de lecciones técnicas durables. El detalle vive en las páginas hijas; MEMORY solo apunta acá.

## Hermes / messaging

| Lección | Página |
|---------|--------|
| WA bridge timeouts 408/428/503, paths `platforms/whatsapp` | [[hermes-whatsapp-bridge-failure-mode]] |
| `hermes send` no existe | [[hermes-cli-send-command-gap]] |
| jidDecode / LID / allowlist | [[brisa-tools]], [[whatsapp-authorized]], [[whatsapp-bot-mode-allowlist-by-lid]] |
| Permisos per-contact | [[hermes-per-contact-permission-gap]] |
| Telegram: si polling/reconnect falla → mirar logs gateway; **no reiniciar** sin OK de Jorge | [[hermes-configuration]] |
| Alias `google` → OpenAI client + `thinking_config` 400; patch nativo + reapply post-update | [[hermes-gemini-google-alias-native-client]] |
| Model stack calidad-first (Grok main, OR fallbacks, vision xAI, smart off) | [[hermes-quality-first-model-stack]], [[hermes-configuration]] |

## Tooling / shell

| Lección | Página |
|---------|--------|
| Tirith pipe → interpreter blocking | [[tirith-pipe-to-interpreter-blocking]] |
| Higgsfield CLI + spaces en filenames | [[higgsfield-cli-filename-spaces-bug]] |

## GPU / storage / gen

| Lección | Página |
|---------|--------|
| RunPod S3 access key con `\|` | [[s3-access-key-pipe-char-incompatibility]], [[runpod]] |
| VAE latent cache incompat | [[vae-latent-cache-incompatibility]] |
| Wan 2.2 issues | [[wan22-issues]] |
| Dual LoRA stacking limita a blend de caras (no 2 personas distintas) | [[lora]] |
| FaceID stills: sin CLIPVision ViT-H / faceid bin → `Missing CLIPVision` | [[comfyui]], [[brisa-video-production]] |
| Resume overnight: pin `STAMP` al batch existente o regenera todo con stamp nuevo | [[brisa-video-production]], [[runpod]] |
| Save solo output final (no intermedios `*_jgg_*`) | [[brisa-video-production]] |
| Prod Fanvue post-17/7: solo `brisa_gen_v2.py` + LoRA `brisa_v2_lora2_ep024` | [[brisa-monetize-fanvue-onlyfans]] |

## Comportamiento operativo

- Si una search/tool falla 2–3 veces con el mismo query: preguntar ortografía antes de insistir
- Execute-Verify-Report; reintento ×1; nunca fallar en silencio

## Tags

#ops #lessons #index
