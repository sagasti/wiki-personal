---
title: "Technical lessons (índice)"
created: "2026-07-12"
updated: "2026-07-12"
type: "concept"
tags: ["#ops", "#lessons", "#index", "#brisa"]
related: [[hermes-whatsapp-bridge-failure-mode]], [[hermes-cli-send-command-gap]], [[brisa-tools]], [[runpod]], [[comfyui]]
sources: ["MEMORY.md weekly maintenance 2026-07-12"]
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

## Comportamiento operativo

- Si una search/tool falla 2–3 veces con el mismo query: preguntar ortografía antes de insistir
- Execute-Verify-Report; reintento ×1; nunca fallar en silencio

## Tags

#ops #lessons #index
