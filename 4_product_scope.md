# Product Scope

What the product must do, and when. Sales material may only claim features marked **Works** here. Claims come from the [proposal](proposal/draft_oct_2026/draft_proposal.md) and the demo script in [process_flow.md](process_flow.md).

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
| 1.6 | Demo dataset: Indonesian trading company, 3 months of transactions | Everything above depends on it | ? |

## 2. First paid client

Not needed to demo, but already promised in the proposal or the pricing.

| # | Feature | Why | Status |
| :-- | :-- | :-- | :-- |
| 2.1 | AI question pool per company, usage tracking, 80% warning, hard limit | Retail pricing depends on it. Without the limit, AI cost has no ceiling. | ? |
| 2.2 | Per-company AI key (BYOK) | Enterprise pricing depends on it | ? |
| 2.3 | Request log | Proposal: "Every request is recorded" | ? |
| 2.4 | Indonesian setup: chart of accounts, PPN/PPh, print formats | Proposal: "Built for Indonesian companies" | ? |
| 2.5 | Instance provisioning and backups | The 7-day trial and every go-live need it | ? |
| 2.6 | Excel import templates | Retail setup is "self-service import" | ? |
| 2.7 | Token logging per question (internal) | Needed to finalise pricing ([ai_cost_simulation.md](ai_cost_simulation.md)) | ? |

## 3. Claimed in the proposal, likely weak

Confirm each one. If it is not built, every client who reads the proposal gets a false claim.

| # | Claim | Risk | Status |
| :-- | :-- | :-- | :-- |
| 3.1 | Take action / change setup: preview, Apply, 10-minute expiry | The most complex claim | ? |
| 3.2 | Learn: answers from user guides and the client's own procedures | Needs written content, not only code | ? |
| 3.3 | Autocomplete and role-based suggested questions | — | ? |
| 3.4 | Access limits such as "only my branch" inside the assistant | — | ? |
| 3.5 | "Other modules (manufacturing, projects, customer support) can be switched on as you grow" | Conflicts with "Not offered now" in CLAUDE.md. If a client switches one on, you must support it. | Open decision |

## 4. Long-term (do not sell yet)

| # | Feature | Why it serves the strategy |
| :-- | :-- | :-- |
| 4.1 | Assistant works on data outside ERPNext | AI projects must reuse the Navario assistant. This turns AI projects into product work. The most important long-term technical decision. |
| 4.2 | Proactive alerts (daily WhatsApp or email summary: overdue invoices, low stock) | Trading company owners want to be told, not to ask. Strong demo. |
| 4.3 | e-Faktur export | The most common Indonesian tax request. Until built, say plainly it is not included. |

## Build rule

Build only section 1, then stop and start demos. Build section 2 between demos. Build section 3 only when a real prospect asks for it. Section 4 waits for paying clients.

Why ([X4](1_challenges.md#2-founder-capacity)): an engineer-founder's natural pull is to keep building instead of selling. The product will not fail for lack of features; it will fail for lack of demos.

## Tasks

- [ ] **Fill in status.** Done when: every **?** in sections 1–3 is replaced with Works, Partly or Not built.
- [ ] **Demo-ready.** Depends on: fill in status. Done when: every section 1 feature is **Works** and the demo has been rehearsed 5 times.
- [ ] **First-client-ready.** Done when: every section 2 feature is **Works**.

## Open decisions

- [ ] **Section 3 claims that are not built.** Recommendation: list them as "on request" in the Bahasa Indonesia proposal version, and do not show them in demos.
- [ ] **"Switch on other modules" claim (3.5).** Recommendation: answer "not offered now" if asked, and log it as a proposal change for later.
- [ ] **Which long-term feature first (section 4).** Recommendation: 4.1, because it makes every AI project feed the product.
