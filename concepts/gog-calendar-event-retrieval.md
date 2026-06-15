---
title: "Gog Calendar Event Retrieval"
created: "2026-05-07"
updated: "2026-05-07"
type: "concept"
tags: ["#gog", "#google-calendar", "#cli", "#tool-usage"]
sources: ["hermes-session/20260507_093507_d03a3e"]
hermes_session: "20260507_093507_d03a3e"
confidence: "medium"
---

# Gog Calendar Event Retrieval

## Retrieving Individual Calendar Events

The `gog` CLI can fetch a single event's details in TSV format:

```bash
gog calendar event --account user@domain.com primary <event_id>
```

Returns fields: `id`, `summary`, `timezone`, `start`, `start-day-of-week`, `start-local`, `end`, `end-day-of-week`, `end-local`, `attendee` (one per line with status), `meet`, `video-link`, `reminders`, `link`.

### Pitfall
- Do **not** use `gog calendar event get` — the `get` subcommand does not exist and returns an error.
- Use `gog calendar list --account X --days N` for listing, then `gog calendar event --account X primary <id>` for details.
