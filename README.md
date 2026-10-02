# boring-stack

**All the skills of the Boring platform, in one public repository**, laid out
for the [skills CLI](https://github.com/vercel-labs/skills): one folder per
skill under `skills/<name>/`.

| Repository | Role |
|---|---|
| **hachej/boring-stack** (this one) | The skills: the expert's PM, the workers' stack, the maintainer's setup skill |
| hachej/boring-app | The app template: agents, tools, server, web, declared in `boring.json` |
| hachej/boring-factory | The Factory around an app: triage, workers, the gates, `init` |

## Who installs what

| Who | Command | What they get |
|---|---|---|
| The expert (their local agent) | `npx skills add hachej/boring-stack --skill boring-pm -g` | `boring-pm`: the interview, the contract, approvals, trials |
| A developer or a worker | `npx skills add hachej/boring-stack -g` (or `--skill <name>` for a list) | The whole stack, starting with `boring-mode` |
| The maintainer | `npx skills add hachej/boring-stack --skill boring-new-app -g` | `boring-new-app`: a new app repository, end to end |

The Factory's workers install the stack at run time (`npx skills add
hachej/boring-stack -y`); app repositories carry no skills.

## The skills

| Skill | For |
|---|---|
| `boring-pm` | The expert's product manager: interview, contract pull request, approval by review, builders' questions, trials |
| `boring-new-app` | The maintainer: create and wire a new app repository |
| `boring-mode` + playbooks | The workers' router: work packet, acceptance lines and their proof, playbooks (investigation, bug fix, feature, refactoring, perf, prototype, visual parity, opening a PR with the evidence table) |
| `new-agent`, `verify-app`, `verify-this`, `platform-request`, `reflect` | Working in a Boring app: capabilities, verification, platform requests, learning |
| `principle-*`, `how`, `why`, `architect`, `arena`, `blast-radius`, `interrogate`, `tdd`, `figure-it-out`, `show-me-your-work`, `teach`, `technical-writing`, `unslop`, `no-comments`, `bro`, `typescript-best-practices`, `create-verification-skill`, `maintain-verification-skill` | pstack (Lauren Tan, MIT) |
| `emil-design-eng`, `animate`, `review-animations`, `find-animation-opportunities`, `pick-ui-library`, `mobile-native`, `prototype` | Emil Kowalski's interface skills (MIT) |
| `make-interfaces-feel-better`, `interaction-design`, `frontend-design` | From poteto/noodle (MIT; `frontend-design` Apache-2.0) |

Sources and commits: `SOURCE.json`; attribution: `THIRD_PARTY.md`; each
third-party skill carries its `LICENSE`.

## Evals and checks

`evals/README.md` specifies the PM evals (process rules on every run,
interview quality against a hidden need sheet). `python3 scripts/check.py`
checks every skill offline (front matter, licences, portable links, JSON).

Original material is [MIT licensed](LICENSE). Referenced works retain their own licenses and copyrights.
