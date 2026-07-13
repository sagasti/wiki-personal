---
title: "Fernando Palermo"
created: "2026-05-06"
updated: "2026-05-06"
type: "entity"
tags: ["#amigo", "#montevideo", "#uruguay", "#mundomac", "#socio"]
sources: []
hermes_session: "20260506_144021_586f5a5e"
confidence: "medium"
---

# Fernando Palermo

Amigo de toda la vida de Jorge. Vive en Montevideo, Uruguay.

**Esposa:** Mercedes ("Mecha")
**Hijos:** Mateo y un segundo (nombre por confirmar)
**Teléfono:** +598 99 699 673

**Historia compartida:** Cofundador de [[mundomac-website]] junto a Jorge y [[walter-soto]] — **Sagasti Palermo y Soto S.R.L.**, **Montevideo** (1995). Ya no son socios pero siguen muy amigos los tres. MundoMac Montevideo fue la base **mucho antes** del local **MundoMac Punta**.

**Relación con Brisa:** Autorizado para conversar por WhatsApp.


## Notas técnicas

## WhatsApp allowed users

Los contactos autorizados para WhatsApp se configuran en **dos lugares**:

1. **`~/.hermes/.env`** → `WHATSAPP_ALLOWED_USERS=...` (bridge-level, hard block — si no estás acá, el bridge ni pasa el mensaje)
2. **`~/.hermes/config.yaml`** → `platforms.whatsapp.unauthorized_dm_behavior` (Hermes-level: `ignore`|`pairing`|`allow`)

**Siempre agregar el número en AMBOS lugares.** El bridge es la primera barrera.

Números actuales (May 2026):
- 5491123034606
- 5491176399809
- 5491159809449
- 5491131730763
- 59899699673 (Fer Palermo)

Después de cambiar `.env`, hace falta restart del gateway.


## WhatsApp

## WhatsApp Authorization

- **LID:** `56294337695961@lid` (resolved 6/5/2026 after pairing)
- **Pairing code:** ZK7CNU7T (approved)
- **Bridge allowlist workaround:** Had to empty `WHATSAPP_ALLOWED_USERS` in `.env` because bridge couldn't resolve LID→phone for new contacts. Hermes `pairing` mode handles auth now.
- **Sending messages:** Gateway `send_message` fails with `jidDecode` error. Must use bridge HTTP endpoint: `curl -X POST http://localhost:3000/send -d '{"chatId":"56294337695961@lid","message":"text"}'`
- **First message sent:** 6/5/2026 — text intro from Brisa


## WhatsApp

## WhatsApp JIDs resueltos
- Jorge: `233642076930156@lid` → tel `5491123034606`
- Fer Palermo: `56294337695961@lid` → tel `59899699673`

## Nota técnica
El `send_message` del gateway no resuelve JIDs de WhatsApp. Para mandar mensajes directos, usar el bridge: `curl -s -X POST http://localhost:3000/send -H "Content-Type: application/json" -d '{"chatId": "<JID>", "message": "..."}'`

La allowlist del bridge se vació (`WHATSAPP_ALLOWED_USERS=`) para que pase todo. Hermes controla autorización con `unauthorized_dm_behavior: pairing` en config.yaml.
