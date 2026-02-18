---
name: databases
description: "Manage Koyeb databases: create, delete, get, list, and update databases. Use when the user needs database lifecycle actions."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.1"
---

# Koyeb Databases

## When to use

Use this skill to create or manage databases associated with Koyeb apps or services.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify the target database name or ID.
2. Use list/get/describe to confirm current state.
3. Create, update, or delete as requested.

## Commands

- List databases: `koyeb databases list`
- Get database: `koyeb databases get <database-name>`
- Create database: `koyeb databases create <name> [flags]`
- Update database: `koyeb databases update <database-name> [flags]`
- Delete database: `koyeb databases delete <database-name>`

## Examples

- Create database: `koyeb databases create my-db --app my-app --instance-type free --pg-version 16`
- List databases: `koyeb databases list`
- Get database details: `koyeb databases get my-db --app my-app`

## References

For detailed flags, see references/koyeb-databases-flags.md.

- references/koyeb-cli.md
- references/koyeb-databases-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
