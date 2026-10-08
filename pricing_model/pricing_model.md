# Pricing Model

Internal. **Retail** means direct sales to SMEs at list price, per user. **Enterprise** means a flat monthly fee with unlimited users, sold through partners (see [partnership_model.md](../partnership_model/partnership_model.md)).

## Principles

- **Fixed price.** Every quote is a fixed total agreed before work starts. No hourly billing. Ranges below are internal guides; the client only ever sees one number.
- **Retail is priced per user** (minimum 3 users). **Enterprise is flat** (unlimited users), limited by server capacity and AI questions instead of headcount.
- **One AI unit: "AI question".** One message a user sends to the assistant, however many tool steps it takes to answer. Use this term everywhere (not "token" or "query"), because it is what users see in their usage tracking.
- **Scope matches the proposal.** Only list what the demo can show: Accounting, Buying, Selling, Stock, Asset Management, Indonesian chart of accounts, PPN and PPh setup, Bahasa Indonesia, local document formats, company branding.
- **PPN:** Depends on whether the new entity is PKP (see [README](../README.md#open-business-decisions)). If it is, prices exclude PPN.

## 1. Retail (direct)

| | |
| :-- | :-- |
| **Subscription** | IDR 400,000 / user / month *(draft; confirm after the cost simulation and the Odoo comparison in section 4)* |
| **Minimum** | 3 users (IDR 1,200,000 / month) |
| **Annual** | 15% off (12 months prepaid) |
| **Modules** | Accounting, Buying, Selling, Stock, Asset Management |
| **AI Business Assistant** | 100 AI questions per user per month, pooled across the company |
| **Hosting** | Shared cloud, daily backups kept 14 days |
| **Support** | Chat, first response within 24 hours |

Server health is monitored and backed up automatically 24/7.

### Setup (one-time, choose one)

| | **Fast-Track** | **Standard** |
| :-- | :-- | :-- |
| **Price** | IDR 3,500,000 | IDR 8,500,000 |
| **Suggested for** | Up to ~10 users, 1 warehouse | Up to ~30 users, multiple warehouses or branches |
| **Needs discussion** | 1 × 45-min call | 1 × 90-min workshop |
| **Configuration** | Trading company template, chart of accounts, tax defaults, users and roles | Fast-Track + company-branded print formats, approval rules, multiple warehouses or branches |
| **Data import** | Self-service Excel templates | Self-service Excel templates |
| **Training** | Video library + 1 × 90-min live online session | Video library + 2 × 90-min live online sessions |

Anything not in this table is an add-on (section 3) or a change request, quoted separately at a fixed price.

## 2. Enterprise (through partners)

| | |
| :-- | :-- |
| **Subscription** | Flat monthly fee, for example **IDR 12,500,000 / month** |
| **Users** | Unlimited |
| **Server** | Dedicated server, spec *TBD (vCPU / RAM / storage)* |
| **AI Business Assistant** | *TBD* AI questions per month, company pool *(set after the cost simulation)* |
| **Hosting** | Daily backups kept 30 days |
| **Support** | Priority, first response within 6 hours. Partner handles first line, Navario second line. |
| **Setup** | Navario's technical part from IDR 25,000,000 (multi-company, custom workflows, integrations). Partner consultancy is billed separately by the partner. |

When a client outgrows the limits, move them to a larger server tier or add AI top-ups. Seats never trigger a price change.

## 3. Add-ons (retail and enterprise)

### AI question top-ups (monthly, added to the company pool, unused questions don't roll over)

> **Below cost on Gemini 3.8 Flash at 2027 prices** (~IDR 1,500 per question). Re-price at ≥ 2x the cost per question of the chosen model stack. See [ai_cost_simulation.md](../cost_simulation/ai_cost_simulation.md).

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
- **Enterprise:** at 30+ users, Odoo Custom costs over Rp 7.6M per month in licences alone, before hosting and partner fees. A flat IDR 12.5M with unlimited users wins as headcount grows.

To do:
- [ ] Ask 2–3 Odoo partners in Jakarta for a quote for a 5-user and a 30-user trading company (licence + implementation), to get real first-year totals to compare against.
- [ ] Try Odoo's AI on a trial database and note what our assistant does better in Bahasa Indonesia.

## 5. Check before using these prices

- [ ] **AI cost per question.** First estimate: IDR 350–1,500 per question depending on the Gemini model ([ai_cost_simulation.md](../cost_simulation/ai_cost_simulation.md)). Choose the model stack, then set allowances and top-up prices.
- [ ] **Is 100 questions per user enough?** That is ~5 per user per working day. Track real usage of the first clients and adjust.
- [ ] **Retail per-user price** versus Odoo (section 4) and versus Accurate Online and Jurnal (Mekari).
- [ ] **Enterprise server spec and AI pool** for IDR 12.5M.
