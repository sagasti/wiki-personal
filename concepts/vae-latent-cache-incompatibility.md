---
title: "VAE latent cache incompatibility"
created: "2026-05-09"
updated: "2026-05-09"
type: "concept"
tags: ["#lora", "#vae", "#diffusion-models", "#training", "#cache"]
sources: ["hermes-session/20260509_150545_15540f"]
hermes_session: "20260509_150545_15540f"
confidence: "medium"
---

# VAE latent cache incompatibility

Different diffusion models (e.g., Z-Image vs Wan 2.1/2.2) encode latents with their own specific VAE. Pre-computed cache directories containing these latents are **not compatible** across models.

**Practical implication:** When reusing the same image dataset for LoRA training with a different base model, you must specify a **separate `cache_directory`**. Using a cache from another model's VAE will produce corrupted or suboptimal results.

**Example:** The [[bere-lora-dataset-source]] (38 images) is shared between Z-Image v1 and Wan 2.2 training, but each uses its own cache dir (`bere_final_cache` vs `bere_final_wan22_cache`).

This applies generally to any LoRA training framework (musubi-tuner, kohya, etc.) that pre-encodes dataset latents.
