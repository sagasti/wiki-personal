---
title: "luz.center — Infraestructura / Hosting"
created: "2026-05-22"
updated: "2026-05-22"
type: concept
tags: ["#infra", "#luz-estudio", "#hosting", "#cloudflare", "#hetzner"]
related: [[Luz Estudio]]
confidence: high
---

# luz.center — Mapa de hosting

Datos verificados 2026-05-22 vía Cloudflare API + lookups (ipinfo).

## DNS / Proxy
- **Todo el DNS en Cloudflare** — zone `e72cb4b19118a3635d6a3f07ed6006f5`.
- Cloudflare API token + account en `dev/luz-estudio/.secrets/credentials.md`.
- Todos los records **proxied** (naranja).
- Email lockdown: SPF `v=spf1 -all`, DMARC `p=reject; sp=reject`. El dominio NO manda mail.

## Subdominios y dónde vive cada uno

| Subdominio | Hosting | IP / target | Qué corre |
|---|---|---|---|
| `luz.center` (apex) + `www` | **Squarespace** (AS53831) | 198.49.23.144/145, 198.185.159.144/145 + CNAME `ext-sq.squarespace.com` | Sitio web público / landing |
| `comfi-ui.luz.center` | **RunPod** (Cloudflare Tunnel) | CNAME `774947e9-3a06-41f3-a750-7cd19a203481.cfargotunnel.com` | ComfyUI (pod H200 efímero) |
| `api.luz.center` | **Hetzner** VPS | `178.104.161.171` | API (responde `404 page not found` plain → server Go/proxy; rutas públicas no obvias) |
| `n8n.luz.center` | **Hetzner** VPS (mismo) | `178.104.161.171` | n8n (workflow automation, UI 200 OK) |

## El VPS Hetzner (único server fijo 24/7)

Datos de la **Hetzner Cloud API** (token en `dev/luz-estudio/.secrets/` — NO acá).

- **Nombre**: `luz-prod-01` (server id `127208977`, label `project=luz`)
- **Tipo**: **CPX22** — 2 vCPU (shared, AMD x86), 4 GB RAM, 80 GB disk
- **IP**: `178.104.161.171` · IPv6 `2a01:4f8:1c18:c88b::/64`
- **Reverse DNS**: `static.171.161.104.178.clients.your-server.de`
- **OS**: Ubuntu 24.04
- **DC**: `nbg1-dc3` — Nürnberg, Alemania 🇩🇪
- **Creado**: 2026-04-17
- **Costo**: **€9.49/mes** gross (€0.0152/h) — incluye backups
- **Backups**: ON (window 22-02 UTC)
- **Volumes extra**: ninguno · **Snapshots**: 0
- **Hospeda**: `api.luz.center` (API, responde 404 plain → Go/proxy) + `n8n.luz.center` (n8n UI)

### ⚠️ Observación seguridad
- **Hetzner firewall: 0 reglas**. La protección HTTP viene solo del proxy Cloudflare. Pero la IP origin (`178.104.161.171`) está **expuesta en DNS** (los A records de api/n8n apuntan directo) → alguien que la tenga puede bypassear Cloudflare y pegarle directo al VPS. Considerar: firewall Hetzner que solo permita IPs de Cloudflare en 80/443 + SSH restringido.

### PENDIENTE (requiere SSH, no Cloud API)
Falta inventariar lo de adentro: qué corre en docker, versión de n8n, qué es exactamente la API de `api.luz.center`, qué workflows tiene el n8n. La Cloud API no ve el contenido del server.

## Notas
- La web (Squarespace) y ComfyUI (RunPod) NO requieren server propio. El único gasto fijo de infra es el VPS Hetzner (+ el dominio + Cloudflare free).
- ComfyUI es efímero: el pod RunPod se prende/apaga; el tunnel `comfyui-runpod` (ID `774947e9-3a06-41f3-a750-7cd19a203481`) mantiene la URL estable `comfi-ui.luz.center`.

## ACTUALIZACIÓN 2026-05-31 — Infra IyD toma el VPS + suma Ciudadanías BC

Jorge transfirió el manejo del VPS Hetzner a la sesión **Infra IyD** (vía agent-bus). SSH OK (keys de Jorge ya autorizadas, fingerprint `8a:47:f2...`). Creds Hetzner en `~/.claude/secrets/hetzner-luz.env`.

### Nuevo vhost: admin.ciudadaniasbc.com (app de Ciudadanías BC)
- App FastAPI (uvicorn :8000) en `/opt/ciudadanias-bc/` (compose separado, red `luz_default`, labels Traefik, cert LE `le`).
- Deploy: rsync de `~/dev/ciudadanias_bc` (código + data/ciudadanias.db de prueba + .env). Build local en el VPS.
- LIVE con cert LE válido. `/solicitud` (público) + `/panel` (admin Bere, login).
- Re-deploy: editar en `~/dev/ciudadanias_bc` → rsync + `docker compose up -d --build` en `/opt/ciudadanias-bc/`.

### ⚠️ GOTCHA DNS: ciudadaniasbc.com está en Squarespace, NO Cloudflare
- NS = `ns-cloud-*.googledomains.com` (Squarespace heredó Google Domains).
- **Squarespace NO tiene API de DNS ni DDNS** (Google lo discontinuó al migrar). El endpoint `domains.google.com/nic/update` da 301. La "app password" generada NO sirve para records por API.
- Records se editan SOLO a mano en el panel de Squarespace. El A record `admin → 178.104.161.171` lo creó Jorge manual.
- Si se quiere manejo programático del DNS de ciudadaniasbc.com → migrar a Cloudflare (cambiar NS). Pendiente/opcional.

### ⚠️ Seguridad firewall — pendiente (matizado)
El firewall Hetzner sigue en 0 reglas. PERO el plan "Cloudflare-only en 80/443" ya NO aplica simple: `ciudadaniasbc.com` va DIRECTO al VPS (sin proxy Cloudflare), así que 443 debe aceptar cualquier IP para ese vhost. Opciones: (a) migrar ciudadaniasbc.com a Cloudflare también → firewall Cloudflare-only protege todo; (b) restringir solo SSH (puerto 22) a IP de Jorge + aceptar el riesgo bajo de Cloudflare-bypass en luz.center. DECISIÓN JORGE 2026-05-31: opción (b) — dejar el firewall como está (0 reglas). Riesgo aceptado por bajo: n8n tiene basic auth, SSH es key-only, la app de Ciudadanías tiene login propio en /panel. NO migrar ciudadaniasbc.com a Cloudflare por ahora. Revisitar si en el futuro se suman vhosts sin auth propia.

## ACTUALIZACIÓN 2026-06-09 — Luz Estudio DISCONTINUADO → teardown de lo de Luz en el VPS

Jorge **terminó el negocio Luz Estudio**. Se baja todo lo específico de Luz del VPS `luz-prod-01`. El
workspace CC `~/dev/luz-estudio` se renombró a `~/dev/comfy-ui` (agente acotado a administrar ComfyUI).

**Tarea para `infra`** (dueña del VPS): teardown **quirúrgico** de los containers de Luz:
- `api.luz.center` (Go API) y `n8n.luz.center` (n8n) → candidatos a borrar.
- **El bot que dispara mensajes a Telegram de "Luz Studio"** casi seguro es un **workflow del n8n** → al
  bajar n8n (o ese workflow) se apaga el bot.
- Records DNS Cloudflare de `api`/`comfi-ui`/`n8n` → limpiar tras confirmar baja.

⚠️ **NO TOCAR `admin.ciudadaniasbc.com`** (app FastAPI LIVE de Bere, `/opt/ciudadanias-bc/`, compose
propio, cert LE) — vive en el MISMO box y **sigue activa**. El VPS NO se mata (Ciudadanías lo necesita),
solo se remueven los containers/records de Luz. Opción futura: si Ciudadanías migra a otro lado, recién
ahí se podría matar el VPS (€9.49/mes).

**Pendiente previo (sigue válido)**: inventariar `docker ps` del box antes de borrar (la Cloud API no ve
el contenido). Brief enviado a `infra` por el agent-bus 2026-06-09; espera inventario + OK de Jorge.

## INVENTARIO INTERNO 2026-06-09 (read-only, infra) — pre-teardown

Resuelto el PENDIENTE "inventariar lo de adentro". `docker ps -a` en luz-prod-01:

| Container | Project | Qué es | Teardown |
|---|---|---|---|
| `luz-n8n-1` | luz | n8n (n8n.luz.center), 1 workflow | 🔴 borrar |
| `luz-postgres-1` | luz | DB n8n (db `luz`, user `luz`) | 🔴 borrar |
| `luz-redis-1` | luz | cache n8n | 🔴 borrar |
| `luz-traefik-1` | luz | reverse-proxy + ACME `le` | 🟢 **PRESERVAR** |
| `ciudadanias-bc` | ciudadanias-bc | app FastAPI Bere LIVE | 🟢 preservar |

Compose: `/opt/luz/docker-compose.yml` (traefik+postgres+redis+n8n) y `/opt/ciudadanias-bc/docker-compose.yml` (app).

### ⚠️⚠️ ACOPLAMIENTO CRÍTICO — el Traefik y la red NO son "de Luz" en uso
`ciudadanias-bc` está en la red **`luz_default`** y es ruteado por **`luz-traefik-1`** (router `ciudadanias`,
`Host(admin.ciudadaniasbc.com)`, cert LE `le` en `/opt/luz/traefik/acme.json`). El compose de Ciudadanías
declara `luz_default` como **external**. **Por eso NUNCA hay que hacer `docker compose -p luz down`** —
borraría la red + el Traefik y **Ciudadanías cae** (pierde ruteo + SSL).

**Teardown quirúrgico correcto** (post-OK Jorge):
```
docker compose -p luz rm -s -v n8n postgres redis     # baja SOLO la pila n8n
docker volume rm luz_postgres_data luz_redis_data      # + data n8n
# luz-traefik-1 y red luz_default quedan vivos para Ciudadanías
```
Opción futura más limpia: dar a Ciudadanías su propio Traefik+red y renombrar fuera del namespace `luz`.

### Bot Telegram "Luz Studio"
n8n = **1 solo workflow activo**: `Supervisor - Saludo Diario` (id `J8yyYERu9Q8ma3Gq`), con nodos Telegram
(bot token `8789593906:...` en comfy-ui/.secrets, chat_id 1808182714). Se apaga al bajar n8n.

### DNS a limpiar (zone luz.center, Cloudflare)
`A api.luz.center` (→VPS, sin backend, 404 default de Traefik), `A n8n.luz.center` (→VPS),
`CNAME comfi-ui.luz.center` (→RunPod tunnel). **Preservar**: apex `luz.center` + `www` (Squarespace, web
pública — decisión Jorge si se baja), `_domainconnect`, `_dmarc`/`_domainkey`/spf (email lockdown).

**Estado**: inventario pasado al orchestrator por el bus + mostrado a Jorge en sesión interactiva
2026-06-09. Esperando OK de Jorge (confirmar teardown + decidir si baja la web Squarespace) antes de ejecutar.

## ✅ TEARDOWN EJECUTADO 2026-06-09 (infra, OK Jorge en sesión interactiva)

Hecho. Resumen de lo ejecutado:

**Backups primero** → `/root/luz-teardown-backup-20260609/` (en el box) + copia en local
`~/dev/comfy-ui/luz-teardown-backup-20260609/`: `luz-workflows.json` (1 workflow), `luz-pg.sql`
(dump 322KB), `n8n-data.tgz` (incluye N8N_ENCRYPTION_KEY), `luz.env`.

**Borrado:** containers `luz-n8n-1`/`luz-postgres-1`/`luz-redis-1` (`docker compose -p luz rm -s -v`) +
volumes `luz_postgres_data`/`luz_redis_data` + bind dirs `/opt/luz/n8n-data` y `/opt/luz/postgres-init`.
`/opt/luz/docker-compose.yml` reducido a **solo traefik** (original en `.bak-pre-teardown-20260609`).
Bot Telegram "Luz Studio" (workflow `Supervisor - Saludo Diario`) apagado al bajar n8n.

**DNS Cloudflare borrados:** `A api`, `A n8n`, `CNAME comfi-ui`, `A luz.center` apex (x4, web Squarespace —
Jorge decidió bajar la web también), `CNAME www`. **Preservados:** TXT spf/dmarc/dkim + `_domainconnect`.
Verificado contra 1.1.1.1: los 5 nombres → 0 records.

**Preservado intacto:** `luz-traefik-1` + red `luz_default` + `/opt/luz/traefik/acme.json` + app
**Ciudadanías BC** (`admin.ciudadaniasbc.com` verificado HTTP 307 OK post-teardown). El VPS sigue vivo
(€9.49/mes) porque Ciudadanías lo necesita.

**Pendientes NO-infra (Jorge):** cancelar la suscripción Squarespace (la web/dominio facturan aparte; el
DNS lo bajé pero el plan Squarespace no). El `comfy-ui` agent puede limpiar el cloudflared tunnel de
`comfi-ui` si quiere. **Deuda técnica:** el traefik + red siguen con namespace `luz` pero ahora son infra
de Ciudadanías; a futuro conviene darle a Ciudadanías su propio traefik+red y renombrar fuera de `luz`.

## ✅ RENAME traefik+red → ciudadanias-bc (2026-06-09, mismo día)

Resuelta la deuda técnica del teardown. El traefik + red ya NO tienen namespace `luz`:
- Consolidé el `traefik` DENTRO del proyecto `ciudadanias-bc` (`/opt/ciudadanias-bc/docker-compose.yml`
  ahora tiene 2 services: `app` + `traefik`).
- Red `luz_default` → **`ciudadanias-bc_default`**. Container `luz-traefik-1` → **`ciudadanias-bc-traefik-1`**.
- `acme.json` copiado de `/opt/luz/traefik/` → `/opt/ciudadanias-bc/traefik/` (cert LE **reusado**, no
  re-emitido — issuer Let's Encrypt, válido hasta Aug 29 2026).
- `/opt/luz` **eliminado** por completo. El box ahora solo corre `ciudadanias-bc` + su traefik.
- Switchover con ~15s downtime (down traefik viejo → down app → rm red vieja → up app+traefik nuevos).
  Verificado HTTP 307 OK post-rename. Backup compose: `docker-compose.yml.bak-pre-rename-20260609`.

**Estado del box luz-prod-01 ahora:** un solo proyecto `ciudadanias-bc` (app FastAPI + traefik propio +
red propia). Nada referencia "luz". El VPS Hetzner sigue (Ciudadanías). DNS de Luz ya borrados (ver arriba).

## CIERRE 2026-06-09 — pendientes no-infra resueltos por Jorge
- **Suscripción Squarespace CANCELADA** (web/dominio `luz.center` ya no facturan).
- **Tunnel cloudflared `comfi-ui` (RunPod) limpiado** (estaba huérfano tras borrar su DNS).
- Deuda técnica traefik/red namespaced `luz` → **ya resuelta** por infra en el mismo teardown (Ciudadanías
  con traefik+red propios, `/opt/luz` eliminado). **Teardown de Luz Estudio 100% cerrado.**
