# Brisa — producción limpia (sin versiones)

**Actualizado:** 2026-07-18

## Pipeline actual (Fanvue / relanzamiento — 17/7 noche v2)

**Único gen permitido:** `python3 /workspace/scripts/brisa/brisa_gen_v2.py --prompt "…" [--detailer] [--seed N]`  
- LoRA: **`brisa_v2_lora2_ep024.safetensors`** · trigger **`brisa`** · sidecar `.txt` siempre.  
- FaceID / JGG+Pony / `brisa_stills` / `brisa_video` / zimage / BRISA_PRODUCTION = **MUERTOS** para prod nueva.  
- Detalle playbook: [[brisa-monetize-fanvue-onlyfans]] § Pipeline v2.

## Nombres canónicos históricos (vault / labs — no gen nueva)

| Rol | Archivo | Dónde |
|---|---|---|
| Stills LoRA (viejo) | `brisa_stills.safetensors` | Extra `brisa_prod/loras/` · Pod `loras/brisa_sdxl/` |
| Video LoRA (viejo) | `brisa_video.safetensors` | Extra `brisa_prod/loras/` · Pod `loras/identity/` |
| Alias stills | `brisa_sdxl_PRODUCTION` → stills | pod |
| Alias video | `brisa_wan22_PRODUCTION` → video | pod |
| Trigger | `brisa` | captions / prompts |

## Pipeline

### Stills (genérico / NSFW)
1. Juggernaut XL + `brisa_stills` @1.0 (identidad por LoRA)
2. Refine CRPony d=0.4 DualCLIP (`clip_l`+`clip_g`) + SDXL VAE
3. Prompt: `brisa, … short red auburn pixie freckles hazel eyes …`

### 🔴 Fanvue / monetización — FaceID PROHIBIDO de nuevo (v2 17/7 noche)
- **NUNCA** IP-Adapter FaceID / InstantID / PuLID (InsightFace research-only + identidad ahora = LoRA v2).
- Gen comercial nueva: **solo** `brisa_gen_v2.py` + `brisa_v2_lora2_ep024` (ver playbook).
- Histórico 16–17/7: Jorge prefirió calidad FaceID sobre batch sin FaceID; batch stamp `20260717_0545` A–D en Extra = vault viejo (cara anterior). **No publicar en relanzamiento v2.**
- Voz Gemini/Aoede: **NO** en Fanvue (ToS Google). Intro = música + texto overlay hasta locutora + clone open-source.

### Stills con escena real (img2img, 15/7)
1. Ref foto de escena (ej. cocina Jorge) → VAEEncode como latente start
2. JGG + `brisa_stills` (± FaceID solo si NO es Fanvue) · denoise base ~0.72
3. Refine CRPony DualCLIP denoise ~0.35
4. Luego I2V con motion prompt de la escena

### Video I2V (erótico o SFW)
1. **Still distinta por escena** (no reusar la misma foto)
2. Wan 2.2 dual MoE high+low 14B fp16 (**nunca** high solo)
3. LoRA `brisa_video` @1.0
4. 720×1280 · 81 frames · ~16 fps nativo · builder `wan_i2v_api_builder.py` o scripts `/tmp/brisa_*`
5. Prompt de **motion** sobre la escena de la still
6. **Redes:** reencode a **24 fps** h264 yuv420p si se sube a IG/Threads (16 fps rechaza)

## Path canónico (2026-07-16/17)
**ÚNICO real:** `/Volumes/Extra/photos/brisa_prod`  
**NO** depender de `~/Desktop/brisa_prod` (symlink removido 17/7).  
No copiar media a Desktop/iCloud sin symlink: purga *dataless* y se rompe el copy.

## Layout Extra
`/Volumes/Extra/photos/brisa_prod/`
- `loras/brisa_stills.safetensors`
- `loras/brisa_video.safetensors`
- `stills/*.png` — bed, mirror, window, close_face, sofa, standing (+ variety grid) + `breakfast.png` + `breakfast_kitchen_pj.png`
- `stills/social/` · `videos/social/` — SFW redes (review)
- `vault/fanvue/public/` — discovery SFW (avatar/banner/intro públicos)
- `vault/fanvue/nsfw/` — soft free teaser + hard
- `vault/fanvue/nsfw/collections/{A..H}/{stills,videos}/` — hard por escena (overnight A–H 17/7)
- `videos/*.mp4` — I2V variety + eróticos + SFW desayuno
- `docs/` + `README.md`

### Videos SFW social (2026-07-15 WA)
| Clip | Notas |
|---|---|
| `breakfast.mp4` | Desayuno genérico · still+I2V · post “Café en pijama…” |
| `breakfast_kitchen_pj.mp4` (+ `_24fps`) | Comedor real Jorge + pijama · img2img ref cocina |
| `sofa_lounge_24fps.mp4` / `mirror_selfie_24fps.mp4` | Reencodes para ticks Buffer |

### Videos eróticos (6/6, 2026-07-15, LoRA `brisa_video`, still distinta c/u) — **privados, no redes**
`erotic_bed`, `erotic_window`, `erotic_sofa`, `erotic_mirror`, `erotic_standing`, `erotic_close` (+ variety: bed_lingerie, mirror_selfie, window_nude, sofa_lounge, standing_studio, close_face, GRID_variety)

## Pod outputs
`/workspace/ComfyUI/output/brisa_prod/{stills,videos}/` — copiado al Desktop; pod **EXITED** post-batch (15/7 mañana eróticos + 15/7 día breakfast/kitchen)

## Dataset (si re-entrenás)
- Stills: Extra `ComfyUI/brisa/datasets/brisa_sdxl_v1/` (100 PNG+txt, trigger `brisa,`, QC Jorge 14/7 OK; buckets v4/sheet/hero/jgg/ref)
- Video frames train: pod `brisa/datasets/brisa_wan22_v2_all6/` (histórico; el LoRA actual ya salió de ahí)

## Reglas operativas
- Train Wan → **apagar Comfy** (OOM)
- SSH: puerto RunPod cambia al reboot; host key puede fallar → `StrictHostKeyChecking=no`
- Comfy a veces pide `pip install sqlalchemy --break-system-packages`; cloudflared 530 → arrancar Comfy por SSH/tmux
- Redes: solo SFW; ver [[brisa]] + [[buffer]] · **pausa visual** durante relanzamiento v2
- Telegram/WA: Jorge sigue desde ahí; leer este doc al despertar
- **Save solo final** (Pony/output final): no dump intermedios `*_jgg_*` (decisión Jorge 17/7)
- **Resume batch por stamp:** pin `STAMP = "YYYYMMDD_HHMM"` en el script si el resume saltea por path existente; no regenerar con stamp nuevo
- Pull S3 → Extra cuando pod EXITED: `aws s3 sync` del vault; path canónico Extra
- FaceID (labs/histórico): requiere CLIPVision ViT-H + `ip-adapter-faceid_sdxl.bin` — sin eso stills fallan

## LatentSync (lip-sync intro — 16–17/7)
- Custom node en pod: `ComfyUI-LatentSyncWrapper` (pesos en `checkpoints/`, incl. `latentsync_unet.pt`)
- Uso previsto: intro SFW talking-head + voz (voz Gemini **no** monetizable; ver playbook)
- Fallo visto: **`Face not detected`** si el crop 512 no centra cara bien
- Patch local: sample-rate / `torchaudio.save` en `nodes.py` (script `/tmp/patch_latentsync_sf.py` histórico)
- Reinicio Comfy a veces necesario post-patch; no es path de redes SFW diarias

## Descartado (no usar)
- spike / prod intermedio / wan22_v2 original / FLUX paths viejos
- I2V con una sola still + prompts de otras escenas
- Subir `erotic_*` / nudes a IG/X/Threads
- FaceID en cualquier asset Fanvue monetizable

## Links
- Personaje: [[brisa]]
- Issues Wan históricos: [[wan22-issues]]
- RunPod: [[runpod]]
