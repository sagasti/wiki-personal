---
title: "osxphotos tool for Apple Photos"
created: "2026-05-02"
updated: "2026-05-02"
type: "project"
tags: ["#osxphotos", "#apple-photos", "#tool", "#mac", "#cli"]
sources: ["hermes-session/20260502_105704_07557de1"]
hermes_session: "20260502_105704_07557de1"
confidence: "medium"
---

# osxphotos tool for Apple Photos

osxphotos (v0.75.9) was installed via pip and provides full CLI access to the Apple Photos library. It can list persons (e.g., Berenice Carbajo: 306 photos), albums, keywords, and locations. Queries support combining criteria like person + location (e.g., Bere in Mendoza). Photos stored only in iCloud (not downloaded) are detected but cannot be exported until locally available; they show `IsMissing=True`, `InCloud=True`. Example: found 2 photos of Bere in Los Penitentes, Mendoza from 2026-03-22. Export to a directory works but may require `--update` to avoid duplicates. The tool also supports batch edits, metadata export, and more. See [[technical-lessons]] for related workarounds.
