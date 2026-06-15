---
title: "MCP (Model Context Protocol)"
created: "2026-04-29"
updated: "2026-04-29"
type: "concept"
tags: ["#concept", "#protocol", "#llm", "#integration", "#anthropic"]
related: [[hermes-ai-assistant]], [[mcp-atlassian]], [[opencode-mcp-migration]]
---

# MCP — Model Context Protocol

Protocolo abierto creado por Anthropic para conectar LLM agents con tools/data sources externos. Cliente-servidor sobre stdio o HTTP, formato JSON-RPC. Es el mecanismo principal por el cual [[hermes-ai-assistant]] (y otros agents como [[claude-code]], [[opencode]]) se conectan a integraciones.

## Cómo funciona

- **Server MCP** expone *tools* (funciones), *resources* (data) y *prompts* (templates) sobre un transport (stdio o streamable-http)
- **Cliente MCP** (el agent) negocia versión, lista tools/resources, y llama via JSON-RPC
- Tools expuestos por MCP aparecen como funciones que el LLM puede invocar igual que cualquier otra tool nativa

## Servers MCP en uso

| Server | Skill/Doc | Uso |
|---|---|---|
| `mcp-atlassian` | [[mcp-atlassian]] | Jira + Confluence de OpenPass |
| `comfyui` | (bundled en ComfyUI) | Operar [[comfyui]] desde el agent |
| `gitlab` | — | GitLab interno de OpenPass |
| `bhub-vast` | — | Vast.ai vía gateway de OpenPass |
| `gemini-imagen` | — | Generación de imágenes con Gemini |

## Decisiones relacionadas

- [[opencode-mcp-migration]] — migración de servers de OpenCode al directorio de Hermes

## Spec

- https://modelcontextprotocol.io
- Versión actual negociada en sesiones de Hermes: 2025-11-25

## Estado

Página stub creada por audit (29-04-2026). Pendiente: documentar protocolo de sesión, transports, autenticación con tokens, troubleshooting común (los logs muestran errores recurrentes con `bhub-vast`).
