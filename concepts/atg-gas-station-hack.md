---
title: "ATG Gas Station Hack"
created: "2026-05-15"
updated: "2026-05-15"
type: "concept"
tags: ["#cybersecurity", "#ot-security", "#iran", "#critical-infrastructure", "#scada"]
sources: ["hermes-session/20260515_165959_e6f48a"]
hermes_session: "20260515_165959_e6f48a"
confidence: "medium"
---

# ATG Gas Station Hack

Part of [[iran-us-war-2026]] cyber operations.

**What was attacked**: Automatic Tank Gauge (ATG) systems — monitors fuel levels in gas station storage tanks. Multiple US states affected.

**How**: ATGs were directly exposed on the internet **without passwords**. No sophisticated exploit — just low-hanging fruit found via [[shodan]] or similar scanning.

**What hackers did**: Modified on-screen display readings. Did **not** alter actual fuel levels or cause physical damage.

**Real risk**: Attacker with ATG access could suppress leak alarms — a fuel leak could go undetected until catastrophic (explosion, environmental contamination).

**Attribution**: Iran's intelligence ministry; hacktivist persona "Handala" (Palestinian cartoon character) used for Telegram propaganda. Researcher Alex Orleans (Sublime Security) notes Iran's cyber capabilities are less sophisticated than China/Russia but sufficient when targets are unprotected.

**Broader problem**: Exemplifies OT (Operational Technology) security crisis — industrial systems connected to internet in 2000s without auth, never updated. Similar exposure in water treatment, SCADA, PLCs.
