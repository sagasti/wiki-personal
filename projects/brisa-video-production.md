# Brisa — producción limpia (sin versiones)

**Actualizado:** 2026-07-17

## Nombres canónicos (sin versionar)

| Rol | Archivo | Dónde |
|---|---|---|
| Stills LoRA | `brisa_stills.safetensors` | Desktop `brisa_prod/loras/` · Pod `loras/brisa_sdxl/` |
| Video LoRA | `brisa_video.safetensors` | Desktop `brisa_prod/loras/` · Pod `loras/identity/` |
| Alias stills | `brisa_sdxl_PRODUCTION` → stills | pod |
| Alias video | `brisa_wan22_PRODUCTION` → video | pod |
| Trigger | `brisa` | captions / prompts |

## Pipeline

### Stills (genérico / NSFW)
1. Juggernaut XL + `brisa_stills` @1.0 (identidad por LoRA)
2. Refine CRPony d=0.4 DualCLIP (`clip_l`+`clip_g`) + SDXL VAE
3. Prompt: `brisa, … short red auburn pixie freckles hazel eyes …`

### 🔴 Fanvue / monetización — FaceID PROHIBIDO (2026-07-16/17, Claudio+Jorge)
- **NUNCA** IP-Adapter FaceID / InstantID / PuLID en material para Fanvue (InsightFace = research-only; ownership de outputs roto).
- Stack comercial: **JGG + `brisa_stills` → Pony d0.4** sin FaceID. Script: `brisa-generate/scripts/brisa_fanvue_nofaceid_regen.py`.
- FaceID light solo en labs / redes SFW no monetizadas si hace falta, **nunca** vault pago.
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
- Redes: solo SFW; ver [[brisa]] + [[buffer]]
- Telegram/WA: Jorge sigue desde ahí; leer este doc al despertar

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
