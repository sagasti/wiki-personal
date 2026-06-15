---
title: "RunPod S3 ForkLift Access"
created: "2026-05-11"
updated: "2026-05-11"
type: "project"
tags: ["#runpod", "#s3", "#forklift", "#storage", "#infrastructure"]
sources: ["hermes-session/20260511_123935_3153ed"]
hermes_session: "20260511_123935_3153ed"
confidence: "medium"
---

# RunPod S3 ForkLift Access

## ForkLift S3 Connection for RunPod Network Volume

ForkLift (Mac) can browse the RunPod network volume directly via S3 protocol.

### Connection Settings

| Field | Value |
|-------|-------|
| Protocol | S3 (Amazon S3) |
| Server / Endpoint | `s3api-us-nc-1.runpod.io` |
| Region | `us-nc-1` |
| Bucket | `f4uirc6q1f` |
| Access Key | from `~/.aws/credentials` `[default]` profile |
| Secret Key | from `~/.aws/credentials` `[default]` profile |

### Setup

1. ForkLift → File → New Connection → S3
2. Fill server, region, bucket, and credentials from `~/.aws/credentials`
3. Path prefix `/datasets/` goes directly to dataset folders

### Key Directories

- `bere_curated/` — potentially solo-Bere photos (verify before use)
- `bere_final/` — **contaminated**: contains Jorge+Bere together, unusable for Soul ID (see [[bere-lora-dataset-source]])
- `cabel_curated/` — Jorge solo photos
- `jorge_sagasti_final/` — Jorge final dataset
- `brisa_v3_curated/` — Brisa v3 dataset
- Various `*_cache/` dirs per model (hunyuan, wan22, zimage, etc.)

### Credential Source

Credentials live in `~/.aws/credentials` `[default]` profile. Access key format is `google-oauth2|<id>` (RunPod Google OAuth).


## Client Compatibility

## ⚠️ Client Compatibility Issue (2026-05-11)

The RunPod S3 Access Key format `google-oauth2|<id>` contains a pipe `|` character that **breaks AWS v4 signature computation in all SDK v2-based clients**. Only AWS CLI v1 (botocore) handles it correctly.

**Clients that FAIL:**
- ForkLift — "Access Key Id does not exist in our records"
- Cyberduck — "region 'us-east-1' is wrong; expecting 'us-nc-1'" (can't set custom region for S3)
- rclone — `SignatureDoesNotMatch`
- mc (MinIO Client) — `401 Unauthorized`

**Workaround:** Use `aws s3 sync` to pull files to a local directory and browse with Finder/ForkLift locally:
```bash
aws s3 sync --region us-nc-1 --endpoint-url https://s3api-us-nc-1.runpod.io \
  s3://f4uirc6q1f/datasets/ ~/RunPod-Storage/datasets/ --exclude "*.txt"
```

This is a RunPod platform limitation, not a client bug.


## Pagination


## ⚠️ Pagination Bug (2026-05-11)

RunPod S3 has a severe pagination bug. ALL listing/sync methods fail except `aws s3 ls` (non-recursive, per-prefix):

| Method | Result |
|--------|--------|
| `aws s3 sync` | "The same next token was received twice" |
| `aws s3 ls --recursive` | Same pagination error |
| `aws s3api list-objects-v2` | Returns empty or pagination error |
| boto3 `list_objects_v2` | Returns 0 results |
| `aws s3 ls` (per-prefix) | ✅ Works |

**Workaround:** List files with `aws s3 ls`, parse filenames from output, download one-by-one with `aws s3 cp`.

**Additional issue:** Filenames with non-breaking spaces (e.g. `Screenshot 2025-01-15 at 5.01.13 PM.png`) return 404 on `aws s3 cp`. Skip these — typically screenshots, not useful for training.

## Dataset Cleanup (2026-05-11)

- **`bere_final/` DELETED from S3** — was contaminated (Jorge+Bere together). `bere_curated/` is now the **only source of truth** for Bere photos.
- **`cabel_curated/`** is preferred over `jorge_sagasti_final/` for Jorge (more photos, better curated).
- Local mirrors: `~/RunPod-Storage/datasets/bere_curated/` (55 imgs), `~/RunPod-Storage/datasets/cabel_curated/` (44 imgs)
- Bere soul_2 (`0e51cf22`) needs retraining from `bere_curated/` photos.
