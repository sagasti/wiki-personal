---
title: "SCHEMA — convenciones wiki-personal"
created: "2026-07-12"
updated: "2026-07-12"
type: "schema"
tags: ["#meta", "#schema"]
---

# SCHEMA — convenciones wiki-personal

Fuente de verdad de forma para `~/.hermes/personal` (= `/Users/jorge/wiki-personal`).

## Alcance (hard rule)

- **Solo** este vault personal.
- **Nunca** `~/wiki` (laboral). Ver [[brisa-personal-only-role]].

## Carpetas

| Dir | Uso |
|-----|-----|
| `entities/` | Personas, orgs, agentes (Brisa, Jorge, Bere, …) |
| `projects/` | Emprendimientos / experimentos personales activos o históricos |
| `concepts/` | Tecnologías, lecciones, ops, ideas |
| `decisions/` | Decisiones con trade-off |
| `comparisons/` | A vs B |
| `queries/` | Preguntas/respuestas de investigación |
| `index.md` | Catálogo de slugs |
| `log.md` | Append-only de cambios estructurales / mantenimiento |
| `SCHEMA.md` | Este archivo |

## Naming

- **Slugs:** kebab-case ASCII, max ~60 chars (`hermes-whatsapp-bridge-failure-mode.md`)
- **Wikilinks:** `[[slug]]` sin path ni extensión
- **Search before create** — no duplicar páginas semánticas

## Frontmatter (YAML)

```yaml
---
title: "Human title"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: "entity|project|concept|decision|comparison|query|index|schema"
tags: ["#tag1", "#tag2"]
related: [[other-slug]]
sources: ["hermes-session/..."]   # opcional
confidence: high|medium|low       # opcional
valid_until: "YYYY-MM-DD"         # solo facts de setup puntual (pods, IPs, keys rotables)
---
```

## Tags frecuentes

- Personas: `#person` `#amigo` `#familia` `#ai-agent`
- Tech: `#hermes` `#ops` `#comfyui` `#runpod` `#whatsapp` `#cli`
- Meta: `#index` `#schema` `#lessons` `#gotcha`
- Estado: `#wip` `#deprecated`

## MEMORY.md / USER.md (built-in Hermes)

- Límites: `memory_char_limit: 2200`, `user_char_limit: 1800` (`config.yaml`)
- MEMORY = **solo punteros** (`Tema: ver [[slug]]`). Detalle → este vault
- USER = preferencias estables de Jorge (voseo, trash>rm, TTS, etc.)
- Rotar setup puntual con `valid_until` al wiki; no dejar IPs/pod IDs en built-in

## Jobs

- Consolidación diaria ~02:00 — captura, no reestructura
- Mantenimiento semanal (este pass) — links, rotación, index/log, SCHEMA
- Autocommit git del vault (cron mac)

## Secrets

No escribir API keys, tokens, PEM, app passwords. 11 patterns de filtro en el diseño del wiki plugin (ver [[brisa]]).
