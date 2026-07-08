# R223I Local Note Non-Chat Review

## Review Question

Does the bottom input still look like a local supplement, or does it invite open
chat?

## Current Evidence

```text
placeholder = 补充本环节材料限制...
scope = current_section_only
persistence = none
smoke note state = 已暂存到本页内存 · 不写回教案
```

## Judgment

The local note passes the non-chat review.

It does not say:

```text
问我任何问题
继续聊天生成
告诉小教你想怎么改整份教案
重新生成完整教案
```

It is also visually lower weight than the prep canvas and component strip.

## Remaining Risk

The existence of any bottom input can still remind users of a chat composer. The
next stage should keep the label and placeholder tightly scoped, and should not
add open-ended send behavior.

## Decision

```text
LOCAL_NOTE_DECISION = PASS_NON_CHAT_WITH_LABEL_GUARD
```

Future carrier checks should retain:

```text
current section only
no persistence by default
no model submission
no whole-lesson rewrite
```
