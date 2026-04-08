---
name: deploy
description: Deploy services and apps to Koyeb. Use when the user mentions Koyeb, asks to deploy code to Koyeb, trigger a redeploy, push to production, launch a service, ship changes, check deployment status, or view deploy logs.
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
  author: koyeb
  version: "0.0.2"
---

# Koyeb Deploy

## When to use

Use this skill when the user mentions Koyeb and wants to deploy code, redeploy a service, push to production, launch or ship changes, check deployment status, or view deployment logs.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Identify target app and service.
2. If needed, create an archive (see archives skill).
3. Deploy or redeploy the service.
4. Verify the deployment succeeded (see Validation below).
5. If deployment failed, troubleshoot using the error handling steps.

## Commands

| Action | Command |
|---|---|
| Deploy a directory | `koyeb deploy <path> <app>/<service> [flags]` |
| Redeploy a service | `koyeb services redeploy <service-name> [flags]` |
| List deployments | `koyeb deployments list --service <service-id-or-name>` |
| Get deployment status | `koyeb deployments get <deployment-id>` |
| View deployment logs | `koyeb deployments logs <deployment-id>` |

## Validation

After deploying, confirm the deployment reached a healthy state:

1. Run `koyeb deployments list --service <service-name>` and check the status column.
2. A successful deployment shows status `HEALTHY`. A failed deployment shows `ERROR` or `STASHED`.
3. If the status is not `HEALTHY`, proceed to Error handling.

## Error handling

If a deployment fails:

1. Check build and runtime logs: `koyeb deployments logs <deployment-id>`.
2. Fix the reported issue in the source code or configuration.
3. Redeploy: `koyeb services redeploy <service-name> --app <app-name>`.
4. Re-run validation to confirm the fix.

## Examples

- Deploy a directory: `koyeb deploy ./dist my-app/my-service`
- Redeploy a service: `koyeb services redeploy my-service --app my-app`
- Check deployment status: `koyeb deployments get abc123`

## References

For detailed flags, see references/koyeb-deploy-flags.md.

- references/koyeb-cli.md
- references/koyeb-deploy-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
- scripts/koyeb-cli.sh
