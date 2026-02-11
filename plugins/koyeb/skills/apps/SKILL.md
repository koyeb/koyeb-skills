---
name: apps
description: "Manage Koyeb apps: create, update, pause or resume, delete, list, describe, and fetch app details. Use when the user asks about Koyeb apps or app lifecycle operations."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
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

- List apps: `koyeb app list`
- Get app: `koyeb app get <app-id-or-name>`
- Describe app: `koyeb app describe <app-id-or-name>`
- Create app: `koyeb app create <name>`
- Update app: `koyeb app update <app-id-or-name> ...`
- Pause app: `koyeb app pause <app-id-or-name>`
- Resume app: `koyeb app resume <app-id-or-name>`
- Delete app: `koyeb app delete <app-id-or-name>`

## Examples

- Create an app: `koyeb app create my-app`
- Pause an app: `koyeb app pause my-app`
- Get details: `koyeb app get my-app`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
