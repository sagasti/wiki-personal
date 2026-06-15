---
title: "S3 access key pipe char incompatibility"
created: "2026-05-11"
updated: "2026-05-11"
type: "concept"
tags: ["#s3", "#aws", "#runpod", "#debugging", "#compatibility"]
sources: ["hermes-session/20260511_134707_cc9fe7"]
hermes_session: "20260511_134707_cc9fe7"
confidence: "medium"
---

# S3 access key pipe char incompatibility

## S3 Access Key Special Characters Break Most Clients

RunPod (and potentially other providers) issue S3 access keys containing a pipe `|` character. This breaks AWS v4 request signing in most S3 clients because they use AWS SDK v2, which signs differently than AWS CLI v1.

### Clients That FAIL

| Client | Result |
|--------|--------|
| ForkLift | Cannot authenticate |
| Cyberduck | Cannot authenticate |
| Transmit | Cannot authenticate |
| rclone | `Failed to list directory` |
| mc (MinIO Client) | `401 Unauthorized` |
| goofys | Mount fails |
| s3fs | Requires Linux (FUSE), not macOS |

### Only Working Client

- **AWS CLI v1** (`aws s3 sync`, `aws s3 ls`, etc.) — handles pipe in access key correctly

### Workaround

```bash
aws s3 sync s3://<bucket>/<prefix> ~/local-mirror/
```

Sync the bucket locally with `aws s3 sync`, then browse the local mirror with Finder/ForkLift. For ongoing work, set up a cron/script to re-sync periodically.

### Alternative: MinIO Gateway Proxy

Run a local MinIO server as a proxy with clean credentials, then point GUI clients at `localhost`. More elegant but more setup.
