---
name: secrets
description: "Manage Koyeb secrets: create, delete, describe, get, list, reveal, and update secrets. Use when users need to store or rotate sensitive values for services."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Secrets

## When to use

Use this skill to create or manage secrets for Koyeb services.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify the target secret name and scope.
2. Use list/get/describe to verify current state.
3. Create, update, reveal, or delete as requested.

## Commands

- List secrets: `koyeb secret list`
- Get secret: `koyeb secret get <secret-id-or-name>`
- Describe secret: `koyeb secret describe <secret-id-or-name>`
- Create secret: `koyeb secret create <name> --value <value>`
- Update secret: `koyeb secret update <secret-id-or-name> ...`
- Reveal secret: `koyeb secret reveal <secret-id-or-name>`
- Delete secret: `koyeb secret delete <secret-id-or-name>`

## Examples

- Create a secret: `koyeb secret create DATABASE_URL --value "..."`
- Reveal a secret: `koyeb secret reveal DATABASE_URL`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
