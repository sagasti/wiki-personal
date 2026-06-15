---
title: "gog gmail cli"
created: "2026-05-06"
updated: "2026-05-06"
type: "entity"
tags: ["#email", "#gmail", "#cli", "#google", "#oauth", "#tool"]
sources: ["hermes-session/20260506_192921_fc0d74"]
hermes_session: "20260506_192921_fc0d74"
confidence: "medium"
---

# gog gmail cli

## gog — Gmail CLI

A terminal CLI for Gmail (and other Google services) using OAuth authentication. Distinct from `gws` (Google Workspace skill).

### Installed version
- v0.9.0 (built 2026-01-22)
- Path: `/opt/homebrew/bin/gog`

### Authenticated accounts
| Account | Profile | Services | Auth Date |
|---|---|---|---|
| jorge@sagasti.com | personal | gmail, calendar, drive, docs, contacts, chat, sheets, tasks, people | 2026-02-17 |
| jorge@openpass.com.ar | default | gmail, calendar, drive, docs, contacts, chat, sheets, tasks, people, classroom | 2026-04-19 |
| ia@openpass.com.ar | default | chat | 2026-04-14 |

### Sending email
```bash
gog gmail send --account jorge@sagasti.com --to recipient@example.com --subject "Subject" --body "Message"
```

### Adding new account
```bash
gog auth add user@example.com --services gmail
# Opens browser OAuth flow
```

### Gap
- `brisa@sagasti.com` has no gog OAuth yet — needs `gog auth add brisa@sagasti.com --services gmail`
