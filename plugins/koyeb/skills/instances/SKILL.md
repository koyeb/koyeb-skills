---
name: instances
description: "Manage Koyeb instances: copy files, describe, exec, get, list, and view logs. Use when debugging or operating running instances."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Instances

## When to use

Use this skill to inspect or interact with running instances, including exec, logs, and file copy.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify the service and instance.
2. Use list/get/describe to confirm instance details.
3. Run exec, copy files, or read logs as requested.

## Commands

- List instances: `koyeb instance list --service <service-id-or-name>`
- Get instance: `koyeb instance get <instance-id>`
- Describe instance: `koyeb instance describe <instance-id>`
- Instance logs: `koyeb instance logs <instance-id>`
- Exec command: `koyeb instance exec <instance-id> -- <command>`
- Copy files: `koyeb instance cp <src> <instance-id>:<dest>`

## Examples

- List instances: `koyeb instance list --service my-service`
- Exec into instance: `koyeb instance exec <instance-id> -- bash`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
