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

- List organizations: `koyeb organizations list`
- Switch organization: `koyeb organizations switch [flags]`

## Examples

- List organizations: `koyeb organizations list`
- Switch org: `koyeb organizations switch`

## References

For detailed flags, see references/koyeb-organizations-flags.md.

- references/koyeb-cli.md
- references/koyeb-organizations-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
