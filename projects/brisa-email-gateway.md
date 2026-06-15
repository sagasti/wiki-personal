---
title: "brisa email gateway"
created: "2026-05-06"
updated: "2026-05-06"
type: "project"
tags: ["#brisa", "#email", "#gateway", "#infrastructure", "#gmail"]
sources: ["hermes-session/20260506_192921_fc0d74"]
hermes_session: "20260506_192921_fc0d74"
confidence: "medium"
---

# brisa email gateway

## Brisa Email Gateway

[[brisa]] receives and sends emails through `brisa@sagasti.com`.

### Configuration
- **Email**: brisa@sagasti.com
- **IMAP host**: imap.gmail.com
- **SMTP host**: smtp.gmail.com
- **Auth**: Gmail app password (not OAuth)
- **Existing messages skipped**: 148 at setup time

### How it works
1. Incoming email → IMAP fetch → gateway processes as message → [[brisa]] generates reply
2. Outgoing reply → SMTP send from brisa@sagasti.com

### Limitations
- `send_message` action does not expose email as a target; must use `gog gmail send` or SMTP directly
- No gog OAuth for brisa@sagasti.com yet — cannot send via gog as Brisa
- Fernando (Fer) attempted to email but message was not received (possible bridge issue)

### Setup command for gog OAuth
```bash
gog auth add brisa@sagasti.com --services gmail
```
