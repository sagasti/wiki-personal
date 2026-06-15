---
title: "Hermes Per-Contact Permission Gap"
created: "2026-05-09"
updated: "2026-05-09"
type: "concept"
tags: ["#hermes", "#permissions", "#architecture", "#security", "#whatsapp"]
sources: ["hermes-session/20260509_164736_143358"]
hermes_session: "20260509_164736_143358"
confidence: "medium"
---

# Hermes Per-Contact Permission Gap

## The Problem

Jorge wants certain contacts (e.g. [[martin-pizzi]], [[lorena-napoli]]) to chat with Brisa on WhatsApp but NOT execute actions (wiki writes, command execution, data access).

## Current State

- **Authorization is binary**: contacts in SOUL.md/USER.md authorized list get full access to all tools.
- **Removing from auth** = either they can't message at all (removed from bridge allowlist) or only soft protection via prompt instructions.
- **Prompt-only guard** is unreliable: an LLM can misinterpret what counts as an "order" vs. a "conversation".
- **Tirith** (command approval) only protects shell commands — not wiki_create, wiki_append, memory, write_file, patch.

## What's Needed

A granular permission system per contact (e.g. `chat_only`, `read_only`, `full_auth`). Does not exist in Hermes today.

## Implications

- Adding someone to the allowlist gives them full destructive capability.
- Saraceros (people who state things with conviction even when wrong) could contaminate the wiki with incorrect data.
- No hard system-level guarantee that a "chat-only" contact can't trigger tool execution.
