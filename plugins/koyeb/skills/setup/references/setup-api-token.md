# Koyeb API Token Setup

## Generate an API token

1. Go to https://app.koyeb.com/settings/api
2. Click "Create API Token" or "Generate Token"
3. Copy the token (appears once)
4. Store securely

## Set environment variable

The Sandbox SDKs (JS and Python) read the `KOYEB_API_TOKEN` environment variable by default.

### macOS/Linux

```bash
export KOYEB_API_TOKEN="your-token-here"
```

To persist across sessions, add to `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:

```bash
echo 'export KOYEB_API_TOKEN="your-token-here"' >> ~/.zshrc
source ~/.zshrc
```

### Windows (PowerShell)

```powershell
$env:KOYEB_API_TOKEN = "your-token-here"
```

To persist, use System Properties or environment variable tools.

### Windows (Command Prompt)

```cmd
set KOYEB_API_TOKEN=your-token-here
```

### .env file (local development)

Create a `.env` file in your project root:

```
KOYEB_API_TOKEN=your-token-here
```

Use a package like `python-dotenv` (Python) or `dotenv` (Node.js) to load it:

**Python:**

```python
from dotenv import load_dotenv
load_dotenv()
```

**Node.js:**

```javascript
import dotenv from 'dotenv';
dotenv.config();
```

## Verify setup

### Node.js

```javascript
import { Sandbox } from '@koyeb/sandbox-sdk';

const sandbox = await Sandbox.create({ wait_ready: true });
console.log('Authentication successful!');
await sandbox.delete();
```

### Python

```python
from koyeb import Sandbox

sandbox = Sandbox.create(wait_ready=True)
print('Authentication successful!')
sandbox.delete()
```

## Security notes

- Never commit tokens to version control
- Use `.env` for local development, not production
- Rotate tokens regularly at https://app.koyeb.com/settings/api
- Use secrets management in production (CI/CD, cloud, etc.)
