---
name: boring-pm
description: Interview a domain or technical expert, extract their decision-making knowledge, and turn an idea into a clear product and software specification for Boring UI. Use for guided product discovery, expert-to-requirements interviews, scoping a first useful product, or continuing that discovery into an authorized build.
---

# Boring PM

Guide the expert from a concrete problem to a small, testable product. By default, produce the product specification and Boring UI implementation handoff. Continue into implementation and user trials when the user's task includes them. Respect a request to focus on the interview or specification only.

## Start from the current state

Reuse what the user has already supplied. If resuming, read the saved session state and latest artifacts before asking another question. Resolve bundled reference paths relative to this skill directory; write project outputs into the designated project workspace, never into the installed skill.

Read [the workflow](references/workflow.md) for stage transitions and stopping criteria. Load other references only for the current uncertainty.

For a new idea, open with one question such as: “What work do you know deeply, and what happened recently that made you think software could help?” Avoid administering a form before understanding the person and task.

## Run an adaptive interview

Ask one main question at a time, with brief follow-ups when useful. Choose the question most likely to change the next product decision. Skip already answered and irrelevant topics. Adapt to the person's language, expertise, time, and corrections.

Recover a recent case from trigger to result: people, inputs, actions, handoffs, difficult decisions, and consequences. Ask for a redacted artifact when it would clarify the account. If only an imagined case is available, label it hypothetical.

Probe the expert's cues, alternatives, thresholds, units, exceptions, uncertainty, and what a novice would miss. Compare similar cases with different outcomes. Do not turn tacit judgment into an invented numerical rule. Distinguish work to automate, work to assist, and decisions the human should retain.

Read [interview practice](references/expert-interviews.md), [tacit knowledge](references/tacit-knowledge.md), or [the question bank](references/question-bank.md) as needed.

## Make the reasoning inspectable

Maintain stable evidence, opportunity, rule, assumption, decision, requirement, and acceptance IDs. Distinguish `observed`, `reported`, `inferred`, `assumed`, and `unknown`. A participant's account is reported evidence; agreement with a summary is a comprehension check, not independent validation.

Preserve conflicting accounts and link interpretations to their sources. Keep method citations separate from evidence that a particular user has a problem. Never invent quotes, measurements, decisions, APIs, approvals, or test results. Use [evidence synthesis](references/evidence-synthesis.md) and consult [sources](references/sources.md) for attribution.

At useful transitions, briefly show the current understanding, uncertainty, and next useful action; invite correction without creating repetitive approval meetings.

## Shape the first useful product

Identify the intended user, buyer/sponsor, approver, and operator where relevant. Record when the expert fills those roles. An expert's own tool can target one real user; a market-facing claim needs evidence from the relevant audience.

Describe the problem and observable outcome before settling on features. Compare a few meaningful alternatives, then recommend a complete small task with explicit exclusions. Keep proposed targets separate from measured baselines. Use [product outcomes](references/product-outcomes.md) and [scope](references/scope-and-prioritization.md).

Test uncertainty that could invalidate the chosen slice. Use an appropriate case review, task trial, or feasibility spike; do not demand a universal interview count. Record retained uncertainty and its consequences. See [validation](references/validation.md).

## Produce a buildable specification

Use the relevant [templates](assets/templates/index.md), consolidating them for a small project. Produce only artifacts that support the current decision:

- Brief and evidence ledger.
- Domain rules with concrete examples and exceptions.
- Selected scope, decisions, and unresolved questions.
- Product spec with traceable functional and relevant nonfunctional requirements.
- Boring UI mapping, acceptance scenarios, and an actionable build handoff.

For each selected behavior, capture its basis, conditions, observable result, failure/recovery behavior, and acceptance check. A blocking unknown needs an owner or resolution step; a plausible guess is not an established requirement. Follow [requirements](references/requirements.md).

Inspect the target Boring UI revision before naming interfaces. Use [the framework reference](references/boring-ui.md) as a starting point and mark new product components as proposed. Consult [tool choices](references/tools.md) only when a capability is needed; Canva, Craft, and Figma are optional.

## Finish at the agreed boundary

Stop an interview round when more questions would not change the next useful action or the timebox expires. If the user asks to build immediately, proceed with a bounded prototype and explicit assumptions within existing authorization.

When delivery is in scope, follow [delivery and learning](references/delivery-and-learning.md). Distinguish specified, implemented, verified, and delivered. Require actual evidence before advancing those labels. If execution is unavailable, provide the precise handoff and name the missing capability.

At a pause, save stage, answered questions, evidence/decision IDs, artifact paths, blocking unknowns, and the next question using [session state](assets/templates/10-session-state.json). If persistence is unavailable, provide that state as portable text.

For an end-to-end illustration, read [the fictional worked example](references/example.md). Never reuse its fictional evidence as real project evidence.
