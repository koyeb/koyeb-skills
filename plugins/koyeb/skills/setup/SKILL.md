---
name: setup
description: Set up prerequisites for Koyeb skills. Provides installation steps for Koyeb CLI, Sandbox SDKs (JS and Python), authentication, and API tokens.
license: MIT
compatibility: Multi-platform (macOS, Linux, Windows). Requires package manager (npm, pip) and internet access.
metadata:
  author: koyeb
  version: "0.0.2"
---

# Koyeb Setup

## When to use

Use this skill to understand and set up the prerequisites required by other Koyeb skills before you can use them for CLI commands or Sandbox SDK workflows.

## Prerequisites

- **For CLI:** bash/zsh shell, curl, and a Koyeb account
- **For JS SDK:** Node.js (v18+) and npm/pnpm/yarn
- **For Python SDK:** Python (v3.8+) and pip
- Internet access to download packages and authenticate with Koyeb

## Workflow

1. Choose your workflow: CLI-based or SDK-based (or both).
2. Install the required CLI or SDK package(s) using the installation steps in references.
3. Authenticate: log in via CLI or set API token environment variable.
4. Verify installation by running the test commands in references.

## Examples

See references for step-by-step CLI and SDK installation, verified package versions, and test commands.

## References

- [setup-cli-installation.md](references/setup-cli-installation.md) — Koyeb CLI install and authenticate
- [setup-sdk-js-installation.md](references/setup-sdk-js-installation.md) — JS SDK (@koyeb/sandbox-sdk)
- [setup-sdk-python-installation.md](references/setup-sdk-python-installation.md) — Python SDK (koyeb-sdk)
- [setup-api-token.md](references/setup-api-token.md) — API token generation and environment setup
