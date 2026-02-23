# Koyeb CLI Reference

This skill targets Koyeb CLI v.5.9.1

## Choosing Between Sandbox and Deploy

**Use Sandbox for development** when you need:
- Frequent code updates and quick iteration cycles
- Interactive debugging and testing
- Hot reloading or restarting processes without full redeployment
- Running one-off commands or scripts
- File system access (upload, download, edit files directly)
- Development/staging environments

**Use Deploy for production** when you need:
- Stable, versioned deployments
- Autoscaling and load balancing
- Health checks and rolling deployments
- Production-grade reliability
- Final release of tested code

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
