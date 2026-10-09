# SaaS Pricing Model (Retail)

Internal. The retail channel: direct sales to SMEs, list price per user, AI questions included, shared cloud. Enterprise and AI projects are in [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md).

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
- **The AI is no longer unique against Odoo** (Odoo Custom includes agentic AI). Our edge has to be: Bahasa Indonesia first, ERP data and access rules built in, simpler screens, and a local person who answers.

## Tasks

- [ ] **Measure AI cost.** Done when: 50 realistic questions are logged with tokens, and the averages replace the assumptions in the script (see the cost simulation "Next steps").
- [ ] **Choose the model stack.** Depends on: measure AI cost. Done when: the script is re-run and the tables in [ai_cost_simulation.md](ai_cost_simulation.md) match its output.
- [ ] **Fix the price.** Depends on: model stack. Done when: top-ups are priced at ≥ 2x cost per question and the price per user is final.
- [ ] **Odoo first-year total.** Done when: 2–3 Odoo partners in Jakarta have quoted a 5-user and a 30-user trading company (licence + implementation).
- [ ] **Odoo AI test.** Done when: you have tried Odoo's AI on a trial database and noted what our assistant does better in Bahasa Indonesia.
- [ ] **Validate the allowance.** After the first clients go live. Done when: real AI questions per user are measured (is 100 per user enough?), and the allowance is confirmed or changed.

## Open decisions

- [ ] **Price per user vs Odoo** (section 4), Accurate Online and Jurnal (Mekari). Recommendation: decide after the cost data. Compete on first-year total cost, not licence price.
- [ ] **AI model stack.** Recommendation: price on stack C until quality tests prove a cheaper stack.
