---
name: deployments
description: "Manage Koyeb deployments: cancel, describe, get, list, and view logs. Use when the user needs deployment status or troubleshooting."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "1.0"
---

# Koyeb Deployments

## When to use

Use this skill to inspect or manage deployment history, logs, and cancellation.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify the service and deployment to inspect.
2. Use list/get/describe to capture details.
3. Read logs or cancel if requested.

## Commands

- List deployments: `koyeb deployment list --service <service-id-or-name>`
- Get deployment: `koyeb deployment get <deployment-id>`
- Describe deployment: `koyeb deployment describe <deployment-id>`
- Deployment logs: `koyeb deployment logs <deployment-id>`
- Cancel deployment: `koyeb deployment cancel <deployment-id>`

## Examples

- List deployments: `koyeb deployment list --service my-service`
- Cancel a deployment: `koyeb deployment cancel <deployment-id>`

## References

- references/koyeb-cli.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
