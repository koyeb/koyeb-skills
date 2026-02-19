---
name: sandboxes-cli
description: "Manage Koyeb sandboxes: create, list, run commands, manage processes, filesystem operations, and port exposure using the CLI."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
	author: koyeb
	version: "0.0.1"
---

# Koyeb Sandboxes (CLI)

## When to use

Use this skill to interact with Koyeb sandboxes created via `koyeb service create --type=sandbox`, including running commands, managing processes, files, and ports.

## Prerequisites

- Koyeb CLI installed and on PATH
- Authenticated session (see references/koyeb-auth.md)

## Workflow

1. Create or identify a sandbox.
2. Check health and list running processes.
3. Run commands or start background processes.
4. Expose or unexpose ports as needed.
5. Use filesystem commands for data inspection.

## Commands

- Create sandbox: `koyeb sandbox create [flags]`
- List sandboxes: `koyeb sandbox list [flags]`
- Check health: `koyeb sandbox health <sandbox-id> [flags]`
- Run command: `koyeb sandbox run <sandbox-id> -- <command> [args...]`
- Start process: `koyeb sandbox start <sandbox-id> -- <command> [args...]`
- List processes: `koyeb sandbox ps <sandbox-id> [flags]`
- Kill process: `koyeb sandbox kill <sandbox-id> <pid> [flags]`
- Stream logs: `koyeb sandbox logs <sandbox-id> <pid> [flags]`
- Filesystem operations: `koyeb sandbox fs <sandbox-id> <subcommand> [flags]`
- Expose port: `koyeb sandbox expose-port <sandbox-id> <port> [flags]`
- Unexpose port: `koyeb sandbox unexpose-port <sandbox-id> [flags]`

## Examples

- Create a sandbox: `koyeb sandbox create --name my-sandbox`
- Run a command: `koyeb sandbox run <sandbox-id> -- ls -la`
- Start a background process: `koyeb sandbox start <sandbox-id> -- python app.py`
- Expose a port: `koyeb sandbox expose-port <sandbox-id> 8080`

## References

For detailed flags, see references/koyeb-sandbox-flags.md.

- references/koyeb-cli.md
- references/koyeb-sandbox-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
