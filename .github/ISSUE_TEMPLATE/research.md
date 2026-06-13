---
name: Research
about: Use when researching a particular topic
title: "[RSCH]: Investigate [Technology/Concept] for [Project Goal]"
labels: documentation
assignees: ''

---

### I. Objective and Scope Definition (The "Why")
*What specific question are we trying to answer? Be precise.*

1.  **Primary Question:** What is the core problem this research must solve, or what opportunity must it validate? (e.g., *Can we process video streams in real-time using edge computing devices at a cost under $50 per unit?*)
2.  **Success Definition:** How will we know if this research was successful? Define measurable criteria. (e.g., "A viable solution must demonstrate < 100ms latency and integrate with our existing AWS infrastructure.")
3.  **Out of Scope:** What are we explicitly *not* investigating right now? This prevents scope creep.

---

### II. Research Tracks & Methodology (The "How")
*Detail the plan for gathering information.*

#### A. Information Sources:
- [ ] **Literature Review:** Which academic papers, industry reports, or whitepapers must be consulted? (List key authors/journals.)
- [ ] **Vendor Evaluation:** Which commercial tools or services need to be evaluated? (e.g., AWS vs Azure; Tool X vs Tool Y).
- [ ] **Internal Expertise:** Who are the subject matter experts on our team that we must interview?

#### B. Hypothesis & Assumptions:
*State your initial guess, and what assumptions underpin it.*
**Hypothesis:** We believe that [Concept] is viable because of [Reason].
**Key Assumption(s):** (e.g., "We assume the necessary compute power will be available," or "We assume API rate limits are generous.")

---

###  III. Analysis & Trade-off Evaluation (The Critical Thinking)
*Do not just list facts; compare them against defined criteria.*

*\*Weighting: Assign higher weight (5) to the criteria that are non-negotiable for project success.*

---

###  IV. Findings & Recommendation (The Conclusion)
*This section must be definitive and actionable.*

#### A. Key Learnings / Discovered Risks:
1.  [Finding 1]: The biggest blocker is [X]. We need to allocate time/resources to solve this first.
2.  [Finding 2]: While Option B looked promising, its dependency on [Y] introduces unacceptable vendor lock-in risk.

#### B. Recommendation (The Decision):
Based on the analysis above and weighting criteria: **We recommend proceeding with [Option A / Option B / Status Quo].**

*   **Rationale:** This option provides the best balance of [Speed/Cost/Performance], despite its drawback in [Area X].
*   **Next Steps (Actionable Items):** What is the immediate, concrete next step? (e.g., "Create a Proof-of-Concept using Option A's API sandbox," or "Schedule a meeting with the finance team to validate cost projections.")

#### Decision Status: [To Be Determined / Approved for POC / Rejected]
