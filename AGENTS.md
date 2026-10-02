# boring-stack repository

All the skills of the Boring platform, one folder each under `skills/<name>/` (the skills CLI layout).

- A skill folder is self-contained: its files and its LICENSE travel with it. A skill may point to a sibling skill (the stack installs them together), never outside `skills/`.
- Keep each SKILL.md short: when to use it, the fixed rules, which file to open. Detail goes in the files it routes to.
- Third-party skills keep their attribution (`THIRD_PARTY.md`, `SOURCE.json`) and their LICENSE file.
- `boring-pm` uses only `git` and `gh`: no servers, no MCP configuration.
- No real interviews, personal data or unpublished product plans in this public repository.
- Run `python3 scripts/check.py` after any change.
