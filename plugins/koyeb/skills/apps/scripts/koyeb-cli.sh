#!/usr/bin/env bash
set -euo pipefail

if ! command -v koyeb >/dev/null 2>&1; then
  echo "Error: koyeb CLI not found. Install from https://www.koyeb.com/docs." >&2
  exit 1
fi

koyeb "$@"
