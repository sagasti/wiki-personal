# Brisa — producción limpia (sin versiones)

**Actualizado:** 2026-07-15

## Nombres canónicos (sin versionar)

| Rol | Archivo | Dónde |
|---|---|---|
| Stills LoRA | `brisa_stills.safetensors` | Desktop `brisa_prod/loras/` · Pod `loras/brisa_sdxl/` |
| Video LoRA | `brisa_video.safetensors` | Desktop `brisa_prod/loras/` · Pod `loras/identity/` |
| Alias stills | `brisa_sdxl_PRODUCTION` → stills | pod |
| Alias video | `brisa_wan22_PRODUCTION` → video | pod |
| Trigger | `brisa` | captions / prompts |

## Pipeline

### Stills NSFW
1. Juggernaut XL + `brisa_stills` @1.0 + FaceID light (0.85, cara canónica)
2. Refine CRPony d=0.4 DualCLIP (`clip_l`+`clip_g`) + SDXL VAE
3. Prompt: `brisa, … short red auburn pixie freckles hazel eyes …`

### Video erótico / I2V
1. **Still distinta por escena** (no reusar la misma foto)
2. Wan 2.2 dual MoE high+low 14B fp16
3. LoRA `brisa_video` @1.0
4. 720×1280 · 81 frames · `wan_i2v_api_builder.py`
5. Prompt de **motion** sobre la escena de la still

## Desktop prolijo
`~/Desktop/brisa_prod/`
- `loras/brisa_stills.safetensors`
- `loras/brisa_video.safetensors`
- `stills/*.png` — bed, mirror, window, close_face, sofa, standing
- `videos/*.mp4` — I2V de esas stills
- `README.md`

## Pod outputs
`/workspace/ComfyUI/output/brisa_prod/{stills,videos}/`

## Dataset (si re-entrenás)
- Stills: Extra `ComfyUI/brisa/datasets/brisa_sdxl_v1/`
- Video frames train: pod `brisa/datasets/brisa_wan22_v2_all6/` (histórico; el LoRA actual ya salió de ahí)

## Reglas operativas
- Train Wan → **apagar Comfy** (OOM)
- SSH: puerto RunPod cambia al reboot; host key puede fallar → `StrictHostKeyChecking=no`
- Comfy a veces pide `pip install sqlalchemy --break-system-packages`
- Telegram: Jorge sigue desde ahí; leer este doc al despertar

## Descartado (no usar)
- spike / prod intermedio / wan22_v2 original / FLUX paths viejos
- I2V con una sola still + prompts de otras escenas

## Links
- Personaje: [[brisa]]
- Issues Wan históricos: [[wan22-issues]]
