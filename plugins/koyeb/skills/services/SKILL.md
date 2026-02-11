---
name: services
description: "Manage Koyeb services: create, delete, describe, exec, get, list, logs, redeploy, pause, resume, check unapplied changes, and update services. Use when working with Koyeb service operations."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Services

## When to use

Use this skill to create or manage Koyeb services, including logs, exec, and lifecycle actions.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify target app and service.
2. Use list/get/describe to confirm state.
3. Create, update, pause/resume, or redeploy as needed.
4. Use exec or logs to troubleshoot.

## Commands

- List services: `koyeb service list`
- Get service: `koyeb service get <service-id-or-name>`
- Describe service: `koyeb service describe <service-id-or-name>`
- Create service: `koyeb service create <app-id-or-name> ...`
- Update service: `koyeb service update <service-id-or-name> ...`
- Delete service: `koyeb service delete <service-id-or-name>`
- Pause service: `koyeb service pause <service-id-or-name>`
- Resume service: `koyeb service resume <service-id-or-name>`
- Redeploy service: `koyeb service redeploy <service-id-or-name>`
- Logs: `koyeb service logs <service-id-or-name>`
- Exec in instance context: `koyeb service exec <service-id-or-name> ...`
- Unapplied changes: `koyeb service unapplied-changes <service-id-or-name>`

## Examples

- Create service: `koyeb service create my-app ...`
- Tail logs: `koyeb service logs my-service`
- Exec a command: `koyeb service exec my-service -- ls -la`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
