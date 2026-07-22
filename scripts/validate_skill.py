#!/usr/bin/env python3
"""Validate the repository copy of the Gewu skill with only the Python stdlib."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "gewu"
REQUIRED_REFERENCES = {
    "completeness-checklists.md",
    "evidence-and-verdict.md",
    "origin-tracing.md",
    "report-format.md",
    "source-routing.md",
    "teardown-lenses.md",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def quoted_yaml_value(text: str, key: str) -> str:
    match = re.search(rf'^\s*{re.escape(key)}:\s*"([^"]*)"\s*$', text, re.MULTILINE)
    if not match:
        fail(f"agents/openai.yaml is missing quoted {key}")
    return match.group(1)


def validate_frontmatter(skill_text: str) -> None:
    if not skill_text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        frontmatter, _ = skill_text[4:].split("\n---\n", 1)
    except ValueError:
        fail("SKILL.md frontmatter is not closed")

    keys = []
    values: dict[str, str] = {}
    for line in frontmatter.splitlines():
        match = re.match(r"^([a-z_]+):\s*(.+)$", line)
        if not match:
            fail(f"invalid frontmatter line: {line!r}")
        key, raw_value = match.groups()
        keys.append(key)
        values[key] = raw_value.strip().strip('"')

    if keys != ["name", "description"]:
        fail("SKILL.md frontmatter must contain only name then description")
    if values["name"] != SKILL.name:
        fail("skill name must match its directory")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", values["name"]):
        fail("skill name must use lowercase letters, digits, and hyphens")
    if len(values["description"]) < 40:
        fail("skill description is too short to trigger reliably")


def validate_links() -> None:
    broken: list[str] = []
    for path in SKILL.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (path.parent / relative).resolve().exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")
    if broken:
        fail("broken relative links: " + "; ".join(broken))


def main() -> None:
    skill_file = SKILL / "SKILL.md"
    if not skill_file.is_file():
        fail(f"missing {skill_file.relative_to(ROOT)}")

    skill_text = skill_file.read_text(encoding="utf-8")
    validate_frontmatter(skill_text)
    if len(skill_text.splitlines()) >= 500:
        fail("SKILL.md must stay under 500 lines")
    if "TODO" in skill_text:
        fail("SKILL.md still contains TODO")
    if (SKILL / "README.md").exists():
        fail("README.md belongs at repository root, not inside the skill package")

    references = SKILL / "references"
    actual_references = {path.name for path in references.glob("*.md")}
    missing_references = sorted(REQUIRED_REFERENCES - actual_references)
    if missing_references:
        fail("missing references: " + ", ".join(missing_references))

    metadata_file = SKILL / "agents" / "openai.yaml"
    if not metadata_file.is_file():
        fail("missing agents/openai.yaml")
    metadata = metadata_file.read_text(encoding="utf-8")
    if quoted_yaml_value(metadata, "display_name") != "格物":
        fail("display_name must be 格物")
    short_description = quoted_yaml_value(metadata, "short_description")
    if not 25 <= len(short_description) <= 64:
        fail("short_description must contain 25-64 characters")
    default_prompt = quoted_yaml_value(metadata, "default_prompt")
    if "$gewu" not in default_prompt:
        fail("default_prompt must explicitly mention $gewu")

    for path in SKILL.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            if "TODO" in path.read_text(encoding="utf-8"):
                fail(f"TODO remains in {path.relative_to(ROOT)}")

    validate_links()
    print("PASS: Gewu skill structure, metadata, references, and links are valid")


if __name__ == "__main__":
    main()

