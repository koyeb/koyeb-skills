# Koyeb CLI Installation & Authentication

## Install

Official docs: https://www.koyeb.com/docs/build-and-deploy/cli/installation

### macOS (Homebrew)

```bash
brew install koyeb
```

### macOS, Linux, Windows (Download binary)

```bash
curl -sL https://cli.koyeb.sh/install.sh | sh
```

The script installs to `~/.koyeb/bin`. Add to your `PATH`:

```bash
export PATH="$HOME/.koyeb/bin:$PATH"
```

### Linux (apt)

```bash
echo "deb [trusted=yes] https://apt.koyeb.sh /" | sudo tee /etc/apt/sources.list.d/koyeb.list
sudo apt update
sudo apt install koyeb
```

### Verify installation

```bash
koyeb --version
```

## Authenticate

### Login (interactive)

```bash
koyeb login
```

Follows OAuth flow to generate and store your API token locally.

### API token auth

Export your API token to skip interactive login:

```bash
export KOYEB_API_TOKEN="your-api-token-here"
```

Get your token at: https://app.koyeb.com/settings/api

### Verify authentication

```bash
koyeb apps list
```

Should list your apps (or return empty if you have none). If you're authenticated, the command succeeds.

## Tested version

- Koyeb CLI: latest (compatible with all current skills)
