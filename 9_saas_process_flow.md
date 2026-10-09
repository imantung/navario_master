# SaaS Process Flow

Internal. A retail (SaaS) client from first contact to ongoing support. The stages follow the "Let's Talk" section of the [proposal](proposal/draft_oct_2026/draft_proposal.md): **live demo → needs discussion → fixed-price quote**.

Enterprise is in [11_enterprise_process_flow.md](11_enterprise_process_flow.md). Prices are in [5_saas_pricing_model.md](5_saas_pricing_model.md). Pilot clients follow the same stages with the terms in [5_saas_pricing_model.md](5_saas_pricing_model.md#5-pilot). If a Referral Partner brought the lead, register it ([8_partnership_model.md](8_partnership_model.md#rules), rule 1); the commission is paid after the client's payment clears.

```
1 Live demo → 2 Needs discussion → 3 Quote & contract → 4 Setup & import → 5 Training & UAT → 6 Go-live → 7 Support
                    └─ optional 7-day trial
```

| Stage | Owner | Time | Exit document |
| :-- | :-- | :-- | :-- |
| 1. Live demo | Founder | 30–45 min | Lead sheet updated |
| 2. Needs discussion | Founder | 45 min (Fast-Track) or 90 min (Standard) | Discovery checklist filled in |
| 3. Quote & contract | Founder | 1–3 days | Signed agreement, payment cleared |
| 4. Setup & import | Founder | ~1–2 weeks **[estimate]** | Master data sign-off |
| 5. Training & UAT | Founder | ~1 week **[estimate]** | UAT acceptance |
| 6. Go-live | Founder | 1 day | Go-live sign-off |
| 7. Support | Founder, later a support hire | Ongoing | — |

## Stage 1: Live Demo (30–45 min, online or onsite)

The demo is the main sales tool, so it is scripted and rehearsed.

* **Before:** A demo company with realistic Indonesian trading data (customers, suppliers, items, 3 months of transactions, a few overdue invoices, low-stock items, pending approvals). A recorded backup video in case the AI or the internet fails.
* **Script** (from the proposal; let the prospect pick what matters to them):
  1. "Which customers are more than 60 days overdue?" and "Which items are below minimum stock?"
  2. "Compare this month's sales with last month."
  3. "Create a sales order for PT Maju Jaya": a pre-filled form, checked and saved by the user.
  4. Log in as a sales staff member and ask for bank balances: the assistant declines.
  5. A purchase request going from request to approval.
  6. "Open the asset register."
* **You give:** The demo, and the proposal PDF afterwards.
* **You receive:** Company name, decision maker, number of staff who would use the system, current tools (spreadsheets, Accurate, Jurnal, etc.), and their main pain.
* **Qualify:** SaaS fits roughly 3–30 users. Larger or multi-company prospects go to enterprise ([6_enterprise_pricing_model.md](6_enterprise_pricing_model.md)). During the pilot phase, check the pilot criteria ([5_saas_pricing_model.md](5_saas_pricing_model.md#who-qualifies)).

## Stage 2: Needs Discussion (included in setup)

* **You give:** A discovery checklist covering:
  * Flow: buy → receive stock → sell → deliver → invoice → collect payment
  * Number of branches and warehouses
  * Tax status (PKP or not), e-Faktur volume. e-Faktur export is not built; say so plainly ([4_product_scope.md](4_product_scope.md), 4.3).
  * Documents they print (invoice, PO, delivery note) and the reports they rely on
  * Users and roles, approval rules
  * Data to bring in: customers, suppliers, items, opening balances
* **You receive:** Answers, sample documents and a user list.
* **Decide:** Fast-Track or Standard setup, and any add-ons.
* **Optional: 7-day trial.** Their own instance, pre-loaded with the trading template, capped at 200 AI questions. If they need more time, the 30-day extension fee is credited to setup. An instance with no decision is frozen on day 7 and deleted on day 10.

## Stage 3: Fixed-Price Quote & Contract

* **You give:**
  * A quotation in Bahasa Indonesia: package, add-ons, **one fixed total**, what is included and excluded, and the target go-live date.
  * A service agreement in Bahasa Indonesia, including the server location and AI processing ([L7](2_legal.md#1-rules)).
  * An invoice for 100% of the setup fee + the first month (or year), minus any trial extension fee already paid.
* **You receive:** The signed agreement and payment.
* **Rule:** No quotation before the legal entity exists ([L1](2_legal.md#1-rules)). Work starts after payment clears. Anything outside the quote is a change request with its own fixed quote ([C8](0_business_constraint.md#3-commercial-rules)).

## Stage 4: Setup & Data Import

* **You give:** A production instance on the shared cloud, configured from the needs discussion (trial instances are cleaned of test transactions), plus Excel import templates or the data migration add-on. Configuration is stored as data ([techstack.md](techstack.md#4-design-rules), rule 3).
* **You receive:** Master data (customers, suppliers, items, assets, chart of accounts mapping) and a signed master data sign-off.

## Stage 5: Training & UAT

* **You give:** Video library access, the live training sessions in the package, and a UAT checklist based on their real flow.
* **You receive:** A signed UAT acceptance.

## Stage 6: Go-Live

* **You give:** Opening balances posted (bank, stock, AR/AP), production access for all users, the AI question pool switched on, and a go-live confirmation.
* **You receive:** A signed go-live sign-off.

## Stage 7: Ongoing Support

* **You give:** Hosting, backups, upgrades and chat support (first response within 24 hours). The monthly AI question pool, with a heads-up when they reach 80%.
* **You receive:** Monthly or annual subscription payments.
* **One month after go-live:** Review AI usage together and offer a top-up if needed. **Ask for a testimonial, logo permission and a short case study.** Every early client is also portfolio.
* **If the client leaves:** Give a full data export. They keep their data and configuration ([techstack.md](techstack.md#5-if-a-client-leaves)).

### Support coverage

The SLA is a **first response** time, not a fix time. A fix follows with an estimate. Enterprise SLA and the partner support split are in [8_partnership_model.md](8_partnership_model.md#support-split-enterprise).

**While solo** ([C1](0_business_constraint.md#1-founder-and-capacity), [X6, X7](1_challenges.md#2-founder-capacity)):
- One support channel: a WhatsApp Business number with an auto-reply stating support hours, and every request logged as a ticket (the Helpdesk/Issue doctype in our own ERP works).
- Reduce "how do I" tickets: the video library, plus the assistant's **Learn** capability answering from the user guide.
- Backup: a freelance ERPNext developer on a small monthly retainer, who has server access, for when you are sick or away. One person running production for paying clients is the biggest operational risk.

**Hire the first support person when** either is true for 3 months in a row:
- Recurring revenue covers the hire at no more than ~30% of monthly recurring revenue. At roughly IDR 6–8M/month fully loaded (Jakarta UMP + BPJS; less outside Jakarta), that is **about IDR 25M monthly recurring revenue**, e.g. 2 enterprise clients, or ~60 retail users.
- Support takes more than ~10 hours a week of your time.

**Profile:** A functional support and implementation person with an accounting background (D3/S1 Akuntansi), not a developer. Most tickets will be accounting and process questions, and the same person can run training, data import and UAT, which frees you for product work. A cheaper first step is a part-time hire or an accounting student intern (*magang*) for data import and training.

## Tasks

Legal entity and sales documents (quotation, service agreement): see [2_legal.md](2_legal.md#tasks).

- [ ] **Discovery checklist.** Done when: the stage 2 checklist exists as a one-page Bahasa Indonesia form.
- [ ] **UAT checklist template.** Done when: a template covers the trading flow from stage 2.
- [ ] **Backup developer.** Done when: a freelance ERPNext developer has server access, before the first go-live.
- [ ] **First delivery.** Done when: the first client is live (stages 4–6) and has signed the go-live sign-off.
- [ ] **Proof.** Done when: you have a testimonial, logo permission and a short case study, one month after go-live.

## Open decisions

- [ ] **"Estimation" in the proposal vs fixed-price quote.** The proposal's "Let's Talk" ends with a "cost estimate"; the process sends one fixed total. Recommendation: keep the fixed-price quote, and change the proposal wording to "fixed-price quote" when it is next revised.
- [ ] **Stage durations** (stages 4–5 are estimates). Recommendation: measure them on the first pilot and replace the estimates.
- [ ] **Parallel setups.** Recommendation: at most 2 setups at the same time while solo.
- [ ] **Non-payment and cancellation.** Recommendation: 14 days' grace, then read-only, then a data export is offered, then deletion. Write it into the service agreement.
