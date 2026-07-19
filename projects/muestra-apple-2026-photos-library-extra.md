---
title: "Photos Library → /Volumes/Extra"
created: "2026-07-13"
updated: "2026-07-19"
type: "project"
tags: ["#apple", "#photos", "#ops"]
related: [[muestra-apple-2026-charla]], [[osxphotos-tool-for-apple-photos]]
---

# Photos Library → /Volumes/Extra (2026-07-13)

## Estado final (verificado)

| Pieza | Path / valor |
|--------|----------------|
| **System Photo Library (CPL)** | `/Volumes/Extra/photos/Photos Library.photoslibrary` |
| **Modo iCloud** | Sync **sin optimizar** (originales en el disco de la lib = Extra) |
| **Fotos UI** | Abierta sobre Extra (sqlite en Extra) |
| **cloudphotod SystemLibrary** | `clientLibraryBasePath` → Extra `…/resources/cpl/cloudsync.noindex` |
| **Backup viejo (Pictures)** | `/Users/jorge/Pictures/Photos Library.photoslibrary` (~18 GB residual, bajando de 29 GB) |

## Hecho

1. Copia `ditto` de la lib a Extra.
2. Path final: **`/Volumes/Extra/photos/Photos Library.photoslibrary`** (no `downloads/Photos`).
3. Jorge marcó **System Photo Library** + **sincronizar sin optimizar**.
4. Free en interno: ~**29 GB** libres en `/` al momento del check post-cambio.

## Qué esperar ahora

- Descarga de **originales** a Extra: puede tardar **mucho** (depende del tamaño real en iCloud). Disco Extra ~1.9 TB libres.
- Personas/caras del iPhone deberían **pegar mejor** con originales locales.
- `photolibraryd` puede seguir mirando Pictures un rato: residual, no es la System Library de iCloud.

## NO hacer todavía

- **No borrar** `~/Pictures/Photos Library.photoslibrary` hoy.
- Esperar **1–2 días** de sync estable con Extra enchufado.
- Luego renombrar a `.BACKUP-YYYYMMDD` y, si todo OK, `trash`.

## Checklist post-sync

```bash
defaults read com.apple.cloudphotod | rg -A5 'CPLEngineParameters-SystemLibrary'
lsof -c Photos | rg 'Extra/photos/Photos Library'
du -sh "/Volumes/Extra/photos/Photos Library.photoslibrary"
```

## Extra tiene que estar montado

Si arrancás sin Extra, Fotos se va a quejar o no abre la System Library.
