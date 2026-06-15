---
title: "Browser Harness"
created: "2026-05-06"
updated: "2026-05-06"
type: "concept"
tags: ["#tool", "#browser-automation", "#cdp", "#agent"]
sources: []
hermes_session: "20260506_195623_2c8829"
confidence: "medium"
---

# Browser Harness

## Qué es
[Browser Harness](https://github.com/browser-use/browser-harness) — arnés minimalista (~1k líneas) que conecta un LLM directamente a Chrome real vía CDP (Chrome DevTools Protocol). Un solo websocket, nada en el medio. Del equipo de **browser-use**.

## Instalación
- **Repo**: `/Users/jorge/dev/browser-harness`
- **Instalado con**: `uv tool install -e .` (editable, apunta al repo)
- **Comando**: `browser-harness` (global en `$PATH`)
- **Versión**: 0.1.0 (git)

## Estado actual
- ✅ Instalado y en PATH
- ❌ Daemon no conectado a Chrome (falta habilitar remote debugging)
- ❌ Cloud browsers no configurados (BROWSER_USE_API_KEY no set)

## Para conectar a Chrome
1. En Chrome, navegar a `chrome://inspect/#remote-debugging`
2. Tildar "Allow remote debugging for this browser instance"
3. En Chrome 144+, clickear "Allow" en el popup
4. Verificar: `browser-harness -c 'print(page_info())'`

## Arquitectura
```
Chrome → CDP WS → browser_harness.daemon → IPC → browser_harness.run
```
- Protocolo: una línea JSON por dirección
- IPC: Unix socket en `/tmp/bu-<NAME>.sock`
- Archivos core: `admin.py`, `daemon.py`, `helpers.py`, `run.py`

## Conceptos clave
- **Self-healing**: el agente escribe helpers nuevos durante ejecución en `agent-workspace/agent_helpers.py`
- **Domain skills**: playbooks por sitio (LinkedIn, Amazon, GitHub…) en `agent-workspace/domain-skills/`, se activan con `BH_DOMAIN_SKILLS=1`
- **Screenshots first**: `capture_screenshot()` → `click_at_xy(x, y)` → verificar. No buscar selectores.
- **Bulk HTTP**: `http_get(url)` + ThreadPoolExecutor para páginas estáticas (sin browser)

## Comandos útiles
- `browser-harness --doctor` — diagnóstico
- `browser-harness --update -y` — actualizar
- `browser-harness -c 'print(page_info())'` — test conexión
- `browser-harness -c 'new_tab("https://example.com"); wait_for_load(); print(page_info())'` — uso básico

## Cloud browsers (opcional)
- Key: `BROWSER_USE_API_KEY` desde [cloud.browser-use.com/new-api-key](https://cloud.browser-use.com/new-api-key)
- Free tier: 3 browsers concurrentes, proxies, captcha solving
- `start_remote_daemon("work")` para browser remoto aislado


## Estado (actualizado)
- ✅ Instalado y en PATH
- ✅ Daemon conectado a Chrome
- ✅ 1 conexión activa
- Remote debugging habilitado en profile principal (sticky, no hay que repetir)
