---
title: "brisa email gateway"
created: "2026-05-06"
updated: "2026-07-17"
type: "project"
tags: ["#brisa", "#email", "#gateway", "#infrastructure", "#gmail"]
related: [[brisa]]
sources: ["hermes-session/20260506_192921_fc0d74", "hermes-session/20260716_084703_952c46"]
confidence: "high"
---

# brisa email gateway

[[brisa]] recibe y envía mail como `brisa@sagasti.com`.

## Canales actuales (2026-07-17)

1. **Canal Hermes email** (preferido ops): Jorge armó el canal en Hermes — el mail entra como mensajes del gateway. **No hay cron de polling** (confirmado con Jorge 16/7: “armé un canal por hermes”).
2. **`gog` Gmail** para la cuenta: `gog auth add brisa@sagasti.com` ya se usó (Fanvue, Claudio, etc.).
3. **IMAP/SMTP clásico** (setup histórico): imap.gmail.com / smtp.gmail.com — app password en secrets; no re-pegar en chat.

## Reglas
- No crear cron de “check inbox” salvo que Jorge lo pida.
- Respuestas formales a terceros: confirmar tono con Jorge si no es ops Brisa/Fanvue.
- Secrets solo en `~/.hermes/secrets/` / gog keyring — nunca en wiki ni MEMORY.

## Links
- Personaje: [[brisa]]
- Monetización: [[brisa-monetize-fanvue-onlyfans]]
