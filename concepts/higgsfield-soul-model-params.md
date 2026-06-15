---
title: "higgsfield soul model params"
created: "2026-05-11"
updated: "2026-05-11"
type: "concept"
tags: ["#higgsfield", "#soul", "#image-generation", "#cli", "#params"]
sources: ["hermes-session/20260511_123355_2f57fa"]
hermes_session: "20260511_123355_2f57fa"
confidence: "medium"
---

# higgsfield soul model params

## Higgsfield Soul Model Param Differences

### Soul V2 (`text2image_soul_v2`)
- Identity reference: `--custom_reference_id <soul-uuid>`
- Works directly with the Soul UUID
- Other params: `aspect_ratio`, `medias`, `prompt`, `quality`

### Soul Cinematic (`soul_cinematic`)
- Identity reference: `--medias` (complex JSON structure)
- Does **NOT** support `--custom_reference_id`
- `--medias` requires array of objects with:
  - `role`: one of `image`, `start_image`, `end_image`, `video`, `audio`, `file`
  - `data.id`: UUID of the media/job
  - `data.type`: one of `media_input`, `soul_cinematic_job`, `text2image_soul_v2_job`, etc.
- **Unsolved**: passing Soul ID as identity reference — tried `type: media_input`, `type: soul_cinematic_job`, both failed. Without medias, generates generic faces (no identity).

### Param Discovery
- `higgsfield generate create --help` does NOT show model-specific params
- Use `higgsfield model get <model_name>` to see all params, types, defaults, and required flags

### Related
- See [[higgsfield-ai]] for general CLI reference
