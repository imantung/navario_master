# Product Scope

What the product must do, and when. Sales material may describe as working only features marked **Works** here. Features not built yet may be sold as planned, with a delivery date in the quote ([X19](1_challenges.md#2-founder-capacity)). Claims come from the [proposal](proposal/draft_oct_2026/draft_proposal.md) and the demo script in [9_saas_process_flow.md](9_saas_process_flow.md).

**Status** values: **Works** (shown in a demo today), **Partly**, **Not built**, **?** (not confirmed yet).

## 1. Demo (before messaging warm contacts)

If one of these fails in a live demo, you lose trust you cannot win back.

| # | Feature | Demo moment | Status |
| :-- | :-- | :-- | :-- |
| 1.1 | Find and analyse data: overdue invoices, low stock, period comparison, P&L summary | "Which customers are more than 60 days overdue?" | ? |
| 1.2 | Pre-filled document from chat | "Create a sales order for PT Maju Jaya" | ? |
| 1.3 | Access rules in the assistant | A sales staff member asks for bank balances and is declined | ? |
| 1.4 | Approvals: pending list and history | A purchase request from request to approval | ? |
| 1.5 | Chat basics: Bahasa Indonesia, live progress, tables, links to documents | Every answer | ? |
| 1.7 | Asset Management through the assistant | "Open the asset register" | ? |
| 1.8 | Demo dataset: Indonesian trading company, 3 months of transactions | Everything above depends on it | ? |

## 2. First paid client

Not needed to demo, but already promised in the proposal or the pricing.

| # | Feature | Why | Status |
| :-- | :-- | :-- | :-- |
| 2.1 | AI Quota per company in credits: credits per message, per-user daily cap, usage screen, 80% warning, hard limit | Retail pricing depends on it. Without the limit, AI cost has no ceiling. | ? |
| 2.2 | Per-company AI key (BYOK) | Enterprise pricing depends on it | ? |
| 2.3 | Request log | Proposal: "Every request is recorded" | ? |
| 2.4 | Indonesian setup: chart of accounts, PPN/PPh, print formats | Proposal: "Built for Indonesian companies" | ? |
| 2.5 | Instance provisioning and backups | The 7-day trial and every go-live need it | ? |
| 2.6 | Excel import templates | Retail setup is "self-service import" | ? |
| 2.7 | Token and credit logging per message (internal) | Needed to finalise pricing ([ai_cost_simulation.md](ai_cost_simulation.md)) | ? |
| 2.8 | Multiple warehouses, branches and companies | Standard setup and enterprise depend on it | ? |
| 2.9 | Full data export that restores on plain ERPNext | Promised as "no vendor lock-in" ([techstack.md](techstack.md#5-if-a-client-leaves)) | ? |

## 3. Claimed in the proposal, likely weak

Confirm each one. If it is not built, every client who reads the proposal gets a false claim.

| # | Claim | Risk | Status |
| :-- | :-- | :-- | :-- |
| 3.1 | Take action / change setup: preview, Apply, 10-minute expiry | The most complex claim | ? |
| 3.2 | Learn: answers from user guides and the client's own procedures | Needs written content, not only code | ? |
| 3.3 | Autocomplete and role-based suggested questions | — | ? |
| 3.4 | Access limits such as "only my branch" inside the assistant | — | ? |
| 3.5 | "Other modules (manufacturing, projects, customer support) can be switched on as you grow" | True for enterprise, where the partner configures them ([C5](0_business_constraint.md#2-offer)). Not offered for retail. | Open decision |

## 4. Long-term (sell only as planned, with a delivery date)

| # | Feature | Why it serves the strategy |
| :-- | :-- | :-- |
| 4.1 | Assistant works on data outside ERPNext | Lets the assistant answer from a client's other systems. Could share code with AI projects such as MCP servers ([12_ai_project.md](12_ai_project.md)). |
| 4.2 | Proactive alerts (daily WhatsApp or email summary: overdue invoices, low stock) | Trading company owners want to be told, not to ask. Strong demo. |
| 4.3 | e-Faktur export | The most common Indonesian tax request. Until built, say plainly it is not included. |

## Build rule

Build and sell in parallel ([C1](0_business_constraint.md#1-founder-and-capacity)). Start demos as soon as section 1 works; keep building section 2 between demos. Build section 3 when a real prospect asks for it. Section 4 can be sold as planned, with a delivery date, once a paying client wants it.

Why ([X4](1_challenges.md#2-founder-capacity)): an engineer-founder's natural pull is to keep building instead of selling. The product will not fail for lack of features; it will fail for lack of demos.

## Assumptions

- The section 1 features are close to working. The demo is being built (9 Oct 2026), but no status is filled in yet.

## Tasks

- [ ] **AI test set.** Done when: 50 test questions with expected answers run on the demo data before every release ([X15](1_challenges.md#6-product-and-technology)).
- [ ] **Fill in status.** Done when: every **?** in sections 1–3 is replaced with Works, Partly or Not built.
- [ ] **Demo-ready.** Depends on: fill in status. Done when: every section 1 feature is **Works** and the demo has been rehearsed 5 times.
- [ ] **First-client-ready.** Done when: every section 2 feature is **Works**.

## Open decisions

- [ ] **Section 3 claims that are not built.** Recommendation: list them as "on request" in the Bahasa Indonesia proposal version, and do not show them in demos.
- [ ] **"Switch on other modules" claim (3.5).** Recommendation: for retail, answer "not offered now"; for enterprise, "yes, configured by our implementation partner". Log it as a proposal change for later.
- [ ] **Which long-term feature first (section 4).** AI projects no longer have to reuse the assistant, so 4.1 is less urgent. Recommendation: 4.2 proactive alerts, the strongest demo for trading company owners.
