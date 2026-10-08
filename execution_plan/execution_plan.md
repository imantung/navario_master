# Execution Plan

The living tracker: what to settle, in what order, and what is still undecided. Update it every week. Other documents hold the details; this file holds status.

## 1. Review order

Settle the areas in this order. Each one feeds the next.

| # | Area | Document | Why at this step |
| :-- | :-- | :-- | :-- |
| 1 | **Pricing** | [pricing_model.md](../pricing_model/pricing_model.md), [ai_cost_simulation.md](../cost_simulation/ai_cost_simulation.md) | Every quote, offer and web page needs prices. Retail top-ups sell below cost, and AI project prices are not set. |
| 2 | **Marketing** | [marketing_strategy.md](../marketing_strategy/marketing_strategy.md), [process_flow.md](../process_flow/process_flow.md) | Turns prices into offers and demos. Warm network first. |
| 3 | **Partnership** | [partnership_model.md](../partnership_model/partnership_model.md) | Needs final prices for the commission base. Not urgent until a partner wants to sign. |
| 4 | **Website** | [website/requirement.md](../website/requirement.md) | Last. It shows the decisions from 1–3. Start with the rebrand plus home, pricing and contact. |

## 2. Tasks

Spec style: each task has a clear "done when". Do not start a task before the tasks it depends on are done.

### 2.1 Pricing

- [ ] **T01 Measure AI cost.** Done when: 50 realistic questions are logged with tokens, and the averages replace the assumptions in the script (see the cost simulation "Next steps").
- [ ] **T02 Choose the retail model stack.** Depends on T01. Done when: D02 is decided, the script is re-run, and the tables in `ai_cost_simulation.md` match its output.
- [ ] **T03 Fix retail pricing.** Depends on T02. Done when: top-ups are priced at ≥ 2x cost per question and the retail price per user is decided (D01).
- [ ] **T04 Enterprise BYOK package.** Done when: the server spec is set (D03), and you can show the per-company AI key setting working in a demo (D05).
- [ ] **T05 AI project pricing.** Done when: a price guide for development and a monthly server maintenance fee are in pricing_model.md section 6 (D04).

### 2.2 Marketing

- [ ] **T06 Demo ready.** Done when: the demo dataset is loaded, the script in process_flow.md has been rehearsed 5 times, and a 3-minute Bahasa Indonesia demo video is recorded.
- [ ] **T07 Founding client offer.** Depends on T03. Done when: a one-page offer in Bahasa Indonesia exists, with a deadline or a client limit (D06).
- [ ] **T08 AI project offer.** Depends on T05. Done when: a one-page offer exists: what we build, how scoping works, BYOK, and 2–3 example projects that reuse the Navario assistant.
- [ ] **T09 Lead sheet.** Done when: one sheet tracks source, date, offer (product or AI project), demo, quote, and won/lost with the reason.
- [ ] **T10 Warm network.** Depends on T06. Done when: 30 contacts have been messaged and ≥ 5 demos are booked. Pitch AI projects to your startup network, and the product to trading companies.
- [ ] **T11 Content.** Done when: 4 short demo videos are published (marketing strategy, section 3).

### 2.3 Partnership

- [ ] **T12 Partner summary.** Done when: a one-page partner summary exists, with BYOK explained for enterprise.
- [ ] **T13 Partner agreement draft.** Depends on D07 and D08. Done when: a Bahasa Indonesia draft with confidentiality and non-solicitation clauses exists, checked by a notary or lawyer.
- [ ] **T14 Partner outreach.** Depends on T12. Done when: 15 accountants, tax consultants or IT consultants have been contacted. Follow rule 0 in [partnership_model.md](../partnership_model/partnership_model.md#rules): sign before you teach.

### 2.4 Website

- [ ] **T15 Minimum website.** Depends on T03 and T05. Done when: rebrand section 0 is done and home, pricing and contact are live on navario.id (D09).
- [ ] **T16 Enterprise and AI project content.** Done when: the enterprise card mentions BYOK, and AI projects appear on the site (D10).

### 2.5 Legal and sales documents (needed before the first paid deal)

- [ ] **T17 Legal entity.** Done when: the PT Perorangan is registered and has a business bank account (D11).
- [ ] **T18 Sales documents.** Depends on T03 and T17. Done when: the quotation template, service agreement, and Terms/Privacy exist in Bahasa Indonesia and have been checked by a notary or lawyer.

### 2.6 Deliver and prove (after the first client pays)

- [ ] **T19 First delivery.** Done when: the client is live (process flow stages 4–6) and has signed the go-live sign-off.
- [ ] **T20 Proof.** Done when: you have a testimonial, logo permission and a short case study, one month after go-live.
- [ ] **T21 Real usage.** Done when: real AI questions per user are measured, and the retail allowance is confirmed or changed.

### Every Friday

- [ ] Update the lead sheet and this task list. Spend at most ~50% of the week on AI projects (decision log, 8 Oct 2026).

## 3. Open business decisions

| ID | Area | Decision | Recommendation | Needed by |
| :-- | :-- | :-- | :-- | :-- |
| D01 | Pricing | Retail price per user vs Odoo (see [pricing_model.md](../pricing_model/pricing_model.md#4-benchmark-odoo)) | Decide after the cost data. Compete on first-year total cost, not licence price. | T03 |
| D02 | Pricing | AI model stack for retail | Price on stack C until quality tests prove a cheaper stack. | T02 |
| D03 | Pricing | Enterprise server spec (vCPU / RAM / storage) | Set it from the load of a 30-user demo. | T04 |
| D04 | Pricing | AI project price guide: development and monthly server maintenance | Fixed price per project after a scoping call. Charge for the scoping call only if it includes a written design. | T05 |
| D05 | Pricing | BYOK: which AI providers, and does the product support a per-company key today? | Gemini only for now; the cost model and product are built on it. Do not quote BYOK until the key setting works in a demo. | T04 |
| D06 | Marketing | Founding client offer terms (see [marketing_strategy.md](../marketing_strategy/marketing_strategy.md#2-the-real-problem-no-portfolio-yet)) | 50% off setup for the first 3 clients, in exchange for a logo, testimonial and case study. | T07 |
| D07 | Partnership | **Partner commission model** (see [partnership_model.md](../partnership_model/partnership_model.md)) | Option A (simple). BYOK AI usage is outside the commission base. | T13 |
| D08 | Partnership | Do partners earn commission on AI projects they refer? | Yes, a one-time share of the development fee only. | T13 |
| D09 | Website | Website scope | Rebrand plus home, pricing and contact first. | T15 |
| D10 | Website | Show the enterprise price publicly, or "Talk to us" only? | "Talk to us" only. Enterprise is sold through partners, who need room to add their consultancy. | T16 |
| D11 | Legal | **Legal entity.** Register a *PT Perorangan* (a new entity, not PT Inovasi Teknologi Terintegrasi). | Register before sending the first quotation. | T17 |
| D12 | Legal | **PKP (PPN registration).** Mandatory only above IDR 4.8 billion turnover per year **[unverified]**. | Stay non-PKP at first. Revisit when an enterprise client needs a *faktur pajak*. | First enterprise deal |
| D13 | Marketing | **Retail per-user pricing vs the proposal.** The proposal says "no per-user licence fees". That is true for enterprise only. | Soften those lines in the retail (Bahasa Indonesia) version before you show it to retail prospects. | T10 |
| D14 | Website | Logo | Later. Use a text logo for now. | — |

*Note: D11, D12 and the clauses in T13 must be validated with a certified Indonesian tax consultant or notary.*

## 4. Decision log

| Date | Decision |
| :-- | :-- |
| 8 Oct 2026 | **AI first.** Navario is an AI company; the ERP is the data foundation. |
| 8 Oct 2026 | **No ERP-only deals.** Every deal includes AI. |
| 8 Oct 2026 | **AI projects for any industry**, only when they reuse the Navario assistant. At most ~50% of weekly time. |
| 8 Oct 2026 | **AI projects:** charge for development and server maintenance only. AI usage is BYOK. |
| 8 Oct 2026 | **Enterprise is BYOK.** The client pays Google directly for AI usage. Retail keeps included AI questions. |
| 8 Oct 2026 | **Sign before you teach** with partners (partnership model, rule 0). |
| 8 Oct 2026 | The proposal stays as is (product only). AI projects get a separate one-page offer (T08). |

## 5. Confidence score

This is an honest judgment, not data. Re-score it on the last Friday of every month.

| Factor | Weight | Score (1–5) | Why |
| :-- | --: | --: | :-- |
| Product works in a live demo | 15% | 3 | Demo script exists; BYOK key setting not confirmed (D05) |
| Differentiation (AI assistant in Bahasa Indonesia on own ERP data) | 15% | 4 | Real and easy to show in a demo |
| AI delivery skill | 15% | 4 | Startup engineering background; AI-first strategy plays to it |
| Sales and ERP domain experience | 15% | 1 | None yet. This is the biggest gap. |
| Trust and portfolio | 15% | 1 | No clients, solo, new brand |
| Pricing and unit economics | 10% | 3 | BYOK removes AI cost risk on enterprise and AI projects; retail top-ups still below cost |
| Distribution (network, partners) | 15% | 2 | Warm network untested; no partner yet |
| **Readiness score** | | **51 / 100** | |

**Odds (judgment, 8 Oct 2026):**

| Outcome | Chance |
| :-- | --: |
| First paying client (AI project or product) by end Jan 2027 | ~55% |
| 3 paying product clients by end Mar 2027 | ~30% |

**Main risk: focus split.** AI projects can eat all your time and leave the product unsold. The reuse rule and the ~50% time cap are the guard.

**How to raise the score:**
- Sales experience 1 → 3: do 15+ demos by Jan 2027. Log the reason for every lost deal.
- Trust 1 → 3: one live client with a case study (T20).
- Distribution 2 → 4: one active partner bringing leads.
