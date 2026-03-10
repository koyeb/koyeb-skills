#!/usr/bin/env python3
import subprocess
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "plugins" / "koyeb" / "skills"
SHARED_REF_DIR = SKILLS_DIR / "_shared" / "references"
SHARED_SCRIPTS_DIR = SKILLS_DIR / "_shared" / "scripts"

COMMON_REFS = [
    "koyeb-auth.md",
    "koyeb-cli.md",
    "koyeb-output.md",
    "koyeb-regions-instance-types.md",
]

GLOBAL_FLAGS = [
    "- `-c, --config string` - Config file (default: `$HOME/.koyeb.yaml`)",
    "- `-d, --debug` - Enable debug output",
    "- `--debug-full` - Show sensitive info in debug output",
    "- `--force-ascii` - Only output ASCII characters",
    "- `--full` - Do not truncate output",
    "- `-o, --output output` - Output format (`yaml`, `json`, `table`)",
    "- `--organization string` - Organization ID",
    "- `--token string` - API token",
    "- `--url string` - API URL",
    "- `-h, --help` - Show help",
]

SKILL_SPECS = {
    "apps": {
        "section": "Apps",
        "flag_file": "koyeb-apps-flags.md",
        "commands": [
        "koyeb apps create",
        "koyeb apps delete",
        "koyeb apps describe",
        "koyeb apps get",
        "koyeb apps init",
        "koyeb apps list",
        "koyeb apps pause",
        "koyeb apps resume",
        "koyeb apps update",
        ],
    },
    "archives": {
        "section": "Archives",
        "flag_file": "koyeb-archives-flags.md",
        "commands": ["koyeb archives create"],
    },
    "databases": {
        "section": "Databases",
        "flag_file": "koyeb-databases-flags.md",
        "commands": [
        "koyeb databases create",
        "koyeb databases delete",
        "koyeb databases get",
        "koyeb databases list",
        "koyeb databases update",
        ],
    },
    "deploy": {
        "section": "Deploy",
        "flag_file": "koyeb-deploy-flags.md",
        "commands": ["koyeb deploy", "koyeb services redeploy"],
    },
    "deployments": {
        "section": "Deployments",
        "flag_file": "koyeb-deployments-flags.md",
        "commands": [
        "koyeb deployments cancel",
        "koyeb deployments describe",
        "koyeb deployments get",
        "koyeb deployments list",
        "koyeb deployments logs",
        ],
    },
    "domains": {
        "section": "Domains",
        "flag_file": "koyeb-domains-flags.md",
        "commands": [
        "koyeb domains attach",
        "koyeb domains create",
        "koyeb domains delete",
        "koyeb domains describe",
        "koyeb domains detach",
        "koyeb domains get",
        "koyeb domains list",
        "koyeb domains refresh",
        ],
    },
    "instances": {
        "section": "Instances",
        "flag_file": "koyeb-instances-flags.md",
        "commands": [
        "koyeb instances cp",
        "koyeb instances describe",
        "koyeb instances exec",
        "koyeb instances get",
        "koyeb instances list",
        "koyeb instances logs",
        ],
    },
    "organizations": {
        "section": "Organizations",
        "flag_file": "koyeb-organizations-flags.md",
        "commands": [
        "koyeb organizations list",
        "koyeb organizations switch",
        ],
    },
    "sandboxes-cli": {
        "section": "Sandbox",
        "flag_file": "koyeb-sandbox-flags.md",
        "commands": [
        "koyeb sandbox create",
        "koyeb sandbox expose-port",
        "koyeb sandbox fs download",
        "koyeb sandbox fs ls",
        "koyeb sandbox fs mkdir",
        "koyeb sandbox fs read",
        "koyeb sandbox fs rm",
        "koyeb sandbox fs upload",
        "koyeb sandbox fs write",
        "koyeb sandbox health",
        "koyeb sandbox kill",
        "koyeb sandbox list",
        "koyeb sandbox logs",
        "koyeb sandbox ps",
        "koyeb sandbox run",
        "koyeb sandbox start",
        "koyeb sandbox unexpose-port",
        ],
    },
    "secrets": {
        "section": "Secrets",
        "flag_file": "koyeb-secrets-flags.md",
        "commands": [
        "koyeb secrets create",
        "koyeb secrets delete",
        "koyeb secrets describe",
        "koyeb secrets get",
        "koyeb secrets list",
        "koyeb secrets reveal",
        "koyeb secrets update",
        ],
    },
    "services": {
        "section": "Services",
        "flag_file": "koyeb-services-flags.md",
        "commands": [
        "koyeb services create",
        "koyeb services delete",
        "koyeb services describe",
        "koyeb services exec",
        "koyeb services get",
        "koyeb services list",
        "koyeb services logs",
        "koyeb services pause",
        "koyeb services redeploy",
        "koyeb services resume",
        "koyeb services scale",
        "koyeb services scale delete",
        "koyeb services scale get",
        "koyeb services scale update",
        "koyeb services unapplied-changes",
        "koyeb services update",
        ],
    },
    "version": {
        "section": "Version",
        "flag_file": "koyeb-version-flags.md",
        "commands": ["koyeb version"],
    },
    "volumes": {
        "section": "Volumes",
        "flag_file": "koyeb-volumes-flags.md",
        "commands": [
        "koyeb volumes create",
        "koyeb volumes delete",
        "koyeb volumes get",
        "koyeb volumes list",
        "koyeb volumes update",
        ],
    },
}


NON_CLI_SECTION_TEXT = """# Koyeb CLI - Command Index

Quick reference for Koyeb CLI commands used by these skills.

This skill does not have a dedicated CLI command section in the shared command index.
Use the area-specific CLI skills for command-level references.
"""


def run_help(command: str) -> str:
    result = subprocess.run(
        f"{command} --help",
        shell=True,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        return f"[error running: {command}]\n{result.stderr.strip()}"
    return result.stdout


def extract_options(help_text: str) -> tuple[list[str], list[str]]:
    options: list[str] = []
    inherited: list[str] = []
    mode = None
    for line in help_text.splitlines():
        stripped = line.rstrip()
        if stripped.strip() in {"Flags:", "Options:"}:
            mode = "options"
            continue
        if stripped.strip().startswith("Global Flags:") or stripped.strip().startswith("Options inherited from parent commands"):
            mode = "inherited"
            continue

        if (
            stripped.strip().startswith("Examples:")
            or stripped.strip().startswith("Usage:")
            or stripped.strip().startswith("Available Commands:")
            or stripped.strip().startswith("Additional Help Topics:")
        ):
            if mode in {"options", "inherited"}:
                mode = None

        if mode == "options" and stripped.strip():
            options.append(stripped)
        elif mode == "inherited" and stripped.strip():
            inherited.append(stripped)

    return options, inherited


def build_section(command: str) -> str:
    help_text = run_help(command)
    options, inherited = extract_options(help_text)

    lines: list[str] = [f"## `{command}`", "", "```text"]
    if options:
        lines.append("Options:")
        lines.extend(options)
    else:
        lines.append("Options: (none)")

    if inherited:
        lines.append("")
        lines.append("Options inherited from parent commands:")
        lines.extend(inherited)

    lines.extend(["```", ""])
    return "\n".join(lines)


def build_commands_index(section: str, flag_file: str, commands: list[str]) -> str:
    content: list[str] = [
        "# Koyeb CLI - Command Index",
        "",
        "Quick reference for Koyeb CLI commands used by these skills.",
        "For complete, command-specific flags, use the `koyeb-*-flags.md` references.",
        "",
        "## Global Flags",
        "",
        "These flags are available on all commands:",
        "",
        "- `-c, --config string` - Config file (default: `$HOME/.koyeb.yaml`)",
        "- `-d, --debug` - Enable debug output",
        "- `--debug-full` - Do not hide sensitive information in debug output",
        "- `--force-ascii` - Only output ASCII characters",
        "- `--full` - Do not truncate output",
        "- `-h, --help` - Help for command",
        "- `-o, --output output` - Output format: `yaml`, `json`, or `table`",
        "- `--organization string` - Organization ID",
        "- `--token string` - API token",
        "- `--url string` - API URL (default: `https://app.koyeb.com`)",
        "",
        "## Skill-Covered Commands",
        "",
        f"### {section}",
    ]
    content.extend([f"- `{cmd}`" for cmd in commands])
    content.append(f"- Flags: `references/{flag_file}`")
    content.append("")
    return "\n".join(content)


def clean_generated_shared_refs() -> None:
    for path in SHARED_REF_DIR.glob("koyeb-*-flags.md"):
        path.unlink(missing_ok=True)
    (SHARED_REF_DIR / "koyeb-commands.md").unlink(missing_ok=True)


def clean_generated_skill_refs(skill_ref_dir: Path) -> None:
    for path in skill_ref_dir.glob("koyeb-*-flags.md"):
        path.unlink(missing_ok=True)
    (skill_ref_dir / "koyeb-commands.md").unlink(missing_ok=True)


def sync_shared_content_to_skills() -> None:
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == "_shared":
            continue

        scripts_dir = skill_dir / "scripts"
        references_dir = skill_dir / "references"

        if scripts_dir.exists():
            shutil.rmtree(scripts_dir)
        scripts_dir.mkdir(parents=True, exist_ok=True)
        references_dir.mkdir(parents=True, exist_ok=True)

        for source_script in SHARED_SCRIPTS_DIR.iterdir():
            if source_script.is_file():
                shutil.copy2(source_script, scripts_dir / source_script.name)

        for ref_name in COMMON_REFS:
            source_ref = SHARED_REF_DIR / ref_name
            if source_ref.exists():
                shutil.copy2(source_ref, references_dir / ref_name)


def main() -> None:
    sync_shared_content_to_skills()
    clean_generated_shared_refs()

    generated_flags = 0
    generated_commands = 0

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == "_shared":
            continue

        ref_dir = skill_dir / "references"
        ref_dir.mkdir(parents=True, exist_ok=True)
        clean_generated_skill_refs(ref_dir)

        spec = SKILL_SPECS.get(skill_dir.name)
        if spec is None:
            (ref_dir / "koyeb-commands.md").write_text(NON_CLI_SECTION_TEXT, encoding="utf-8")
            generated_commands += 1
            continue

        filename = spec["flag_file"]
        commands = spec["commands"]
        title = filename.replace("koyeb-", "").replace("-flags.md", "").replace("-", " ").title()

        content: list[str] = [
            f"# Koyeb CLI Flags: {title}",
            "",
            "Reference generated from `koyeb --help` output.",
            "",
            "## Global Flags",
            "",
            *GLOBAL_FLAGS,
            "",
        ]

        for command in commands:
            content.append(build_section(command))

        (ref_dir / filename).write_text("\n".join(content).rstrip() + "\n", encoding="utf-8")
        generated_flags += 1

        command_doc = build_commands_index(spec["section"], filename, commands)
        (ref_dir / "koyeb-commands.md").write_text(command_doc, encoding="utf-8")
        generated_commands += 1

    print(
        f"Generated {generated_flags} per-skill flag reference files and "
        f"{generated_commands} per-skill command index files."
    )


if __name__ == "__main__":
    main()
