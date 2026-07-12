---
title: "hermes send — command gap"
created: "2026-07-12"
updated: "2026-07-12"
type: "concept"
tags: ["#hermes", "#cli", "#gotcha", "#ops"]
related: [[hermes-configuration]], [[brisa-tools]], [[technical-lessons]]
sources: ["MEMORY.md weekly maintenance 2026-07-12"]
confidence: high
---

# hermes send — command gap

## Gotcha

El comando **`hermes send` no existe**. Agentes y crons que lo invocan fallan.

## Forma correcta

```bash
hermes message send --channel telegram --target "1808182714" --message "texto"
hermes message send --channel whatsapp --target "+549..." --message "texto"
# con media:
hermes message send --channel telegram --target "1808182714" --message "desc" --media /path/file.mp4
```

## WhatsApp fallback

Si el gateway tira `jidDecode` / contacto sin mapping:

```bash
curl -X POST http://localhost:3000/send \
  -H 'Content-Type: application/json' \
  -d '{"chatId":"<phone|lid>@s.whatsapp.net","message":"texto"}'
```

Detalle: [[brisa-tools]], [[hermes-whatsapp-bridge-failure-mode]].

## Tags

#hermes #cli #gotcha
