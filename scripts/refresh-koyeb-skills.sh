#!/usr/bin/env bash
set -euo pipefail

SCRIPT_REAL="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$0")"
SKILLS_SRC="$(cd "$(dirname "$SCRIPT_REAL")/.." && pwd)/plugins/koyeb/skills"
SKILLS_DEST="$HOME/.claude/skills"
CLAUDE_MD="$HOME/.claude/CLAUDE.md"

echo "Syncing Koyeb skills to $SKILLS_DEST..."
mkdir -p "$SKILLS_DEST"
rsync -a --delete --exclude='_shared' "$SKILLS_SRC/" "$SKILLS_DEST/"

# Collect skill names and descriptions from each SKILL.md
declare -a skill_lines
for skill_dir in "$SKILLS_DEST"/*/; do
  skill_name="$(basename "$skill_dir")"
  skill_md="$skill_dir/SKILL.md"
  if [[ -f "$skill_md" ]]; then
    desc="$(awk '/^description:/{found=1; sub(/^description:[[:space:]]*/,""); gsub(/^"|"$/,""); print; exit} found && /^[^ ]/{exit}' "$skill_md")"
    skill_lines+=("- **$skill_name** (\`~/.claude/skills/$skill_name/SKILL.md\`): $desc")
  fi
done

# Build the block to inject/replace in CLAUDE.md
block="$(cat <<'BLOCK'
<!-- koyeb-skills:start -->
## Koyeb Skills

The following Koyeb skills are installed at `~/.claude/skills/` and available globally:

BLOCK
)"
for line in "${skill_lines[@]}"; do
  block+="$line"$'\n'
done
block+=$'\n<!-- koyeb-skills:end -->'

touch "$CLAUDE_MD"

if grep -q '<!-- koyeb-skills:start -->' "$CLAUDE_MD"; then
  # Replace existing block using Python for reliable multiline replacement
  python3 - "$CLAUDE_MD" "$block" <<'PYEOF'
import sys, re
path, block = sys.argv[1], sys.argv[2]
content = open(path).read()
content = re.sub(
    r'<!-- koyeb-skills:start -->.*?<!-- koyeb-skills:end -->',
    block,
    content,
    flags=re.DOTALL
)
open(path, 'w').write(content)
PYEOF
else
  # Append block
  printf '\n%s\n' "$block" >> "$CLAUDE_MD"
fi

echo "Updated $CLAUDE_MD"
echo ""
echo "Installed skills:"
for line in "${skill_lines[@]}"; do echo "  $line"; done
