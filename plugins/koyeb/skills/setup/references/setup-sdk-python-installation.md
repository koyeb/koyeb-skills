# Koyeb Sandbox SDK (Python) Installation

## Install

### pip

```bash
pip install koyeb-sdk
```

### pip (with extras, if available)

```bash
pip install koyeb-sdk[dev]
```

### Virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

pip install koyeb-sdk
```

## Verify installation

```bash
pip list | grep koyeb-sdk
```

Should output the installed version.

## Test import

```bash
python3 -c "from koyeb import Sandbox; print('SDK loaded successfully')"
```

## API token setup

See [setup-api-token.md](setup-api-token.md).

## Tested version

- `koyeb-sdk`: v1.2.2
- Python: 3.8 or later required
