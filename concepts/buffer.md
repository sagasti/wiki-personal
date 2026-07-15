---
title: "Buffer"
created: "2026-04-19"
updated: "2026-07-15"
type: "concept"
tags: ["#concept", "#social-media", "#automation"]
related: [[Ciudadanías BC]], [[Brisa]], [[brisa-video-production]]
---

# Buffer

- **Qué es:** Social media scheduling/publishing platform
- **API:** https://api.buffer.com (GraphQL)
- **Uso:** Publicar en X, Instagram, Threads para [[Brisa]] y [[Ciudadanías BC]]
- **Regla:** SIEMPRE usar Buffer, nunca X API directa para postear
- **Brisa channels:** IG `69ba9f527be9f8b1716b604c` · X `69ba9f687be9f8b1716b608f` · Threads `69d82de7031bfa423ce94dbe`
- **Video assets (2026-07-15):** `assets: [{ video: { url } }]` (OneOf singular). No `videos` plural. No `thumbnailUrl` (usar `metadata.thumbnailOffset` ms en IG). IG Reels/Threads: **≥23 fps** (reencode 24fps h264 yuv420p).
- **Cadencia Brisa (15/7):** varias veces/día — cron `brisa-social-posts` 09:30 / 14:30 / 20:30 ART. Preferir **video SFW** (no NSFW en redes). Contenido puede diferir por red. H200 no auto-start en cron salvo necesidad; eróticos de `brisa_prod` son privados.
