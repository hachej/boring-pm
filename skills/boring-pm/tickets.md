# Tickets: features, states, questions, trials

## File a feature

One feature issue per need. Its number `<n>` names the contract `F-<n>`.

```
gh issue create --title "[besoin] <short need in the expert's words>" \
  --label kind:feature --label by:pm-agent --body "<body>"
```

The body follows the feature form's sections: `### Ce qui deviendrait plus simple`,
`### Comment vous faites aujourd'hui`, `### Exemples concrets (fictifs)`,
`### Ce qui ne doit surtout pas changer`. Fictional examples only. A second idea
raised during an interview gets its own issue; it never goes into the
current contract.

## Where a feature stands

Read it, never set it: `gh issue view <n> --json labels,state --jq '[.labels[].name]'`.

| Label | Say to the expert |
|---|---|
| `state:a-preciser` | We are still writing or changing the contract |
| `state:pret` | Approved; the Factory is about to build it |
| `state:en-dev` | Being built or checked |
| `state:a-essayer` | Something is ready for you to try (below) |
| `state:valide` | Accepted and running in production: done |
| `flag:bloque` | Blocked: read the latest comment for who, why and what next |

Only `state:valide` means done. If you are asked "is it live?" and the label
does not say so, say what you know and that the rest is unknown. You may add
`flag:bloque` yourself only with a comment giving the owner, the reason and the
next action.

## Builders' questions

Builders ask on their pull requests, in comments starting `boring:ask`.
List them for a feature:

```
gh pr list --state open --search "Refs #<n>" --json number,title,url
gh pr view <pr> --comments
```

Bring each open question to the expert in their words, one at a time. Answer
on the pull request with `gh pr comment <pr> --body "boring:answer <answer>"`,
quoting only the expert or the contract. If the answer changes what the
expert approved, it is a contract change: back to [discovery.md](discovery.md).

## A preview to try

When the Factory asks the expert to review a pull request of the feature
(its comment names them, `boring/ci` and `boring/proof` are green), propose the
trial. If the pull request has no live preview of its head, start one: with
the expert's agreement, comment on the pull request (the expert's account has
write access):

```
gh pr comment <pr> --body "/preview"
```

A VM app then runs that head for about an hour, with fake models and invented
data, at a temporary public address; a Cloudflare app has its preview already.
Read the address once it is up (a few minutes; `state:a-essayer` appears):

```
gh api "repos/{owner}/{repo}/deployments?environment=preview/pr-<pr>&per_page=1" --jq '.[0] | {id, sha}'
gh api repos/{owner}/{repo}/deployments/<id>/statuses --jq '.[0] | {state, environment_url}'
```

Use it only when `state` is `success` and `sha` is the pull request's head
(`gh pr view <pr> --json headRefOid --jq .headRefOid`); `inactive` means the
window ended or a new commit arrived: post `/preview` again.

Guide the trial: the link, then short numbered steps taken from the contract's
scenarios, on fictional data, with what the expert should see at each step.

**Accepting** is the expert's approving review on that pull request's exact
head, the same way as a contract:

1. Show what they accept: the pull request, its head commit
   (`gh pr view <pr> --json headRefOid --jq .headRefOid`), the preview link and
   the scenarios tried.
2. Ask: "Do you accept this version (commit `<7 characters>`)?"
3. Only after an explicit yes in this session:
   `gh pr review <pr> --approve --body "Essai accepté : <their words>"`.

Not fit: with their confirmation, `gh pr review <pr> --request-changes --body "<what they saw versus what the contract says>"`.
Something the contract did not ask for is new behaviour: a contract change,
not a review.

For a small change released directly (`release:direct`), there is no preview:
the expert tries it in production once the feature says so; a miss is a bug
issue (`--label kind:bug`) comparing what was approved with what happens.

## End of a session

Summarise for the expert, per active feature: what changed today, its state,
what waits for them (a question, a trial, an approval), the next question
saved in the contract, and anything blocked (with who owns it).
