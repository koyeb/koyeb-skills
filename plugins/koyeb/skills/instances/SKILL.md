---
name: instances
description: "Manage Koyeb instances: copy files, describe, exec, get, list, and view logs. Use when debugging or operating running instances."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.1"
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

- List instances: `koyeb instances list [flags]`
- Get instance: `koyeb instances get <instance-name>`
- Describe instance: `koyeb instances describe <instance-name>`
- Instance logs: `koyeb instances logs <instance-name> [flags]`
- Exec command: `koyeb instances exec <instance-name> <cmd> -- [args...]`
- Copy files: `koyeb instances cp <src> <dst>`

## Examples

- List instances: `koyeb instances list --service my-service`
- Exec into instance: `koyeb instances exec <instance-id> /bin/bash`
- Copy file from instance: `koyeb instances cp <instance-id>:/path/file.txt ./`

## References

For detailed flags, see references/koyeb-instances-flags.md.

- references/koyeb-cli.md
- references/koyeb-instances-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
