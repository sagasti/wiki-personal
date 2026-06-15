---
title: "Video Rating System — Brisa aprende qué les gusta"
created: "2026-04-19"
updated: "2026-04-21"
type: "project"
---

# Video Rating System — Brisa aprende qué les gusta

## Cuestionario por video

Después de cada video, le pregunto a Jorge/Bere:

1. **¿Te gustó en general?** (1-5)
2. **¿El movimiento te convence?** (1-5) — fluido, natural, no robótico
3. **¿La estética/estilo te gusta?** (1-5) — colores, lighting, vibe
4. **¿El sujeto/personaje se ve bien?** (1-5) — consistencia, realismo
5. **¿La cámara/prompt funcionó?** (1-5) — el movimiento de cámara matchea lo que pedí
6. **¿Qué cambiarías?** (texto libre)
7. **¿Lo postearías?** (sí/no/tal vez)

## Categorías de video

| Categoría | Ejemplo | Prioridad |
|---|---|---|
| **Reel Bere** | Bere hablando de ciudadanía, myth-busting | Alta |
| **Reel Brisa** | Brisa presentando algo, con actitud | Alta |
| **VFX shot** | Pasaporte flotando, partículas doradas | Media |
| **T2V test** | Prueba de modelo/params, sin personaje | Baja |
| **I2V animación** | Animar foto existente | Media |
| **LoRA test** | Probar LoRA entrenado | Baja |

## Parámetros a trackear por video

- Modelo (Hunyuan, WAN, LTX)
- Resolución
- Frames
- Steps
- CFG
- Shift
- Sampler/Scheduler
- LoRA + strength
- Prompt
- Seed
- Tiempo de generación

## Rating log

### hunyuan_test02 (18/04/2026)
- **Modelo:** Hunyuan T2V bf16
- **Params:** 448×256, 33f, 20 steps, CFG 6.0, shift 7.0, euler/simple
- **Prompt:** "A young Argentine woman with long dark hair, standing on a rooftop at sunset in Buenos Aires, wind blowing her hair, golden hour, cinematic, photorealistic"
- **Categoría:** T2V test
- **Tiempo:** ~8 min (MPS)
- **Rating Jorge:** "Es muy lindo" → estimado 4/5 general
- **Notas:** Primer video generado local. Chiquito pero funcional.

---

## Cómo uso esto

1. Genero video → muestro a Jorge/Bere
2. Pregunto el cuestionario → anoto ratings
3. Busco patrones: ¿qué params dan mejores ratings? ¿qué prompts? ¿qué estilo?
4. Ajusto: si "movimiento" puntúa bajo → más steps o diferente sampler
5. Si "estética" puntúa bajo → cambio prompt o modelo
6. Si "sujeto" puntúa bajo → ajustar LoRA strength o character sheet

Con el tiempo, los ratings me dicen exactamente qué hacer.
