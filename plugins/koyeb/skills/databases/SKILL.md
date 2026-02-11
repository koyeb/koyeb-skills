---
name: databases
description: "Manage Koyeb databases: create, delete, get, list, and update databases. Use when the user needs database lifecycle actions."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
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

- List databases: `koyeb database list`
- Get database: `koyeb database get <database-id-or-name>`
- Create database: `koyeb database create <name> ...`
- Update database: `koyeb database update <database-id-or-name> ...`
- Delete database: `koyeb database delete <database-id-or-name>`

## Examples

- Create database: `koyeb database create my-db ...`
- List databases: `koyeb database list`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
