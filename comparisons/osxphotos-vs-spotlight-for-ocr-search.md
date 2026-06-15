---
title: "osxphotos vs Spotlight for OCR search"
created: "2026-05-02"
updated: "2026-05-02"
type: "comparison"
tags: ["#osxphotos", "#spotlight", "#ocr", "#search"]
sources: ["hermes-session/20260502_105704_07557de1"]
hermes_session: "20260502_105704_07557de1"
confidence: "medium"
---

# osxphotos vs Spotlight for OCR search

The osxphotos tool can query photos by keyword, title, album, person, date, etc., but it cannot search the OCR-recognized text within photos. For that, Apple's Spotlight (via mdfind command) indexes the same OCR data and allows full-text search directly on photo content. Example: `mdfind 'kMDItemTextContent == "Federación Sinológica"'`.

Conclusion: For searching by text in photos, use Spotlight instead of osxphotos.
