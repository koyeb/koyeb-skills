---
name: apps
description: "Manage Koyeb apps: create, update, pause or resume, delete, list, describe, and fetch app details. Use when the user asks about Koyeb apps or app lifecycle operations."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.2"
---

# Koyeb Apps

## When to use

Use this skill when the user wants to create, update, pause, resume, delete, list, describe, or fetch details about Koyeb apps.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Determine the organization and target app name or ID.
2. Use `list` or `get` to confirm the app exists and capture its ID.
3. Apply the requested lifecycle action.
4. If the user needs a service created for the app, use the services skill after app creation.

## Commands

- List apps: `koyeb apps list`
- Get app: `koyeb apps get <app-id-or-name>`
- Describe app: `koyeb apps describe <app-id-or-name>`
- Create app: `koyeb apps create <name>`
- Create app and service: `koyeb apps init <name> [flags]`
- Update app: `koyeb apps update <app-id-or-name> [flags]`
- Pause app: `koyeb apps pause <app-id-or-name>`
- Resume app: `koyeb apps resume <app-id-or-name>`
- Delete app: `koyeb apps delete <app-id-or-name>`

## Examples

- Create an app: `koyeb apps create my-app`
- Pause an app: `koyeb apps pause my-app`
- Get details: `koyeb apps get my-app`
- Create app and service: `koyeb apps init my-app --docker nginx --port 8080:http`

## References

For detailed flags, see references/koyeb-apps-flags.md.

- references/koyeb-cli.md
- references/koyeb-apps-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
