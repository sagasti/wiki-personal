---
title: "Apple Photos OCR data storage"
created: "2026-05-02"
updated: "2026-05-02"
type: "concept"
tags: ["#apple-photos", "#ocr", "#database", "#text-recognition"]
sources: ["hermes-session/20260502_105704_07557de1"]
hermes_session: "20260502_105704_07557de1"
confidence: "medium"
---

# Apple Photos OCR data storage

The ZCHARACTERRECOGNITIONATTRIBUTES table in the Photos.sqlite database contains columns ZCHARACTERRECOGNITIONDATA and ZTEXTUNDERSTANDINGDATA, which store binary plist data from Vision framework text recognition. Extracting readable text requires parsing these blobs (e.g., using Python's plistlib and decoding Vision observation objects).

Relevant columns: ZALGORITHMVERSION, ZCHARACTERRECOGNITIONDATA (BLOB), ZTEXTUNDERSTANDINGDATA (BLOB).
