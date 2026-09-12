# Boring PM

**A skill that interviews experts, explores solutions that fit them, and turns the chosen approach into a buildable software specification.**

Boring PM establishes the person's technical comfort and desired involvement, guides them through a real case, and uncovers the judgment behind their work. It compares solutions for the actual users and available support, then writes testable requirements with a [Boring UI](https://github.com/hachej/boring-ui) implementation handoff.

## Use the skill

The complete portable skill is in [skills/boring-pm](skills/boring-pm/SKILL.md). Its entry point is `SKILL.md`; supporting references and templates travel with it.

Invoke it in a host where it is installed:

> Use $boring-pm to understand my technical comfort, explore solutions that fit me, and turn the best-supported approach into a Boring UI specification.

Or ask an agent with repository access to read `skills/boring-pm/SKILL.md` and use it for the task. In a chat-only environment, supply that file and the relevant bundled references as context. Tools and persistent storage depend on the host.

The skill honors the requested stopping point. It can focus on the interview, produce a provisional spec from existing notes, or continue into an authorized build and user trial. It does not launch an application or install external integrations by itself.

## What is included

- A compact skill entry point with adaptive interview and evidence rules.
- Ten knowledge modules covering outcomes, interviewing, tacit knowledge, evidence synthesis, scope, requirements, validation, delivery, user profiling, and solution exploration.
- A workflow and question bank that avoid forcing the expert through a long questionnaire.
- Twelve templates for briefs, evidence, domain rules, solution comparisons, experiments, specs, handoffs, private user profiles, and resumable session state.
- A fictional end-to-end example that distinguishes reported evidence, product decisions, and unrun acceptance checks.
- A verified Boring UI reference and a short optional tool note covering Canva, Craft, and Figma.

The [source register](skills/boring-pm/references/sources.md) contains 31 primary sources: PM and interviewing guidance, original ACTA research, requirements and usability methods, upstream framework files, and optional provider documentation. It is also available as [JSON](skills/boring-pm/references/sources.json).

## Skill structure

The skill has a compact instruction file supported by a knowledge base and reusable templates. The agent loads detailed material when the current task needs it.

| Part | Location | Responsibility |
| --- | --- | --- |
| Core instructions | [SKILL.md](skills/boring-pm/SKILL.md) | Establish technical comfort, ask one main question at a time, reuse previous answers, explore suitable solutions, and respect the requested stopping point. |
| Adaptive workflow | [workflow.md](skills/boring-pm/references/workflow.md) | Define each stage's purpose, output, and conditions for moving forward or revisiting an earlier decision. |
| Knowledge base | [References and source register](skills/boring-pm/references/sources.md) | Support the interview-to-product workflow, user adaptation, and solution comparison with attributed methods and original Boring PM procedures. |
| Output templates | [Template index](skills/boring-pm/assets/templates/index.md) | Provide twelve reusable formats for project artifacts, including profiles, decisions, and resumable session state. Small projects can consolidate them. |
| Implementation references | [Boring UI](skills/boring-pm/references/boring-ui.md) and [tool choices](skills/boring-pm/references/tools.md) | Map the specification to verified framework capabilities and consider optional Canva, Craft, or Figma support when useful. |

The core, references, and templates all live inside `skills/boring-pm`, so copying that directory preserves the complete skill. Project-specific interview records and specifications belong in the user's separate project workspace.

## Technical comfort and solution exploration

When the person's technical comfort is unknown, the first discovery question is:

> What are you comfortable doing with software today—for example, using apps, setting up workflows, or writing code?

If already answered, the skill uses that context. It then builds a [correctable profile](skills/boring-pm/references/user-profile.md) of concrete experience, desired involvement, explanation preferences, and relevant support. Coding ability, domain expertise, and willingness to maintain software stay separate. A programmer may want a hands-off result; a noncoding expert may have an implementation team. The interviewee's profile is also separate from the product audience's needs.

[Solution exploration](skills/boring-pm/references/solution-exploration.md) compares different ways to complete the same task. The agent presents concrete alternatives at the person's preferred level of detail, checks the assumption most likely to change the choice, and recommends the best-supported fit with tradeoffs and a reconsideration trigger. It respects an explicit Boring UI constraint while comparing workflows and degrees of automation within it.

Profiles and considered options are linked from session state for later correction and reuse. Real profiles stay in the designated private project workspace. The skill provides the format and workflow; automatic identity, profile storage across projects, and application integrations depend on the host.

## How the interview becomes a product

The workflow moves through nine stages: **frame, reconstruct, extract, choose, test, specify, build, try, and deliver**. It can move backward when new evidence changes an earlier decision. The default endpoint is a product specification and Boring UI implementation handoff; building and delivery continue when included in the user's request.

The central behavior is turning expert judgment into explicit, testable behavior. For example, if an expert says, "I can tell when a dataset looks wrong," the agent explores:

- A recent case where that happened.
- The signals they noticed and alternatives they considered.
- Exceptions and what a beginner would miss.
- Which decisions software can automate, assist, or leave with the expert.

The resulting artifacts link **evidence → domain rule → requirement → acceptance check**, with stable IDs and decision rationale. If the expert cannot explain a threshold yet, it stays an unresolved question with a way to investigate it. This example illustrates the interview method; it is not evidence for a real project.

Claims remain labeled as observed, reported, inferred, assumed, or unknown. An expert's opinion does not establish market demand, and a generated spec does not establish that software works. Specified, implemented, verified, and delivered are separate states backed by appropriate evidence.

At a pause, [session state](skills/boring-pm/assets/templates/10-session-state.json) records answered questions, evidence and decisions, profile paths and revisions, considered options, artifact paths, blocking unknowns, and the next useful question. The agent reads that state before resuming, so the expert does not need to repeat the interview.

## Status and checks

This release focuses on the **skill**, as the foundation for a future Boring PM agent. No standalone Boring PM application, custom Boring UI panels, or SaaS integrations are implemented here.

Initial research reviewed: **2026-09-11**. Profiling and solution-exploration research added: **2026-09-12**. Boring UI reference commit: `75b3d051157a32c3f960fa452da54704451fb049`. Refresh framework contracts before coding. The combined protocol is an original synthesis and has not been empirically validated as a complete methodology.

Run offline link/source checks with Python 3.10+:

```bash
python3 scripts/check.py
```

See [validation notes](docs/validation.md) and [publishing instructions](docs/publishing.md). Keep real interviews and project-specific artifacts in the designated private project workspace.

Original material is [MIT licensed](LICENSE). Referenced works retain their own licenses and copyrights.
