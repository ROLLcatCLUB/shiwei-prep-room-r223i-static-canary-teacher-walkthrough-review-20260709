# R223I Static Canary Review Checklist

## Checklist

| Requirement | Evidence From R223H | Result |
| --- | --- | --- |
| Teacher recognizes this as a prep workbench | title, mode rail, lesson canvas, component strip | pass |
| Not mistaken for chat tool | no chat composer, local note is low-weight and scoped | pass |
| Mode states are identifiable | `精备 / 日常 / 快速` visible, daily default, quick switch tested | pass |
| Main prep canvas is easy to find | center canvas and `data-primary-reading-object=true` | pass |
| Focused section is clear | `材料与印痕探究` appears as highlighted section | pass |
| Lesson type guard is visible | paper printing guard retained | pass |
| Daily components understandable | 3 cards show problem and evidence | pass_with_note |
| Quick components understandable | quick mode shows 2 cards | pass |
| Component-evidence relation visible | each card includes evidence output | pass |
| Binding preview selected only | smoke focused `technique_step_demo`; preview updated | pass |
| Local note is non-chat | placeholder says `补充本环节材料限制...`; state says no writeback | pass |
| Components not implied as executable | no real execution controls beyond static confirm/replace/delete labels | pass |
| Quick mode 3-minute readable | concise chain and 2 components | pass |
| Information pressure acceptable | acceptable for static canary, but needs carrier-fit check | pass_with_density_note |

## Density Notes

The canary is small enough to continue, but R223J should specifically test:

1. whether three component cards fit inside an R97B-like carrier without
   crowding the prep canvas;
2. whether the right binding preview should stay as a right panel, inline
   expansion, or drawer;
3. whether source/risk rail can stay visible or should collapse harder by
   default;
4. whether quick mode still feels lighter than daily after carrier constraints.

## Checklist Decision

```text
PASS_CONTINUE_TO_R223J_CARRIER_FIT_CHECK
```
