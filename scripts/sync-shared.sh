#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "sync-shared.sh is now a compatibility wrapper."
echo "Running unified refresh: scripts/generate-koyeb-flag-refs.py"
python3 "$ROOT_DIR/scripts/generate-koyeb-flag-refs.py"
