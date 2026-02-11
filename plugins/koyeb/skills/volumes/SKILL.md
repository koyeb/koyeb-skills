---
name: volumes
description: "Manage Koyeb volumes: create, delete, get, list, and update volumes. Use when the user needs persistent storage management."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Volumes

## When to use

Use this skill to create or manage persistent volumes.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify the target volume name or ID.
2. Use list/get to confirm current state.
3. Create, update, or delete as requested.

## Commands

- List volumes: `koyeb volume list`
- Get volume: `koyeb volume get <volume-id-or-name>`
- Create volume: `koyeb volume create <name> ...`
- Update volume: `koyeb volume update <volume-id-or-name> ...`
- Delete volume: `koyeb volume delete <volume-id-or-name>`

## Examples

- Create volume: `koyeb volume create my-volume ...`
- List volumes: `koyeb volume list`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
