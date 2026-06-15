---
title: "Browser Harness CDP Agent"
created: "2026-05-06"
updated: "2026-05-06"
type: "concept"
tags: ["#tool", "#browser", "#cdp", "#automation", "#chrome"]
sources: ["hermes-session/20260506_224855_0142a5"]
hermes_session: "20260506_224855_0142a5"
confidence: "medium"
---

# Browser Harness CDP Agent

## Browser Harness

- **Repo:** installed at `~/Developer/browser-harness`
- **Install:** `uv tool install -e .` (editable, global CLI)
- **CLI:** `browser-harness`
- **Protocol:** Connects to Chrome via Chrome DevTools Protocol (CDP)
- **Architecture:** ~1k lines, self-healing agent harness
- **Notoriety:** 11k GitHub stars in 3 weeks
- **Pending:** Needs Chrome remote debugging enabled (`chrome://inspect/#devices`) to connect

### Usage
```bash
browser-harness  # launches the agent, connects to Chrome via CDP
```
