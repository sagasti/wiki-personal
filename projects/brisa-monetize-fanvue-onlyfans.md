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
4. Watermark suave en packs duros: `AI · @brisa_sagasti` (opcional pero safe).
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
