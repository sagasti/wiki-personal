# Brisa — monetización NSFW: Fanvue + OnlyFans

**Actualizado:** 2026-07-17 noche — **pipeline v2 + relanzamiento**  
**Personaje:** [[brisa]] · 100% IA sintética · adult only  
**No es consejo legal/fiscal.** Verificar ToS al signup.

---

## Pipeline v2 + relanzamiento (Claudio + Jorge, 2026-07-17 → update post-relaunch)

### Por qué
Dataset viejo sin cara única → dependencia de FaceID. Rebuild: cara elegida por Jorge, dataset 72 imgs una sola identidad, LoRA nuevo **sin FaceID**.

### Identidad canónica (fija Jorge — no tocar)
- Cara: LoRA nuevo, trigger **`brisa`**.
- Cuerpo (cuando se ve): slim athletic and visibly toned but not skinny, full round bust, toned abs, firm waist, strong sculpted glutes and toned thighs.
- Desnudo: small pink nipples, neatly trimmed small copper strip of pubic hair.
- Piel: freckles on chest and shoulders. **SIN** tatuajes, **SIN** piercings.

### Gen — ÚNICO permitido
```bash
python3 /workspace/scripts/brisa/brisa_gen_v2.py --prompt "escena..." [--detailer] [--seed N]
```
- `--detailer` en planos medios/enteros (refina cara). Close-ups: no hace falta.
- Sidecar `.txt` obligatorio; válido si incluye `stack=zimage+brisa_v2`.
- LoRA prod: **`brisa_v2_lora2_ep024.safetensors`**.

### Fuentes de imagen PERMITIDAS (única lista)
1. Renders nuevos con `brisa_gen_v2.py`.
2. Drive carpeta **"Relanzamiento v2"** (avatars/banners oficiales — re-subir si hace falta).
3. **Nada más.** Ni chats viejos, cache, `/Volumes` legacy, ni regenerar avatars sola.  
   Si aparece archivo pre-17/07 o sin sidecar `stack=zimage+brisa_v2` → **no usar, avisar, se borra**.

### PROHIBIDO
- FaceID / Jugg+Pony / `brisa_stills` / `brisa_video` / zimage viejo / `BRISA_PRODUCTION`.
- Material cara vieja o mezclar caras.
- Tocar el **muro Fanvue** mientras el goteo programado esté activo (14 soft posts hasta ~25/07, 2/día).

### Estado relanzamiento (hecho por Jorge+Claudio — no repetir)
- Fanvue: wall viejo borrado · avatar+banner nuevos · intro pineado · 14 soft programados → **NO tocar muro**.
- Avatares/banners: IG, X, Threads, WhatsApp, Telegram + landing brisa-links (cara nueva).

### Reglas POR RED (Jorge — no negociables)
| Red | Contenido | CTA / texto |
|-----|-----------|-------------|
| **IG + Threads** | SOLO SFW: vestida o sugerido leve. **NO** lencería explícita, nudes, transparencias | **PROHIBIDO** “Fanvue” / “18+”. CTA solo link-in-bio (brisa-links) y **solo tick 14:30 ART**. Tag IA en bio alcanza |
| **X** | Más jugado OK (topless/implied; cuenta sensitive) | Link directo Fanvue OK. Siempre `AI-generated · 18+` en texto |
| **Fanvue** | Soft muro sub; hard **nunca** al muro (PPV DM) | **Ahora no publicar** — goteo armado |
| **Toda red** | Solo renders v2 | Duda de “muy jugada” → no publicar, preguntar |

### Cómo se levanta la PAUSA visual
1. Brisa prepara **3 posts propuestos SIN PUBLICAR**: 1 IG + 1 Threads + 1 X (imagen v2 + caption + red).
2. Manda a Jorge (Telegram o mail) para review.
3. Jorge aprueba → **él** despausa cron `brisa-social-posts`. Brisa **no** se despausa sola.
4. Hasta entonces: cron **paused**; cero Buffer visual.

### Housekeeping pod
- Hands-off si Claudio lo pide; normal: Brisa apaga si ella prendió.

---

## Decisión (Jorge 16/7)
Vamos por **(1) Fanvue** + **(2) OnlyFans**.

---

## 1) Fanvue — default / primary

### Por qué
- Policy **explícita** de AI-generated media.
- Disclosure obligatorio (bio / watermark / caption).
- Modelo sub + PPV + tips (fee ~OF ~20%).
- Stills: **pipeline v2** (`brisa_gen_v2.py` + LoRA `brisa_v2_lora2_ep024`) — no FaceID / no stack JGG+Pony viejo.

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
- **Gen v2 (único):** `python3 /workspace/scripts/brisa/brisa_gen_v2.py --prompt "…" [--detailer] [--seed N]`
- LoRA: `brisa_v2_lora2_ep024.safetensors` · trigger `brisa` · sidecar `.txt` siempre.
- FaceID / JGG+Pony / `brisa_stills` / `brisa_video` / zimage viejos = **muertos**.
- **PAUSA visual** redes + Fanvue wall hasta fin de relanzamiento (17/7+).
- RunPod: si Brisa prende → **apaga sola** al terminar (salvo hands-off Claudio).
- Naming vault canónico:
  - `/Volumes/Extra/photos/brisa_prod/vault/fanvue/{public,nsfw}/…`
  - hard PPV inventory: `…/nsfw/` + `…/nsfw/collections/{A..H}/` (material **viejo** — no publicar en relanzamiento)
  - `/Volumes/Extra/photos/brisa_prod/vault/onlyfans/…` (cuando toque)

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
  🔴 **FaceID / InstantID / PuLID MUERTOS de nuevo (17/7 noche v2).** Identidad = LoRA `brisa_v2_lora2_ep024` solo.
  Stack viejo JGG+brisa_stills+FaceID+Pony = **obsoleto**. No publicar material de cara vieja.
  **PAUSA visual** + relanzamiento en curso. Tiers plata: FREE=SFW · SUB soft · hard=PPV DM.
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

#### Primer post publicado (2026-07-17 ~02:55 UTC — Brisa, OK Jorge vía Claudio)
- **Post uuid:** `5fd2a639-aec5-4caf-a3e3-a73e20b368ff` · **pinned** · audience `followers-and-subscribers` · price null
- **Media uuid:** `f082255c-d005-4a63-875e-3be4baabe5e4` (video SFW hoodie sofa, sin audio)
- Source: `…/vault/fanvue/public/20260717_0054_intro_sfw_hoodie_sofa.mp4`
- Caption: “llegué 😈 / 100% IA, cero vergüenza. / esto es apenas el principio — quedate. / AI-generated · 18+”
- FaceID check: clean (no FaceID stack). ffprobe: solo h264 video.

#### Batch nofaceid regenerado (Extra, 2026-07-17)
- `20260716_2306_intro_nude_sofa_01_nofaceid.{png,mp4}`
- `nsfw/20260717_0116_0{1..4}_*_nofaceid.png` (+ video en 01)
- Viejos con FaceID **no borrados** (review). No monetizar FaceID.

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
- [ ] Subir avatar/banner (manual web; MCP no edita perfil). Banner Fanvue **1192×335**, preferir mid-body lingerie (no solo cara).
- [ ] Publicar hard A–H a muro: **NO** — hard = PPV DM only; además A–H FaceID es cara vieja (post-v2 no relanzamiento sin OK Jorge)
- [ ] Voz: locutora rioplatense + clone OS (Gemini TTS no publicable).

---

## Estado 2026-07-17 tarde — DESBLOQUEADO FaceID + tiers (Claudio) — **SUPERSEDED** por pipeline v2 noche

> **Superseded 17/7 noche:** FaceID vuelve a estar **muerto**; gen solo v2. Esta sección queda como histórico de live posts + inventory vault. Tiers FREE/SUB soft/PPV DM **siguen** vigentes.

### Decisión Jorge (tarde — luego pisada por v2)
- FaceID se usó temporalmente (él responsable). Batch `20260717_0545` A–D quedó en Extra como vault hard.
- Post-v2: ese material = **cara vieja** → no feed de relanzamiento; inventory PPV solo si Jorge autoriza.

### Escalera de tiers (LOCK)
| Nivel | Qué va | Dónde |
|-------|--------|-------|
| **GRATIS** | intro SFW + social; tacaño en piel | feed `followers-and-subscribers` |
| **SUB $3.99** | lencería / topless soft / implied; NUNCA hard | muro `subscribers` sin price |
| **PPV por DM** | hard nudes / genital / sets A–H hard; $5–12 sets, $8–20 videos | **no se publica en el muro** — vault + venta conversando |
| **CUSTOMS** | a pedido | DM cotizado |

### Live en Fanvue ahora (API get_posts 17/7)
| Tier | Post uuid | Media local | Audience |
|------|-----------|-------------|----------|
| **GRATIS · pin** | `5fd2a639-aec5-4caf-a3e3-a73e20b368ff` | `public/20260717_0054_intro_sfw_hoodie_sofa.mp4` | followers-and-subscribers · pinned |
| **SUB soft still** | `869a1485-b716-4802-b457-6c232254ae93` | `public/20260717_0354_nofaceid_lingerie_sofa.png` | subscribers · coll A Sofa |
| **SUB soft still** | `1e49c245-2be8-4d84-980a-39162b2a795f` | `stills/bed_lingerie.png` | subscribers · coll B Bedroom |
| **SUB soft video** | `87b211cf-7d52-45a3-a107-e47b27a47a32` | `public/20260717_0354_nofaceid_lingerie_sofa.mp4` | subscribers · coll A Sofa |

### Sacado del muro (estaba mal de tier; no se re-publica al wall)
Hard free wall + video hard en sub — **soft-deleted** en el control de daños anterior. **Bien para la escalera**: hard no va al muro.
Paths en Extra listos para **PPV por DM** (no wall posts):

| Set | Paths (FaceID original + nofaceid) |
|-----|-------------------------------------|
| sofa window | `nsfw/20260717_0116_01_nude_sofa_window{.png,.mp4,_nofaceid.png,_nofaceid.mp4}` |
| bed sheets | `nsfw/20260717_0116_02_bed_sheets{.png,_nofaceid.png}` |
| mirror | `nsfw/20260717_0116_03_mirror_selfie{.png,_nofaceid.png}` |
| kneeling | `nsfw/20260717_0116_04_kneeling_close{.png,_nofaceid.png}` |
| intro nude | `vault/fanvue/20260716_2306_intro_nude_sofa_01{_nofaceid}.{png,mp4}` |
| **Batch A–D 0545** | `nsfw/collections/{A_sofa_window,B_bedroom,C_mirror,D_shower}/{stills,videos}/` · 36 stills FaceID + ~35 mp4 · hard → **solo PPV DM** |

### Pod
- `comfyui-luz-h200` **EXITED** (no facturando).

### Next (cuando digan)
- [ ] Más soft al muro sub (volumen/constancia)
- [ ] Primer pack PPV hard por DM (pricing $5–12 / $8–20) desde vault 0116 o A01
- [ ] No auto-publicar A–H hard al muro — solo vault + DM
- [ ] X bio + sensitive media (Jorge)
- [ ] Banner mid-body web manual si aún no subido

---

## Estado 2026-07-17 madrugada (TG Jorge + Brisa) — histórico

### Audience (regla operativa — SUPERSEDED por escalera de la tarde)
| Nivel | Audience API | Contenido |
|-------|--------------|-----------|
| Discovery público | avatar / banner / intro perfil | **SFW only** |
| ~~Soft free hard~~ | ~~followers free nudes~~ | **NO** — hard no en free |
| Soft sub | `subscribers` | lingerie / soft |
| Hard | **PPV DM** | no muro |

### Posts free ya publicados (MCP) — histórico
- Pinned intro SFW: `5fd2a639-…` (sigue live)
- Soft free stills hard (4) + video hard: **deleted** → material en vault PPV

### Collections Fanvue (MCP `create_collection`, 17/7)
| Label | UUID |
|-------|------|
| A · Sofa Window | `07959922-66da-488c-b86b-968a5b83b4c6` |
| B · Bedroom | `9e652279-a010-48a1-813f-9ac358115ac3` |
| C · Mirror | `46d50cd9-be27-4765-9e64-2e942b1c154e` |
| D · Shower | `24992a4e-0f5e-4889-af71-c7a1690fe168` |
| E · Kitchen | `a14dc0e6-90a6-4ea0-b73b-81b038ee73c1` |
| F · Desk | `0f38efe9-778c-43d1-b55d-da00368b7a14` |
| G · Floor | `31271bf0-9b47-4652-baf0-26805d1f19d8` |
| H · Night | `1f1c2bd1-c48a-40fa-b2ff-8c42e329c483` |

JSON local: `/Volumes/Extra/photos/brisa_prod/vault/fanvue/nsfw/collections/fanvue_collection_uuids.json`

### Batch overnight hard A–D (gen) — ops 17/7 TG
- Stamp `20260717_0545` · FaceID · pull Extra mañana 17/7: **A10/B10/C10/D6 stills + D5 videos** (~35/80); E–H no gen en ese pull
- Resume mismo día: pin `STAMP=20260717_0545` en `brisa_collections_ah_faceid.py` + skip por path existente; cron `faceid-batch-watch-stop` (cada 30m sync+stop) **creado y removido** por Jorge (“Stop reminder FaceID”) — no re-armar sin pedido
- Output: `…/vault/fanvue/nsfw/collections/{A..D}/{stills,videos}/`
- **Uso post-v2:** vault histórico (cara vieja) — **no** relanzamiento visual; hard nunca al muro sub

### Specs perfil
- Avatar: 1080×1080 (help Fanvue)
- Banner: **1192×335** (no face-only; mid-body) — relanzamiento v2 solo Jorge+Claudio
- MCP: lee/posts/collections OK; **no** set bio/avatar/banner (REST profile write 401 con scopes MCP)
