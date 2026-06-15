---
title: "Finding photos by text content in Apple Photos"
created: "2026-05-02"
updated: "2026-05-02"
type: "query"
tags: ["#apple-photos", "#ocr", "#search", "#workflow"]
sources: ["hermes-session/20260502_105704_07557de1"]
hermes_session: "20260502_105704_07557de1"
confidence: "medium"
---

# Finding photos by text content in Apple Photos

To locate photos containing specific text (e.g., a document scan), two approaches exist:
1. **Spotlight** – Use `mdfind` with `kMDItemTextContent`. Fast, uses iOS OCR indexing.
2. **Direct SQLite** – Query `ZCHARACTERRECOGNITIONATTRIBUTES` table in the Photos database and parse binary plist blobs. More control but requires decoding Vision observation objects.

Both methods work on the local Photos library; neither requires exporting photos first.
