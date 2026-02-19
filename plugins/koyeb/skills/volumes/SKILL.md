---
name: volumes
description: "Manage Koyeb volumes: create, delete, get, list, and update volumes. Use when the user needs persistent storage management."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.2"
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

- List volumes: `koyeb volumes list`
- Get volume: `koyeb volumes get <volume-name>`
- Create volume: `koyeb volumes create <name> [flags]`
- Update volume: `koyeb volumes update <volume-name> [flags]`
- Delete volume: `koyeb volumes delete <volume-name>`

## Examples

- Create volume: `koyeb volumes create my-volume --size 5Gi`
- List volumes: `koyeb volumes list`
- Get volume info: `koyeb volumes get my-volume`

## References

For detailed flags, see references/koyeb-volumes-flags.md.

- references/koyeb-cli.md
- references/koyeb-volumes-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
