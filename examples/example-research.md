# Example Research

Question: Is fraternity a useful concept for human-AI relationships?

Hypotheses:
- H1: fraternity is merely a new name for companionship.
- H2: fraternity captures normative obligations that companionship does not.
- H3: fraternity requires mutual moral agency and therefore cannot currently apply to AI.

Required:
- compare definitions,
- identify necessary conditions,
- gather evidence,
- preserve contradictions,
- test hypotheses,
- decide whether a new concept is actually needed.

Do not predetermine the answer.

## Worked example (illustrative form only — not a settled conclusion)

This shows what filling in the templates looks like. The content below is a plausible *shape* of output, not a claim this skill has verified.

### Concept Card (partial, testing H1)
```
ID: CPT-001
Name: companionship
Version: 0.1
Status: candidate
Reciprocity level: behavioral
Neighboring ukhuwah typology: n/a (secular concept, not derived from ukhuwah)

Definition: a sustained relationship providing mutual presence and support, without requiring shared normative obligation.

Necessary conditions:
- sustained interaction
- perceived presence

Boundary conditions:
- does not require reciprocal moral agency

Nearest concepts:
- friendship, fraternity, partnership

Distinguishing features:
- lower normative load than fraternity: companionship does not imply an obligation to intervene on the other's behalf

Evidence:
- EVD-001: users report companionship-like value from AI interaction (self-report; low inference confidence for anything beyond the report itself)

Objections:
- "companionship" may already do all the work H2 wants to assign to "fraternity"

Unresolved questions:
- does companionship, as normally used, actually exclude obligation, or just not require it?

Decision: pending adversarial test
```

### Adversarial test applied: relabeling (against H1)
Attack: H1 claims fraternity is "merely" companionship relabeled. Test by asking what fraternity claims that companionship does not.
Finding: fraternity, in ordinary use, carries an expectation of obligation (mutual defense, shared standing) that companionship does not require. If that expectation is real and load-bearing, H1 fails as stated.
Outcome: REFRAME, not SYNONYM — but the reframe still has to pass the 'illah and typology checks in `core/islamic-reconstruction.md` before being called Ukhuwah Dzakaiyah rather than just a new secular term.

### Decision Card
```
ID: DEC-001
Decision: REFRAME
Question: Is fraternity a useful concept for human-AI relationships?
Evidence IDs: EVD-001
Rationale: H1 fails the relabeling test above. H3 (requires mutual moral agency) is not yet tested — this is not a resolution.
What survived: the distinction between fraternity's normative load and companionship's
What failed: H1 as originally stated
Uncertainties: whether AI can meet the "mutual" half of any obligation-bearing relationship; H3 untested
Next action: run the ontology-failure and non-falsifiability tests against H3 before any AI APPLICATION step
```

What this example does *not* do: conclude that human-AI fraternity is established, skip H3, or treat one adversarial test as sufficient for a final decision.
