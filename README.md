# Boring PM

**A skill that interviews experts and turns their knowledge into buildable software specifications.**

Boring PM guides a domain or technical expert through a real case, uncovers the judgment behind their work, narrows an idea into one useful product, and writes testable requirements with a [Boring UI](https://github.com/hachej/boring-ui) implementation handoff.

## Use the skill

The complete portable skill is in [skills/boring-pm](skills/boring-pm/SKILL.md). Its entry point is `SKILL.md`; supporting references and templates travel with it.

Invoke it in a host where it is installed:

> Use $boring-pm to interview me about my idea and help me write a clear product specification for Boring UI.

Or ask an agent with repository access to read `skills/boring-pm/SKILL.md` and use it for the task. In a chat-only environment, supply that file and the relevant bundled references as context. Tools and persistent storage depend on the host.

The skill honors the requested stopping point. It can focus on the interview, produce a provisional spec from existing notes, or continue into an authorized build and user trial. It does not launch an application or install external integrations by itself.

## What is included

- A compact skill entry point with adaptive interview and evidence rules.
- Eight research-backed knowledge modules covering outcomes, interviewing, tacit knowledge, evidence synthesis, scope, requirements, validation, and delivery.
- A workflow and question bank that avoid forcing the expert through a long questionnaire.
- Eleven templates for briefs, evidence, domain rules, experiments, specs, handoffs, and resumable session state.
- A fictional end-to-end example that distinguishes reported evidence, product decisions, and unrun acceptance checks.
- A verified Boring UI reference and a short optional tool note covering Canva, Craft, and Figma.

The [source register](skills/boring-pm/references/sources.md) contains 28 primary sources: PM and interviewing guidance, original ACTA research, requirements and usability methods, upstream framework files, and optional provider documentation. It is also available as [JSON](skills/boring-pm/references/sources.json).

## Skill structure

The skill has a compact instruction file supported by a knowledge base and reusable templates. The agent loads detailed material when the current task needs it.

| Part | Location | Responsibility |
| --- | --- | --- |
| Core instructions | [SKILL.md](skills/boring-pm/SKILL.md) | Ask one main question at a time, reuse previous answers, probe expert judgment, track uncertainty, and respect the requested stopping point. |
| Adaptive workflow | [workflow.md](skills/boring-pm/references/workflow.md) | Define each stage's purpose, output, and conditions for moving forward or revisiting an earlier decision. |
| Knowledge base | [References and source register](skills/boring-pm/references/sources.md) | Support outcomes, interviewing, tacit knowledge, evidence synthesis, prioritization, requirements, validation, and delivery with attributed methods. |
| Output templates | [Template index](skills/boring-pm/assets/templates/index.md) | Provide eleven reusable formats for project artifacts, including decisions and resumable session state. Small projects can consolidate them. |
| Implementation references | [Boring UI](skills/boring-pm/references/boring-ui.md) and [tool choices](skills/boring-pm/references/tools.md) | Map the specification to verified framework capabilities and consider optional Canva, Craft, or Figma support when useful. |

The core, references, and templates all live inside `skills/boring-pm`, so copying that directory preserves the complete skill. Project-specific interview records and specifications belong in the user's separate project workspace.

## How the interview becomes a product

The workflow moves through nine stages: **frame, reconstruct, extract, choose, test, specify, build, try, and deliver**. It can move backward when new evidence changes an earlier decision. The default endpoint is a product specification and Boring UI implementation handoff; building and delivery continue when included in the user's request.

The central behavior is turning expert judgment into explicit, testable behavior. For example, if an expert says, "I can tell when a dataset looks wrong," the agent explores:

- A recent case where that happened.
- The signals they noticed and alternatives they considered.
- Exceptions and what a beginner would miss.
- Which decisions software can automate, assist, or leave with the expert.

The resulting artifacts link **evidence → domain rule → requirement → acceptance check**, with stable IDs and decision rationale. If the expert cannot explain a threshold yet, it stays an unresolved question with a way to investigate it. This example illustrates the interview method; it is not evidence for a real project.

Claims remain labeled as observed, reported, inferred, assumed, or unknown. An expert's opinion does not establish market demand, and a generated spec does not establish that software works. Specified, implemented, verified, and delivered are separate states backed by appropriate evidence.

At a pause, [session state](skills/boring-pm/assets/templates/10-session-state.json) records answered questions, evidence and decisions, artifact paths, blocking unknowns, and the next useful question. The agent reads that state before resuming, so the expert does not need to repeat the interview.

## Status and checks

This release focuses on the **skill**, as the foundation for a future Boring PM agent. No standalone Boring PM application, custom Boring UI panels, or SaaS integrations are implemented here.

Research reviewed: **2026-09-11**. Boring UI reference commit: `75b3d051157a32c3f960fa452da54704451fb049`. Refresh framework contracts before coding. The combined protocol is an original synthesis and has not been empirically validated as a complete methodology.

Run offline link/source checks with Python 3.10+:

```bash
python3 scripts/check.py
```

See [validation notes](docs/validation.md) and [publishing instructions](docs/publishing.md). Keep real interviews and project-specific artifacts in the designated private project workspace.

Original material is [MIT licensed](LICENSE). Referenced works retain their own licenses and copyrights.
