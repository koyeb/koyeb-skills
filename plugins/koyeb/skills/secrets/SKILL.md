---
name: secrets
description: "Manage Koyeb secrets: create, delete, describe, get, list, reveal, and update secrets. Use when users need to store or rotate sensitive values for services."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.1"
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

- List secrets: `koyeb secrets list`
- Get secret: `koyeb secrets get <secret-name>`
- Describe secret: `koyeb secrets describe <secret-name>`
- Create secret: `koyeb secrets create <name> --value <value> [--type <type>]`
- Update secret: `koyeb secrets update <secret-name> [flags]`
- Reveal secret: `koyeb secrets reveal <secret-name>`
- Delete secret: `koyeb secrets delete <secret-name>`

## Examples

- Create a secret: `koyeb secrets create DATABASE_URL --value "postgres://..."`
- Reveal a secret: `koyeb secrets reveal DATABASE_URL`
- List all secrets: `koyeb secrets list`

## References

For detailed flags, see references/koyeb-secrets-flags.md.

- references/koyeb-cli.md
- references/koyeb-secrets-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
