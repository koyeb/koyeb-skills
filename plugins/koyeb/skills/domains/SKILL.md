---
name: domains
description: "Manage Koyeb domains: attach, detach, create, delete, describe, get, list, and refresh domains. Use when the user needs domain configuration for a service."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
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

- List domains: `koyeb domain list`
- Get domain: `koyeb domain get <domain-id-or-name>`
- Describe domain: `koyeb domain describe <domain-id-or-name>`
- Create domain: `koyeb domain create <domain-name>`
- Delete domain: `koyeb domain delete <domain-id-or-name>`
- Attach domain: `koyeb domain attach <domain-id-or-name> --service <service-id-or-name>`
- Detach domain: `koyeb domain detach <domain-id-or-name> --service <service-id-or-name>`
- Refresh domain: `koyeb domain refresh <domain-id-or-name>`

## Examples

- Create a domain: `koyeb domain create example.com`
- Attach a domain: `koyeb domain attach example.com --service my-service`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
