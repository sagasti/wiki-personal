---
title: "Hermes configuration (Brisa ops)"
created: "2026-07-12"
updated: "2026-07-14"
type: "concept"
tags: ["#hermes", "#brisa", "#ops", "#configuration"]
related: [[brisa]], [[brisa-tools]], [[brisa-email-gateway]], [[hermes-cli-send-command-gap]], [[hermes-whatsapp-bridge-failure-mode]], [[fernando-palermo]], [[hermes-quality-first-model-stack]], [[hermes-gemini-google-alias-native-client]], [[runpod]]
sources: ["MEMORY.md weekly maintenance 2026-07-12", "Telegram session 20260710_213913_df08e117 2026-07-12/13", "Desktop OpenArt MCP 20260713_174939_5f4b63", "Telegram Apple/Brave 20260713_122217_cf1951"]
confidence: high
---

# Hermes configuration (Brisa ops)

Cheat sheet de config operativa que antes vivía como punteros sueltos en MEMORY.md.

## Paths clave

| Qué | Path |
|-----|------|
| Config | `~/.hermes/config.yaml` |
| Secrets | `~/.hermes/.env` |
| Memories injectables | `~/.hermes/memories/{MEMORY,USER}.md` |
| Wiki personal | `~/.hermes/personal` → `/Users/jorge/wiki-personal` |
| WA bridge log | `~/.hermes/platforms/whatsapp/bridge.log` |
| Gateway logs | `~/.hermes/logs/` |
| Local patches | `~/.hermes/patches/` (p.ej. Gemini alias) |
| Pre-update backups | `~/.hermes/backups/` |
| MCP OAuth tokens | `~/.hermes/mcp-tokens/` |

## Model stack (calidad-first, 2026-07-12/13)

Decision: [[hermes-quality-first-model-stack]]. Resumen:

| Rol | Valor actual |
|-----|----------------|
| Main | `xai-oauth` / `grok-4.5` |
| Fallbacks | OR `claude-opus-4.8` → `gpt-5.5` → `x-ai/grok-4.5` |
| Vision aux | `xai-oauth` / `grok-4.5` |
| smart_model_routing | **off** |
| session_search | `auto` |
| image_gen | `xai` / `grok-imagine-image-quality` |
| TTS | Gemini (path TTS; distinto del chat) |
| `model.max_tokens` | **16384** (2026-07-13; evita 402 OR por max_tokens altos y tool_calls cortados) |

Editar config con `hermes config set` / shell — no patch ciego de `config.yaml`.

**Gotcha Desktop (2026-07-13):** si SuperGrok da **403 spending-limit** y el fallback OpenRouter hincha tool results, los `tool_call` se truncan (`finish_reason=length`). Fix: `/new` + créditos SuperGrok/OR + no reenviar el texto de error como mensaje.

**Gotcha Gemini:** alias `google` sin canónica → 400 `thinking_config`. Parche local: [[hermes-gemini-google-alias-native-client]] (`~/.hermes/patches/gemini-google-alias-native-client.patch`, reaplicar post-`hermes update`).

Versión post-update 2026-07-12: Hermes Agent v0.18.2 · upstream `aaf56912` (patch Gemini quedó dirty y validado).

## Web search (2026-07-13)

| Pieza | Estado |
|-------|--------|
| `web.search_backend` | **`brave-free`** |
| `BRAVE_SEARCH_API_KEY` | en `~/.hermes/.env` |
| `SEARXNG_URL` | **comentado** en `.env` (valor conservado) |
| Docker `searxng-brisa` (8889) / `searxng-fleet` (8888) | **stopped** (Jorge OK 2026-07-13) |
| `web.extract_backend` | Brave free **no** hace extract; usar firecrawl/tavily/exa/browser |

Brave free: 429 si spameás queries en paralelo — serializar / reintentar.

## MCP servers

| Name | Transport | Notas |
|------|-----------|--------|
| **openart** | HTTPS OAuth → `https://mcp.openart.ai/mcp` | **16 tools**; timeout 300s; login 1×: `hermes mcp login openart` + `/reload-mcp` |
| comfyui | npx comfyui-mcp | local/RunPod |
| gemini-imagen | uv script | Imagen barato; **Veo** = pedir OK (plata) |

### OpenArt MCP (listo 2026-07-13)

- OAuth cacheado en `~/.hermes/mcp-tokens/openart.*`
- Flujo: `openart_model_list` → `openart_model_form_get` → `openart_generate_{image,video}` → `openart_creation_wait` / `show`
- También: account/projects, cost estimate, uploads/references, creation list
- **NSFW: no** (help: restricted/flagged). Adulto → Comfy local/[[runpod]]
- No reemplaza Comfy: es marketplace multi-modelo (Kling, Seedance, GPT Image, etc.) con credits de la cuenta OpenArt

## TTS

- **Principal:** Gemini TTS (preview flash), voz **Aoede** (rioplatense) vía proxy local `http://127.0.0.1:9090/v1`
- **Fallback:** Edge ElenaNeural (es-AR); luego ElevenLabs
- **Regla UX:** strip emojis antes de sintetizar; voice msg → reply TTS (ver USER.md)
- Si hay timeout: reintentar 1×; si sigue, reportar (no inventar audio)

## Email Brisa

- Cuenta: `brisa@sagasti.com` — ver [[brisa-email-gateway]]
- IMAP/SMTP Gmail; gog OAuth de Brisa **aún pendiente** (`gog auth add brisa@sagasti.com --services gmail`)
- Outbound con gog: cuentas de Jorge (`jorge@sagasti.com`, etc.) — ver [[google-workspace]]

## Mensajería CLI

- **`hermes send` NO existe** → ver [[hermes-cli-send-command-gap]]
- Correcto: `hermes message send --channel <telegram|whatsapp> --target "..." --message "..."`
- Telegram Jorge: `1808182714`
- WA envíos con `jidDecode` → bypass HTTP al bridge — ver [[brisa-tools]] + [[hermes-whatsapp-bridge-failure-mode]]

## Fer Palermo (contacto WA)

- Entity: [[fernando-palermo]]
- LID / allowlist: ver [[whatsapp-authorized]]
- Primeros envíos a contactos nuevos: decision tree en [[brisa-tools]] (gateway vs `localhost:3000/send`)

## Reglas duras (ops)

- **No reiniciar el gateway** salvo que Jorge lo pida (`hermes update` puede reiniciarlo solo)
- No diagnosticar canales como “caídos” sin mirar logs primero
- Wiki: solo `wiki-personal` — ver [[brisa-personal-only-role]]

## Tags

#hermes #brisa #ops
