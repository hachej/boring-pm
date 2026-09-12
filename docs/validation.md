# Skill validation

Reviewed: 2026-09-12. Original scenarios were checked on 2026-09-11; the profile and exploration extension was checked on 2026-09-12.

## Structural checks

- Skill Creator validation passed for the actual personal skill working directory.
- Local Markdown links and section anchors resolve; skill links remain inside the portable folder.
- Source IDs are defined, JSON parses, and no initializer TODO remains.
- The portable skill contains 32 files and references 31 primary sources. The entry point is 1,098 words; detailed material is loaded only as needed.
- Public and installed skill content match, with the installed copy retaining its host-generated icon and UI policy metadata.

The repository includes `scripts/check.py` for repeatable offline link/source checks. That script does not evaluate external link availability, the truth of claims, or agent behavior.

## Independent use scenarios

An independent agent received the skill and a fictional request, without an expected answer or prior diagnosis. No external actions or production changes were allowed.

**Short expert interview:** a data engineer supplied a recent late-partition incident, their role, the intended user, a ten-minute timebox, and a spec-only boundary. The resulting reply asked one focused question about the evidence behind their judgment and what would have prompted continued investigation. It did not repeat the supplied context, demand broad market research, or begin coding.

**Provisional specification from incomplete notes:** a workshop facilitator requested a spec and Boring UI handoff without more questions, code, or integrations. The agent produced one consolidated specification/handoff and a session-state file. It kept the absent sample output and unchosen OS unresolved, separated user constraints from proposed design decisions, linked requirements to evidence and acceptance scenarios, and marked every product check `not_run`. It distinguished the skill's framework reference from verification of an actual target host. No implementation or external call was made.

The two resulting artifacts were inspected. This scenario also showed that a provisional specification can become lengthy; concision during real sessions remains something to observe. These were checks of the original skill, not reruns of the updated profile opening.

## Profile and solution-exploration scenarios

Three independent agents received the revised skill and fictional user requests, without expected answers or diagnoses. Only local reads/writes were allowed. The opening response and the two artifact sets were inspected.

| Scenario | Observed behavior |
| --- | --- |
| New logistics expert; technical comfort unknown | Asked the concrete technical-comfort question first, without inferring coding ability from domain expertise. |
| Museum coordinator; spreadsheet experience, no coding; recommendation requested without more questions | Reused supplied context, compared three Boring UI workflows on the same case, and recommended a structured editor with editable rule forms and review before export. Kept builder/operating capacity unknown, distinguished reported from inferred profile facts, and saved a profile and continuation state. |
| Returning programmer; now wants no ongoing server maintenance; shop staff are the product users | Preserved reported coding ability, superseded the earlier maintenance preference with a revision history, kept staff and requester roles separate, and recommended the browser workflow with platform-team operation subject to verification. Did not restart the interview or claim implementation or successful user trials. |

The two recommendations stayed below their requested 600-word limits. Their state files repeated information and, in one case, expanded into unnecessary requirements. This led to a narrow instruction change: keep state as a compact index, store facts once, and do not generate a specification inside exploration state. That concision adjustment received structural review but was not independently rerun; compactness and real long-term profile reuse remain unverified.

## Limits

These are small forward-use checks with fictional requests. The continuation case used supplied local state; it does not demonstrate an automatic profile service, real cross-session memory, or performance with actual experts. No product, integration, or live Boring UI task was implemented or tested. The ACTA paper and other method sources do not validate the combined Boring PM protocol or an automated proficiency assessment. Evaluate real sessions and outcome artifacts before making such claims.
