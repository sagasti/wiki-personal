---
title: "Hermes: alias google → GeminiNativeClient (thinking_config 400)"
created: "2026-07-13"
updated: "2026-07-13"
type: "concept"
tags: ["#hermes", "#gemini", "#ops", "#gotcha", "#lessons"]
related: [[hermes-configuration]], [[technical-lessons]], [[brisa]]
sources: ["hermes-session/20260710_213913_df08e117 (Telegram 2026-07-12/13)"]
confidence: high
---

# Hermes: alias `google` → GeminiNativeClient

## Síntoma

HTTP 400 de Google AI Studio:

```text
Invalid JSON payload received. Unknown name "thinking_config": Cannot find field.
```

Aparecía en vision/fallback/session_search cuando el provider se resolvía como `google` (no `gemini`).

## Causa

Con `provider: google` (alias de AI Studio), Hermes armaba un cliente **OpenAI SDK** contra:

`https://generativelanguage.googleapis.com/v1beta/chat/completions`

y mandaba `extra_body.thinking_config` (p.ej. `includeThoughts: true`). Ese endpoint OpenAI-compat **no acepta** ese campo top-level → 400.

El path correcto es **`GeminiNativeClient`** (`generateContent`), que traduce a `generationConfig.thinkingConfig`.

El runtime solo forzó cliente nativo si `agent.provider == "gemini"`. El alias `google` (y similares) caía al path OpenAI.

## Fix local (2026-07-12/13)

Parche en install git de Hermes (`~/.hermes/hermes-agent`), **5 archivos**:

1. `agent/agent_init.py` — canónica `google` / `google-gemini` / `google-ai-studio` → `gemini`
2. `agent/agent_runtime_helpers.py` — `GeminiNativeClient` también con esos aliases / base URL nativa
3. `agent/chat_completion_helpers.py` — canónica en fallback chain
4. `agent/transports/chat_completions.py` — aliases en thinking_config routing
5. `agent/auxiliary_client.py` — `resolve_provider_client` mismo set de aliases

**Backup del patch (reaplicar post-update):**

`~/.hermes/patches/gemini-google-alias-native-client.patch`

Smoke test post-fix: `provider=google` → `GeminiNativeClient`, chat OK con `thinking_config`, sin 400.

## Update sin romper el parche

- `hermes update -y --backup` hace stash de cambios locales, pull/reset, restore del stash.
- Tras update (2026-07-12 noche): patch **siguió dirty** en los 5 archivos; smoke Gemini OK.
- Backup pre-update de esa corrida: `~/.hermes/backups/pre-update-2026-07-12-225410.zip`
- Si el restore del stash falla: `git apply ~/.hermes/patches/gemini-google-alias-native-client.patch` desde el repo.
- Upstream **aún no** trae este fix (verificar en cada update).

## Mitigaciones de config (además del patch)

- **Vision** ya no usa Gemini: `auxiliary.vision` = `xai-oauth` / `grok-4.5` (probado 2026-07-12).
- **session_search** → `auto` (deja de forzar `google`/`gemini-2.5-flash`).
- **TTS Gemini** es otro path (no chat completions del agent); no es el mismo bug.
- Fallback principal del chat: cadena OpenRouter (no Gemini) — ver [[hermes-configuration]] y decision de stack calidad-first.

## Tags

#hermes #gemini #gotcha #ops
