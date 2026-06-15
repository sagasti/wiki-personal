---
title: "Shodan"
created: "2026-05-15"
updated: "2026-05-15"
type: "concept"
tags: ["#cybersecurity", "#tool", "#ot-security", "#reconnaissance"]
sources: ["hermes-session/20260515_165959_e6f48a"]
hermes_session: "20260515_165959_e6f48a"
confidence: "medium"
---

# Shodan

Created by John Matherly, launched 2009. Like Google but indexes **devices** responding on the network — routers, IP cameras, industrial controllers, ATGs, PLCs, SCADA systems, anything with an open port.

**Usage**: Queries like `"default password" port:161` return thousands of accessible industrial devices. Filters by country, device type, software, port.

**Legitimate uses**: Security researchers, pentesters, CISA use it for exposure assessment.

**Abuse**: State hackers use it to find soft targets — e.g., [[atg-gas-station-hack]] ATGs found via basic Shodan search.

**Notable findings**: 2016 — two water treatment plants (Florida, Indiana) accessible without password; chlorine levels modifiable from browser.

**Access**: Free tier (limited), paid tier (full access). API key via shodan.io registration — 100 searches/month free.

**Alternatives**: FOFA (Chinese, similar), Censys (academic, cert/host focused).
