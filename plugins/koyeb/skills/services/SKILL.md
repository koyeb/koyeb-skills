---
name: services
description: "Manage Koyeb services: create, delete, describe, exec, get, list, logs, redeploy, pause, resume, check unapplied changes, and update services. Use when working with Koyeb service operations."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.2"
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

- List services: `koyeb services list [flags]`
- Get service: `koyeb services get <service-name> --app <app-name>`
- Describe service: `koyeb services describe <service-name> --app <app-name>`
- Create service: `koyeb services create <service-name> --app <app-name> [flags]`
- Update service: `koyeb services update <service-name> --app <app-name> [flags]`
- Delete service: `koyeb services delete <service-name> --app <app-name>`
- Pause service: `koyeb services pause <service-name> --app <app-name>`
- Resume service: `koyeb services resume <service-name> --app <app-name>`
- Redeploy service: `koyeb services redeploy <service-name> --app <app-name>`
- Logs: `koyeb services logs <service-name> --app <app-name>`
- Exec command: `koyeb services exec <service-name> <cmd> -- [args...] --app <app-name>`
- Unapplied changes: `koyeb services unapplied-changes <service-name> --app <app-name>`

## Examples

- Create service: `koyeb services create my-service --app my-app --docker nginx --port 8080:http`
- Tail logs: `koyeb services logs my-service --app my-app`
- Exec a command: `koyeb services exec my-service bash -- --app my-app`

## References

For detailed flags, see references/koyeb-services-flags.md.

- references/koyeb-cli.md
- references/koyeb-services-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
