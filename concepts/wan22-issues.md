# Wan 2.2 I2V Issues

## Fecha: 2026-06-13

## Problema principal
Wan 2.2 I2V **no mantiene identidad** de la imagen source. El video arranca con la foto y después diverge completamente — la persona ya no está.

## LoRA brisa_wan22_v2
- Formato original: `lora_wan` (musubi-tuner)
- Conversión a ComfyUI: `convert_lora.py --target other` → `brisa_wan22_v2_comfy.safetensors` (293MB)
- **strength 1.0-1.5**: quema la imagen (naranja, granulada, oversaturated)
- **strength 0.2-0.6**: no alcanza para mantener identidad, sigue divergiendo
- **No hay sweet spot encontrado**

## Config correcta
- UNET: `wan2.2_i2v_low_noise_14B_fp16.safetensors` (o high_noise)
- TE: `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (**NO** el .pth, **NO** qwen)
- VAE: `wan_2.1_vae.safetensors`
- Sampler: dpmpp_2m / normal / CFG 2.0 / steps 25
- DecodeAndSaveVideo requiere `tiling: "disabled"`

## TE Issue
`CLIPLoader` con `type: "wan"` + `.pth` carga SD1ClipModel (768 dim) en vez de T5 (4096 dim) → shape mismatch. Usar `.safetensors` fp8 funciona.

## Posibles soluciones a explorar
1. IP-Adapter para video (identity preservation)
2. FaceID / PuLID nodes para Wan
3. Re-entrenar LoRA con settings diferentes
4. Modelo diferente (Hunyuan Video, CogVideoX)
5. Frame-by-frame con ControlNet + face reference
