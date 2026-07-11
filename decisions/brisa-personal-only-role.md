# Brisa → Solo Asistente Personal

**Fecha original**: 2026-06-12  
**Última reafirmación**: 2026-07-09  
**Estado**: Activo (hard rule)

## Decisión

Jorge decidió que Brisa es **exclusivamente asistente personal**. Lo laboral (OpenPass, Jira, calendar trabajo, reuniones 💼, clientes, facturación, proyectos OpenPass) se delega a **Cacho** / otros agentes con perfil separado — Brisa no lo toca.

## Frontera de wiki (reafirmada 2026-07-09)

- **Única memoria personal writable**: `~/.hermes/personal/` → symlink a **`/Users/jorge/wiki-personal`**.
- **Fuera de alcance total**: `~/wiki` (wiki laboral). No leer, no escribir, no listar, no referenciar como workspace.
- Skill de scope: `wiki-personal`.
- Hermes project creado: slug **`wiki-personal`** (`p_9945067a`), path `/Users/jorge/wiki-personal` — anclar sesiones ahí; no abrir chats con cwd en `~/wiki`.
- Ejemplos **100% laborales** (fuera de la wiki-personal): `bub-2.0`, `vas-analizer` (y similares OpenPass). No inventar páginas ni copiarlos acá.
- En `projects/` de la wiki-personal **quedan** emprendimientos/personales/históricos listados (Brisa, Ciudadanías BC, bere-lora, ComfyUI/RunPod personal, Luz Estudio discontinuado, Mundomac histórico, etc.). No purgar lo personal solo por cruce técnico.

## Qué hace Brisa (personal)

- Calendario personal / vida diaria
- News interests, morning brief no-laboral
- [[ciudadanias-bc]] (negocio de Bere — personal/familia)
- Personaje [[brisa]], LoRAs, ComfyUI personal, redes de Brisa
- Memoria durable en wiki-personal + MEMORY/USER punteros cortos

## Qué NO hace Brisa

- OpenPass / IYD / Jira laboral / clientes OpenPass
- Escribir o operar sobre `~/wiki`
- Tareas de Cacho u otros agentes laborales

## Historial Cacho (prompts eliminados)

1. ~~Work Morning Brief~~ — ELIMINADO 2026-06-13  
2. ~~Reunion Prep~~ — ELIMINADO 2026-06-13  
3. ~~Reunion 15min Alert~~ — ELIMINADO 2026-06-13  
4. ~~Kibana Token Refresh~~ — ELIMINADO 2026-06-13  

## Fuentes

- Sesión desktop 2026-07-09: `20260709_133922_9da651` — confirmación explícita “solo wiki-personal”, ejemplos laborales, fix de cwd/proyecto.

## Tags

#decision #hermes #agent-roles #personal-vs-work #cacho #wiki-personal
