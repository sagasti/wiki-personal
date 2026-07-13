---
title: "Hermes model stack — calidad first"
created: "2026-07-13"
updated: "2026-07-13"
type: "decision"
tags: ["#decision", "#hermes", "#models", "#brisa"]
related: [[hermes-configuration]], [[hermes-gemini-google-alias-native-client]], [[brisa]]
sources: ["hermes-session/20260710_213913_df08e117 (Telegram 2026-07-12/13)"]
confidence: high
---

# Hermes model stack — calidad first

**Fecha:** 2026-07-12/13  
**Estado:** Activo

## Contexto

Jorge pidió el mejor stack priorizando **calidad de resultados** (no costo). Había Gemini roto en path `google` + `thinking_config` 400, y vision auxiliar en Gemini.

## Decisión

| Rol | Provider | Modelo | Notas |
|-----|----------|--------|-------|
| **Main chat** | `xai-oauth` | `grok-4.5` | SuperGrok OAuth |
| **Fallback chain** | openrouter | `anthropic/claude-opus-4.8` → `openai/gpt-5.5` → `x-ai/grok-4.5` | `fallback_providers` (no legacy `fallback_model` Gemini) |
| **Vision aux** | `xai-oauth` | `grok-4.5` | Probado con PNG sintético |
| **smart_model_routing** | — | off | No degradar prompts “simples” a Haiku |
| **session_search** | `auto` | — | Evita Gemini forzado |
| **image_gen** | `xai` | `grok-imagine-image-quality` | Sin cambio de política |
| **TTS** | `gemini` | `gemini-2.5-flash-preview-tts` (Aoede vía proxy) | Path TTS distinto; se mantiene |
| **STT** | openai-compat | whisper OpenPass | Sin cambio |

## Por qué

- Calidad: main Grok 4.5 + fallbacks top (Opus → GPT-5.5 → Grok) vía OpenRouter.
- Resiliencia: no depender de Gemini en el path crítico del agent (bug de alias documentado en [[hermes-gemini-google-alias-native-client]]).
- Vision alineada al main (xAI); Grok 4.5 soporta visión nativa; aux es fallback.
- Smart routing off: Jorge prioriza calidad, no ahorrar en prompts cortos.

## Ops

- Cambios de config: `hermes config set` / shell — **no** editar `config.yaml` a ciegas con patch tool si hay riesgo de formato.
- Gateway: Brisa no reinicia; Jorge `/restart` o `hermes gateway restart` cuando haga falta.
- Patch local Gemini: reaplicar tras `hermes update` si hace falta.

## Tags

#decision #hermes #models
