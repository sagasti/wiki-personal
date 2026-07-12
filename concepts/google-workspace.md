---
title: "Google Workspace (gog / gws)"
created: "2026-07-12"
updated: "2026-07-12"
type: "concept"
tags: ["#google", "#gog", "#gmail", "#calendar", "#cli"]
related: [[gog-gmail-cli]], [[gog-calendar-event-retrieval]], [[brisa-email-gateway]], [[hermes-configuration]]
sources: ["MEMORY.md weekly maintenance 2026-07-12"]
confidence: high
---

# Google Workspace (gog / gws)

Índice de acceso a Google vía CLI. Skill Hermes: `google-workspace` (gws) o binario **gog**.

## gog — cuentas autenticadas

Ver detalle en [[gog-gmail-cli]]:

| Account | Uso |
|---------|-----|
| jorge@sagasti.com | personal (gmail, calendar, drive, …) |
| jorge@openpass.com.ar | trabajo |
| ia@openpass.com.ar | chat (laboral — fuera de alcance Brisa salvo pedido) |
| brisa@sagasti.com | **sin gog OAuth aún** |

## Gmail search (gog)

```bash
gog gmail search --account jorge@sagasti.com 'newer_than:7d is:unread'
gog gmail send --account jorge@sagasti.com --to X --subject "S" --body "B"
```

Sintaxis de query = la de Gmail (`from:`, `subject:`, `after:YYYY/MM/DD`, `has:attachment`, etc.).

## Calendar

```bash
gog calendar list --account jorge@sagasti.com --days 7
# detalle de un evento (NO existe "event get"):
gog calendar event --account jorge@sagasti.com primary <event_id>
```

Pitfall documentado en [[gog-calendar-event-retrieval]].

## Relacionado

- Email gateway de Brisa: [[brisa-email-gateway]]
- Config ops: [[hermes-configuration]]

## Tags

#google #gog #cli
