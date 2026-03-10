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

### Services
- `koyeb services create`
- `koyeb services delete`
- `koyeb services describe`
- `koyeb services exec`
- `koyeb services get`
- `koyeb services list`
- `koyeb services logs`
- `koyeb services pause`
- `koyeb services redeploy`
- `koyeb services resume`
- `koyeb services scale`
- `koyeb services scale delete`
- `koyeb services scale get`
- `koyeb services scale update`
- `koyeb services unapplied-changes`
- `koyeb services update`
- Flags: `references/koyeb-services-flags.md`
