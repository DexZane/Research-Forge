# Fast Audit Report: <Candidate Idea / Title>

- **Project ID:** `<project-id>`
- **Mode:** `FAST_AUDIT`
- **Candidate ID:** `C-<xxxx>`
- **Active Baseline ID:** `BL-<xxxx>`
- **Audit Date / Cutoff:** `<YYYY-MM-DD>`
- **Overall Verdict:** `[PROCEED_TO_FULL_FORGE | REFINE | KILL]`

---

## 1. Idea Intake & Baseline Delta Contract

- **Proposed Idea / Method:** <Concise description of the method or architectural idea>
- **Claimed Bottleneck & Mechanism:** <Underlying causal problem and why the method is claimed to fix it>
- **Selected Primary Baseline (`BL-<xxxx>`):** <Exact baseline variant, benchmark, split, and evaluation metric>
- **Baseline Delta Statement:** <What is strictly modified relative to the baseline and what remains matched>

---

## 2. Adversarial Prior-Art & Novelty Collision Scan

| Competitor Paper / Artifact (`P-ID`) | Threat Level (`T0`–`T5`) | Reading Depth (`R0`–`R4`) | Specific Overlap / Subsuming Mechanism | Surviving Residual? |
|---|---|---|---|---|
| `P-<xxxx>` (Author, Year) | `T4` / `T5` | `R3` | <Exact overlap in bottleneck, formulation, or mechanism> | <None / Narrowed condition> |
| `P-<xxxx>` (Author, Year) | `T2` / `T3` | `R2` | <Adjacent approach or overlapping objective> | <Yes, distinct formulation> |

- **Emergency Collision Flag:** `[NONE | TRIGGERED]`
- **Strongest Competitor Summary:** <Interpretation of the closest competitor in its strongest reasonable form>

---

## 3. Innovation Peeling & Residual Gap

- **Killed / Overlapping Claims:**
  - `CL-<xxxx>`: <Claim text> → Killed by `P-<xxxx>` (`EU-<xxxx>`).
- **Surviving Residual Claim:**
  - `CL-<xxxx>`: <Bounded claim text surviving after peeling>.
- **Residual Gap Classification:** `[RG_A_STRONG_SCIENTIFIC | RG_B_CONDITIONAL | RG_C_METHODOLOGICAL | RG_D_EMPIRICAL | RG_E_COMBINATION]`
- **Conceptual Stitching Check (Name Removal & Reviewer Compression):**
  - *Can this be dismissed as simple "X + Y"?* <Assessment and defense or failure condition>

---

## 4. Hypothesis & Competing Alternative Explanations

- **Method-Free Core Hypothesis (`H-<xxxx>`):** <Hypothesis formulated without module brand names>
- **Hypothesis Ladder Level:** `[H0_DESCRIPTIVE | H1_ASSOCIATIONAL | H2_MECHANISTIC | H3_INTERVENTIONAL]`
- **Top Competing Alternative Explanations:**
  1. *Alternative A (Confounder/Capacity/Data):* <Simpler explanation for observed gains>
  2. *Alternative B (Optimization/Hyperparameter):* <Why standard baseline tuning might match it>

---

## 5. Single Cheapest Killer Falsifier (`EX-<xxxx>`)

- **Experimental Tier:** `[F0_OUTPUT_ANALYSIS | F1_LIGHTWEIGHT_PROBE | F2_CONTROLLED_TRAIN]`
- **Discriminative Variable / Intervention:** <Controlled single-variable perturbation or probe>
- **Preregistered Kill Condition:** <Quantitative or qualitative result that kills the hypothesis before full experiments>
- **Ambiguity Branch:** <What happens if outcome is marginal>
- **Estimated Resource Cost:** <Hours / GPU-hours / Dataset requirements>

---

## 6. Rapid Reviewer Risk Panel

- **Novelty Reviewer (`R_N`):** <Main vulnerability regarding novelty, prior art, or incremental combination>
- **Mechanism Reviewer (`R_M`):** <Main vulnerability regarding causal explanation, confounding, or metric validity>
- **Experiment Reviewer (`R_E`):** <Main vulnerability regarding baseline fairness, benchmark leakage, or compute matching>

---

## 7. Final Triage Decision & Actionable Recommendation

- **Verdict:** `[PROCEED_TO_FULL_FORGE | REFINE | KILL]`
- **Decision Rationale:** <Why this idea should proceed to full S00–S18 lifecycle, undergo structural refinement, or be abandoned>
- **Next Immediate Action:** <Exact next step: refine hypothesis, execute F0/F1 probe, or archive with negative record>
