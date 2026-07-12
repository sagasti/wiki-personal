---
title: "Hermes WhatsApp bridge — failure mode"
created: "2026-07-11"
updated: "2026-07-12"
type: "concept"
tags: ["#whatsapp", "#hermes", "#bridge", "#ops", "#brisa"]
related: [[whatsapp-authorized]], [[whatsapp-bot-mode-allowlist-by-lid]], [[brisa-tools]], [[fernando-palermo]]
sources: ["hermes-session/20260626_164237_fb723f12"]
confidence: high
---

# Hermes WhatsApp bridge — failure mode

Diagnóstico operativo del bridge Baileys de Hermes (cuenta Brisa). Jorge pidió revisar errores del canal WhatsApp el **2026-07-11** (Telegram).

## Paths actuales (2026-07)

> ⚠️ Rutas viejas en docs anteriores (`~/.hermes/whatsapp/...`) **quedaron desactualizadas**.

| Qué | Path |
|-----|------|
| Bridge log | `~/.hermes/platforms/whatsapp/bridge.log` |
| Session dir | `~/.hermes/platforms/whatsapp/session/` |
| PID | `~/.hermes/platforms/whatsapp/session/bridge.pid` |
| Listen | `localhost:3000` · `mode: bot` |

## Síntomas recurrentes (log)

- `Timeout in AwaitingInitialSync, forcing state to Online and flushing buffer`
- `timed out waiting for message`
- **Connection closed** con códigos:
  - **408** — timeout esperando mensajes (ráfagas largas)
  - **428** — cierre frecuente; reconnect en 3s
  - **503** — `stream:error` / stream errored out
- Reconnects automáticos en bucle (`Reconnecting in 3s...`)
- A veces **QR / "Waiting for scan..."** cuando la sesión se invalidó

El bridge suele volver a `✅ WhatsApp connected!` solo, pero el canal queda **inestable** (mensajes demorados o caídas intermitentes).

## Allowlist observado en runtime (2026-07-11)

```
Allowed users: 233642076930156, 90761618051243, 124021693755633, 229424284885240, 56294337695961
```

(Corresponden a Jorge, Bere, Vivi, Lorena, Fer — ver [[whatsapp-authorized]]. El log a veces omite el sufijo `@lid`.)

## Qué hacer cuando Jorge reporta “WhatsApp no anda”

1. `tail -80 ~/.hermes/platforms/whatsapp/bridge.log`
2. Buscar `408` / `428` / `503` / `AwaitingInitialSync` / `Waiting for scan`
3. Si hay QR o sesión rota → avisar a Jorge (rescaneo QR); **no reiniciar gateway** sin que lo pida
4. Gateway paralelo: `~/.hermes/logs/gateway.error.log`, `errors.log`
5. Envíos con `jidDecode` → bypass HTTP al bridge (`localhost:3000/send`) — ver [[brisa-tools]]

## Relacionado

- Auth / allowlist: [[whatsapp-authorized]], [[whatsapp-bot-mode-allowlist-by-lid]]
- LID / jidDecode: páginas `whatsapp-bridge-lid-and-jiddecode-pitfalls` (si existen) + [[brisa-tools]]
- MEMORY pointer: `WA bridge: ver [[hermes-whatsapp-bridge-failure-mode]]`

## Tags

#whatsapp #hermes #bridge #ops
