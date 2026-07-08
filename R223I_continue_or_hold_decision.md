# R223I Continue Or Hold Decision

## Allowed Decision Values

R223I must choose exactly one:

```text
PASS_CONTINUE_TO_R223J_CARRIER_FIT_CHECK
HOLD_FOR_R223H_P1_DENSITY_OR_INTERACTION_REDUCTION
STOP_FORMAL_UI_NOT_READY
```

## Decision

```text
R223I_DECISION = PASS_CONTINUE_TO_R223J_CARRIER_FIT_CHECK
```

## Why Continue

R223H remains inside the R223G canary boundary:

- fixture-only state;
- independent static HTML;
- no R97B route/component/CSS;
- no formal frontend/backend implementation;
- no provider/model/runtime/prompt/db;
- no lesson body writeback;
- no real component execution;
- no formal apply.

Teacher-facing readability is acceptable:

- the page reads as a prep workbench, not chat;
- mode switch is understandable;
- main prep canvas is visible;
- focused section is clear;
- daily and quick component limits are preserved;
- right binding preview is selected-component-only;
- local note is scoped and non-chat.

## Why Not Hold

The density concerns are real but not severe enough to require an R223H-P1
reduction before carrier-fit checking. They are exactly the kind of questions a
carrier-fit check should answer:

1. whether right binding preview remains useful in constrained width;
2. whether daily 3-card component strip needs compact card treatment;
3. whether source/risk rail should collapse more aggressively;
4. whether quick mode remains lighter in the actual carrier.

## Why Not Formal UI

R223I explicitly does not authorize formal UI. It only allows the next static
review step:

```text
NEXT_ALLOWED = R223J_CARRIER_FIT_CHECK
R223_FORMAL_UI = BLOCKED
R97B / UI / runtime / prompt / model / db = UNTOUCHED
```

## Stop Conditions For R223J

R223J must stop or hold if carrier-fit checking requires:

- R97B route/component/CSS modification;
- frontend/backend implementation;
- runtime/provider/model/prompt/db;
- lesson body writeback;
- real component execution;
- formal apply.
