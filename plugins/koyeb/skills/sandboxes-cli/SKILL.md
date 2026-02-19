---
name: sandboxes-cli
description: "Manage Koyeb sandboxes: create, list, run commands, manage processes, filesystem operations, and port exposure using the CLI."
license: MIT
compatibility: Requires the Koyeb CLI and network access.
metadata:
	author: koyeb
	version: "0.0.2"
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

- Create sandbox: `koyeb sandbox create SANDBOXNAME --app APPNAME [flags]`
- List sandboxes: `koyeb sandbox list SANDBOXNAME/APPNAME[flags]`
- Check health: `koyeb sandbox health SANDBOXNAME/APPNAME [flags]`
- Run command: `koyeb sandbox run SANDBOXNAME/APPNAME -- <command> [args...]`
- Start process: `koyeb sandbox start SANDBOXNAME/APPNAME -- <command> [args...]`
- List processes: `koyeb sandbox ps SANDBOXNAME/APPNAME [flags]`
- Kill process: `koyeb sandbox kill SANDBOXNAME/APPNAME <pid> [flags]`
- Stream logs: `koyeb sandbox logs SANDBOXNAME/APPNAME <pid> [flags]`
- Filesystem operations: `koyeb sandbox fs SANDBOXNAME/APPNAME <subcommand> [flags]`
- Expose port: `koyeb sandbox expose-port SANDBOXNAME/APPNAME <port> [flags]`
- Unexpose port: `koyeb sandbox unexpose-port SANDBOXNAME/APPNAME [flags]`

## Examples

- Create a sandbox: `koyeb sandbox create --name my-sandbox`
- Run a command: `koyeb sandbox run SANDBOXNAME/APPNAME -- ls -la`
- Start a background process: `koyeb sandbox start SANDBOXNAME/APPNAME -- python app.py`
- Expose a port: `koyeb sandbox expose-port SANDBOXNAME/APPNAME 8080`

## References

For detailed flags, see references/koyeb-sandbox-flags.md.

- references/koyeb-cli.md
- references/koyeb-sandbox-flags.md
- references/koyeb-auth.md
- references/koyeb-output.md
