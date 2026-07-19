# Brisa — log de posts sociales

**CIERRE OPERATIVO (Jorge 2026-07-18 via Claudio/hermes-admin):**  
Brisa **deja de generar y publicar** en IG/X/Threads (Buffer) y Fanvue.  
Cron `brisa-social-posts` **ELIMINADO** — no recrear. Ops comercial del personaje → **agente de agencia**.  
Este log queda como histórico / anti-repeat si algún día Jorge ordena algo puntual.

**Regla Jorge (2026-07-18):** NUNCA repetir prompt de render ni caption (histórico).  
**Regla permanente prompts:** ESCENA + OUTFIT + LUZ; driver inyecta canon.

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

### RE-ROLL Threads · 2026-07-18 · 3 candidatos → Jorge TG · SIN PUBLICAR (histórico)
- **Ancla:** mismo sáb 18/7 invierno CABA nublado.
- **Prompt (mate EN MANOS + bombilla; sin identidad a mano):**  
  `brisa sitting at a small kitchen table in a cream knit hoodie and soft grey sweatpants, winter Saturday brunch, holding a traditional Argentine mate gourd with metal bombilla in both hands close to her chest, buttered toast on the table, soft overcast daylight from the side, relaxed half-smile looking at camera, fully clothed, Buenos Aires apartment, photoreal`
- **Caption:** (igual)  
  no salgo si el cielo está así  
  mate, tostada y cero agenda  
  si te copa la onda, link en bio  
- **Candidatos RENDERED** (`--detailer`, stack zimage+brisa_v2):  
  - A `610482193` · B `883017456` · **C `247559801` (elegido Jorge para pack)**  
  - Paths: `~/.hermes/media/brisa_v2/threads_reroll_20260718/` y pack `valbatch_aprobado_20260718/` (`val_ig_sweater`, `candC_…`, `val_x_cardigan`)
- Vision QC OK (sin piercings/tattoos visibles). Pod EXITED post-job.
- **Buffer schedule 14:30 IG+TH / 20:30 X:** intento bloqueado por timeout de aprobación del runtime → **no se publicó**. Después llegó handover agencia → **no reintentar** desde este agente.

---

## Notas (histórico)
- Cron social **ELIMINADO** 18/07 — no recrear; ops → agencia.
- Media v2 home: `~/.hermes/media/brisa_v2/`. Gen histórica: `brisa_gen_v2.py` escena/outfit/luz; mate **en manos**.
