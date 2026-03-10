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

### Apps
- `koyeb apps create`
- `koyeb apps delete`
- `koyeb apps describe`
- `koyeb apps get`
- `koyeb apps init`
- `koyeb apps list`
- `koyeb apps pause`
- `koyeb apps resume`
- `koyeb apps update`
- Flags: `references/koyeb-apps-flags.md`
