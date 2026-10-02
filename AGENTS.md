# Boring PM repository

The deliverable is the portable skill at [skills/boring-pm/SKILL.md](skills/boring-pm/SKILL.md), installed with `npx skills add hachej/boring-pm`.

- Keep SKILL.md short: the role, the start checks, the fixed rules, and which file to open. Detail goes in the files it routes to.
- Keep every file the skill needs inside `skills/boring-pm/`, with no links outside it: a copied directory is the whole skill.
- The process is hachej/boring-factory's `FACTORY.md`: approvals are the expert's GitHub reviews on an exact commit, submitted only after the expert confirms in the session. Never weaken that rule.
- The skill uses only `git` and `gh`. Do not add servers, MCP configuration or other tools.
- Do not add real interviews, real personal data or unpublished product plans to this public repository.
- Evals live in `evals/`, outside the skill. Run `python3 scripts/check.py` after any change.
