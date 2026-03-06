#!/usr/bin/env bash
set -euo pipefail

SCRIPT_REAL="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$0")"
SKILLS_SRC="$(cd "$(dirname "$SCRIPT_REAL")/.." && pwd)/plugins/koyeb/skills"
SKILLS_DEST="$HOME/.vibe/skills"
VIBE_CONFIG="$HOME/.vibe/config.toml"

echo "Syncing Koyeb skills to $SKILLS_DEST..."
mkdir -p "$SKILLS_DEST"
rsync -a --delete --exclude='_shared' "$SKILLS_SRC/" "$SKILLS_DEST/"

# Collect skill paths for config.toml
declare -a skill_paths
for skill_dir in "$SKILLS_DEST"/*/; do
  skill_name="$(basename "$skill_dir")"
  skill_md="$skill_dir/SKILL.md"
  if [[ -f "$skill_md" ]]; then
    skill_paths+=("$HOME/.vibe/skills/$skill_name")
  fi
done

# Update or create config.toml
mkdir -p "$(dirname "$VIBE_CONFIG")"
touch "$VIBE_CONFIG"

# Build the skill_paths array for TOML
skill_paths_toml="skill_paths = ["
first=true
for path in "${skill_paths[@]}"; do
  if [ "$first" = true ]; then
    skill_paths_toml+="\"$path\""
    first=false
  else
    skill_paths_toml+=", \"$path\""
  fi
done
skill_paths_toml+="]"

# Update config.toml using Python
python3 - "$VIBE_CONFIG" "$skill_paths_toml" <<'PYEOF'
import sys, re

config_path = sys.argv[1]
skill_paths_line = sys.argv[2]

try:
    with open(config_path, 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""

# Check if skill_paths already exists
if re.search(r'^\s*skill_paths\s*=', content, flags=re.MULTILINE):
    # Replace existing skill_paths line
    content = re.sub(
        r'^\s*skill_paths\s*=.*$',
        skill_paths_line,
        content,
        flags=re.MULTILINE
    )
else:
    # Append skill_paths if file is not empty
    if content and not content.endswith('\n'):
        content += '\n'
    if content:
        content += '\n'
    content += skill_paths_line + '\n'

with open(config_path, 'w') as f:
    f.write(content)
PYEOF

echo "Updated $VIBE_CONFIG"
echo ""
echo "Installed skill paths:"
for path in "${skill_paths[@]}"; do
  skill_name="$(basename "$path")"
  echo "  - $skill_name ($path)"
done
