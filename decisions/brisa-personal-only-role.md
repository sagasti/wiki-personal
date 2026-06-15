# Brisa → Solo Asistente Personal

**Fecha**: 2026-06-12
**Estado**: En progreso (transición gradual)

## Decisión

Jorge decidió que Brisa pasa a ser **exclusivamente asistente personal**. Lo laboral (OpenPass, Jira, calendar trabajo, reuniones 💼) se delega a **Cacho**, otro agente Hermes con perfil separado.

## Contexto

- Jorge tiene otros agentes para lo laboral — Brisa no necesita redundar
- La wiki no se toca (otros agentes la usan)
- Solo se saca de **memoria** (MEMORY.md) lo laboral, no de la wiki
- Transición gradual: "pasitos de bebé", de a uno

## Qué cambia

### Brisa (personal)
- Calendario: solo `jorge@sagasti.com`
- News interests: sigue siendo de Brisa (contenido personal)
- Morning brief: solo clima, noticias, eventos 🏠
- Wiki: lectura/escritura (compartido)

### Cacho (laboral)
- Calendario: solo `jorge@openpass.com.ar`
- Morning brief: reuniones 💼, Jira IYD
- Reunion prep + 15min alert: solo eventos laborales
- Kibana token refresh
- Se arregla solo para hacer lo que se le pide (sin scripts pre-hechos)

## Pendiente

- [ ] Crear/configurar perfil Cacho en Hermes
- [ ] Brisa: pausar cron jobs laborales cuando Cacho esté andando
- [ ] Brisa: ajustar scripts calendar para solo ver sagasti.com
- [ ] MEMORY.md: limpiar entries laborales de Brisa
- [ ] USER.md: actualizar rol de Brisa

## Prompts para Cacho (definidos)

1. ~~**Work Morning Brief**~~ — **ELIMINADO** (2026-06-13): Jorge decidió que no lo necesita.

2. ~~**Reunion Prep**~~ — **ELIMINADO** (2026-06-13): Jorge decidió que no lo necesita.

3. ~~**Reunion 15min Alert**~~ — **ELIMINADO** (2026-06-13): Jorge decidió que no lo necesita.

4. ~~**Kibana Token Refresh**~~ — **ELIMINADO** (2026-06-13): Brisa no accede a Kibana.

## Tags

#decision #hermes #agent-roles #personal-vs-work #cacho
