# Maintain the public repository

Public repository: [hachej/boring-stack](https://github.com/hachej/boring-stack). Default branch: `main`.

The portable skill lives in `skills/boring-pm`. Keep its references and templates together when copying or installing it. Repository documentation explains the structure; the skill entry point controls agent behavior.

## Publish changes

Use an authenticated checkout of the repository. Inspect the current branch, remote state, and any existing edits before changing files. Preserve unrelated work and use the user's authorized branch or pull-request workflow.

Before committing changes to the skill or its references, run:

```bash
python3 scripts/check.py
```

Review the diff, commit the intended files, and push without forcing the branch. When using the GitHub API, build changes on the current branch commit and use a non-forced ref update so concurrent work is preserved.

Verify the remote commit and changed file contents after publishing. Keep real interviews, credentials, and unpublished project plans in the designated private project workspace.
