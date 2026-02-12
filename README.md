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

Copy `plugins/railway/skills/` to your agent's skills directory:
- Claude: `~/.claude/skills/`
- Codex: `~/.codex/skills/`
- OpenCode: `~/.config/opencode/skill/`
- Cursor: `~/.cursor/skills/`
</details>


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
│   └── sync-shared.sh
└── README.md
```

## Development

Shared files live in `plugins/koyeb/skills/_shared/`. After editing shared files, run:

```bash
./scripts/sync-shared.sh
```

Do not edit shared copies inside individual skills directly.


## References

- https://agentskills.io/specification
- https://www.koyeb.com/docs

## License

MIT
