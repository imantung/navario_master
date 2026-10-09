# SaaS Pricing Model (Retail)

Internal. The retail channel: direct sales to SMEs, list price per user, AI questions included, shared cloud. Also the retail pilot offer (section 5) and the potential profit per client (section 6). Enterprise and AI projects are in [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md).

## Principles

- **Fixed price** ([C8](0_business_constraint.md#3-commercial-rules)). Every quote is a fixed total agreed before work starts. No hourly billing. Ranges below are internal guides; the client only ever sees one number.
- **No ERP-only deals** ([C3](0_business_constraint.md#2-offer)). Every package includes the AI Business Assistant.
- **Priced per user** (minimum 3 users), AI questions included.
- **One AI unit: "AI question".** One message a user sends to the assistant, however many tool steps it takes to answer. Use this term everywhere (not "token" or "query"), because it is what users see in their usage tracking.
- **Navario carries the AI cost.** So the price must cover AI at 2027 Gemini rates, and the product must enforce a hard limit ([X9, X10](1_challenges.md#3-margin)).
- **Scope matches the proposal.** Only list what the demo can show: Accounting, Buying, Selling, Stock, Asset Management, Indonesian chart of accounts, PPN and PPh setup, Bahasa Indonesia, local document formats, company branding.
- **PPN:** Depends on whether the new entity is PKP (see [2_legal.md](2_legal.md#open-decisions)). If it is, prices exclude PPN.

## 1. Subscription

| | |
| :-- | :-- |
| **Price** | IDR 400,000 / user / month *(draft; confirm after the cost simulation and the Odoo comparison in section 4)* |
| **Minimum** | 3 users (IDR 1,200,000 / month) |
| **Annual** | 15% off (12 months prepaid) |
| **Modules** | Accounting, Buying, Selling, Stock, Asset Management |
| **AI Business Assistant** | 100 AI questions per user per month, pooled across the company |
| **Hosting** | Shared cloud, daily backups kept 14 days |
| **Support** | Chat, first response within 24 hours |

Server health is monitored and backed up automatically 24/7.

## 2. Setup (one-time, choose one)

| | **Fast-Track** | **Standard** |
| :-- | :-- | :-- |
| **Price** | IDR 3,500,000 | IDR 8,500,000 |
| **Suggested for** | Up to ~10 users, 1 warehouse | Up to ~30 users, multiple warehouses or branches |
| **Needs discussion** | 1 × 45-min call | 1 × 90-min workshop |
| **Configuration** | Trading company template, chart of accounts, tax defaults, users and roles | Fast-Track + company-branded print formats, approval rules, multiple warehouses or branches |
| **Data import** | Self-service Excel templates | Self-service Excel templates |
| **Training** | Video library + 1 × 90-min live online session | Video library + 2 × 90-min live online sessions |

Anything not in this table is an add-on (section 3) or a change request, quoted separately at a fixed price.

## 3. Add-ons

### AI question top-ups (monthly, added to the company pool, unused questions don't roll over)

> **Below cost on Gemini 3.8 Flash at 2027 prices** (~IDR 1,500 per question). Re-price at ≥ 2x the cost per question of the chosen model stack. See [ai_cost_simulation.md](ai_cost_simulation.md).

| Pack | Price | Price per question |
| :-- | :-- | :-- |
| +500 questions | IDR 250,000 / month | IDR 500 |
| +1,000 questions | IDR 450,000 / month | IDR 450 |
| +2,500 questions | IDR 1,000,000 / month | IDR 400 |

### Trial extension

- Extra 30 days on the client's own trial instance: **IDR 500,000**, fully credited to the setup fee if they sign.

### Professional services

- Additional needs discussion or training session (online, 90 min): **IDR 1,500,000**
- Onsite visit, Jabodetabek (up to 4 hours): **IDR 2,500,000**

### Data migration

- Self-service import with Excel templates: **Free**
- Master data cleanup and import (up to 5,000 records): **IDR 3,000,000**
- Open AR/AP invoice migration: **IDR 4,000,000**
- Historical general ledger migration: **IDR 8,000,000 per fiscal year**

### Customization (fixed quote after review)

- Custom print format: from **IDR 1,500,000** per document layout
- Custom fields and workflow on a document type: from **IDR 3,000,000**
- New module or integration: from **IDR 8,000,000**

## 4. Benchmark: Odoo

Odoo Indonesia list prices, from [odoo.com/id_ID/pricing](https://www.odoo.com/id_ID/pricing) (checked 8 Oct 2026):

| Odoo plan | Price per user per month | Notes |
| :-- | :-- | :-- |
| One App Free | Rp 0 | One app only, unlimited users |
| Standard | Rp 137,500 (annual) / Rp 170,000 (monthly) | All apps, Odoo Online only, no custom modules. First 12 months discounted to Rp 110k / 136k. |
| Custom | Rp 255,000 (annual) / Rp 320,000 (monthly) | Adds Studio, **agentic AI**, multi-company, external API, on-premise or Odoo.sh (hosting extra). First 12 months discounted to Rp 203k / 255k. |
| Light user | Rp 45,000 | By quote |

**What this means for us:**
- **Don't compete on licence price.** Odoo Standard is about a third of our draft retail price per user. At IDR 400k we are above even Odoo Custom.
- **Compete on total cost and "done for you".** An Odoo licence comes without implementation; Indonesian SMEs usually hire an Odoo partner separately, at variable cost. Our price includes hosting, the Indonesian setup, the AI assistant and a fixed-price setup. Compare **first-year total cost**, not monthly licence.
- **The AI is no longer unique against Odoo** (Odoo Custom includes agentic AI). Our edge is listed in [3 §2 Competitive advantage](3_brand_identity.md#competitive-advantage).

### Local accounting software

The low-price competitor for small traders ([market_analysis.md](market_analysis.md#3-competitors)).

| Product | Price | Notes |
| :-- | :-- | :-- |
| Accurate Online, base plan | Rp 333,000 / month, incl. PPN | 1 user, 1 company, all features. Extra user Rp 22,200 / month; extra branch Rp 99,900 / month. Monthly billing, 30-day free trial. From [accurate.id/harga](https://accurate.id/harga/) (checked 9 Oct 2026). |
| Jurnal Essentials | Rp 399,000 / month list; Rp 359,100 first contract, paid yearly | 3 users. Accounting "supported by AI", inventory, multiple warehouses, approvals. From [jurnal.id/id/harga](https://www.jurnal.id/id/harga/) (checked 9 Oct 2026). |
| Jurnal Plus | Rp 899,000 / month list; Rp 629,300 first contract, paid yearly | 5 users. Adds BOM, multi-currency. Free implementation help and training in all plans. |
| Jurnal 360 | By quote | 10 users. Batch/serial, bin locations. |

**What this means for us:** a 3-user company pays several times more for Navario than for Accurate or Jurnal. Don't compete for the smallest traders. Target companies that have outgrown these tools.

## 5. Pilot

A limited offer for the first retail clients: **3 slots**, open for 90 days. Pilots run instead of enterprise pilots, not next to them ([7_go_to_market.md](7_go_to_market.md#4-pilot-capacity-saas-or-enterprise)).

### Why pilots

- **Proof:** each pilot becomes a logo, a testimonial, a case study and a reference call ([X2](1_challenges.md#1-sales-and-trust)).
- **Cost data:** real AI questions per user, to fix the retail price and allowance ([X8](1_challenges.md#3-margin)).
- **Product feedback:** what trading companies actually ask the assistant.

### Who qualifies

- [ ] Trading company (distributor, wholesaler, trader) ([C4](0_business_constraint.md#2-offer)).
- [ ] Fits the Fast-Track or Standard setup (section 2). No customization or historical ledger migration during the pilot.
- [ ] The owner or a director attended the demo and will sponsor the pilot.
- [ ] Can provide master data (customers, suppliers, items, opening balances) in the Excel templates within 2 weeks.
- [ ] Agrees in writing to the pilot commitments (pilot terms below).

### Pilot terms

| | Navario gives | Client gives |
| :-- | :-- | :-- |
| **Price** | Pilot discount (open decision below), on top of the list offer | Pays upfront, like any client ([C8](0_business_constraint.md#3-commercial-rules)). No free pilots. |
| **Scope** | List offer: modules, AI questions, hosting, support | Uses only what the demo showed, plus any planned feature with a delivery date in the quote |
| **Attention** | Direct founder access and a fortnightly check-in | 30 minutes every 2 weeks for feedback |
| **Data** | Data export anytime | Permission to log AI usage per question (for cost, not content) |
| **Proof** | — | Logo, testimonial, short case study and one reference call, one month after go-live |

**Pilot period:** 3 months from go-live. After that, the client continues on the list offer or leaves with its data.

All terms go into the Bahasa Indonesia service agreement ([L2](2_legal.md#1-rules)). No pilot before the legal entity exists ([L1](2_legal.md#1-rules)).

### Success criteria (measured at the end of the pilot)

- [ ] **Live.** Daily transactions (sales, purchases, stock) are entered in Navario, not in spreadsheets.
- [ ] **Used.** The assistant is used every week by at least half of the users.
- [ ] **Measured.** AI questions per user are logged and fed into [ai_cost_simulation.md](ai_cost_simulation.md).
- [ ] **Proof.** Testimonial, logo permission and case study are received.
- [ ] **Converted.** The client continues on the list offer.

## 6. Financial model

Potential profit per retail client, from [financial_model.py](script/financial_model.py). It uses the draft prices above and the AI cost from [ai_cost_simulation.py](script/ai_cost_simulation.py). To change assumptions, edit the script and re-run it. Never calculate by hand.

**Status:** Before server, support and fixed costs, which are unknown. Assumes every client uses its full AI question allowance, so AI cost is the worst case.

### AI cost per user per month (IDR, 100 questions)

| Stack | AI cost | Share of price |
| :-- | --: | --: |
| A. Budget (2.5 Lite + 2.5 Flash) | 34,763 | 9% |
| B. Current 2026 (3.1 Lite + 3.8 Flash) | 75,232 | 19% |
| C. Current 2027 (3.1 Lite + 3.8 Flash) | 148,839 | 37% |

### Profit per client (IDR)

"Referred" pays the partner 15% of the subscription (option A in [8_partnership_model.md](8_partnership_model.md#1-saas-commission), not decided).

| Stack | Client | Revenue / month | Profit / month, direct | Profit / month, referred | Year 1, direct, incl. setup | Year 1, annual prepaid, incl. setup |
| :-- | :-- | --: | --: | --: | --: | --: |
| A | 3 users, Fast-Track | 1.20M | 1.10M | 0.92M | 16.65M | 14.49M |
| A | 10 users, Fast-Track | 4.00M | 3.65M | 3.05M | 47.33M | 40.13M |
| A | 30 users, Standard | 12.00M | 10.96M | 9.16M | 139.99M | 118.39M |
| B | 3 users, Fast-Track | 1.20M | 0.97M | 0.79M | 15.19M | 13.03M |
| B | 10 users, Fast-Track | 4.00M | 3.25M | 2.65M | 42.47M | 35.27M |
| B | 30 users, Standard | 12.00M | 9.74M | 7.94M | 125.42M | 103.82M |
| C | 3 users, Fast-Track | 1.20M | 0.75M | 0.57M | 12.54M | 10.38M |
| C | 10 users, Fast-Track | 4.00M | 2.51M | 1.91M | 33.64M | 26.44M |
| C | 30 users, Standard | 12.00M | 7.53M | 5.73M | 98.92M | 77.32M |

**What this means:**
- **On stack C, AI takes 37% of the price** before server and support. Plan prices on stack C until a cheaper stack passes quality tests.
- **A 3-user referred client on stack C leaves about 0.57M a month** to cover its share of the server, support and fixed costs. Small referred clients are the thinnest margin.
- **Annual prepaid costs a lot of year-1 profit** (the 15% discount comes out of the profit, not the AI cost). Offer it for cash flow, not by default.

### Market potential

Market size from [market_analysis.md](market_analysis.md#1-market-size): about 42,600 trading small and medium firms (estimate). Assumes 10 users per client at list price, stack C, direct sales.

| Paying clients | Share of trading firms | Subscription revenue / year (IDR) | Profit / year, before server, support, fixed (IDR) |
| --: | --: | --: | --: |
| 10 | 0.02% | 0.5B | 0.3B |
| 30 | 0.07% | 1.4B | 0.9B |
| 100 | 0.23% | 4.8B | 3.0B |
| 300 | 0.70% | 14.4B | 9.0B |

If every trading small and medium firm were a client: about IDR 2,045B subscription revenue a year. This is a ceiling, not a target.

**What this means:** 100 clients is a 3B-a-year business and needs under a quarter of one percent of the market. Growth is limited by sales and support capacity, not by market size.

### Company costs and break-even

Shared by retail, enterprise and AI projects.

| Input | Source | Value |
| :-- | :-- | :-- |
| Server cost per retail client (shared cloud) | [techstack.md](techstack.md#open-decisions) | Unknown |
| Dedicated server cost per enterprise client | [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#open-decisions) | Unknown |
| Support hire cost | [9_saas_process_flow.md](9_saas_process_flow.md#support-coverage) | Estimate |
| Payment processing and bank fees | — | Unknown |
| Fixed costs: tools, domain, backup developer retainer, notary and lawyer, bookkeeping | — | Unknown |

- **Break-even:** monthly fixed costs ÷ average profit per client.
- **Support hire trigger:** check against [9_saas_process_flow.md](9_saas_process_flow.md#support-coverage).
- Founder time is not a cost line. It is limited by [C1](0_business_constraint.md#1-founder-and-capacity), not by money.

## Tasks

- [ ] **Measure AI cost.** Done when: 50 realistic questions are logged with tokens, and the averages replace the assumptions in the script (see the cost simulation "Next steps").
- [ ] **Choose the model stack.** Depends on: measure AI cost. Done when: the script is re-run and the tables in [ai_cost_simulation.md](ai_cost_simulation.md) match its output.
- [ ] **Fix the price.** Depends on: model stack. Done when: top-ups are priced at ≥ 2x cost per question and the price per user is final.
- [ ] **Odoo first-year total.** Done when: 2–3 Odoo partners in Jakarta have quoted a 5-user and a 30-user trading company (licence + implementation).
- [ ] **Odoo AI test.** Done when: you have tried Odoo's AI on a trial database and noted what our assistant does better in Bahasa Indonesia.
- [ ] **Validate the allowance.** After the first clients go live. Done when: real AI questions per user are measured (is 100 per user enough?), and the allowance is confirmed or changed.

- [ ] **Pilot offer page.** Depends on: the pilot open decisions below. Done when: a one-page Bahasa Indonesia offer exists with the 3-slot limit and the deadline.
- [ ] **Pilot clause in the service agreement.** Depends on: [2_legal.md](2_legal.md#tasks) sales documents. Done when: the pilot terms in section 5 are in the agreement.
- [ ] **Fixed costs.** Done when: every monthly fixed cost is listed with its real amount, and the script computes break-even.
- [ ] **Server cost.** Done when: the cost per retail client and per enterprise server is measured ([techstack.md](techstack.md#open-decisions)) and added to the script.

## Assumptions

- SMEs accept a per-user price above Odoo because the setup is "done for you".
- A 3-user minimum fits small traders.
- Pilot clients pay the full subscription, use the system daily, and give a case study.
- One shared server holds many retail clients.

## Open decisions

- [ ] **Full margin check.** Section 6 checks the price against AI cost and partner commission only. Recommendation: add server and support cost to the script before fixing the price.
- [ ] **Target profit per retail user.** Recommendation: set it once server and support cost are measured, before the retail price is final.
- [ ] **12-month revenue target.** Recommendation: set it from break-even (section 6), and use it in [7_go_to_market.md](7_go_to_market.md).
- [ ] **Price changes for existing clients.** Recommendation: the service agreement allows one price review a year, with 30 days' notice.
- [ ] **Price per user vs Odoo** (section 4), Accurate Online and Jurnal (Mekari). Recommendation: decide after the cost data. Compete on first-year total cost, not licence price.
- [ ] **AI model stack.** Recommendation: price on stack C until quality tests prove a cheaper stack.
- [ ] **Pilot: trial and pilot together?** Recommendation: pilots skip the 7-day trial. The pilot is the trial.
- [ ] **Pilot: AI limit.** A hard limit hides the real usage you want to measure. Recommendation: a higher limit during the pilot, with full logging.
- [ ] **Pilot: discount.** Recommendation: 50% off setup, list subscription. Don't discount the subscription: it sets the price clients expect after the pilot, and the retail price may still rise after cost data.
- [ ] **Pilot: period.** Recommendation: 3 months from go-live. Long enough for one month-end closing and the case study.
- [ ] **Pilot: no testimonial or case study.** Recommendation: the setup discount is paid back, written in the agreement.
