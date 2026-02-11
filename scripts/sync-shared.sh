#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SHARED_DIR="$ROOT_DIR/plugins/koyeb/skills/_shared"

for skill_dir in "$ROOT_DIR"/plugins/koyeb/skills/*; do
  if [[ ! -d "$skill_dir" ]]; then
    continue
  fi
  if [[ "$(basename "$skill_dir")" == "_shared" ]]; then
    continue
  fi

  rm -rf "$skill_dir/scripts" "$skill_dir/references"
  mkdir -p "$skill_dir/scripts" "$skill_dir/references"
  cp -R "$SHARED_DIR"/scripts/. "$skill_dir/scripts"
  cp -R "$SHARED_DIR"/references/. "$skill_dir/references"
  echo "Synced shared files to $(basename "$skill_dir")"
 done
