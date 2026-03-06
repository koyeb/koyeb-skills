# Koyeb Skills

Agent skills for Koyeb, following the Agent Skills open format.

## Installation

This allows you to pick and choose which skills to install. Re-run to update.

### Manual install

Copy the skills folder to your agent’s skills directory:

```
plugins/koyeb/skills/
```

Supports any Agent Skills-compatible product. See Agent Skills docs for product-specific install locations.

## Editor & agent integrations

The skills are authored in the Agent Skills open format. For VS Code, Cursor, Codex, Mistral Vibe, Claude Code, and OpenCode, install via one of the following:

- **Manual install:**
	- Copy [plugins/koyeb/skills](plugins/koyeb/skills) into the tool’s skills directory.

If a tool uses a custom skills directory or import flow, follow its product documentation and point it at [plugins/koyeb/skills](plugins/koyeb/skills).

<details>
<summary>Local skills copies for different agents</summary>

Copy `plugins/koyeb/skills/` to your agent’s skills directory:
- Claude: `~/.claude/skills/`
- Codex: `~/.codex/skills/`
- OpenCode: `~/.config/opencode/skill/`
- Cursor: `~/.cursor/skills/`
</details>

### Claude Code: refresh-claude-skills

`scripts/refresh-claude-skills.sh` syncs all skills from this repo into `~/.claude/skills/` and updates `~/.claude/CLAUDE.md` so Claude always knows which skills are available.

**One-time setup** — symlink the script so it's available as a shell command:

```bash
sudo ln -sf "$(pwd)/scripts/refresh-claude-skills.sh" /usr/local/bin/refresh-claude-skills
```

**Usage** — run any time skills are added or updated:

```bash
refresh-claude-skills
```

This will:
1. Sync all skills from `plugins/koyeb/skills/` to `~/.claude/skills/`
2. Update the `koyeb-skills` block in `~/.claude/CLAUDE.md` with the current skill list and paths

### Mistral Vibe: refresh-vibe-skills

`scripts/refresh-vibe-skills.sh` syncs all skills from this repo into `~/.vibe/skills/` and updates `~/.vibe/config.toml` with the skill paths.

**One-time setup** — symlink the script so it's available as a shell command:

```bash
sudo ln -sf "$(pwd)/scripts/refresh-vibe-skills.sh" /usr/local/bin/refresh-vibe-skills
```

**Usage** — run any time skills are added or updated:

```bash
refresh-vibe-skills
```

This will:
1. Sync all skills from `plugins/koyeb/skills/` to `~/.vibe/skills/`
2. Update the `skill_paths` array in `~/.vibe/config.toml` with the installed skill paths


## Available Skills

- setup
- apps
- archives
- deploy
- domains
- organizations
- secrets
- services
- deployments
- instances
- databases
- sandboxes-js-sdk
- sandboxes-python-sdk
- version
- volumes

## Repository Structure

```
koyeb-skills/
├── plugins/koyeb/
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       ├── _shared/
│       │   ├── scripts/
│       │   └── references/
│       └── {skill-name}/
│           ├── SKILL.md
│           ├── scripts/
│           └── references/
├── scripts/
│   ├── sync-shared.sh
│   ├── refresh-claude-skills.sh
│   └── refresh-vibe-skills.sh
└── README.md
```

## Development

Shared files live in `plugins/koyeb/skills/_shared/`. After editing shared files, run:

```bash
chmod +x ./scripts/sync-shared.sh
./scripts/sync-shared.sh
```

Do not edit shared copies inside individual skills directly.


## References

- https://agentskills.io/specification
- https://www.koyeb.com/docs

## License

MIT
