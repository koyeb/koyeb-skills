---
name: archives
description: Create Koyeb archives for deployments. Use when the user needs to upload or create an archive for a service deployment.
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Archives

## When to use

Use this skill to create archives that can be referenced by deployments.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify the source directory or file to archive.
2. Create the archive with the CLI.
3. Use the resulting archive ID in a service deploy step.

## Commands

- Create archive: `koyeb archive create <path>`

## Examples

- Create an archive from a directory: `koyeb archive create ./dist`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
