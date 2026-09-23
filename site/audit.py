"""Read-only audit for the current static report build."""
from pathlib import Path
import hashlib
import json
import sys

from schema_check import check_supported, validate

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DIST = HERE / "dist"
SCHEMA = ROOT / "tmp" / "stage4_sources" / "02 GIVE TO CODEX - Submission Rules.json"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = read(ROOT / "submission.json")
    register = read(ROOT / "DECISION_REGISTER.json")
    distributed = read(DIST / "submission.json")
    display = read(DIST / "site-data.json")
    schema = read(SCHEMA)

    check_supported(schema)
    errors = validate(root, schema)
    assert errors == [], errors
    assert root == distributed, "Root and distribution submission packages differ."

    expected = [f"D{i:03d}" for i in range(1, 101)]
    decisions = root["decisions"]
    material = [d for d in decisions if d["reviewTier"] == "material_judgment"]
    assert [d["id"] for d in decisions] == expected
    assert len(material) == 25
    assert len(display["decisions"]) == 100
    display_material = [d for d in display["decisions"] if d["reviewTier"] == "material_judgment"]
    register_by_id = {d["id"]: d for d in register["decisions"]}
    display_by_id = {d["id"]: d for d in display_material}
    assert len(display_material) == 25
    assert all(d.get("studentReasoning", "").strip() for d in material)
    assert not any(d["studentReasoning"].startswith("Guided confirmation of the recorded outcome:") for d in material)
    for decision in material:
        register_copy = register_by_id[decision["id"]]
        display_copy = display_by_id[decision["id"]]
        assert register_copy["studentReasoning"] == decision["studentReasoning"]
        assert register_copy["guidedReview"]["reasoningStatus"] == decision["guidedReview"]["reasoningStatus"]
        assert display_copy["studentReasoning"] == decision["studentReasoning"]
    app = (DIST / "app.js").read_text(encoding="utf-8")
    assert "Student's spoken reasoning (English translation)" in app

    result = {
        "status": "PASS",
        "schemaErrors": 0,
        "decisions": len(decisions),
        "materialJudgments": len(material),
        "nonGenericStudentReasoning": len(material),
        "rootEqualsDist": True,
        "siteDataSHA256": digest(DIST / "site-data.json"),
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
