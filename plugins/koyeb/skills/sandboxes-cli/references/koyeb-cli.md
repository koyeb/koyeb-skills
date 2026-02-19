# Koyeb CLI Reference

This skill targets the latest available Koyeb CLI.

## Authentication

Use one of:
- `koyeb login`
- `KOYEB_API_TOKEN` environment variable

## Common patterns

- List resources: `koyeb <resource> list`
- Get resource: `koyeb <resource> get <id-or-name>`
- Describe resource: `koyeb <resource> describe <id-or-name>`
- Create resource: `koyeb <resource> create ...`
- Update resource: `koyeb <resource> update <id-or-name> ...`
- Delete resource: `koyeb <resource> delete <id-or-name>`

## Tips

- Use `koyeb <resource> --help` for flags and examples.
- Prefer explicit IDs when available to avoid ambiguity.
- When scripting, consider `--output json` if supported.

## Docs

- https://www.koyeb.com/docs
