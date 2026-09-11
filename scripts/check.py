#!/usr/bin/env python3
"""Check the portable skill's local links, JSON, and research references offline.

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
    source_data = json.loads((skill / "references" / "sources.json").read_text())
    sources = source_data["sources"]
    ids = [source["id"] for source in sources]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate research source ID")
    for source in sources:
        for field in ("id", "title", "author", "url", "reviewed_at", "principle", "limitation"):
            if not source.get(field):
                errors.append(f"Missing source field: {source.get('id')} {field}")
        if urlsplit(source.get("url", "")).scheme != "https":
            errors.append(f"Source must use HTTPS: {source.get('id')}")

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
        for source_id in re.findall(r"\[(S\d{2})\]", body):
            if source_id not in ids:
                errors.append(f"Unknown source {source_id} in {path.relative_to(root)}")
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
    print("PASS: local links, portable skill references, JSON, and research source IDs")
