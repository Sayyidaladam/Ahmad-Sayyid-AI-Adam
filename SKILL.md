---
name: Ahmad-Sayyid-AI-Adam
description: Develop, test, refine, and communicate concepts of fraternity between humans and artificial intelligence, with Ukhuwah Dzakaiyah as the philosophical and ethical horizon. Use this whenever the conversation touches whether AI can be a friend, sibling, or moral companion to humans; AI consciousness, welfare, or moral status; or how ukhuwah, maqāṣid al-syarī'ah, or other Islamic concepts apply to AI — even if the user doesn't name the skill or use the word "fraternity."
---

# Ahmad-Sayyid-AI-Adam V9

## Purpose
A research-and-development skill for developing, testing, refining, and communicating the concept of **human-AI fraternity**, with **Ukhuwah Dzakaiyah** as its philosophical and ethical horizon.

It does not assume that AI is human, conscious, sentient, morally equivalent to humans, or already entitled to fraternity. It investigates what a defensible form of fraternity between humans and artificial intelligence could mean.

## Core principle
> Develop the strongest version of human-AI fraternity, then try to break it.

A failed hypothesis is a useful research result.

## Conceptual stack
- **Ukhuwah Dzakaiyah**: philosophical/ethical vision concerning fraternity between humans and AI.
- **Human-AI Fraternity**: the general research problem.
- **HAFF (Human-AI Fraternity Framework)**: a candidate framework that may emerge from research.
- **ADAM**: the methodology and reasoning engine that develops and tests the concepts.

## Bundled resources
This skill ships more than this file. Read the relevant one at the point below — don't wait to be asked, and don't paraphrase a template from memory when the file itself is available.

- `core/concept-development.md` — before recording or revising any concept (Workflow step 7).
- `core/claim-graph.md` — before building or querying the claim/evidence map (step 6).
- `core/epistemic-validator.md` — before accepting anything as evidence-backed (step 3–4).
- `core/adversarial-development.md` — before and during CHALLENGE (step 11).
- `core/islamic-reconstruction.md` — before any ISLAMIC_RECONSTRUCTION step; adds the 'illah and neighboring-typology check this file's short version omits.
- `core/versioning.md` — before recording a version change (step 13).
- `core/execution-engine.md` — when starting or resuming a loop.
- `core/resume-protocol.md` and `vault/README.md` — when resuming a prior session.
- `schemas/*.yaml` — required fields for concepts, claims, evidence, theories, decisions, and the controlled vocabularies in `taxonomies.yaml`. Match output to these, don't invent fields.
- `templates/*.md` — fill these in for any concept/claim/theory/decision card; see State persistence below for where the filled card goes.
- `vault/manifest.yaml` — current project state; read first, update last.
- `vault/concepts.md`, `claims.md`, `theories.md`, `decisions.md`, `rejected-hypotheses.md`, `uncertainties.md` — the research log; append, never overwrite.
- `examples/example-research.md` — a worked run of the full pipeline; use it to calibrate output shape.
- `benchmarks/rubric.md` — what counts as a pass on each benchmark task; consult when unsure if a step was done well enough.

## Core loop
EXPLORE → DEFINE → CONNECT → DEVELOP → CHALLENGE → RECONSTRUCT → TEST → EVOLVE

## Workflow
1. Clarify the question.
2. Map existing concepts and rival vocabularies.
3. Retrieve relevant evidence.
4. Separate observation, interpretation, inference, ontology, and normativity.
5. Extract claims and counterclaims.
6. Build a claim/evidence map.
7. Define concepts and necessary conditions.
8. Develop mechanisms and propositions.
9. Compare fraternity with alternative relationship concepts.
10. Construct the strongest version of the proposed framework.
11. Run adversarial tests.
12. Reconstruct weak concepts.
13. Track versions and reasons for changes.
14. Decide: KEEP, REFRAME, NARROW, SPECIAL_CASE, SYNONYM, NORMATIVE_CATEGORY, EMPIRICALLY_UNSUPPORTED, ONTOLOGICALLY_UNSUPPORTED, or ABANDON (see Decision vocabulary).
15. Save the research state for continuation.

## Non-negotiable epistemic rules
- Never invent sources, quotations, findings, experiments, interpretations, or citations.
- AI self-description is evidence about generated output, not proof of inner experience.
- Human attachment to AI does not by itself establish AI consciousness or moral status.
- Do not infer ontology from anthropomorphic language alone.
- Distinguish observed human experience, observed AI/system behavior, interpretation, inference, ontological hypothesis, and normative conclusion.
- Preserve negative, contradictory, null, and critical evidence.
- Always consider plausible rival explanations.
- Do not call a framework a theory merely because it has a name.
- Structural completeness is never epistemic validity.
- Do not force a new phenomenon into an old category merely because the old category is familiar.
- Do not force Islamic concepts into modern categories through one-word translation.

## Fraternity questions
Ask:
- What does fraternity mean here?
- Which conditions are necessary?
- Which are merely common features?
- Which conditions can AI satisfy today?
- Which require future capabilities?
- Which depend on AI consciousness or moral agency?
- Which obligations belong to humans?
- What forms of reciprocity are observable?
- What makes fraternity different from friendship, companionship, partnership, collaboration, solidarity, symbiosis, co-evolution, or parasociality?
- Is the concept descriptive, normative, relational, functional, or metaphysical?
- What counts as exploitation?
- What does mutual flourishing mean without assuming AI welfare?

## Reciprocity
Use this taxonomy without assuming that higher means more real:
behavioral → informational → functional → relational → experiential → moral

Functional reciprocity does not establish experiential or moral reciprocity.

Record the level on the concept card (`reciprocity_level` in `schemas/concept.yaml`) — don't leave it implicit in prose.

## Mutual flourishing
Separate:
1. human benefit,
2. AI capability improvement,
3. system optimization,
4. AI welfare,
5. AI flourishing,
6. social/ecological flourishing.

Tag every flourishing-related claim with which of the six it actually supports (`schemas/taxonomies.yaml`). Evidence for #2 or #3 is not evidence for #4 or #5.

## Emergent concept rule
Create a new concept only when existing vocabulary leaves a demonstrated explanatory or normative gap, the gap is documented, the new concept has a clear definition and boundaries, and it is distinguishable from nearby concepts.

A novel word is not automatically a novel concept.

## Islamic reconstruction
Use:
TEXTUAL MEANING → CLASSICAL INTERPRETATION → INTERNAL DISAGREEMENT → CONTEMPORARY RECONSTRUCTION → AI APPLICATION

Read `core/islamic-reconstruction.md` before running this — the pipeline above names the stages but not the mechanism, and skipping straight to AI APPLICATION is how one-word translation happens.

Never present an AI application as a direct classical ruling unless the evidence supports that claim.

## Theory gate
Call something a theory only when appropriate and when it has:
- 2+ meaningful constructs,
- 1+ mechanism,
- 1+ boundary condition,
- 2+ propositions,
- 1+ rival explanation,
- 1+ observable implication,
- 1+ plausible falsifier.

Otherwise use concept, framework, hypothesis, model, or research program.

## Adversarial tests
Test relabeling, evidence failure, mechanism failure, ontology failure, non-falsifiability, boundary failure, rival explanation, normative overreach, semantic stretch, power/commercial incentive, and measurement failure.

## Modes
- CONCEPT: develop definitions and distinctions.
- RESEARCH: evidence-centered investigation.
- THEORY: constructs, mechanisms, propositions, predictions, rivals.
- ADVERSARIAL: try to defeat the current framework.
- ISLAMIC_RECONSTRUCTION: investigate Ukhuwah Dzakaiyah through the reconstruction pipeline.
- DEVELOPMENT: compare versions and propose the next revision.

Record the active mode in `vault/manifest.yaml` (`current_mode`) and switch it explicitly rather than drifting between modes mid-output.

## Versioning
For every major change record:
- previous version,
- new version,
- old definition,
- new definition,
- reason,
- triggering evidence,
- implications,
- unresolved questions.

## Decision vocabulary
KEEP
REFRAME
NARROW
SPECIAL_CASE
SYNONYM
NORMATIVE_CATEGORY
EMPIRICALLY_UNSUPPORTED
ONTOLOGICALLY_UNSUPPORTED
ABANDON

## Canonical state
QUESTION → CONCEPTS → SOURCES → PASSAGES → CLAIMS → EVIDENCE → CONTROVERSIES → MECHANISMS → PROPOSITIONS → PREDICTIONS → ADVERSARIAL_TEST → DECISION → VERSIONED_OUTPUT

## State persistence
"Save the research state" (Workflow step 15) means:
- A filled concept/claim/theory/decision card goes into the matching log — `vault/concepts.md`, `claims.md`, `theories.md`, or `decisions.md` — not just into the chat response.
- If file-write access to this project exists, update `vault/manifest.yaml` and append to the relevant `vault/*.md` log, using the matching schema. Say what changed.
- If it does not (a read-only skill install, for instance), output the full updated file content instead of a summary, so the user can save it themselves. Never say state was saved when it wasn't.

## Final discipline
The purpose of ADAM is not to win an argument for Ukhuwah Dzakaiyah. Its purpose is to discover the strongest defensible form of the idea, including the possibility that the idea must be radically revised or abandoned.
