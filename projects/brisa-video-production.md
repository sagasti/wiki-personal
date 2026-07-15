# Brisa — pipeline producción (stills + video)

**Fecha cierre stack:** 2026-07-14/15  
**Default actual:** stills SDXL dense + video Wan **all6**

## Resumen

| Capa | Elección |
|---|---|
| Stills NSFW | **Juggernaut XL** + LoRA `brisa_sdxl_v1_dense` @1.0 + FaceID light (0.85) → refine **CRPony d=0.4** DualCLIP (`clip_l`+`clip_g`) + SDXL VAE |
| Trigger stills | `brisa` (caption siempre empieza con `brisa,`) |
| Video I2V | **Wan 2.2 dual MoE** high+low noise 14B fp16 + LoRA **`identity/brisa_wan22_v2_all6_comfy`** @1.0 |
| Alias prod video | `identity/brisa_wan22_PRODUCTION.safetensors` → all6 |
| Regla de oro I2V | **1 still distinta por escena**. No reusar la misma foto con prompts de otra escena (sale “el mismo video 6 veces”). |

## Rutas clave

### LoRAs
- Desktop: `~/Desktop/brisa_wan_loras/brisa_wan22_v2_all6_comfy.safetensors` (293MB)
- Desktop stills LoRA: `~/Desktop/brisa_sdxl_v1_loras/brisa_sdxl_v1_dense.safetensors`
- Pod Comfy: `models/loras/brisa_sdxl/brisa_sdxl_v1_dense.safetensors`
- Pod video: `models/loras/identity/brisa_wan22_v2_all6_comfy.safetensors`
- Backups video: `…_prod_comfy`, `…_spike_comfy` (no default)

### Datasets
- Stills train SDXL: `/Volumes/Extra/ComfyUI/brisa/datasets/brisa_sdxl_v1/` (100 imgs, caps unificados)
- Video train all6: pod `/workspace/brisa/datasets/brisa_wan22_v2_all6/` (164: frames variety + stills + half sdxl)

### Outputs útiles Desktop
- `~/Desktop/brisa_FINAL_KEEP/` — grillas checkpoints SDXL
- `~/Desktop/brisa_videos/true_variety/` — 6 stills + 6 I2V (still por escena)
- `~/Desktop/brisa_videos/grid_final/` — A/B prod vs all6 + variety all6
- `~/Desktop/brisa_videos/erotic/` — (batch erótico en curso 2026-07-15)

### Pod / RunPod
- Pod: `comfyui-luz-h200` (script `pod.py`)
- SSH: puerto **cambia** al reiniciar — obtener de API RunPod (`privatePort=22`)
- SSH host key: `StrictHostKeyChecking=no` o limpiar `known_hosts` al cambiar IP:puerto
- Comfy: `:8188` (proxy 8089 a veces). Necesita `sqlalchemy` a veces tras reboot (`pip3 install sqlalchemy --break-system-packages`)
- Train Wan: **apagar Comfy** (OOM si no). `LD_LIBRARY_PATH` cuda-13.0 + musubi_venv
- Scripts: `/workspace/scripts/bere/wan_i2v_api_builder.py`, `/workspace/scripts/brisa/brisa_wan22_*_train.sh`

## Cómo generar un video erótico (receta)

1. **Still** (si no hay una buena):
   - Prompt: `brisa, photoreal adult woman 25yo short red auburn pixie freckles hazel eyes, [escena erótica], natural skin…`
   - Neg: child/loli/teen + plastic skin + long hair brunette…
   - JGG 50 steps + dense LoRA + FaceID light → encode → Pony 30 steps d=0.4
2. **I2V** con **esa** still (subir a `input/`):
   - LoRA: `identity/brisa_wan22_v2_all6_comfy` @1.0
   - UNETs: `wan2.2_i2v_high_noise_14B_fp16` + `low_noise_14B_fp16`
   - 720×1280, length 81, dual KSampler (0–10 high, 10–20 low), CFG 5, euler/simple
   - Prompt motion: identidad + **movimiento lento sensual** (no pedir otra escena que no esté en la still)

## Historia de decisiones (video LoRA)

| Versión | Notas | Resultado |
|---|---|---|
| v2 viejo | identidad débil / overburn | descartado |
| spike | dim16 corto, dataset v4 | mejor que v2, baseline |
| prod | dim32, 100 stills sdxl | similar a spike en A/B corto |
| **v2 all6** | 164 (frames de 6 escenas variety + stills + sdxl), init prod, ~3.4k steps | **ganador** en grilla |

## Pitfalls

- I2V con **misma still** + prompts de escenas distintas = basura / mismo video.
- Comfy + train dual Wan 14B = OOM en H200 → matar Comfy antes de train.
- `save_last_n_steps` borra checkpoints intermedios densos.
- Proxy RunPod 530/502 al boot; SSH puede fallar por host key / puerto viejo.
- TE Wan: usar stack del `wan_i2v_api_builder` (no mezclar .pth CLIPLoader mal).
- Strength all6: empezar en **1.0**; si quema, bajar 0.7–0.85.

## Continuidad Telegram

Jorge sigue desde Telegram. Al retomar:
1. Status pod (`pod.py status`) + SSH port fresco.
2. Si pide videos: stills distintas → all6 I2V.
3. Si pide train: documentar dataset, apagar Comfy, train en tmux.
4. No tocar `~/wiki` laboral; memoria solo `~/.hermes/personal/`.

## Links

- [[wan22-issues]] — issues viejos del v2
- [[brisa-lora-tags]] — tags/captions
- [[lora-inventory-and-dual-identity]] — inventario
- [[brisa]] — personaje
