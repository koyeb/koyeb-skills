# Koyeb CLI - Command Index

Quick reference for Koyeb CLI commands used by these skills.
For complete, command-specific flags, use the `koyeb-*-flags.md` references.

## Global Flags

These flags are available on all commands:

- `-c, --config string` - Config file (default: `$HOME/.koyeb.yaml`)
- `-d, --debug` - Enable debug output
- `--debug-full` - Do not hide sensitive information in debug output
- `--force-ascii` - Only output ASCII characters
- `--full` - Do not truncate output
- `-h, --help` - Help for command
- `-o, --output output` - Output format: `yaml`, `json`, or `table`
- `--organization string` - Organization ID
- `--token string` - API token
- `--url string` - API URL (default: `https://app.koyeb.com`)

## Skill-Covered Commands

### Sandbox
- `koyeb sandbox create`
- `koyeb sandbox expose-port`
- `koyeb sandbox fs download`
- `koyeb sandbox fs ls`
- `koyeb sandbox fs mkdir`
- `koyeb sandbox fs read`
- `koyeb sandbox fs rm`
- `koyeb sandbox fs upload`
- `koyeb sandbox fs write`
- `koyeb sandbox health`
- `koyeb sandbox kill`
- `koyeb sandbox list`
- `koyeb sandbox logs`
- `koyeb sandbox ps`
- `koyeb sandbox run`
- `koyeb sandbox start`
- `koyeb sandbox unexpose-port`
- Flags: `references/koyeb-sandbox-flags.md`
