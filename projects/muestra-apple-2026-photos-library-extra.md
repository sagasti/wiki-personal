# Photos Library → /Volumes/Extra (2026-07-13)

## Hecho por Brisa
- Cerrada app **Photos**.
- Copia bit-a-bit con `ditto` (exit 0):
  - **Origen (backup):** `/Users/jorge/Pictures/Photos Library.photoslibrary` (~29 GB)
  - **Nueva:** `/Volumes/Extra/downloads/Photos/Photos Library.photoslibrary` (~29 GB)
- Apertura: `open -a Photos "/Volumes/Extra/downloads/Photos/Photos Library.photoslibrary"`
- `lsof` confirma que **Photos** tiene abierta la DB de **Extra**.
- Raíz de Extra es **root:wheel** (no se pudo crear `/Volumes/Extra/Photos` sin sudo password) → quedó bajo `downloads/Photos` (escribible por jorge).

## Te falta a vos (1 minuto en la Mac)

1. En **Fotos** (ya debería mostrar la lib de Extra):
2. **Fotos → Ajustes…** (o Preferencias) → pestaña **General**.
3. Clic en **Usar como Librería de fotos del sistema** / **Use as System Photo Library**.
4. (Recomendado) dejá **Fotos de iCloud** activado; cuando termine de asentar, ahí sí podés valorar quitar optimización en el **disco interno** porque la lib vive afuera.

### Que la próxima máquina arranque en Extra
- Mantené el disco **Extra** enchufado al login.
- Opcional: al abrir Fotos con **Option** apretado, elegí siempre la de Extra hasta que quede System Library.

### Liberar espacio del interno (solo cuando confirmes)
Cuando veas bien caras/iCloud en Extra y System Photo Library seteada:

```bash
# NO borrar todavía — opcional: renombrar el backup
mv "/Users/jorge/Pictures/Photos Library.photoslibrary" \
   "/Users/jorge/Pictures/Photos Library.photoslibrary.BACKUP-$(date +%Y%m%d)"
```

Solo **trash**/borrar el BACKUP cuando confirmes que Extra + iCloud están OK **varios días**.

### Acceso a subcarpeta limpia (opcional)
Si preferís `/Volumes/Extra/Photos/...` en vez de `downloads/Photos`:

```bash
sudo mkdir -p /Volumes/Extra/Photos
sudo chown jorge:staff /Volumes/Extra/Photos
# luego mover el package y reabrir
```

## Notas
- Dispositivo: USB APFS “Extra”, ~1.9 TB libres.
- No se tocó “Optimizar en la Mac” automáticamente.
- Accessibility bloqueó automatizar keystrokes a Photos (`osascript is not allowed to send keystrokes`).

## Verif
```bash
lsof -c Photos | rg 'Photos Library.photoslibrary/database/Photos.sqlite'
# debería listar path under /Volumes/Extra/...
du -sh "/Volumes/Extra/downloads/Photos/Photos Library.photoslibrary"
```
