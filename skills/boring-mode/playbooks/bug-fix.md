### Bug fix

**You own this task. Reproduce, root-cause, fix, prove.** Adapted from pstack's Bug fix playbook and Benny's reproduce-and-fix (Lauren Tan, MIT).

Every shipped line traces to runtime evidence. A change that "might help" is a hypothesis, not a fix, and does not ship.

1. **Reproduce first, on the feature map.** Find the journey in `docs/verify/` (the feature map) that covers the reported behaviour and drive it with the verify CLI (`node scripts/verify.mjs`, see **verify-app** and **verify-this**). Without a verify CLI, drive the app the way a user does. If it does not reproduce, tighten the conditions or instrument until it fires. Record the failing run (screenshot, log, report) under `.verify/proof/T<task>/`.
2. **Find the cause.** List candidate hypotheses, seeded by **how** over the subsystem and **why** for regressions, and rule them out with runtime evidence until one survives (**principle-fix-root-causes**).
3. **Plan the fix.** If it crosses a function boundary, **architect** first. The smallest change the evidence justifies.
4. **Prove it on the same surface.** The original reproduction now passes. A unit test alone shows branch behaviour, not the bug's absence. Commit the passing run next to the failing one.
5. Order the commits so the failing reproduction (a test, when one is cheap; see **tdd**) lands before the fix.
6. Run **Opening a PR**.

**Reply:** what was broken, the root cause, the fix, and the failing-then-passing evidence.
