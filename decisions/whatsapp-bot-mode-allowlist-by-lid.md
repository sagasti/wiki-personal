---
title: "WhatsApp: bot mode + allowlist explícito por LID"
created: "2026-05-08"
updated: "2026-05-08"
type: "decision"
status: "active"
supersedes: "[[whatsapp-pairing-over-allowlist]]"
tags: ["#hermes", "#whatsapp", "#authorization", "#allowlist"]
related: [[brisa]], [[whatsapp-authorized]], [[hermes-configuration]]
confidence: "high"
---

# WhatsApp: bot mode + allowlist explícito por LID

## Contexto

El `hermes update` del 2026-05-08 trajo el commit upstream `6a4ecc0a9` (`fix(whatsapp): reject strangers by default, never respond in self-chat`), que invalidó el esquema previo [[whatsapp-pairing-over-allowlist]]. Brisa dejó de contestar a todos.

## Decisión

**Volver a allowlist explícito por LID, mode `bot`.**

### Config

En `~/.hermes/.env`:
```bash
WHATSAPP_MODE=bot
WHATSAPP_ALLOWED_USERS=233642076930156@lid,90761618051243@lid,124021693755633@lid,229424284885240@lid,56294337695961@lid
```

(Jorge, Bere, Vivi, Lore, Fer — ver [[whatsapp-authorized]] para el catálogo.)

`config.yaml` queda:
```yaml
platforms:
  whatsapp:
    unauthorized_dm_behavior: pairing
```

— pero el flow de pairing ahora **rara vez se dispara**, porque el bridge filtra antes con el allowlist.

## Trade-offs evaluados

### Opción A — `bot` + allowlist explícito por LID ✅ ELEGIDA

**Pro:** strangers nunca llegan al gateway → cero superficie de spam/fishing. Cero costo de tokens en mensajes basura.
**Contra:** agregar contacto nuevo requiere edit manual del `.env` + restart. Pairing automático muerto.

### Opción B — `bot` + `WHATSAPP_ALLOWED_USERS=*`

**Pro:** mantiene el comportamiento de [[whatsapp-pairing-over-allowlist]] — pasa todo al gateway, Hermes filtra con pairing.
**Contra:** strangers (incluido números equivocados) reciben código de pairing automático → footgun documentado por upstream.

### Por qué A

- El catálogo de contactos autorizados (5 personas) cambia muy poco en el tiempo.
- La fricción de agregar uno nuevo (un edit + restart) es trivial vs el riesgo de B.
- Upstream tiene razón en que B es un footgun.

## Cómo agregar un contacto nuevo

1. La persona te manda un mensaje (será rechazado pero el bridge loggea el LID)
2. Sacar el LID:
   ```bash
   tail -100 ~/.hermes/platforms/whatsapp/bridge.log | grep allowlist_mismatch | tail -5
   ```
3. Append al `.env`:
   ```bash
   sed -i.bak "s|^WHATSAPP_ALLOWED_USERS=.*|&,NUEVO_LID@lid|" ~/.hermes/.env
   ```
4. `hermes gateway restart`
5. La persona te manda de nuevo, esta vez pasa.

## Verificación

```bash
ps aux | grep whatsapp-bridge | grep -v grep
# debería mostrar: ... --mode bot

tail -3 ~/.hermes/platforms/whatsapp/bridge.log
# debería mostrar:
# 🌉 WhatsApp bridge listening on port 3000 (mode: bot)
# 🔒 Allowed users: 233642076930156, 90761618051243, ...
# ✅ WhatsApp connected!
```
