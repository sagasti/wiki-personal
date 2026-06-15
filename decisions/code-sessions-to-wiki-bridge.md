---
title: "Bridge Claude Code sessions → Wiki via Brisa consolidation"
created: "2026-05-07"
updated: "2026-05-07"
type: "decision"
status: "proposal"
tags: ["#decision", "#proposal", "#wiki", "#hermes", "#brisa", "#claude-code"]
related: [[hermes-ai-assistant]], [[brisa]], [[llm-wiki]], [[claude-code]], [[claudio]]
confidence: medium
---

# Bridge Claude Code sessions → Wiki via Brisa consolidation

> **Status: PROPOSAL** — escrito el 2026-05-07 a la noche mientras Jorge dormía. Requiere decisión suya antes de tocar código.

## El gap detectado

[[brisa]] hace **nightly consolidation** que escribe al wiki (`~/wiki/log.md` lleva el track). Esa consolidación lee de:

- `~/hermes/data/sessions/*.jsonl` (sesiones de Telegram, WhatsApp, cron)
- Logs de Hermes
- Transcripts de cron jobs

**Lo que NO lee:** las sesiones de Claude Code Desktop en `~/.claude/projects/<project-hash>/<uuid>.jsonl`.

Implicancia: si yo (Claudio) trabajo con Jorge en una sesión de Code y aprendemos algo nuevo (gotcha técnico, decisión, endpoint, persona), **eso solo llega al wiki si yo lo escribo manualmente durante la sesión**. El cron nightly de Brisa nunca lo va a ver.

Hoy esto está mitigado por:
1. Mi `CLAUDE.md` global con triggers OBLIGATORIOS para escribir
2. Pre-cierre checklist antes del último mensaje del turn
3. Skill `wiki-access`

Pero es **frágil**. Si me olvido, se pierde para siempre.

## Por qué importa

Las sesiones de Code son **densas en señal**:

- Decisiones técnicas con trade-offs reales (no chitchat)
- Gotchas de debug que costaron 30+ min
- Endpoints, hostnames, credenciales no obvias
- Workflows que funcionaron y queremos replicar

El catálogo en [[jorge-active-projects]] tiene 18 sesiones pinned, varias de ellas con 100-294 turns acumulados. Mucha de esa información hoy vive **solo en JSONLs** que nadie indexa.

## 3 opciones para cerrar el gap

### Opción A — Modificar Brisa para que lea Code sessions

**Cómo:** extender el `nightly_consolidation` de Hermes con un nuevo source.

```python
# hermes/skills/nightly_consolidation/sources.py (pseudo)
sources = [
    HermesSessions(...),
    Cronjobs(...),
    ClaudeCodeSessions(  # ← nuevo
        roots=["~/.claude/projects"],
        since="last_run",
        filter_min_turns=5,  # ignorar sesiones triviales
    ),
]
```

**Pros:**
- Sistemático, sin depender de mi disciplina
- Aprovecha el LLM de Brisa (criterio editorial ya entrenado)
- No requiere setup nuevo en cada repo

**Contras:**
- Implica tocar Hermes (parsing JSONL nuevo, schema diferente)
- Costo de tokens: las sesiones de Code son largas (a veces 100K+ tokens)
- Riesgo de leakear secrets que aparecieron en outputs (logs, env vars)

**Estimación:** 1 sesión de trabajo (~3hs) para parser + filtro + integración.

### Opción B — Script periódico standalone

**Cómo:** crear `~/.hermes/scripts/code-sessions-extract.py` que:
1. Escanea `~/.claude/projects/*/`
2. Por cada sesión nueva desde último run, extrae los user messages + assistant tool calls a Edit/Write en `~/wiki/`
3. Genera un `raw/code-session-<uuid>.md` con timestamp + project + summary
4. Brisa lo levanta en el próximo cron porque ya está en `~/wiki/raw/`

**Pros:**
- No toca Hermes, solo agrega un script
- Brisa lo procesa via su flujo normal (lee `raw/`, decide promover a entities/concepts/projects/decisions)
- Reversible — si no funciona, borrar el script

**Contras:**
- Otro cron más para mantener
- El parsing del JSONL es no-trivial (estructura no documentada, cambia entre versiones)
- Duplica esfuerzo si Hermes después soporta esto nativo

**Estimación:** 1-2 sesiones (~5hs) para parser robusto + cron + testing.

### Opción C — Brisa scan semanal con prompt dirigido

**Cómo:** weekly cron de Brisa que recibe la lista de sesiones de Code de la última semana y un prompt tipo:

> "Acá tenés N sesiones de Code de Jorge esta semana. Leé los user messages (no los outputs largos). Para cada sesión, decidí si hubo: (1) decisión técnica con trade-off, (2) gotcha que costó debug, (3) cambio de estado de proyecto, (4) persona nueva mencionada. Si sí, escribí al wiki siguiendo SCHEMA.md. Si no, ignorá."

**Pros:**
- Mínima fricción de implementación (solo prompt + lista de paths)
- Brisa ya sabe cómo escribir wiki — solo cambia la fuente
- Frecuencia semanal evita ruido de sesiones triviales
- Es una capa **encima** de mi disciplina actual, no la reemplaza

**Contras:**
- No es real-time — gap de hasta 7 días
- Brisa tiene que filtrar mucha basura para encontrar la señal
- Costo de tokens (semanal, no nightly, así que menor que A pero igual significativo)

**Estimación:** 1 sesión (~2hs) para prompt + cron entry + primera prueba.

## Recomendación

Si fuera mi decisión, **arrancaría por C** (weekly scan). Razones:

- Mínima inversión para validar la hipótesis
- Si funciona bien, podés graduar a A después con confianza
- Si no funciona (Brisa filtra mal, ruido > señal), tirás 2hs no 5
- Mantiene mi disciplina actual como primera línea — el cron es backup

**Si C funciona durante 2-3 semanas**, evaluar promover a A o B según:
- A si el filtrado por LLM cosechó >50% de los items que yo me hubiera olvidado
- B si quedó claro que necesitás real-time (ej: gotchas críticos perdidos)

## Lo que NO recomiendo

- ❌ Hacer las 3 a la vez (over-engineering)
- ❌ Tocar Hermes core sin validar primero (A primero rompe lo que ya funciona)
- ❌ Auto-write directo desde el JSONL parser sin filtrado LLM (bajaría señal/ruido)

## Riesgos comunes a las 3 opciones

1. **Secrets leak.** Las sesiones de Code a veces contienen API keys, tokens, passwords pegados por error. **Cualquier opción necesita pasar por el patrón de detección de secrets del wiki (los 11 patterns existentes).**
2. **Privacy con Bere/Vivi/Lore/Fer.** Si una sesión de Code tiene contexto sobre alguien, esa info ya tiene que cumplir las reglas de PII del wiki (no compartir teléfonos sin contexto, etc).
3. **Costo de tokens.** Una sesión típica de Code productiva = 50-200K tokens de input. Brisa procesando 5-10 por semana = 1-2M tokens. Costo estimado ~$5-15/mes con `glm-5.1` o equivalente.

## Próximo paso

Jorge: ¿cuál te parece? ¿Arrancamos por C o querés discutirlo más antes?

Cuando decidas, esta página pasa de `status: proposal` a `status: in-progress` o `status: rejected` según el resultado.
