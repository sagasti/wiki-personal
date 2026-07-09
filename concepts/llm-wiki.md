---
title: "LLM-Wiki"
created: "2026-04-19"
updated: "2026-04-21"
type: "concept"
tags: ["#concept", "#architecture", "#knowledge-management"]
related: [[hermes-ai-assistant]]
---

# LLM-Wiki

Patrón de Karpathy (abril 2026) para knowledge management con LLMs.

## Core idea
- Markdown files que el LLM lee, mantiene y enriquece
- **Compila** conocimiento una vez y lo mantiene (no RAG por query)
- Grafo de páginas interlinkadas con `[[]]` syntax

## Supermemory (deprecado)
Migrado a [[LLM-Wiki]] el 15/04. Ver decisión en `wiki/decisions/supermemory-to-llm-wiki.md`.

## Ventajas de LLM-Wiki
- Open source, sin vendor lock-in
- Markdown puro = portable, future-proof
- Costo: solo el LLM (sin servicio extra)
- Local: todo en filesystem
- Traceable: citas a fuente original

## Implementación en Hermes
- Directorio: `~/wiki-personal/`
- Brisa mantiene las páginas como parte de su operación normal
- Auto-capture → escribir en wiki en vez de llamar a API
- Auto-recall → leer wiki pages relevantes antes de responder
