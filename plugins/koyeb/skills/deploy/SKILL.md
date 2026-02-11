---
name: deploy
description: Deploy Koyeb services and apps. Use when the user asks to deploy code, trigger a redeploy, or roll out changes.
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Deploy

## When to use

Use this skill to deploy code or trigger redeploys for existing services.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify target app and service.
2. If needed, create an archive (see archives skill).
3. Deploy or redeploy the service.
4. Verify via deployments list and logs.

## Commands

- Deploy service: `koyeb service deploy <service-id-or-name> ...`
- Redeploy service: `koyeb service redeploy <service-id-or-name>`
- List deployments: `koyeb deployment list --service <service-id-or-name>`
- Deployment logs: `koyeb deployment logs <deployment-id>`

## Examples

- Deploy a service: `koyeb service deploy my-service ...`
- Redeploy a service: `koyeb service redeploy my-service`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
