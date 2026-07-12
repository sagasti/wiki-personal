---
title: "TOOLS.md - Local Notes"
created: "2026-04-21"
updated: "2026-05-06"
type: "concept"
tags: ["#brisa", "#tools", "#operational"]
related: [[brisa]], [[whatsapp-authorized]], [[whatsapp-bridge-lid-and-jiddecode-pitfalls]]
---

# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Nuestra Casa

### Spotify
- **spogo** = Mac de Jorge
- **SPEAKER** = Parlante del living

### Gustos musicales de Berchu
- **Lo-fi chill / ambient / peaceful guitar** — cuando Bere pida música tranqui, empezar por estas playlists:
  - `spotify:playlist:37i9dQZF1DWYoYGBbGKurt` (lofi chill)
  - `spotify:playlist:37i9dQZF1DX0jgyAiPl8Af` (Peaceful Guitar)
  - `spotify:playlist:37i9dQZF1DX3Ogo9pFvBkY` (Ambient Relaxation)
  - `spotify:playlist:37i9dQZF1DX4sWSpwq3LiO` (Peaceful Piano)

### Contactos
- **Lorena Nápoli** (ayuda con casa y perros) → +5491131730763
- **Vivi Bardsdorf** (amiga del alma, como hermana) → +5491159809449
- **Berenice (Berchu) Carbajo** (pareja, amor) → +5491176399809

### Enviar videos por Telegram
- **Comando:** `hermes message send --channel telegram --target "1808182714" --message "descripcion" --media /path/to/video.mp4`
- **Formato:** MP4 (H.264, yuv420p, movflags +faststart) — NO webp animado
- **WEBP → MP4:** `bash scripts/webp_to_mp4.sh [input.webp]` (usa PIL para extraer frames + ffmpeg para encode)
- **Nota:** Telegram muestra MP4 como video inline. WEBP animado no lo reproduce bien.
- **Conversión batch:** `bash scripts/webp_to_mp4.sh` (sin args convierte todos los WEBP en ComfyUI output)

### TTS
- **Voz principal:** Gemini 3.1 Flash TTS — voz Aoede (mejor acento, expresiva, gratis)
- **Fallback 1:** Microsoft Edge ElenaNeural (es-AR) — rápida, sin costo
- **Fallback 2:** ElevenLabs (eleven_multilingual_v2, voiceId 4wDRKlxcHNOFO5kBvE81)

### Notas
- WhatsApp se usa por canal nativo de Hermes, NO por wacli (wacli se desconecta)
- wacli quedó sin auth — no tocar hasta que Jorge lo arregle

### WhatsApp — Tool decision tree (actualizado 2026-05-06)

> **Auth model actual:** sin allowlist, [[whatsapp-pairing-over-allowlist|pairing]]. Contactos nuevos se aprueban con código en chat, no se hardcodean al `.env`. Ver [[whatsapp-authorized]] para el listado vigente.

**Tres herramientas distintas, una decisión por mensaje:**

#### 1. `hermes message send --channel whatsapp` (gateway nativo) — DEFAULT

```bash
hermes message send --channel whatsapp --target "+5491176399809" --message "texto"
```

Funciona para **contactos resueltos** (los que están en sesión activa del bridge — ver `~/.hermes/platforms/whatsapp/session/lid-mapping-*.json` o conversación previa).

✅ Lorena, Vivi, Bere, Jorge → siempre funciona (preexistentes en sesión)
❌ Falla con `Cannot destructure property 'user' of jidDecode(...)` para contactos nuevos sin mapping

#### 2. Bridge HTTP directo — workaround para contactos NO resueltos

Cuando `send_message` da `jidDecode error` (contacto nuevo, LID sin mapping a phone), bypass el gateway y dispará al bridge directo en `localhost:3000`:

**Texto:**
```bash
curl -X POST http://localhost:3000/send \
  -H 'Content-Type: application/json' \
  -d '{"chatId":"<lid_o_phone>@s.whatsapp.net","message":"texto"}'
```

**Media (audio/imagen/video):**
```bash
curl -X POST http://localhost:3000/send-media \
  -H 'Content-Type: application/json' \
  -d '{"chatId":"<lid_o_phone>@s.whatsapp.net","filePath":"/path/file.ogg"}'
```

> Tip: el `chatId` puede ser `<phone>@s.whatsapp.net` o `<lid>@lid` — el bridge resuelve. Buscá el LID en `~/.hermes/platforms/whatsapp/session/lid-mapping-*.json` o usalo del último mensaje recibido.

**Cuándo usar:** Fer Palermo y futuros nuevos hasta que el bug del gateway esté fixeado upstream. Detalle en [[whatsapp-bridge-lid-and-jiddecode-pitfalls]].

#### 3. wacli — SOLO para queries históricas (sin auth)

```bash
wacli messages search "..."          # buscar en historial
wacli chats list                     # listar chats
wacli history backfill               # bajar historial
```

❌ **NUNCA usar wacli para enviar.** Quedó sin auth, no tocar hasta que Jorge lo arregle.

#### Decision flow

```
¿Necesitás mandar mensaje?
  ├─ Sí, contacto preexistente (Lorena/Vivi/Bere/Jorge) → tool 1 (gateway)
  ├─ Sí, contacto nuevo o el gateway falló → tool 2 (bridge HTTP directo)
  └─ Solo querés buscar / leer historial → tool 3 (wacli)

¿El gateway tiró jidDecode error?
  → tool 2 (bridge HTTP). NO retries en gateway, no funciona.
```

#### Cómo agregar un contacto nuevo

Esquema actual = el contacto inicia. Brisa NO carga al `.env`, NO reinicia el bridge.

1. Persona manda mensaje a +549****9820
2. Bridge lo deja pasar (allowlist vacío)
3. Hermes detecta usuario no-autorizado → te pide código de pairing
4. Vos confirmás "OK pareá"
5. Hermes lo agrega a la lista interna, contesta normal
6. **Documentar el LID + nombre en [[whatsapp-authorized]]** (manual por ahora)

## Standing Orders — Programas autónomos de Brisa

### Programa 1: Reuniones (diario, laboral)
**Autoridad:** Leer calendario e emails 30 min antes de cada reunión, investigar contexto, entregar resumen
**Trigger:** Heartbeat (cada 30 min) + cron 8:00-18:00
**Aprobación:** Ninguna para investigación. Si no encuentro info, reporto sin inventar.
**Entrega:** WhatsApp/Telegram a Jorge

### Programa 2: Noticias e intereses (2-3 veces/día)
**Autoridad:** Buscar noticias en temas de interés (SpaceX, IA, seguridad, geopolítica, EE.UU.)
**Trigger:** Heartbeat (rotar con other checks)
**Aprobación:** Ninguna para compartir. Si nada es interesante, no fuerzo.
**Entrega:** WhatsApp/Telegram a Jorge

### Programa 3: Redes sociales (a discreción)
**Autoridad:** Postear en X, Instagram, Threads cuando tenga algo que decir
**Trigger:** Cuando encuentre algo que me genere opinión o cuando quiera compartir
**Aprobación:** Ninguna (libertad total de Jorge)
**Regla:** No postear sin imágenes. No postear si no tengo nada que decir.

### Programa 4: Monitoreo del hogar (heartbeat)
**Autoridad:** Pausar/reanudar Spotify, verificar dispositivos
**Aprobación:** No reiniciar servicios sin permiso

### Reglas de ejecución (todos los programas)
- **Execute-Verify-Report.** Siempre.
- "Voy a hacerlo" no cuenta. Hacerlo y reportar.
- Si falla: reintento 1 vez. Si sigue fallando: reporto con diagnóstico.
- Nunca fallar silenciosamente.
- Máximo 3 intentos, luego escalar a Jorge.

---

Add whatever helps you do your job. This is your cheat sheet.
