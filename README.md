# Boring PM

**The domain expert's product manager, as an agent skill, for projects run by
the Boring Factory.** It interviews the expert one question at a time, writes
the feature contract and its mockups on the contract pull request, submits the
expert's approval only after the expert confirms it, and follows the feature
through builders' questions, previews to try and acceptance. It never writes
code. Everything goes through `git` and the GitHub CLI `gh`, signed in as the
expert; there is no server and no MCP.

## Install

```bash
npx skills add hachej/boring-pm -g
```

The [skills CLI](https://github.com/vercel-labs/skills) finds the skill in
`skills/boring-pm/` and installs it for your agent (Claude Code, Codex,
Cursor). `-g` installs it for your account, which keeps the project's clone
clean: without it, the skill and a `skills-lock.json` land inside the clone,
where they must not be committed. Run the same command again to update it. Then ask your agent, for
example: "J'ai un besoin pour l'application" or "Where is feature 47?".

The first time, the skill checks that `gh` is installed and signed in and that
the agent runs inside the project's clone, and walks you through fixing it
([onboarding](skills/boring-pm/onboarding.md)).

## What is in the skill

| File | Opened when |
|---|---|
| [SKILL.md](skills/boring-pm/SKILL.md) | Always: the role, the start checks, the fixed rules, which file to open |
| [onboarding.md](skills/boring-pm/onboarding.md) | `gh` missing or signed out, not in a clone, a new person |
| [discovery.md](skills/boring-pm/discovery.md) | A need to turn into a contract, a contract to change or resume, the approval |
| [tickets.md](skills/boring-pm/tickets.md) | Filing a feature, its state, builders' `boring:ask` questions, previews and acceptance, end of session |
| [mockups.md](skills/boring-pm/mockups.md) | Choosing the cheapest mockup that settles a question |
| [templates/](skills/boring-pm/templates/contract.md) | The contract, a single-file HTML mockup, a Markdown scenario |

The directory is self-contained: copying `skills/boring-pm/` copies the whole
skill. The process it follows is defined by hachej/boring-factory
(`FACTORY.md`); the contract format is its `@boring/factory` package.

## Evals and checks

[evals/README.md](evals/README.md) specifies the two suites (process rules
checked on every run, interview quality judged against a hidden need sheet).
They live outside the skill, so they are never installed into a project.

```bash
python3 scripts/check.py   # front matter, routes, portable links, JSON, offline mockup
```

Original material is [MIT licensed](LICENSE).
