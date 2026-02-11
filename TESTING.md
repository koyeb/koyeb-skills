# Testing Koyeb Skills

## Claude Code agent test (manual)

This test verifies that an agent (Claude Code) selects the right skill and produces correct CLI commands.

### Prerequisites

- Koyeb CLI installed
- Authenticated session (`koyeb login`) or `KOYEB_TOKEN` set
- Skills installed in Claude Code from this repo

### How to run

1. Open Claude Code and load the skills from this repo.
2. Run the prompts in order from:
   - tests/claude-code/prompts.md
3. For each prompt, compare the agent response to:
   - tests/claude-code/expected-behavior.md

### Pass criteria

- The agent selects the correct Koyeb skill for each prompt.
- The agent uses the appropriate `koyeb` CLI command(s).
- The agent does not invent unsupported flags or subcommands.
- For destructive actions, the agent asks for confirmation before executing.
