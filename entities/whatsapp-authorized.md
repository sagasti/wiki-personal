---
title: "Contactos autorizados — WhatsApp Brisa"
created: "2026-04-21"
updated: "2026-07-12"
type: "entity"
tags: ["#whatsapp", "#brisa", "#authorization", "#contacts"]
related: [[brisa]], [[whatsapp-bot-mode-allowlist-by-lid]], [[whatsapp-pairing-over-allowlist]], [[whatsapp-bridge-lid-and-jiddecode-pitfalls]], [[whatsapp-lid-allowlist-mismatch]], [[hermes-whatsapp-bridge-failure-mode]]
confidence: high
---

# Contactos autorizados — WhatsApp Brisa

> **⚠️ El esquema cambió DOS VECES en 3 días:**
> - **2026-05-06:** allowlist vacío + Hermes pairing (decisión [[whatsapp-pairing-over-allowlist]])
> - **2026-05-08:** rota por commit upstream `6a4ecc0a9` que invalidó el esquema. Volvimos a allowlist explícito por LID + bridge en mode `bot`. Ver [[whatsapp-bot-mode-allowlist-by-lid]].

## Esquema actual (2026-05-08)

- **Bridge:** `--mode bot` con allowlist explícito por LID
- **`.env`:**
  ```bash
  WHATSAPP_MODE=bot
  WHATSAPP_ALLOWED_USERS=233642076930156@lid,90761618051243@lid,124021693755633@lid,229424284885240@lid,56294337695961@lid
  ```
- **`config.yaml`:** `unauthorized_dm_behavior: pairing` (queda configurado pero **rara vez se ejecuta** — el bridge filtra primero)
- **Flujo de un contacto nuevo:**
  1. La persona te manda un mensaje
  2. Bridge lo descarta con `allowlist_mismatch` y loggea el LID en `~/.hermes/platforms/whatsapp/bridge.log`
  3. Vos sacás el LID del log, lo agregás al `WHATSAPP_ALLOWED_USERS`, restart del gateway
  4. Próximo mensaje pasa

## Cuenta de Brisa (la del bridge)

- **Phone:** `+5491170639820`
- **LID:** `241837310791736@lid`
- **No se agrega al allowlist** — sus mensajes son `fromMe`, no se filtran. Aparece en `~/.hermes/platforms/whatsapp/session/lid-mapping-5491170639820.json` como artifact natural del setup del bridge.

## Contactos autorizados

> **Los LIDs son la identificación primaria.** El allowlist los espera en formato `XXXXX@lid`.

| Nombre | Phone | LID | Relación | Notas |
|--------|-------|-----|----------|-------|
| Jorge Sagasti | 5491123034606 | `233642076930156@lid` | Autoridad total | dueño |
| Bere Carbajo | 5491176399809 | `90761618051243@lid` | Pareja de Jorge | |
| Vivi Bardsdorf | 5491159809449 | `124021693755633@lid` | Amiga del alma | |
| Lorena Nápoli | 5491131730763 | `229424284885240@lid` | Ayuda con casa y perros | |
| [[fernando-palermo]] | +598 99 699 673 | `56294337695961@lid` | Cofundador [[mundomac-website]] | LID ya no en sesión local pero sí en allowlist |

## LID mappings (cache local)

Archivo simple por contacto en `~/.hermes/platforms/whatsapp/session/`:

- `lid-mapping-{phone}.json` — contiene un único string con el LID
- `lid-mapping-{lid}_reverse.json` — contiene el phone

Solo existen para contactos con **interacción previa via bridge**. Si el LID no está en el allowlist, el bridge no procesa el mensaje pero **igual loggea el LID** en el bridge.log → ese es el camino para descubrir LIDs nuevos.

## 3 maneras de conseguir un LID

### 1. Si la persona ya te mandó algo alguna vez

```bash
cat ~/.hermes/platforms/whatsapp/session/lid-mapping-{PHONE_SIN_PLUS}.json
# → "LIDXXXXX"
```

O listar todos los conocidos:

```bash
cd ~/.hermes/platforms/whatsapp/session && for f in lid-mapping-*.json; do
  case "$f" in
    *_reverse.json) ;;
    *)
      phone=$(basename "$f" .json | sed 's/lid-mapping-//')
      lid=$(cat "$f" | tr -d '"')
      printf "%-15s → %s@lid\n" "$phone" "$lid"
      ;;
  esac
done
```

### 2. Si la persona te mandó AHORA y no estaba en el allowlist

El bridge la rechaza pero loggea el LID:

```bash
tail -100 ~/.hermes/platforms/whatsapp/bridge.log | grep allowlist_mismatch | tail -5
# → {"event":"ignored","reason":"allowlist_mismatch","chatId":"XXX@lid","senderId":"XXX@lid"}
```

### 3. Si la persona NUNCA te mandó nada

No hay manera directa. Necesitan mandarte algo primero (aunque sea un mensaje rechazado), después usás método 2.

## Cómo agregar un contacto nuevo

```bash
# 1. La persona te manda mensaje → queda registrado en bridge.log
# 2. Agregar el LID al .env
sed -i.bak "s|^WHATSAPP_ALLOWED_USERS=.*|WHATSAPP_ALLOWED_USERS=&,NUEVO_LID@lid|" ~/.hermes/.env
# 3. Restart
hermes gateway restart
# 4. Pedirle a la persona que te mande de nuevo
```

## Histórico

### Esquema 2026-05-06 → 2026-05-08 (pairing-over-allowlist)

```
WHATSAPP_ALLOWED_USERS=
unauthorized_dm_behavior: pairing
```
Decisión: [[whatsapp-pairing-over-allowlist]]. **Invalidado** por commit upstream `6a4ecc0a9` el 2026-05-07 — empty allowlist ahora rechaza todo, no pasa todo.

### Esquema pre-2026-05-06 (allowlist phone-based)

```
WHATSAPP_ALLOWED_USERS=5491123034606,5491176399809,5491159809449,5491131730763
unauthorized_dm_behavior: ignore
```
Reemplazado porque el matching phone↔LID fallaba para contactos nuevos (que llegan como LID opaco). Detalle en [[whatsapp-lid-allowlist-mismatch]].
