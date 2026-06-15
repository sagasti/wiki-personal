---
title: "Ciudadanías BC — stack del sistema de gestión"
created: "2026-05-30"
updated: "2026-05-30"
type: "decision"
tags: ["#decision", "#ciudadanias-bc", "#bere", "#fastapi"]
related: [[ciudadanias-bc]], [[Berenice Carbajo]]
confidence: "high"
---

# Ciudadanías BC — stack del sistema de gestión

## Decisión

App **custom** (FastAPI + SQLite + Jinja2, dockerizada) en vez de una herramienta
low-code (NocoDB / Baserow / Airtable). Repo: `~/dev/ciudadanias_bc`.

## Contexto

Jorge pidió un sistema de gestión de trámites de ciudadanía para Bere y el equipo.
Requisitos: form público + panel del equipo, **auditoría** de cambios (autor + qué/cuándo),
multi-usuario, checklist de documentación, documentos en Google Drive, extensible a otros
servicios, "va a estar en la web" pero primero probar en Docker local.

## Por qué custom y no low-code

- **Google Drive**: requisito explícito. En NocoDB la integración con Drive no es nativa.
- **Web propia**: "va a estar en la web" como producto, no como una herramienta self-hosted
  embebida.
- **Modelo genealógico específico** (cadena cliente→…→ancestro español) + checklist de
  documentación con nota por doc: se modela más limpio a medida.
- **Extensibilidad controlada**: el registry (`app/registry.py`) permite sumar servicios
  sin migrar la base.
- Jorge es técnico y prefiere tener el código.

**Trade-off aceptado:** más laburo inicial que un NocoDB (que daría tablero usable en
minutos). Se mitiga con un MVP chico + código montado con `--reload` para iterar rápido.

## Decisiones de implementación

- **Sin dependencias nativas** (para que el build de Docker sea trivial): password hashing
  con `hashlib.pbkdf2_hmac` (stdlib), sesión con `itsdangerous` (SessionMiddleware).
- **SQLite** con campos JSON (`datos`, `checklist`) para lo específico del servicio →
  agregar servicios no requiere ALTER TABLE.
- **Auditoría** como tabla `audit_log` con diff `{campo: [viejo, nuevo]}`; autor
  denormalizado para sobrevivir borrado de usuarios y solicitudes del público.
- Form público + panel se renderizan dinámicamente desde el registry.

## Pendiente

Subida automática a Drive (OAuth Bere), otros servicios en el registry, hardening para web.
