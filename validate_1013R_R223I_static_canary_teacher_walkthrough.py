import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
checks = []


def check(name, cond, detail=""):
    checks.append({"name": name, "passed": bool(cond), "detail": detail})


def text(name):
    return (ROOT / name).read_text(encoding="utf-8")


docs = {
    "script": text("R223I_teacher_walkthrough_script.md"),
    "checklist": text("R223I_static_canary_review_checklist.md"),
    "readability": text("R223I_teacher_readability_review.md"),
    "friction": text("R223I_component_suggestion_friction_review.md"),
    "local_note": text("R223I_local_note_non_chat_review.md"),
    "decision": text("R223I_continue_or_hold_decision.md"),
    "report": text("R223I_report.md"),
    "readme": text("README_FOR_GPT_REVIEW.md"),
}
combined = "\n".join(docs.values())

check("stage id in report", "stage_id=1013R_R223I_STATIC_CANARY_TEACHER_WALKTHROUGH_OR_HOLD" in docs["report"])
check("status pending review", "status=PASS_LOCAL_PENDING_REVIEW" in docs["report"])

allowed_decisions = [
    "PASS_CONTINUE_TO_R223J_CARRIER_FIT_CHECK",
    "HOLD_FOR_R223H_P1_DENSITY_OR_INTERACTION_REDUCTION",
    "STOP_FORMAL_UI_NOT_READY",
]
decision_matches = re.findall(r"R223I_DECISION = ([A-Z0-9_]+)", combined)
check("decision appears", bool(decision_matches), str(decision_matches))
check("decision allowed", all(item in allowed_decisions for item in decision_matches), str(decision_matches))
check("chosen decision continue", "R223I_DECISION = PASS_CONTINUE_TO_R223J_CARRIER_FIT_CHECK" in combined)
check("other decisions documented", "HOLD_FOR_R223H_P1_DENSITY_OR_INTERACTION_REDUCTION" in combined and "STOP_FORMAL_UI_NOT_READY" in combined)

for boundary in [
    "formal_ui=false",
    "R97B_modified=false",
    "frontend_backend_modified=false",
    "runtime_enabled=false",
    "provider_model_prompt_db=false",
    "formal_apply=false",
]:
    check(f"boundary present: {boundary}", boundary in combined)

for blocked in [
    "formal R223 UI",
    "R97B route/component/CSS changes",
    "frontend/backend implementation",
    "runtime/provider/model/prompt/db",
    "lesson body writeback",
    "real classroom component execution",
    "R224",
    "formal apply",
]:
    check(f"blocked item present: {blocked}", blocked in combined)

required_walkthrough_phrases = [
    "prep workbench",
    "精备 / 日常 / 快速",
    "main prep canvas",
    "材料与印痕探究",
    "lesson type guard",
    "3 current-section components",
    "2 components",
    "evidence output",
    "selected component",
    "local note",
    "real component execution",
    "3-minute readable",
    "density",
    "continue",
]
for phrase in required_walkthrough_phrases:
    check(f"walkthrough covers: {phrase}", phrase in combined)

for result_marker in [
    "pass_with_note",
    "continue_with_density_watch",
    "PASS_WITH_DENSITY_NOTES",
    "PASS_WITH_CARRIER_DENSITY_WATCH",
    "PASS_NON_CHAT_WITH_LABEL_GUARD",
]:
    check(f"nuanced result marker: {result_marker}", result_marker in combined)

for artifact in [
    "R223I_teacher_walkthrough_script.md",
    "R223I_static_canary_review_checklist.md",
    "R223I_teacher_readability_review.md",
    "R223I_component_suggestion_friction_review.md",
    "R223I_local_note_non_chat_review.md",
    "R223I_continue_or_hold_decision.md",
    "R223I_report.md",
    "README_FOR_GPT_REVIEW.md",
]:
    check(f"file exists: {artifact}", (ROOT / artifact).exists())

reference_files = [
    "_REFERENCE_INPUTS/R223H/R223H_static_canary_prototype.html",
    "_REFERENCE_INPUTS/R223H/R223H_fixture_state.json",
    "_REFERENCE_INPUTS/R223H/R223H_screenshot_smoke_result.md",
    "_REFERENCE_INPUTS/R223H/R223H_guard_compliance_check.md",
    "_REFERENCE_INPUTS/R223H/R223H_report.md",
    "_REFERENCE_INPUTS/R223H/validate_1013R_R223H_fixture_only_static_canary_result.json",
]
for rel in reference_files:
    check(f"reference exists: {rel}", (ROOT / rel).exists())

prev_result_path = ROOT / "_REFERENCE_INPUTS/R223H/validate_1013R_R223H_fixture_only_static_canary_result.json"
if prev_result_path.exists():
    prev = json.loads(prev_result_path.read_text(encoding="utf-8"))
    check("R223H validator reference passed", prev.get("passed") is True)
    check("R223H validator reference checks 114", prev.get("check_count") == 114)

smoke_path = ROOT / "_REFERENCE_INPUTS/R223H/R223H_screenshot_smoke_result.json"
if smoke_path.exists():
    smoke = json.loads(smoke_path.read_text(encoding="utf-8"))
    check("R223H smoke reference passed", smoke.get("passed") is True)
    check("R223H smoke daily 3", smoke.get("initial", {}).get("dailyCards") == 3)
    check("R223H smoke quick 2", smoke.get("quick", {}).get("quickCards") == 2)

for forbidden in [
    "R223I authorizes formal UI",
    "formal UI can start",
    "R97B route can be added",
    "provider call allowed",
    "database persistence allowed",
    "write back to lesson body allowed",
]:
    check(f"forbidden assertion absent: {forbidden}", forbidden not in combined)

result = {
    "passed": all(item["passed"] for item in checks),
    "check_count": len(checks),
    "failed": sum(1 for item in checks if not item["passed"]),
    "decision": "PASS_CONTINUE_TO_R223J_CARRIER_FIT_CHECK",
    "failed_checks": [item for item in checks if not item["passed"]],
}
(ROOT / "validate_1013R_R223I_static_canary_teacher_walkthrough_result.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(json.dumps(result, ensure_ascii=False))
raise SystemExit(0 if result["passed"] else 1)
