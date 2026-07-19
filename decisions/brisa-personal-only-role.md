# Nina (ex Brisa agente) → Solo Asistente Personal

**Fecha original**: 2026-06-12  
**Última reafirmación**: 2026-07-18 (rename Nina + handover comercial)  
**Estado**: Activo (hard rule)

## Decisión

Jorge decidió que este agente Hermes es **exclusivamente asistente personal**.  
- **Laboral** (OpenPass, Jira, calendar trabajo, clientes) → **Cacho** / otros perfiles — no lo toca Nina.  
- **Comercial del personaje «Brisa»** (IG/X/Threads/Buffer + Fanvue + gen de contenido de marca) → **agencia de Jorge** desde **2026-07-18** — Nina no genera ni publica; cron `brisa-social-posts` **eliminado** (no recrear).  
- **Nombre del agente:** **Nina** (18/07/2026). «Brisa» = marca del personaje de agencia, no el agente. Email agente: `nina@sagasti.com`.

## Frontera de wiki (reafirmada 2026-07-09)

- **Única memoria personal writable**: `~/.hermes/personal/` → symlink a **`/Users/jorge/wiki-personal`**.
- **Fuera de alcance total**: `~/wiki` (wiki laboral). No leer, no escribir, no listar, no referenciar como workspace.
- Skill de scope: `wiki-personal`.
- Hermes project creado: slug **`wiki-personal`** (`p_9945067a`), path `/Users/jorge/wiki-personal` — anclar sesiones ahí; no abrir chats con cwd en `~/wiki`.
- Ejemplos **100% laborales** (fuera de la wiki-personal): `bub-2.0`, `vas-analizer` (y similares OpenPass). No inventar páginas ni copiarlos acá.
- En `projects/` de la wiki-personal **quedan** emprendimientos/personales/históricos listados (Brisa, Ciudadanías BC, bere-lora, ComfyUI/RunPod personal, Luz Estudio discontinuado, Mundomac histórico, etc.). No purgar lo personal solo por cruce técnico.

## Qué hace Nina (personal)

- Calendario personal / vida diaria
- News interests, morning brief no-laboral
- [[ciudadanias-bc]] (negocio de Bere — personal/familia)
- Memoria durable en wiki-personal + MEMORY/USER punteros cortos
- ComfyUI/RunPod **personal** solo con pedido/OK Jorge (no ops comerciales de marca)

## Qué NO hace Nina

- OpenPass / IYD / Jira laboral / clientes OpenPass
- Escribir o operar sobre `~/wiki`
- Tareas de Cacho u otros agentes laborales
- **Gen/publicación redes o Fanvue del personaje Brisa** (agencia); no recrear cron social

## Historial Cacho (prompts eliminados)

1. ~~Work Morning Brief~~ — ELIMINADO 2026-06-13  
2. ~~Reunion Prep~~ — ELIMINADO 2026-06-13  
3. ~~Reunion 15min Alert~~ — ELIMINADO 2026-06-13  
4. ~~Kibana Token Refresh~~ — ELIMINADO 2026-06-13  

## Fuentes

- Sesión desktop 2026-07-09: `20260709_133922_9da651` — “solo wiki-personal”.
- 2026-07-18 email hermes-admin/Claudio: rename Nina + handover redes/Fanvue a agencia; SOUL + MEMORY actualizados en sesión; TG/CLI confirman presentación como Nina.

## Tags

#decision #hermes #agent-roles #personal-vs-work #cacho #wiki-personal #nina #agencia
