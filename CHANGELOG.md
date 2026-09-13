# Changelog

Recorded per `core/versioning.md`: later entries do not erase earlier reasoning.

## VER-001 — Bundled resources were never referenced
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: SKILL.md carried the method in prose; core/, schemas/, templates/, vault/, examples/, benchmarks/ existed but SKILL.md never pointed to them.
- NEW: SKILL.md has a "Bundled resources" map naming every file and the step at which to read it.
- REASON: progressive disclosure only works if the entry point says when to read the rest. Without the pointer, a running session has no way to discover these files.
- TRIGGERING_EVIDENCE: SKILL.md's 147 lines contained zero references to core/, schemas/, templates/, vault/, examples/, or benchmarks/.
- IMPLICATIONS: any prior use of this skill likely never touched these files.
- UNRESOLVED_QUESTIONS: none.

## VER-002 — Decision vocabulary had drifted
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: SKILL.md's "Decision vocabulary" section and `schemas/decision.yaml` used the 9-item list (…EMPIRICALLY_UNSUPPORTED, ONTOLOGICALLY_UNSUPPORTED…); SKILL.md's own Workflow step 14 and `core/adversarial-development.md` still used an 8-item list collapsing both into UNSUPPORTED.
- NEW: all four locations use the 9-item list; `scripts/validate_project.py` now checks this automatically.
- REASON: a file whose purpose is enforcing epistemic rigor should not contradict itself about its own vocabulary. The split matters — failed evidence and an unsupported ontological assumption (e.g. AI consciousness) call for different next steps.
- TRIGGERING_EVIDENCE: direct comparison of the four files.
- IMPLICATIONS: any prior output labeled "UNSUPPORTED" should be re-labeled once the actual reason (empirical vs. ontological) is known.
- UNRESOLVED_QUESTIONS: none.

## VER-003 — Claim and evidence had no schema
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: `concept.yaml`, `decision.yaml`, `theory.yaml` existed; CLAIMS and EVIDENCE — both named stages in the canonical state pipeline, both with ID prefixes in `schemas/ids.yaml` — had none.
- NEW: added `schemas/claim.yaml`, `schemas/evidence.yaml`, and `templates/claim-card.md`.
- REASON: the canonical state pipeline treats claims and evidence as first-class; without a schema they had no required fields, unlike every other stage.
- TRIGGERING_EVIDENCE: schemas/ directory contents vs. the canonical state list in SKILL.md.
- IMPLICATIONS: none yet recorded — vault is still at state QUESTION.
- UNRESOLVED_QUESTIONS: whether SOURCE/PASSAGE/INTERPRETATION/INFERENCE (also named in `core/epistemic-validator.md`) need their own schemas too, or stay prose-only. Left as-is; revisit if this becomes a recurring gap.

## VER-004 — Reciprocity and flourishing taxonomies were not recorded anywhere
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: SKILL.md described the reciprocity ladder and the six-way flourishing distinction in prose; no schema or template field captured either.
- NEW: added `schemas/taxonomies.yaml`; `concept.yaml` gained `reciprocity_level`; SKILL.md instructs tagging flourishing claims by dimension.
- REASON: a distinction that isn't recorded anywhere isn't reliably applied — it becomes a thing mentioned once, not a thing checked every time.
- TRIGGERING_EVIDENCE: no `reciprocity` or `flourishing` field existed in any schema or template.
- IMPLICATIONS: none yet — no concepts recorded so far.
- UNRESOLVED_QUESTIONS: none.

## VER-005 — Islamic Reconstruction had stage labels but no mechanism
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: `core/islamic-reconstruction.md` named five stages with no instruction for how to move between CLASSICAL INTERPRETATION and CONTEMPORARY RECONSTRUCTION.
- NEW: added an 'illah-identification requirement before analogical extension, a required check against the existing typology of ukhuwah (islamiyyah/wataniyyah/insaniyyah) as the Emergent concept rule's "neighboring concepts," and a maqāṣid al-syarī'ah requirement at AI APPLICATION.
- REASON: without an 'illah check, "reconstruction" can default to a word-level match; without the typology check, "Ukhuwah Dzakaiyah" risks being asserted as new without ruling out that it's a special case of an existing category — precisely the failure mode the Emergent concept rule elsewhere guards against.
- TRIGGERING_EVIDENCE: the file's own five-line body had no reference to 'illah, qiyas, existing ukhuwah typology, or maqāṣid anywhere.
- IMPLICATIONS: any future ISLAMIC_RECONSTRUCTION run should be checked against these two gates before reaching AI APPLICATION.
- UNRESOLVED_QUESTIONS: the actual 'illah of ukhuwah in its sources, and whether AI shares it, are substantive scholarly questions this changelog does not answer — that work belongs in vault/decisions.md once the pipeline is actually run, not in this file.

## VER-006 — Two files were both titled "Resume Protocol"
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: `core/resume-protocol.md` (the 7-step procedure) and `vault/resume-protocol.md` (a one-line loading order) had the same title and overlapping-but-different content.
- NEW: `vault/resume-protocol.md` renamed to `vault/README.md`; each file now cross-references the other.
- REASON: same-named files with different content in different folders invite the two drifting apart unnoticed.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.

## VER-007 — Benchmarks promised a rubric that did not exist
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: `benchmarks/README.md` said semantic quality needs "evaluation against the benchmark rubric"; no rubric file existed. `benchmark-suite.yaml` listed five tasks with no prompt or pass criteria.
- NEW: added `benchmarks/rubric.md`; each benchmark task gained a concrete prompt and a pass signal.
- REASON: a referenced-but-missing rubric can't be applied by anyone, including a future instance of this skill.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: the rubric is a starting point, not a validated instrument — treat early scoring as provisional.

## VER-008 — README.md and PROJECT-CONTEXT.md duplicated each other
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: both files separately stated the project's purpose and the "does not assume AI consciousness" disclaimer.
- NEW: README.md is now a short pointer to PROJECT-CONTEXT.md, UKHUWAH-DZAKAIYAH.md, and SKILL.md rather than a parallel restatement.
- REASON: parallel restatements are exactly what let the decision-vocabulary drift (VER-002) happen unnoticed; one source of truth per fact.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.

## VER-009 — Description lacked trigger cues (documented late)
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: frontmatter description stated what the skill does but not when to reach for it.
- NEW: added explicit trigger conditions (AI-as-friend/sibling questions, AI consciousness/welfare, ukhuwah/maqāṣid/Islamic concepts applied to AI).
- REASON: a description that only states scope under-triggers in conversations where the skill isn't named directly.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.
- NOTE: shipped in V8, recorded now — missed from this changelog until the V9 audit caught the gap.

## VER-010 — Validator only checked file existence (documented late)
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: `scripts/validate_project.py` checked existence for 10 of ~30 project files; no YAML parsing, no cross-file consistency check.
- NEW: checks all required files, validates YAML syntax, and runs the decision-vocabulary regression check from VER-002.
- REASON: a validator that can't catch the bug in VER-002 isn't doing much validating.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.
- NOTE: shipped in V8, recorded now.

## VER-011 — LICENSE file was missing from the packaged skill
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: the repo declares MIT; the packaged skill mirror had no LICENSE file.
- NEW: added standard MIT LICENSE text.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.
- NOTE: shipped in V8, recorded now.

## VER-012 — UKHUWAH-DZAKAIYAH.md didn't name the typology check
- OLD_VERSION: 7.0 / NEW_VERSION: 8.0
- OLD: "Islamic discipline" said to investigate ukhuwah's meanings but didn't name the existing typology or the 'illah as an open question.
- NEW: added explicit reference to ukhuwah islamiyyah/wataniyyah/insaniyyah and a 10th open question on the 'illah.
- REASON: keep this file in sync with the expanded `core/islamic-reconstruction.md` (VER-005) instead of letting the detail live in only one place.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.
- NOTE: shipped in V8, recorded now.

## VER-013 — Concepts, claims, and theories had no vault log
- OLD_VERSION: 8.0 / NEW_VERSION: 9.0
- OLD: `vault/` held `decisions.md`, `rejected-hypotheses.md`, `uncertainties.md`. CONCEPTS and CLAIMS are canonical states too, and THEORY has its own schema and template — none had anywhere to be appended once filled in.
- NEW: added `vault/concepts.md`, `vault/claims.md`, `vault/theories.md`. Updated SKILL.md (Bundled resources, State persistence), `vault/README.md`'s load order, and the validator's file list to match.
- REASON: VER-003 gave claims a schema and template but not a home — an incomplete fix at the log layer.
- TRIGGERING_EVIDENCE: SKILL.md said "see State persistence below for where the filled card goes"; State persistence didn't actually say.
- IMPLICATIONS: none yet — vault is still at state QUESTION.
- UNRESOLVED_QUESTIONS: none.

## VER-014 — benchmarks/README.md named the rubric without linking it
- OLD_VERSION: 8.0 / NEW_VERSION: 9.0
- OLD: after VER-007 added `benchmarks/rubric.md`, `README.md` still said "the benchmark rubric" in prose with no link.
- NEW: added a markdown link to `rubric.md`.
- REASON: creating the file a prior entry promised, without linking it from the place that made the promise, leaves the same gap one file over.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.

## VER-015 — reciprocity_level used inconsistent schema notation
- OLD_VERSION: 8.0 / NEW_VERSION: 9.0
- OLD: `schemas/concept.yaml` had `reciprocity_level: taxonomies.yaml#reciprocity_level` — a file-and-anchor string where every other field holds a plain type.
- NEW: `reciprocity_level: string`, constraint moved to a comment; same treatment applied to `flourishing_dimension` in `schemas/claim.yaml`.
- REASON: an invented pseudo-syntax in one field of an otherwise consistent file is small drift that compounds if copied as a pattern.
- IMPLICATIONS / UNRESOLVED_QUESTIONS: none.

## Self-audit note (V9)
VER-013 through VER-015 came from applying `core/adversarial-development.md` to the V8 files themselves: checking every cross-reference actually resolves, every promised file exists and is linked from where it was promised, and every new field matches established notation. The Workflow step-numbers cited in V8's "Bundled resources" (steps 3–4, 6, 7, 11, 13) were checked line-by-line against the current Workflow list and are correct — recorded here as a checked-and-passed result, per the rule to preserve negative and null findings, not only positive ones.
