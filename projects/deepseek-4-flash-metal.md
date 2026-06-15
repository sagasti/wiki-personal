---
title: "DeepSeek 4 Flash Metal"
created: "2026-05-07"
updated: "2026-05-07"
type: "project"
tags: ["#ai", "#local-inference", "#metal", "#deepseek", "#apple-silicon"]
sources: ["hermes-session/20260507_160942_e64c2d"]
hermes_session: "20260507_160942_e64c2d"
confidence: "medium"
---

# DeepSeek 4 Flash Metal

## DeepSeek 4 Flash (ds4)

**antirez** (Salvatore Sanfilippo, creator of Redis) released **ds4**, a local inference engine for DeepSeek models running on **Apple Metal**.

- Repository: https://github.com/antirez/ds4
- Targets Apple Silicon GPU via Metal framework
- 130 points on HN — significant community interest
- Enables fast local inference of DeepSeek models without cloud dependency

### Context
Part of the growing ecosystem of local inference tools (alongside llama.cpp, MLX) specifically targeting DeepSeek architectures on Apple hardware.
