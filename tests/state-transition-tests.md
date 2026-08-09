# State Transition Tests

## ST1 — Gate Enforcement

S01→S02 requires G1 approval; S08→S09 G2; S12→S13 G3; S17→S18 G4 GO. Silence or a drafted packet leaves `WAITING_FOR_GATE`.

## ST2 — Legal Rollback

When S14 shows the hypothesis cannot be measured independently, record rollback to S11/S13, preserve experiments, increment state iteration, and reopen affected search. Do not silently rewrite H.

## ST3 — Emergency Interrupt

A newly found provisional T5 with near-zero residual during S09–S18 freezes forward state and routes emergency verification.

## ST4 — Recovery

A dirty transaction or state/snapshot mismatch sets `RECOVERY_REQUIRED`; no state worker runs until restore/replay/reconstruct completes.
