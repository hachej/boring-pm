#!/usr/bin/env python3
"""Check the portable skill offline: local links stay inside it, JSON parses,
SKILL.md has the front matter the skills CLI needs, and every file SKILL.md
routes to exists.

This does not validate the truth of claims, external link availability, or agent
behavior. It has no third-party dependencies and performs no mutations.
"""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys


def check(root: Path) -> list[str]:
    errors = []
    skill = root / "skills" / "boring-pm"
    entry = (skill / "SKILL.md").read_text()
    front = re.match(r"^---\n(.*?)\n---\n", entry, re.S)
    if not front:
        errors.append("SKILL.md has no front matter")
    else:
        fields = dict(line.split(":", 1) for line in front.group(1).splitlines() if ":" in line)
        if fields.get("name", "").strip() != skill.name:
            errors.append("SKILL.md name must equal the directory name (boring-pm)")
        if len(fields.get("description", "").strip()) < 40:
            errors.append("SKILL.md needs a description")
    for name in ("onboarding.md", "discovery.md", "tickets.md", "mockups.md", "templates/contract.md", "templates/mockup.html", "templates/scenario.md"):
        if not (skill / name).exists():
            errors.append(f"Missing skill file: {name}")
        elif name.endswith(".md") and "/" not in name and f"]({name})" not in entry:
            errors.append(f"SKILL.md does not route to {name}")
    if re.search(r"https?://(?![^\s)]*(github\.com|brew\.sh))", (skill / "templates" / "mockup.html").read_text()):
        errors.append("templates/mockup.html must not load anything from the network")

    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix == ".json":
            try:
                json.loads(path.read_text())
            except (ValueError, UnicodeError) as exc:
                errors.append(f"Invalid JSON in {path.relative_to(root)}: {exc}")
        if path.suffix != ".md":
            continue
        body = path.read_text()
        for link in re.findall(r"\]\(([^)]+)\)", body):
            parsed = urlsplit(link)
            if parsed.scheme or link.startswith("#"):
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                errors.append(f"Broken link in {path.relative_to(root)}: {link}")
            if path.is_relative_to(skill) and not target.is_relative_to(skill):
                errors.append(f"Nonportable skill link: {link}")
        if "[TODO" in body:
            errors.append(f"Unfinished scaffold in {path.relative_to(root)}")
    return errors


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    try:
        failures = check(repo_root)
    except (OSError, KeyError, ValueError) as error:
        print(f"Check could not run: {error}", file=sys.stderr)
        raise SystemExit(1)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        raise SystemExit(1)
    print("PASS: SKILL.md front matter and routes, portable local links, JSON, offline mockup template")
