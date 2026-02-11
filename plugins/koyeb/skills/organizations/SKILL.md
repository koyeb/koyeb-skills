---
name: organizations
description: List and switch Koyeb organizations. Use when the user needs to select the correct org context before running other commands.
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Organizations

## When to use

Use this skill to list organizations or switch the active organization context.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. List organizations to find the target.
2. Switch context to the correct organization.
3. Continue with the requested operation.

## Commands

- List organizations: `koyeb organization list`
- Switch organization: `koyeb organization switch <org-id-or-name>`

## Examples

- List organizations: `koyeb organization list`
- Switch org: `koyeb organization switch my-org`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
