---
name: domains
description: "Manage Koyeb domains: attach, detach, create, delete, describe, get, list, and refresh domains. Use when the user needs domain configuration for a service."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.2"
---

# Koyeb Domains

## When to use

Use this skill to manage domain resources and attach or detach domains from services.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify target domain and service.
2. Use `list` or `get` to confirm current status.
3. Create/attach/detach or refresh domain as requested.

## Commands

- List domains: `koyeb domains list`
- Get domain: `koyeb domains get <domain-name>`
- Describe domain: `koyeb domains describe <domain-name>`
- Create domain: `koyeb domains create <domain-name> [flags]`
- Delete domain: `koyeb domains delete <domain-name>`
- Attach domain: `koyeb domains attach <domain-name> <app-name>`
- Detach domain: `koyeb domains detach <domain-name>`
- Refresh domain: `koyeb domains refresh <domain-name>`

## Examples

- Create a domain: `koyeb domains create example.com`
- Attach a domain to an app: `koyeb domains attach example.com my-app`
- List all domains: `koyeb domains list`

## References

For detailed flags, see references/koyeb-domains-flags.md.

- references/koyeb-cli.md
- references/koyeb-domains-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
