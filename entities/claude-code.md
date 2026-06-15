---
title: "Claude Code (CLI agent)"
created: "2026-04-29"
updated: "2026-04-30"
type: "entity"
tags: ["#tool", "#cli-agent", "#coding", "#anthropic"]
related: [[opencode]], [[hermes-ai-assistant]], [[brisa]]
---

# Claude Code

CLI agent oficial de Anthropic para tareas de coding. Es donde Jorge corre la mayor parte de su trabajo de desarrollo asistido por IA, incluyendo el desarrollo y mantenimiento del wiki memory provider.

## Uso de Jorge

- **Principal CLI agent para coding**: refactors, implementación de features, code review, debugging.
- Corre en proyectos en `/Users/jorge/dev/*` (post-mudanza 2026-05-13) y `/Users/jorge/Documents/development/repo/*` (clones de terceros, librerías, archivos), más `/Users/jorge/.hermes`.
- Sesiones persistidas en `/Users/jorge/.claude/projects/`.

## Skills relacionados en Hermes

- `autonomous-ai-agents/claude-code/SKILL.md` — guía bundled para delegar tareas a Claude Code desde Hermes.

## Diferencias con [[opencode]] y [[hermes-ai-assistant]]

| Tool | Modelo | Modo de uso |
|---|---|---|
| [[claude-code]] | Anthropic Sonnet/Opus | Sessions interactivas largas para coding focused |
| [[opencode]] | Multi-provider | Sessions cortas, alternativa cuando Claude Code no está disponible |
| [[hermes-ai-assistant]] | GLM-5.1 (default) | Asistente personal 24/7 con gateways de mensajería |

## Estado

Página stub creada por audit (29-04-2026). Pendiente: documentar setup propio (instalación, config, hooks), workflow típico, integración con Hermes, sessions notables.

## Sessions notables
- **runpod-autostop.py rewrite (28/4):** Jorge usó `claude -p` para reescribir el script. Resultado: mejor idle tracking con state file, API calls mejorados, logging mejorado. Script en `~/.hermes/scripts/runpod-autostop.py`.
