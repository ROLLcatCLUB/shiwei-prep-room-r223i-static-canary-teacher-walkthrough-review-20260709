# R223I Teacher Walkthrough Script

```text
stage_id=1013R_R223I_STATIC_CANARY_TEACHER_WALKTHROUGH_OR_HOLD
status=static_canary_teacher_walkthrough_only
formal_ui=false
R97B_modified=false
frontend_backend_modified=false
runtime_enabled=false
provider_model_prompt_db=false
formal_apply=false
```

## Walkthrough Purpose

R223I reviews the R223H fixture-only static canary from a teacher's point of
view. It does not add UI, change R97B, connect runtime, or expand interaction.

The question is:

> Does the teacher understand what this surface is for quickly enough that the
> project can continue to a narrow carrier-fit check, or should it hold for
> density and interaction reduction?

## Walkthrough Steps

| Step | Teacher Task | Expected Signal | R223I Judgment |
| --- | --- | --- | --- |
| 1 | Open the canary and identify the page type | Sees a prep workbench for `有趣的纸印`, not a chat page | pass |
| 2 | Identify current mode | Sees `精备 / 日常 / 快速` and the active daily state | pass |
| 3 | Find the main prep canvas | Center canvas is visually dominant and labeled with lesson title | pass |
| 4 | Find the focused section | `材料与印痕探究` is visible and embedded in the canvas | pass |
| 5 | Understand the lesson type guard | Sees paper printing must preserve material, mark, technique, and evidence | pass |
| 6 | Read daily component suggestions | Sees 3 current-section components, not a full component shelf | pass_with_note |
| 7 | Switch to quick mode | Sees 2 components and a concise 3-minute readable chain | pass |
| 8 | Focus one component | Binding preview changes only for selected component | pass |
| 9 | Interpret binding preview | Sees screen prompt, learning sheet, teacher language, and evidence | pass_with_note |
| 10 | Inspect local note | Placeholder and state show local supplement only, not chat | pass |
| 11 | Check execution expectation | No wording implies real component execution or runtime generation | pass |
| 12 | Judge density | Page is readable, but right binding + 3 components still needs carrier-fit review | continue_with_density_watch |

## Walkthrough Decision

```text
DECISION = PASS_CONTINUE_TO_R223J_CARRIER_FIT_CHECK
```

R223I does not authorize formal UI. It only says R223H is clear enough to be
checked against a future carrier fit. The next step should still be static,
read-only, and non-runtime.
