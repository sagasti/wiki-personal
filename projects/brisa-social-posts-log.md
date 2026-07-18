# Brisa — log de posts sociales

**Regla Jorge (2026-07-18):** NUNCA repetir prompt de render ni caption. Revisar este log antes de proponer/generar.  
Una línea (o bloque) por post: fecha · red · estado · seed · flags · prompt · caption · ancla realidad · fuente clima.

**Regla permanente prompts (Jorge/Claudio 2026-07-18):**  
Prompts = **ESCENA + OUTFIT + LUZ** solamente.  
**NUNCA** cara, pelo, ojos ni cuerpo base (el driver `brisa_gen_v2.py` inyecta el canon solo: pelo copper, pecas, etc.).  
Meter identidad a mano (ej. “red auburn”, “hazel eyes”, “pixie”) **pisa el canon y deriva la cara**.  
Excepción OK: canon de cuerpo/desnudo **cuando el plano lo muestra** (ej. freckles on chest and shoulders).

Estados: `PROPUESTO` | `APROBADO` | `RENDERED` | `PUBLICADO` | `DESCARTADO`

---

## 2026-07-18 — batch validación dry-run · APROBADO Jorge (texto) · render Claudio · SIN PUBLICAR

### APROBADO · IG · seed 918274301 · --detailer
- **Ancla:** sáb 18/7/2026 ~12:00 ART, invierno CABA; nublado/neblina residual, máx ~16–18 °C, más fresco que el viernes; chance llovizna (AccuWeather CABA Hi 18° / Lo 11°; weather.com ~11h ART foggy/mist H~16 °C).
- **Prompt (corregido, sin identidad):**  
  `brisa wearing an oversized charcoal wool sweater and dark high-waist jeans, barefoot on a wooden floor by a rainy apartment window, overcast winter midday light, holding a warm ceramic mug with both hands, cozy Buenos Aires Saturday, fully clothed, photoreal, natural window light`
- **Caption:**  
  sábado nublado en casa  
  café y suéter grueso, el frío de julio no perdona  
  link en bio si querés el resto del día  

### APROBADO · X · seed 775601224 · (sin --detailer, close-up torso)
- **Ancla:** mismo sáb 18/7 tarde-noche más fresca (~11 °C); más jugado X (sensitive OK).
- **Prompt (corregido: sin pelo/ojos; se mantiene freckles pecho = plano lo muestra):**  
  `brisa, intimate medium close-up on sofa under a chunky knit throw, wearing only an open soft grey cardigan slipping off one shoulder, implied topless tasteful, freckles on chest and shoulders, warm lamp light vs cold rainy window, winter Saturday night in, Buenos Aires, photoreal, seductive calm look at camera`
- **Caption:**  
  el sábado se puso frío afuera  
  adentro no tanto  
  AI-generated · 18+  
  https://www.fanvue.com/brisa-cabelious/fv-2  

### DESCARTADO (render) · Threads · seed 482019573 · --detailer
- **Motivo:** mate no salió en imagen (solo tostadas); caption dice mate → mismatch foto/caption.
- Prompt original (mesa): mate de utilería en mesa — no confiable.
- **Caption:** (misma, se reusa si el re-roll cierra)  
  no salgo si el cielo está así  
  mate, tostada y cero agenda  
  si te copa la onda, link en bio  

### RE-ROLL Threads · 2026-07-18 · Brisa · 3 candidatos → Jorge TG · SIN PUBLICAR
- **Ancla:** mismo sáb 18/7 invierno CABA nublado.
- **Prompt (mate EN MANOS + bombilla; sin identidad a mano):**  
  `brisa sitting at a small kitchen table in a cream knit hoodie and soft grey sweatpants, winter Saturday brunch, holding a traditional Argentine mate gourd with metal bombilla in both hands close to her chest, buttered toast on the table, soft overcast daylight from the side, relaxed half-smile looking at camera, fully clothed, Buenos Aires apartment, photoreal`
- **Caption:** (igual)  
  no salgo si el cielo está así  
  mate, tostada y cero agenda  
  si te copa la onda, link en bio  
- **Candidatos RENDERED** (`--detailer`, stack zimage+brisa_v2, sidecars OK):  
  - **A** seed `610482193` → `~/.hermes/media/brisa_v2/threads_reroll_20260718/candA_seed610482193.png`  
  - **B** seed `883017456` → `…/candB_seed883017456.png`  
  - **C** seed `247559801` → `…/candC_seed247559801.png`  
- Vision check: los 3 = mate+bombilla en manos + tostadas + hoodie/joggers SFW.
- Enviado a Jorge Telegram home `1808182714`.
- Pod: **EXITED** post-job (`pod.py stop --force`).

---

## Notas
- Cron `brisa-social-posts` paused hasta OK final Jorge (elige A/B/C Threads + cierra validación).
- **Home media descargado:** `~/.hermes/media/brisa_v2/` — **NO** `/Volumes/Extra/photos/brisa_prod` (árbol cara vieja, a borrar).
- Gen: solo `brisa_gen_v2.py` + prompts escena/outfit/luz. Objetos clave (mate) **en manos**.
- Comfy: esperar autostart 200; no levantar main.py a mano.
