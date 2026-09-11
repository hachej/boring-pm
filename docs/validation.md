# Skill validation

Reviewed: 2026-09-11.

## Structural checks

- Skill Creator validation passed for the actual personal skill working directory.
- Local Markdown links and section anchors resolve; skill links remain inside the portable folder.
- Source IDs are defined, JSON parses, and no initializer TODO remains.
- The skill contains 29 files and references 28 primary sources. The entry point is 808 words; detailed material is loaded only as needed.

The repository includes `scripts/check.py` for repeatable offline link/source checks. That script does not evaluate external link availability, the truth of claims, or agent behavior.

## Independent use scenarios

An independent agent received the skill and a fictional request, without an expected answer or prior diagnosis. No external actions or production changes were allowed.

**Short expert interview:** a data engineer supplied a recent late-partition incident, their role, the intended user, a ten-minute timebox, and a spec-only boundary. The resulting reply asked one focused question about the evidence behind their judgment and what would have prompted continued investigation. It did not repeat the supplied context, demand broad market research, or begin coding.

**Provisional specification from incomplete notes:** a workshop facilitator requested a spec and Boring UI handoff without more questions, code, or integrations. The agent produced one consolidated specification/handoff and a session-state file. It kept the absent sample output and unchosen OS unresolved, separated user constraints from proposed design decisions, linked requirements to evidence and acceptance scenarios, and marked every product check `not_run`. It distinguished the skill's framework reference from verification of an actual target host. No implementation or external call was made.

The two resulting artifacts were inspected. This scenario also showed that a provisional specification can become lengthy; concision during real sessions remains something to observe. No claim is made that these two cases cover the full behavior of the skill.

## Limits

These are small forward-use checks with fictional requests. They do not demonstrate performance with real experts, sustained multi-session recall, correctness of an implemented product, or deployed Boring UI compatibility. The ACTA paper and other method sources do not validate the combined Boring PM protocol. Evaluate real sessions and outcome artifacts before making such claims.
