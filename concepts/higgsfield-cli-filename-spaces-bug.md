---
title: "higgsfield cli filename spaces bug"
created: "2026-05-11"
updated: "2026-05-11"
type: "concept"
tags: ["#higgsfield", "#cli", "#bug", "#lora-training"]
sources: ["hermes-session/20260511_103403_fe64a552"]
hermes_session: "20260511_103403_fe64a552"
confidence: "medium"
---

# higgsfield cli filename spaces bug

The `higgsfield soul-id create` CLI fails when image filenames contain spaces.

**Error:**
```
Error: Image "/tmp/higgsfield_soul/jorge/cabel" is neither a UUID nor an existing file path.
```

The CLI splits on spaces and treats each token as a separate argument.

**Workaround:** Rename files before passing them:
```bash
i=1; for f in *.jpg; do mv "$f" "jorge_$(printf '%02d' $i).jpg"; ((i++)); done
```

Related: [[higgsfield-ai]]
