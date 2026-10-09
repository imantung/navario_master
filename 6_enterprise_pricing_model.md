# Enterprise Pricing Model

Internal. Two offers where the client brings its own AI key (BYOK): **Enterprise** (flat fee, unlimited users, any industry, direct or with a partner, see [8_partnership_model.md](8_partnership_model.md)) and **AI projects** (custom AI work, any industry). Also the enterprise pilot offer (section 5) and the potential profit per client (section 6). Retail is in [5_saas_pricing_model.md](5_saas_pricing_model.md).

## Principles

- **Fixed price** ([C8](0_business_constraint.md#3-commercial-rules)). Every quote is a fixed total agreed before work starts. No hourly billing. The client only ever sees one number.
- **No ERP-only deals** ([C3](0_business_constraint.md#2-offer)). Every enterprise package includes the AI Business Assistant.
- **Flat fee, unlimited users.** Limited by server capacity only. Seats and AI usage never trigger a price change.
- **BYOK (bring your own key).** The client connects its own AI key and pays the provider directly for AI usage. One model for now (Gemini), until a client opportunity needs another ([techstack.md](techstack.md#2-nava-ai)). Do not quote BYOK until the per-company key works in a demo ([4_product_scope.md](4_product_scope.md#2-first-paid-client), 2.2). Navario charges only for the platform, development and server maintenance. So AI price changes (e.g., the Jan 2027 Gemini increase) do not hit Navario's margin.
- **PPN:** Depends on whether the new entity is PKP (see [2_legal.md](2_legal.md#open-decisions)). If it is, prices exclude PPN.

## 1. Enterprise subscription

| | |
| :-- | :-- |
| **Subscription (client price)** | Flat monthly fee, for example **IDR 12,500,000 / month**. List price for clients who contract with Navario. |
| **Navario's share** | **IDR 7,500,000 / month**, fixed, for the dedicated server and maintenance (hosting, backups, upgrades, second-line support). If the client contracts with the partner, the partner pays this share and sets its own client price. If the client contracts with Navario, the rest of the client price is the partner's share. See [8_partnership_model.md](8_partnership_model.md#2-enterprise-partner-share). Direct deals with no partner: Navario keeps the full client price. |
| **Users** | Unlimited |
| **Server** | Dedicated server, spec *TBD (vCPU / RAM / storage)* |
| **AI Business Assistant** | Included, **BYOK**: the client's own AI key, billed by the provider to the client. No AI Quota from Navario. Give the client an estimated AI cost per month from [ai_cost_simulation.md](ai_cost_simulation.md) so they can budget. |
| **Hosting** | Daily backups kept 30 days |
| **Support** | Priority, first response within 6 hours. Partner handles first line, Navario second line. |

When a client outgrows the server, move them to a larger server tier. The server cost comes out of Navario's share, so the server spec sets Navario's margin.

## 2. Enterprise setup

| | |
| :-- | :-- |
| **Navario's technical part** | From IDR 25,000,000 (multi-company, custom workflows, integrations) |
| **Partner consultancy** | Billed separately by the partner, at the partner's own rate |
| **Data migration and customization** | Same price list as retail: [5_saas_pricing_model.md](5_saas_pricing_model.md#3-add-ons) |

## 3. Benchmark: Odoo

At 30+ users, Odoo Custom costs over Rp 7.6M per month in licences alone, before hosting and partner fees (Odoo prices in [5_saas_pricing_model.md](5_saas_pricing_model.md#4-benchmark-odoo)). A flat IDR 12.5M with unlimited users wins as headcount grows.

## 4. AI projects

Custom AI work for any industry, on any system ([C4](0_business_constraint.md#2-offer)). Scope and process: [12_ai_project.md](12_ai_project.md).

| | |
| :-- | :-- |
| **Development** | Fixed price per project, quoted after a scoping call. *Price guide TBD.* |
| **Server maintenance** | Monthly fee if Navario hosts and runs it. *Price TBD.* |
| **AI usage** | BYOK: the client's own API key, billed by the provider to the client. Navario does not resell AI usage. |

## 5. Pilot

A limited offer for the first enterprise clients: **1–2 slots**, open for 90 days. Pilots run instead of SaaS pilots, not next to them ([7_go_to_market.md](7_go_to_market.md#4-pilot-capacity-saas-or-enterprise)).

### Why pilots

- **Proof:** an enterprise reference is what partners and larger prospects ask for first ([X2](1_challenges.md#1-sales-and-trust)).
- **Server spec:** real load sets the dedicated server spec and the enterprise fee (open decision below).
- **Partner model:** the first deal shows partners how the split works in practice.

### Who qualifies

- [ ] Any industry ([C4](0_business_constraint.md#2-offer)), with enough users or branches that a flat fee makes sense. Modules beyond the retail five need a partner who configures them ([C5](0_business_constraint.md#2-offer)).
- [ ] A decision maker attended the demo and has a budget.
- [ ] Can set up its own paid AI key on a billing account it owns (BYOK).
- [ ] Pilot scope uses features marked **Works**; anything planned has a delivery date in the quote. Integrations and custom workflows are quoted separately, after the pilot.
- [ ] Agrees in writing to the pilot commitments (pilot terms below).

### Pilot terms

| | Navario gives | Client gives |
| :-- | :-- | :-- |
| **Price** | Pilot discount (open decision below), on top of the list offer | Pays upfront ([C8](0_business_constraint.md#3-commercial-rules)). No free pilots. |
| **Scope** | List offer: unlimited users, dedicated server, priority support | A fixed pilot scope agreed before work starts. Anything extra is a change request. |
| **Attention** | Direct founder access and a weekly check-in during setup | A project owner on their side, and 30 minutes a week for feedback |
| **AI** | Monthly AI cost estimate from [ai_cost_simulation.md](ai_cost_simulation.md) | Its own AI key, paid to the provider directly |
| **Proof** | — | Logo, testimonial, short case study and one reference call, one month after go-live |

**Pilot period:** 3 months from go-live. After that, the client continues on the list offer or leaves with its data.

All terms go into the Bahasa Indonesia service agreement ([L2](2_legal.md#1-rules)). No pilot before the legal entity exists ([L1](2_legal.md#1-rules)).

### Before the first enterprise pilot

- [ ] Per-company AI key (BYOK) is **Works** ([4_product_scope.md](4_product_scope.md#2-first-paid-client), 2.2).
- [ ] A backup developer with server access is in place ([X6](1_challenges.md#2-founder-capacity)).

### Success criteria (measured at the end of the pilot)

- [ ] **Live.** All pilot users enter daily transactions in Navario.
- [ ] **Used.** The assistant is used every week across the departments in the pilot.
- [ ] **Measured.** Server load and monthly AI cost on the client's key are recorded, and the server spec is set.
- [ ] **Proof.** Testimonial, logo permission and case study are received.
- [ ] **Converted.** The client continues on the list offer.

## 6. Financial model

Potential profit per enterprise client, from [financial_model.py](script/financial_model.py). It uses the draft prices above. To change assumptions, edit the script and re-run it. Never calculate by hand. Company costs and break-even are in [5_saas_pricing_model.md](5_saas_pricing_model.md#company-costs-and-break-even).

**Status:** Before dedicated server cost, which is unknown (open decision below). AI cost is zero for Navario (BYOK). Setup uses the "from" price, so year 1 is the minimum.

| Deal | Profit / month | Year 1, incl. setup |
| :-- | --: | --: |
| Through a partner (Navario's share) | 7.50M | 115.00M |
| Direct, no partner | 12.50M | 175.00M |

**What this means:**
- **One enterprise client through a partner earns about as much a month as a 30-user retail client on stack C**, with no AI cost risk. Enterprise is the better use of founder time once a partner sells it.
- **The server spec sets the margin.** Every rupiah of dedicated server cost comes out of the profit above.
- **AI projects are not modelled yet.** Profit per project = development price − founder days × a target day rate. Both are open decisions below.

## Tasks

- [ ] **Enterprise BYOK package.** Done when: the server spec is set and the per-company AI key setting works in a demo.
- [ ] **AI project pricing.** Done when: section 4 has a development price guide and a monthly server maintenance fee, and the script computes profit per project.
- [ ] **Pilot offer page.** Depends on: the pilot open decisions below. Done when: a one-page Bahasa Indonesia offer exists with the slot limit and the deadline.
- [ ] **Pilot scope template.** Done when: a one-page template lists what is in and out of the pilot scope, to attach to the quotation.

## Assumptions

- Navario's share covers the dedicated server, maintenance and second-line support.
- Partners can add a markup that clients will pay.
- A direct enterprise pilot (no partner) can be run solo.

## Open decisions

- [ ] **Minimum term.** A dedicated server and a large setup on a monthly plan is risky. Recommendation: 12-month minimum term for enterprise. Retail stays monthly.
- [ ] **BYOK on a free AI tier.** Providers such as Google may use free-tier data for training, which breaks the proposal's "your data isn't used to train AI". Recommendation: the agreement requires a paid billing account with the provider.
- [ ] **Who picks the model stack under BYOK?** Recommendation: Navario sets it and gives the client the cost estimate.
- [ ] **Enterprise server spec** (vCPU / RAM / storage) and its monthly cost, for the enterprise fee and section 6. Recommendation: set it from the load of a 30-user demo.
- [ ] **AI project price guide** for development and monthly server maintenance. Recommendation: fixed price per project after a scoping call. Charge for scoping only if it includes a written design.
- [ ] **Target day rate for AI projects.** Needed to check profit per project. Recommendation: set it with the price guide, and quote no project below it.
- [ ] **Pilot: slots before a partner is signed.** With no partner, the founder also does first-line support. Recommendation: only 1 enterprise pilot until a partner is signed.
- [ ] **Pilot: discount.** Recommendation: 50% off Navario's setup part, full monthly fee. The monthly fee is the recurring revenue and sets the price after the pilot.
- [ ] **Pilot: direct or through a partner.** Recommendation: take the first enterprise pilot direct if it comes from the warm network, and bring in a signed partner only for consultancy and training. Partners handle only sales and functional work ([C9](0_business_constraint.md#3-commercial-rules)).
- [ ] **Pilot: period.** Recommendation: 3 months from go-live, the same as the SaaS pilot.
- [ ] **Pilot: no testimonial or case study.** Recommendation: the setup discount is paid back, written in the agreement.
