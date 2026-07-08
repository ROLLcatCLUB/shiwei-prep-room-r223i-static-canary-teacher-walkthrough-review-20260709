# R223H Screenshot Smoke Result

stage_id: `1013R_R223H_FIXTURE_ONLY_STATIC_CANARY_PROTOTYPE`

status: `PASS`

## Smoke Target

- URL: `http://127.0.0.1:8793/R223H_static_canary_prototype.html`
- Screenshot: `R223H_static_canary_screenshot.png`
- Result JSON: `R223H_screenshot_smoke_result.json`
- Viewport requested: `1440 x 1000`

## Verified Signals

| Check | Result |
| --- | --- |
| Static stage marker is `R223H` | PASS |
| Fixture-only marker is true | PASS |
| Independent static HTML marker is true | PASS |
| R97B modified marker is false | PASS |
| Formal frontend/backend marker is false | PASS |
| Runtime marker is false | PASS |
| Provider/model/prompt/db marker is false | PASS |
| Lesson body writeback marker is false | PASS |
| Formal apply marker is false | PASS |
| Minimum required slots are present | PASS |
| Daily default renders 3 component cards | PASS |
| Quick mode switch renders 2 component cards | PASS |
| Selected component binding updates to `technique_step_demo` | PASS |
| Source/risk slot is readonly high-risk hint only | PASS |
| Binding preview is selected-component-only | PASS |
| Local note is current-section-only and non-persistent | PASS |
| No forbidden chat or component shelf text found | PASS |
| No horizontal overflow in smoke viewport | PASS |
| Screenshot was created and nonempty | PASS |

## Smoke Data

```json
{
  "passed": true,
  "dailyCards": 3,
  "quickCards": 2,
  "selectedBindingAfterFocus": "technique_step_demo",
  "noteState": "已暂存到本页内存 · 不写回教案",
  "bodyScrollWidth": 1265,
  "bodyClientWidth": 1265,
  "screenshotBytes": 122105
}
```

## Boundary Note

This smoke check validates only the independent static canary prototype. It does
not modify R97B, application frontend/backend, runtime, provider/model, prompt,
database, lesson body, classroom component runtime, or formal apply paths.
