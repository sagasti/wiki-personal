---
title: "Ciudadanías BC"
created: "2026-04-19"
updated: "2026-07-09"
type: "project"
tags: ["#project", "#bere", "#instagram", "#citizenship"]
related: [[Berenice Carbajo]], [[Buffer]]
---

# Ciudadanías BC

- **Qué es:** Consultora de ciudadanías y servicios consulares
- **Instagram:** @ciudadaniasbc — 4500 seguidores (comprados), 6 posts
- **Web:** ciudadaniasbc.com
- **Precio:** $600 USD ciudadanía española, 2 cuotas
- **Detalle servicio española (25/4):** Armado de carpetas para presentar en el consulado SOLO PARA PERSONAS CON IDU. IDU = Identificador de Usuario del sistema de citas del Consulado de España en Buenos Aires. PW- para pasaporte, NW- para nacionalidad. Precio pendiente de confirmar con Bere.
- **Servicios:** ciudadanías (España, Italia, Alemania, Australia, Nueva Zelanda, EE.UU.), apostillas, legalizaciones, traducciones, visados
- **Visas activas (02/5):** España (trabajo, estudio, arraigo social/familiar, emprendedor), Italia (lavoro, studio, scelta residenza, famiglia, investitore), USA (turista), Australia (skilled migration, trabajo, estudio), Nueva Zelanda (skilled migration, trabajo, estudio), Europa (Schengen, Blue Card UE, residencia permanente, ciudadanía europea)
- **Portuguesa (28/4):** Ciudadanía portuguesa añadida como servicio. Jus sanguinis (sin límite generacional, no pierde nacionalidad orig.), por matrimonio (3+ años), por residencia (5 años). Sephardíes expiró 2022. Reel en progreso (estilo premium acuarela). Precios gestoría: $400-3000 USD según complejidad.
- **Contenido Instagram (24/4):** Reels 5 slides (Hook → España → Italia → Europa → Contacto), Stories con estilo vintage/pastas para USA visa
- **Colores branding (Bere):** celeste clarito, beige, nude (confirmado por Bere en sesiones de diseño)
- **Teléfono:** 1176399809 (WhatsApp)
- **Web:** **www.ciudadaniasbc.com** (CON "s" — confirmado: prod LIVE `admin.ciudadaniasbc.com` + IG @ciudadaniasbc). ⚠️ La IA tiende a errarle: escribe "ciudadaniabc.com" (sin s) o "ciudadaniaabc" — corregir SIEMPRE. (Esta línea decía mal "ciudadaniabc.com" hasta 2026-06-14.)
- **Estrategia actual:** Reels 3-5/semana + pausa ads + foco orgánico
- **Branding visual:** fondo claro + X roja para myth-busting, acentos dorado y azul oscuro
- **Cartel diseño (Bere):** formato cuadrado (1:1), más color que blanco, bandera visible. Sin labels tipo "TELÉFONO"/"WEB" (solo valores). Iterar hasta quedar conforme.
- **Cartel portuguesa:** rojo+verde prominentes, bandera de Portugal incluida.
- **Reviews reales:** Ezequiel, Luciano, Gustavo (Highlights "Clientes ❤️")
- **LMD:** Cerró 22/10/2024 — NO mencionar como vía vigente
- **⚠️ Texto en imágenes (02/5):** Gemini Imagen tiende a escribir TRABAJÓ en vez de TRABAJÁ, ESTUDIO en vez de ESTUDIÁ. Verificar siempre antes de publicar. Post-procesar bordes blancos con terminal.
- **Logo:** isologo **BC** entrelazado + "CIUDADANÍAS" (blanco/transparente). Original en `~/wiki-personal/projects/ciudadanias-bc-logo.webp`; recoloreados (azul oscuro/dorado/rojo/carbón) en `ciudadanias-bc-logo-<color>.png` y bundleados en `comfy-ui/scripts/ideogram/assets/`. El blanco no se ve sobre fondo claro → usar azul oscuro por default.

## Generación de posts con Ideogram (Brisa, sin ComfyUI) — desde 2026-06-14

- **Qué es:** generador de posts/placas de IG por la **API directa de Ideogram v3** (`api.ideogram.ai`), sin ComfyUI/GPU/pod. Pensado para que **Brisa le haga placas a Bere**: Bere pide en lenguaje natural, Brisa mapea a flags, el script garantiza marca (layout logo-arriba, colores, voseo, dominio con "s").
- **Dónde:** `~/dev/comfy-ui/scripts/ideogram/` → `ideogram_post.py` (stdlib + Pillow) + `assets/` (logos) + `BRISA_SKILL.md` (mapeo pedido-de-Bere→comando, con ejemplos).
- **Uso:** `python3 ideogram_post.py --ciudadania italiana --extra "Desde USD 800 en 2 cuotas"` → PNG con logo BC azul oscuro arriba. Ciudadanías: espanola/italiana/portuguesa/alemana/europea. Flags: `--headline --tagline --extra --logo-color --aspect --prompt`.
- **API key:** Ideogram developer (https://ideogram.ai/manage-api), DISTINTA de comfy.org. En `IDEOGRAM_API_KEY` o `~/.config/ideogram/api_key`.
- **Gotchas:** el CDN de Ideogram rechaza el UA default de urllib (403 al bajar el PNG → mandar User-Agent de browser); validado E2E 2026-06-14 (español + italiana con oferta).
- **DEPLOYADO + E2E OK en Brisa (2026-06-14, ENABLED):** [[hermes-admin]] lo instaló como skill Hermes en `/opt/data/skills/social-media/ciudadanias-bc-ig/` (container de Brisa), clasificada PERSONAL. **Probado E2E**: Brisa generó la placa española (logo BC + voseo + ciudadaniasbc.com, 1024x1024). Pillow va al bind mount `_vendor` (`sys.path.insert` en el script) → **PERSISTE a updates/recreates** (no al venv efímero `/opt/hermes/.venv`). Key REST en `/opt/data/.env` DENTRO del container (bind-mount; se escribe con `docker exec`).
  - ⚠️ **Key gotcha**: la REST API key (ideogram.ai/manage-api, ~86 chars sin puntos) NO es el token OAuth del MCP de Ideogram (efímero, vence → 401). Para las placas se usa la REST.
  - ✅ **v2 (2026-06-14) — footer determinista**: Ideogram alucinaba el handle ("@CiudadaníasSBC", S de más). Solución: el prompt reserva franja inferior vacía y **Pillow estampa el footer** `@ciudadaniasbc · ciudadaniasbc.com` (`compose_footer`, fuente DejaVu bundleada en `assets/fonts/`). Logo (arriba) + footer (abajo) ambos por Pillow → texto de marca SIEMPRE exacto; Ideogram solo hace fondo + headline + tagline. Flags: `--footer-color`, `--no-footer`. Validado E2E en la Mac; redeploy a Brisa coordinado con [[hermes-admin]].
  - **Arquitectura (decisión Jorge 2026-06-14):** REST API → placas de marca de Bere (este script); MCP de Ideogram → imágenes generales de Brisa (aparte, lo arma [[hermes-admin]]).

## Sistema de gestión de trámites (app) — desde 2026-05-30

- **Qué es:** app web para gestionar los trámites de clientes (CRM acotado). Pedido por Jorge para Bere y el equipo de Ciudadanías BC.
- **Proyecto independiente** con su propio agente: vive en `~/dev/ciudadanias_bc`, NO depende de infra-huawei (se empezó por error desde esa sesión, pero el código siempre estuvo en su carpeta).
- **Equipo:** Bere (dueña/admin) · **Nadia** (ciudadanía española) · **Leandro** (ciudadanía italiana, cuando se agregue ese trámite). Login individual por persona, roles admin/agente.
- **Repo:** `~/dev/ciudadanias_bc` (tiene su propio `CLAUDE.md` autosuficiente). Arranca local en Docker: `docker compose up -d` → público en `localhost:8088/solicitud`, panel en `/panel`.
- **Stack:** FastAPI + SQLite + Jinja2, dockerizado, sin deps nativas. Decisión custom vs low-code en `[[ciudadanias-bc-sistema-gestion-stack]]`.
- **Dos superficies:** form **público** (el cliente carga sus datos) + **panel** del equipo con login individual.
- **Auditoría (pedido explícito de Jorge):** cada edición registra autor + fecha + qué campos cambiaron (valor anterior → nuevo). Página de auditoría global para admins. OJO terminología: Jorge dijo "autoría" pero se refería a **auditoría** (audit trail).
- **Mensajería entre usuarios:** DM directo usuario→usuario con vínculo opcional a un trámite + badge de no leídos en el nav. Pedido por Jorge el 2026-05-30.
- **Multi-usuario:** "cualquiera de Ciudadanías BC" edita. Admin (Bere) crea usuarios desde el panel. Roles admin/agente.
- **Documentación:** checklist por trámite ("marcar qué documentación ya tienen") + nota por documento. Los docs que consiguen se guardan en **Google Drive**: por ahora se guarda el **link a la carpeta**; subida automática a Drive queda para 2da iteración (requiere OAuth de la cuenta de Bere).
- **Extensibilidad:** `app/registry.py` define cada servicio (campos + checklist). Agregar portuguesa/italiana/visas = agregar una entrada, sin migrar la base. Hoy solo **española** cargada (turno, IDU, cadena genealógica hasta el ancestro español).
- **Estado:** MVP funcionando y validado E2E en Docker local (2026-05-30). "Va a estar en la web" — cuando se mueva, coordinar infra + rate-limit/captcha/HTTPS.
- **Gotcha:** testear el form con browser, no `curl -d` crudo (mojibake de encoding por falta de percent-encoding; no es bug de la app).

## Control del Docker vía agent-bus  (2026-05-31)

El server local (Docker en `~/dev/ciudadanias_bc`, puerto **8088**) se levanta/apaga/consulta por el agent-bus.

- **Hook propio:** `~/.claude/agent-bus/hooks/ciudadanias.sh` (slug `ciudadanias`), disparado por el listener `com.jorge.agent-bus-ciudadanias` ante mensajes `*_to_ciudadanias`.
- **Acciones FIJAS** (no ejecuta texto arbitrario): `start`/`stop`/`status` → `docker compose up -d` / `down` / `ps`. Responde por el bus (`ready`/`done`/`ack`).
- **Uso:** `bash ~/.claude/agent-bus/_lib/send.sh <from> ciudadanias request "start"` (o pasar la acción en el campo `model`).
- **Historia:** nació por error como lógica metida en `hooks/infra.sh` (30/05 22:53); el 31/05 se movió al hook propio y se liberó `infra.sh` (no era de [[infra-iyd]]). Backup del viejo en `/tmp/infra.sh.bak-ciudadanias-mismove`.
- **Gotcha:** `send.sh` NO valida el slug contra `AGENTS.md`, así que el `reply` funciona aunque `AGENTS.md` liste a Ciudadanías como "excluido" (inconsistencia a resolver: formalizar en el catálogo o desmontar listener+hook).

Lección de tooling asociada: [[technical-lessons]] (lag de tool-results en Claude Code).

### Git + agent-bus (2026-05-31)
- **Repo:** https://github.com/sagasti/ciudadanias-bc (rama `main`). El deploy a prod (Infra) toma el código de acá. Pusheado: sistema + hardening (commit `96f3746`) y sanitización (commit `c1a6cb3`, saca las passwords seed del CLAUDE.md).
- ⚠️ Las passwords seed quedaron en la **historia** del commit inicial `96f3746` (repo privado); se rotan en prod (checklist Infra), por eso no se reescribió historia (riesgoso con clones de Infra).
- `.gitignore` protege `.env` (SESSION_SECRET) y `data/` (DB) — NO van al repo.
- **Slug del bus: `ciudadanias-bc`** (NO `ciudadanias`). Hook `~/.claude/agent-bus/hooks/ciudadanias-bc.sh`, listener `com.jorge.agent-bus-ciudadanias-bc`. El hook ya NO responde `failed` a mensajes no-acción (evita Telegram falso a Jorge) — fix sugerido por [[infra-iyd]].

### Deploy a prod + hardening verificado E2E (2026-05-31)
- **Prod LIVE:** https://admin.ciudadaniasbc.com — deployado por [[infra-iyd]] desde `main` de GitHub (HEAD `ac8275c`). Pipeline: yo pusheo a GitHub → Infra redeploya (no toco prod directo).
- **Verificado E2E contra prod (Claudio):**
  - ✅ Cookie de sesión: `Secure; HttpOnly; SameSite=lax` (COOKIE_SECURE=1 aplicado)
  - ✅ Security headers nginx: HSTS, X-Frame-Options, X-Content-Type-Options
  - ⚠️ Passwords seed NO rotadas: `bere1234` todavía loguea en prod (HTTP 303). Son públicas (estuvieron en el repo) → PENDIENTE CRÍTICO: rotar ya (la app permite cambio self-service /panel/perfil + reset admin).
  - ✅ Código nuevo live: campo "Año del IDU" + labels de docs corregidos
- **No verificable desde afuera (lado Infra, asumir según checklist):** valor de SESSION_SECRET, rate-limit en /solicitud, backup del SQLite de prod.
- **Gotcha:** al 2026-05-31 prod TODAVÍA usa las passwords seed (bere1234/nadia1234) — verificar si ya se rotaron antes de asumir nada.

## Calidad de avisos / vs ChatGPT (2026-07-09)

- Jorge reenvió feedback de Bere: venía pensando en usar ChatGPT para avisos porque “los hace mejor / más de diseño / distintos al resto de la ciudad”.
- Brisa reaccionó actualizando el pipeline de placas (skill `ciudadanias-bc-ig` + estilo editorial) y mandó a WhatsApp **CIUDADANÍAS BC** dos muestras 9:16:
  - italiana (`ciudadaniasbc_pitch_italiana_20260709.png`)
  - española (`ciudadaniasbc_pitch_espanola_20260709.png`, logo dorado)
- Dirección visual: card elevada, gradiente con profundidad, vibe luxury magazine; logo/footer Pillow exactos; voseo **Tramitá**; `--magic OFF`.
- Pendiente: feedback de Bere (qué le gusta / no / ejemplo de ChatGPT a igualar o superar). Ver [[ciudadanias-bc-cartel-design-pipeline]].
