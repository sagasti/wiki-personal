# Brisa — producción limpia (sin versiones)

**Actualizado:** 2026-07-16

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
1. Juggernaut XL + `brisa_stills` @1.0 + FaceID light (0.85, cara canónica)
2. Refine CRPony d=0.4 DualCLIP (`clip_l`+`clip_g`) + SDXL VAE
3. Prompt: `brisa, … short red auburn pixie freckles hazel eyes …`

### Stills con escena real (img2img, 15/7)
1. Ref foto de escena (ej. cocina Jorge) → VAEEncode como latente start
2. JGG + `brisa_stills` + FaceID (cara canónica) · denoise base ~0.72
3. Refine CRPony DualCLIP denoise ~0.35
4. Luego I2V con motion prompt de la escena

### Video I2V (erótico o SFW)
1. **Still distinta por escena** (no reusar la misma foto)
2. Wan 2.2 dual MoE high+low 14B fp16 (**nunca** high solo)
3. LoRA `brisa_video` @1.0
4. 720×1280 · 81 frames · ~16 fps nativo · builder `wan_i2v_api_builder.py` o scripts `/tmp/brisa_*`
5. Prompt de **motion** sobre la escena de la still
6. **Redes:** reencode a **24 fps** h264 yuv420p si se sube a IG/Threads (16 fps rechaza)

## Desktop prolijo
`~/Desktop/brisa_prod/`
- `loras/brisa_stills.safetensors`
- `loras/brisa_video.safetensors`
- `stills/*.png` — bed, mirror, window, close_face, sofa, standing (+ variety grid) + `breakfast.png` + `breakfast_kitchen_pj.png`
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

## Descartado (no usar)
- spike / prod intermedio / wan22_v2 original / FLUX paths viejos
- I2V con una sola still + prompts de otras escenas
- Subir `erotic_*` / nudes a IG/X/Threads

## Links
- Personaje: [[brisa]]
- Issues Wan históricos: [[wan22-issues]]
- RunPod: [[runpod]]
