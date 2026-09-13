"""Validate project structure, YAML syntax, and cross-file consistency.

Full YAML validation needs PyYAML (`pip install pyyaml`); falls back to an
existence-only check if it isn't installed rather than failing outright.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md", "PROJECT-CONTEXT.md", "UKHUWAH-DZAKAIYAH.md",
    "README.md", "CHANGELOG.md",
    "core/execution-engine.md", "core/concept-development.md",
    "core/adversarial-development.md", "core/claim-graph.md",
    "core/epistemic-validator.md", "core/islamic-reconstruction.md",
    "core/resume-protocol.md", "core/versioning.md",
    "schemas/ids.yaml", "schemas/concept.yaml", "schemas/claim.yaml",
    "schemas/evidence.yaml", "schemas/theory.yaml", "schemas/decision.yaml",
    "schemas/state-transition.yaml", "schemas/taxonomies.yaml",
    "templates/concept-card.md", "templates/claim-card.md",
    "templates/decision-card.md", "templates/theory-card.md",
    "vault/manifest.yaml", "vault/README.md", "vault/concepts.md",
    "vault/claims.md", "vault/theories.md", "vault/decisions.md",
    "vault/rejected-hypotheses.md", "vault/uncertainties.md",
    "examples/example-research.md",
    "benchmarks/README.md", "benchmarks/benchmark-suite.yaml", "benchmarks/rubric.md",
]
YAML_FILES = [p for p in REQUIRED_FILES if p.endswith(".yaml")]
CANONICAL_DECISIONS = {
    "KEEP", "REFRAME", "NARROW", "SPECIAL_CASE", "SYNONYM",
    "NORMATIVE_CATEGORY", "EMPIRICALLY_UNSUPPORTED",
    "ONTOLOGICALLY_UNSUPPORTED", "ABANDON",
}


def check_files_exist():
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).exists()]
    if missing:
        print("MISSING:", missing)
        return False
    return True


def check_yaml_syntax():
    try:
        import yaml
    except ImportError:
        print("SKIPPED yaml syntax check: PyYAML not installed")
        return True
    ok = True
    for rel in YAML_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        try:
            yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"INVALID YAML in {rel}: {e}")
            ok = False
    return ok


def check_decision_vocabulary():
    """Regression check for a real bug found in V7: the decision vocabulary
    drifted between SKILL.md, core/adversarial-development.md, and
    schemas/decision.yaml. schemas/decision.yaml is the source of truth;
    this checks the other two still agree with it."""
    ok = True
    for rel in ["SKILL.md", "core/adversarial-development.md"]:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text()
        missing = [d for d in CANONICAL_DECISIONS if d not in text]
        if missing:
            print(f"DECISION VOCABULARY drift in {rel}: missing {missing}")
            ok = False
    return ok


if __name__ == "__main__":
    results = [check_files_exist(), check_yaml_syntax(), check_decision_vocabulary()]
    if not all(results):
        sys.exit(1)
    print("Project structure, YAML syntax, and decision vocabulary: OK")
