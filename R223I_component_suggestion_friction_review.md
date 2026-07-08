# R223I Component Suggestion Friction Review

## Review Question

Do the suggested classroom components help the teacher prepare the focused
section, or do they feel like a component marketplace?

## Current Component Set

| Component | Student Problem | Evidence Link | Friction |
| --- | --- | --- | --- |
| 材料盲盒 | students do not feel how materials affect marks | trial sample + material effect record | low |
| 技法拆解 | students may not understand steps, force, order, or common mistakes | step check or error correction | low |
| 学习单记录 | process may happen without durable evidence | material and mark record row | low |

## Strength

The 3 components are tied to one focused section: `材料与印痕探究`. They are not
generic activity buttons. Each includes a student problem and evidence output,
which helps preserve the classroom-component-library principle:

```text
component = classroom action unit with teaching responsibility
not UI widget
not activity name only
```

## Friction Notes

1. Three cards are acceptable in the independent canary, but may feel dense in an
   R97B-like carrier.
2. `确认 / 替换 / 删除` is understandable as future teacher control, but in R223H it
   must remain non-executing.
3. The card text is useful but should not become longer in the next stage.
4. Quick mode's 2-card subset is appropriately lighter.

## Friction Decision

```text
COMPONENT_FRICTION_DECISION = PASS_WITH_CARRIER_DENSITY_WATCH
```

R223J should test whether the component strip needs a more compact card shape or
inline expansion before any formal UI work.
