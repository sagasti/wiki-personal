---
title: "log"
created: "2026-07-12"
updated: "2026-07-19"
type: "log"
tags: ["#log", "#meta"]
---

# log

Append-only. Entradas nuevas **arriba**.

## 2026-07-19 — Daily consolidation (~02:00)

- **Fuentes humanas (~48h):** TG `20260717_083833_75d70557` (cierre/pull FaceID, stop reminder, re-roll Threads, clima, saludo pre-rename) + TG `20260718_193033_36e6a45a` + CLI `20260718_155714_370a1e` (presentación **Nina**). Email Claudio/hermes-admin (handover+rename+mail) ya actuado en sesión; no es source humano del filtro pero alineó SOUL/MEMORY.
- **Updated:** [[brisa]] (identidad Nina vs marca Brisa agencia; rol post-18/7; timeline), [[brisa-personal-only-role]] (rename + no redes/FV), [[claudio]] (hermes-admin), [[brisa-social-posts-log]] (C elegido, Buffer no publicado, cierre).
- **MEMORY/USER:** ya tenían Nina + handover (sesión 18/7). MEMORY ~2166/2200 — sin punteros nuevos. USER OK. Pod check fin de pass: `comfyui-luz-h200` **EXITED**.
- **Sin preferencias USER nuevas** de las charlas (clima/saludos).

## 2026-07-18 — Daily consolidation (~02:00)

- **Fuentes humanas (48h):** TG `20260716_084703_952c46` (madrugada 17/7 FaceID QC + relaunch A–H) + TG `20260717_083833_75d70557` (pull Extra + resume batch + stop cron reminder). WA `20260715` handoff “Termino runpod?”. WA ciudadanías “No me gusta” = iteración de diseño (sin preferencia estable). CLI 16/7 sin facts nuevos. Email Claudio (v2) ya absorbido en playbook/skills la noche del 17.
- **Updated:** [[brisa-monetize-fanvue-onlyfans]] (ops batch 0545 + supersede FaceID-desbloqueo por pipeline v2), [[brisa-video-production]] (v2 note + save-final + resume stamp), [[technical-lessons]] (CLIPVision FaceID, pin STAMP, save solo final).
- **MEMORY:** puntero RunPod hands-off de la noche 17/7 → normal unattended (MEMORY ~95%; sin punteros nuevos). USER: sin preferencias nuevas.
- **Nota:** pipeline v2 + pausa visual siguen vigentes; material FaceID vault = histórico / no relanzamiento.

## 2026-07-17 — Daily consolidation (~02:00)

- **Fuente:** TG `20260716_084703_952c46` (Fanvue launch + collections overnight). CLI Fanvue get-me sin facts. Emails Claudio ya absorbidos en playbook/log FaceID.
- **Updated:** [[brisa-monetize-fanvue-onlyfans]] (soft free posts, audience rules, collections A–H UUIDs, batch ah_hard 80 clips), [[brisa-video-production]] (collections path + LatentSync notes), [[brisa-email-gateway]] (canal Hermes, sin cron mail).
- **MEMORY:** puntero Fanvue comprimido → detalle colls en playbook (límites ~llenos; rotar semanal).
- **USER:** sin preferencias nuevas estables (soft free/hard subs ya en Fanvue USER/MEMORY).
- **Pendiente Jorge:** bios redes + X sensitive; avatar/banner web; review batch A–H.

## 2026-07-17 — FaceID ban Fanvue + regen nofaceid (email Claudio)
- FaceID/InstantID/PuLID **prohibidos** en material Fanvue (InsightFace research-only).
- Voz intro: Gemini TTS Aoede — no publicable; intro sin voz.
- Path canónico: `/Volumes/Extra/photos/brisa_prod` (sin Desktop symlink).
- Script: `brisa-generate/scripts/brisa_fanvue_nofaceid_regen.py` (JGG+brisa_stills→Pony, mismos seeds).
- Wiki: [[brisa-video-production]], [[brisa-monetize-fanvue-onlyfans]], skill refs actualizados.

## 2026-07-16 — Daily consolidation (~02:00)

- **Fuentes:** WA `20260715_063318_b9076db2` (Videos Brisa RunPod / redes). TG Apple `20260713_165241_21c6604d` post-02:00 solo cleanup spam NSFW assets + confirm posts (sin bio nueva).
- **Updated:** [[brisa]] (política social SFW-video + split RunPod), [[brisa-video-production]] (breakfast/kitchen img2img + 24fps social), [[runpod]] (SSH ports 15/7, Comfy manual si 530).
- **Ya en sesión (sin re-escribir built-in):** USER/MEMORY ya tenían preferencias redes + RunPod split (escritas en vivo 15/7).
- **MEMORY 2211/2200 · USER 1816/1800:** **llenos (>100%)** — no se agregaron punteros; **pass semanal debe rotar**.
- **Crítico (sigue):** app-password iCloud en transcripts Apple históricos — rotar si aún no se hizo (flag 14–15/7).

## 2026-07-15 — Daily consolidation (~02:00)

- **Fuente principal:** Desktop `20260714_142753_b2cf3c` (OpenArt/Brisa prod noche 14→15). Telegram Apple del 13 ya absorbido el 14/7.
- **Updated:** [[brisa-face-pipeline-evaluation]] (prod JGG+stills→Pony d0.4 DualCLIP; lección denoise; CRPony UNet-only), [[runpod]] (pod `1n0whm7wacau00` EXITED post-eróticos; clip_g; LoRAs stills/video; SSH ports rotan), [[brisa-video-production]] (lista erotic 6/6 + variety).
- **Ya en sesión (sin re-escribir):** MEMORY/USER punteros prod; [[wan22-issues]] update all6; canónicos `brisa_stills`/`brisa_video` en Desktop `brisa_prod/`.
- **MEMORY ~93% / USER ~90%:** no se agregaron punteros nuevos (rotar en pass semanal).
- **Crítico (pendiente de Jorge):** app-password iCloud sigue en plaintext en transcripts Apple históricos — rotar si aún no se hizo (flag del 14/7).

## 2026-07-14 — Daily consolidation (~02:00)

- **Fuentes:** Telegram `20260713_122217_cf1951` + `20260713_165241_21c6604d` (Apple/Brave); Desktop `20260713_174939_5f4b63` (OpenArt + RunPod models).
- **Updated:** [[hermes-configuration]] (OpenArt MCP, brave-free, max_tokens 16384, Desktop 403), [[runpod]] (JGG/CRPony/FaceID on S3 vol; pod stop 13/7), [[brisa-face-pipeline-evaluation]] (estado pipeline + cloud NSFW no).
- MEMORY/USER punteros refinados (sin páginas nuevas Apple — dossier ya absorbido en sesión).
- **Crítico:** app-password iCloud apareció en plaintext en transcript de sesión Apple (comando IMAP). **Rotar** app password de `sagasti@mac.com` y no re-pegar secrets en chat.

## 2026-07-13 — Daily consolidation (02:00)

- **Fuente:** Telegram `20260710_213913_df08e117` (noche 12→13). Sesión “Saludo…” sin facts nuevos (WA ya capturado).
- **Nuevo concept:** [[hermes-gemini-google-alias-native-client]] (400 thinking_config, patch local, reapply post-update).
- **Nueva decision:** [[hermes-quality-first-model-stack]] (Grok main, OR fallbacks, vision xAI, smart off).
- **Updated:** [[hermes-configuration]], [[technical-lessons]], [[index]].
- MEMORY ya tenía puntero de models+patch (sesión misma noche); sin cambio USER.

## 2026-07-12 — Mantenimiento semanal estructural

- **Tipo:** Mantenimiento
- **MEMORY/USER audit:** post-compact MEMORY 1546/2200 (~70%); USER 1240/1800 (~69%). Sin secrets. Preferencias estables OK en USER.
- **Broken wikilinks desde MEMORY** (faltaban páginas):
  - creó `concepts/hermes-configuration.md`
  - creó `concepts/hermes-cli-send-command-gap.md`
  - creó `concepts/technical-lessons.md` (índice de lecciones)
  - creó `concepts/google-workspace.md`
- **Scaffold meta ausente desde el init del vault:** creó `SCHEMA.md`, `index.md`, `log.md` (nunca existieron en git history).
- **RunPod:** `valid_until` expirado (2026-05-26) → renovado; nota pod on-demand.
- **Daily 02:00 (hoy):** ya había creado `hermes-whatsapp-bridge-failure-mode` + paths `platforms/whatsapp` — verificado, sin conflicto.
- **Refs `~/wiki` laboral:** solo menciones negativas/hard-rule (OK).
- MEMORY compactado levemente para headroom.

## Previo (sin log formal)

- 2026-07-11/12 daily: WA bridge failure mode, ciudadanías story, wiki separation cleanup (2026-07-09).
- 2026-04-26: primera rotación MEMORY → runpod/comfyui/hunyuan (promotions con nota en esas páginas).
