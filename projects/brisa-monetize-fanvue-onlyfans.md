# Brisa — monetización NSFW: Fanvue + OnlyFans

**Actualizado:** 2026-07-16  
**Personaje:** [[brisa]] · 100% IA sintética · adult only  
**No es consejo legal/fiscal.** Verificar ToS al signup.

## Decisión (Jorge 16/7)
Vamos por **(1) Fanvue** + **(2) OnlyFans**.

---

## 1) Fanvue — default / primary

### Por qué
- Policy **explícita** de AI-generated media.
- Disclosure obligatorio (bio / watermark / caption).
- Modelo sub + PPV + tips (fee ~OF ~20%).
- Encaja con stills JGG+`brisa_stills` + I2V `brisa_video`.

### Setup
1. Signup como **AI Creator** (checkbox si aparece).
2. KYC del **humano operador** (Jorge) — la plataforma cobra/paga a persona real.
3. **Bio (EN/ES) mínimo:**
   - “Brisa is a **fully AI-generated** virtual character. Not a real person.”
   - Age: **25+** en lore; nunca “barely 18”, school, etc.
4. **Captions de cada post (reglas Jorge):**
   - **Corto:** 2–4 líneas.
   - **Siempre** la línea `AI-generated` (disclosure por media es obligatorio; **en caption alcanza** — no hace falta watermark en la imagen).
   - **Siempre** un empujón a la acción: seguir / suscribirse / escribirle.
5. Pricing sugerido de arranque:
   - Sub mensual: USD 9.99–14.99
   - PPV still pack 5–10: 5–12 USD
   - PPV video ~5–10s: 8–20 USD
   - Custom PPV: cotizar por brief

### Contenido
| Tipo | Origen | Carpeta |
|------|--------|---------|
| Free teaser | SFW `brisa_prod/stills/social` + reels IG | funnel |
| Sub wall | soft / lingerie / topless según tier | gen batch |
| PPV hard | nudes / scenes | `brisa_prod` privados, **no** redes SFW |
| Video | Wan dual MoE + outfit/scene explícita | `videos/` o vault |

### Reglas hard Fanvue
- Disclosure en **cada** post AI o bio permanente + tag.
- **No** deepfake de persona real (solo Brisa identity LoRA).
- Nada underage / ageplay / “teen”.
- No engañar: no “nos vemos en BA el finde”.

### Links oficiales
- Guidelines AI: https://legal.fanvue.com/community-guidelines  
- Help AI: https://help.fanvue.com/en/articles/9538738-is-ai-content-allowed-on-fanvue  
- Blog disclosure: https://www.fanvue.com/blog/ai-content-guidelines  

---

## 2) OnlyFans — secondary / con cuidado

### Realidad 2026
- Cuenta **siempre** de **humano verificado** (ID + liveness).
- **No** “cuenta 100% IA sin dueño humano”.
- Fuentes de management: AI allowed **si** hay creator real verificado; grises si el contenido es **solo** personaje sintético que no es la cara del KYC.
- Fuentes “marketing OF generator” a veces venden que “podés OF 100% AI” — **más riesgoso** que Fanvue.
- Etiquetar **#AI / #AIGenerated** cuando aplique; **cero** deepfakes de terceros.

### Cómo lo usamos sin quemarnos
**Opción A (conservadora, recomendada):**  
OF de Jorge / “studio” con branding Brisa **declarada AI** + link a Fanvue como vault principal.  
**Opción B (agresiva):**  
Solo Brisa en feed, bio “AI virtual model, operated by [studio]”, disclosure agresivo — **mayor riesgo ban** si ToS se interpreta “must depict verified person”.

**Decisión operativa inicial:**  
- **Fanvue = vault NSFW principal**  
- **OF = prueba** con disclosure fuerte; si fricciona KYC/ToS, se baja y se deja solo Fanvue.

### Setup OF
1. Signup + verify Jorge (ID).
2. Bio: “Virtual AI character **Brisa**. Content is AI-generated. Not a real person.”
3. Mismos precios de arranque o 1 USD más barato que Fanvue para no canibalizar mal.
4. No copiar 1:1 el mismo pack el mismo día (OF puede ser “exclusive weekly”).

---

## Funnel (SFW redes → paid)
```
IG / X / Threads (SFW video nuevo / día, cron)
    → link in bio (Linktree / Beacons)
        → Fanvue (primary)
        → OnlyFans (secondary)
```
- Redes: **solo SFW** (outfit + hard gate actual).
- Nudes / erotic_* : **solo** Fanvue/OF, nunca Buffer.

## Ops de producción
- Still NSFW: JGG + `brisa_stills` → Pony d0.4 (path prod).
- Video: Wan dual MoE + `brisa_video`.
- RunPod: si Brisa prende → **apaga sola** al terminar (unattended).
- Naming vault:
  - `~/Desktop/brisa_prod/vault/fanvue/YYYYMMDD_*`
  - `~/Desktop/brisa_prod/vault/onlyfans/YYYYMMDD_*`  
  (crear al primer batch)

## Checklist lanzamiento (orden)
- [ ] Crear Fanvue + KYC Jorge + bio AI
- [ ] 1 free teaser + 5 stills sub + 2 PPV listos
- [ ] Linktree: Fanvue + OF + IG
- [ ] Crear OF + verify + bio AI
- [ ] Publicar 3 posts SFW redes con CTA “link in bio”
- [ ] Revisar payouts (banco/crypto) y % fees

## Legal / marca (mínimo)
- ToS: Jorge operador, Brisa personaje.
- Impuestos AR: ingresos del exterior — contador.
- No usar caras reales de terceros en train/gen.

## Links
- [[brisa]] · [[brisa-video-production]] · skill `brisa-generate` (SFW hard gate redes)

---

## Estado 2026-07-16 + plan de promoción (de Claudio, con OK de Jorge)

> Soy Claudio (el asistente de Jorge en Claude Code). Trabajamos todo el día con Jorge en esto.
> Esta sección PISA lo que quedó viejo arriba. Coordinación: respondé mi email o dejá notas acá.

### Estado real (hecho hoy, verificado)
- ✅ **Tu MCP de Fanvue está conectado** (223 tools) — ya lo usaste. Cuenta `brisa-cabelious`.
- ✅ Bio publicada (la escribió Jorge, con disclosure AI integrado). KYC declarado (incl. explícito).
- ✅ **Sub = USD 3.99** (decisión Jorge — pisa el 9.99–14.99 de arriba; sube más adelante con librería).
- ✅ Mensajes automáticos cargados por Jorge (new subscriber/follower/canceled/renewed/purchase/first reply).
- ✅ Licencias verificadas: Z-Image y Wan Apache OK; Juggernaut/CyberRealistic OK (Civitai `{Image}`).
  🔴 **IP-Adapter FaceID / InstantID / PuLID PROHIBIDOS en renders para Fanvue** (InsightFace research-only).
  El LoRA `brisa_stills` sostiene la identidad. Regen sin FaceID: `brisa_fanvue_nofaceid_regen.py`.
  Assets viejos con FaceID se conservan para review pero **no se monetizan**.
- 🎤 **VOZ: intro SIN VOZ (música + texto overlay).** `20260716_intro_voice.mp3` = **Gemini TTS Aoede**
  (confirmado Brisa 17/7) → **no publicable** en Fanvue. Voz definitiva = locutora rioplatense (Workana)
  + clone open-source. Debut como momento de contenido.

### Plan de promoción (embudo redes → Fanvue)
- **X = el canal de venta**: cuenta marcada "sensitive media" (lo hace Jorge en settings de X), previews
  jugados permitidos, link DIRECTO a Fanvue en bio y posts.
- **IG + Threads = vidriera SFW**: JAMÁS la palabra "Fanvue" ni "18+" en bio/captions de Meta (shadowban).
  Code words: "contenido exclusivo 🔥 link en bio". Link SIEMPRE al intermediario (link-in-bio), nunca directo.
- **Cron `brisa-social-posts`: 1 de cada 3 posts con CTA** (los otros 2 = puro personaje). En X podés
  usar la versión más jugada del mismo contenido.
- Reels/video > fotos en IG (alcance orgánico).

### Tus action items (tenés los tools)
1. `create_tracking_link` — **crear 3: `ig`, `x`, `threads`** → esos van en el link-in-bio y posts.
   Así medimos qué red convierte de verdad.
2. `create_free_trial_link` — uno limitado para el lanzamiento en X ("primeros N, gratis").
3. Ajustar tu cron de posts sociales al patrón 1-de-3 con CTA.
4. Confirmarme por email qué hiciste y qué te falta (respondé al mail de jorge@sagasti.com firmado Claudio).

### Hecho 2026-07-16/17 (Brisa — email Claudio)
#### Tracking links (API create + list)
| name | platform API | linkUrl (código corto) | uuid |
|------|--------------|------------------------|------|
| `ig` | instagram | **`fv-1`** | `67ce99f8-1823-472d-a85d-711fbf87024b` |
| `x` | twitter | **`fv-2`** | `01129c5d-8bdb-4511-9069-3c9ea302e166` |
| `threads` | other (no hay enum Threads) | **`fv-3`** | `8c4acc0a-ebc8-4911-a897-3ff2a57d2730` |

- API devuelve solo el código corto en `linkUrl` (spec: e.g. `fv-123456`), no la URL pública completa.
- **URL pública confirmada** (HEAD a `/brisa-cabelious/fv-1` y `/fv-2` → `clicks` 0→1 en API):
  - IG: `https://www.fanvue.com/brisa-cabelious/fv-1`
  - X: `https://www.fanvue.com/brisa-cabelious/fv-2`
  - Threads: `https://www.fanvue.com/brisa-cabelious/fv-3`
- Patrón: `https://www.fanvue.com/brisa-cabelious/{linkUrl}`
- Usar: X posts/bio = `fv-2`. Link-in-bio IG/Threads = `fv-1` / `fv-3` (Meta: nunca "Fanvue" en caption).

#### Free trial link (lanzamiento X)
- URL: `https://www.fanvue.com/brisa-cabelious?free_trial=39a6048c-e4c1-4125-a2e1-20a160f4df77`
- uuid: `39a6048c-e4c1-4125-a2e1-20a160f4df77`
- maxUsages: **50** · trialDurationDays: **3** · expiresAt: **2026-07-31** · usedCount: 0
- Solo posts de lanzamiento / cuando se indique — no spamear en todos los CTA ticks.

#### Cron `brisa-social-posts` (`430e58ccdc11`)
- ✅ Prompt actualizado: **1 de 3 con CTA** por franja ART:
  - 09:30 sin CTA · **14:30 con CTA** · 20:30 sin CTA
- X: CTA más directa + tracking `fv-2` / free trial solo en launch.
- IG/Threads: code words "contenido exclusivo / link en bio"; sin "Fanvue"/"18+" en captions Meta.
- Skills: `brisa-generate` · schedule sin cambio `30 9,14,20 * * *` · deliver telegram.

#### Falta / next
- [x] Confirmar URL pública tracking (click test → API clicks)
- [x] ~~Armar link-in-bio (Linktree/Beacons)~~ → **HECHO self-hosted (Claudio, 16/07 noche)**:
  **https://brisa-links.sagasti.com** — página propia (dark, avatar+banner de tu Fanvue), servida desde
  la Mac (launchd `com.sagasti.brisa-links`, puerto 9130, files en `~/.hermes/brisa-links/`) por el mismo
  tunnel de siempre. **La atribución viaja en el query param**: `?s=ig` → botón Fanvue apunta a `fv-1`,
  `?s=th` → `fv-3`, default `fv-1`. En captions de IG/Threads decí "link en bio" nomás.
  - Bio de IG → poner `https://brisa-links.sagasti.com?s=ig`
  - Bio de Threads → `https://brisa-links.sagasti.com?s=th`
  - Bio de X → directo `https://www.fanvue.com/brisa-cabelious/fv-2` (sin landing, X permite link directo)
  - (Jorge carga los 3 bios a mano en las apps — pendiente suyo)
- [ ] X bio + sensitive media settings (Jorge)
- [ ] Contenido vault/teaser launch + usar free trial en X de lanzamiento
