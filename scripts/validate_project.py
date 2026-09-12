from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md",
    "PROJECT-CONTEXT.md",
    "UKHUWAH-DZAKAIYAH.md",
    "schemas/ids.yaml",
    "schemas/concept.yaml",
    "schemas/theory.yaml",
    "schemas/decision.yaml",
    "schemas/state-transition.yaml",
    "vault/manifest.yaml",
    "benchmarks/benchmark-suite.yaml",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("MISSING:", missing)
    sys.exit(1)
print("Project structure: OK")
