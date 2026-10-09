# Summary

Internal. How the Navario business model fits together. Start here. Prices are not repeated here; they are in [5_saas_pricing_model.md](5_saas_pricing_model.md) and [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md). Assumptions and open decisions live in each doc, under `## Assumptions` and `## Open decisions`.

**Codes used across docs:** C = constraints ([0](0_business_constraint.md)), X = challenges ([1](1_challenges.md)), L = legal rules ([2](2_legal.md#1-rules)).

## 1. The business model

**In one line:** Navario sells an AI Business Assistant with a complete ERP to Indonesian trading companies. It is hosted by Navario and sold at one fixed price. A second offer, AI projects, is custom AI work on any system and brings cash in sooner.

### What is sold

| | **Retail (SaaS)** | **Enterprise** | **AI projects** |
| :-- | :-- | :-- | :-- |
| **Buyer** | Trading SMEs, about 3–30 users | Larger trading companies: many users, branches or companies | Any industry |
| **What** | ERP (five modules) + AI assistant | Same, unlimited users | Types in the scope catalogue (MCP server, automation, …) |
| **Price shape** | Per user per month + one-time setup + add-ons | Flat monthly fee + setup | Fixed price per project + monthly maintenance if Navario hosts it |
| **Who pays for AI** | Navario (AI question pool with a hard limit) | Client (BYOK Gemini key) | Client (BYOK) |
| **Hosting** | Shared cloud | Dedicated server | Navario, if maintained |
| **Channel** | Direct, Referral Partners | Implementation Partners (model A or B), or direct | Founder's startup network |
| **Docs** | [5](5_saas_pricing_model.md), [8](8_pilot_saas_model.md), [11](11_saas_process_flow.md) | [6](6_enterprise_pricing_model.md), [9](9_pilot_enterprise_model.md), [14](14_enterprise_process_flow.md) | [13](13_ai_project.md), [6 §4](6_enterprise_pricing_model.md#4-ai-projects) |

### Where the money comes from

| | Recurring | One-time |
| :-- | :-- | :-- |
| **Retail** | Subscriptions, AI question top-ups | Setup, data migration, customization, training, trial extensions |
| **Enterprise** | Navario's share (model A) or the client price minus the partner share (model B) | Navario's technical setup and customization |
| **AI projects** | Server maintenance | Development |

In the short term, most cash comes from AI projects and setup fees. In the long term, the company's value is its recurring revenue. Whether the prices cover the costs is checked in the [financial model](financial_model.md).

### Why a client picks Navario

- **Lead:** ask questions in plain Bahasa Indonesia and get answers from the company's own live data.
- **Supporting proof:** Indonesian tax and document setup, access rules built in, simpler screens, one fixed-price quote, a local person who answers, no vendor lock-in.
- **Not unique on its own:** the ERP (open source) and the AI (Odoo Custom has agentic AI). The edge is the combination plus "done for you".

### How Navario protects itself

- Platform Core and Nava AI stay closed source and are only ever hosted by Navario ([L6](2_legal.md#1-rules)).
- The client keeps its data, ERPNext and its own Company_Custom code, so "no vendor lock-in" is true while Navario keeps its IP ([techstack.md](techstack.md#5-if-a-client-leaves)).
- Retail AI cost is capped by the question pool. Enterprise and AI project AI cost is the client's (BYOK).
- Partners sign before they are taught ([C9](0_business_constraint.md#3-commercial-rules)).
- No Navario brand in the product: one codebase, and partners can white-label it.

### Critical path

```
Demo features Works (4 §1) ──────┐
                                  ├─► Pilots and first quote ─► Case studies ─► List price + partners
Legal entity registered (2) ─────┘
AI cost measured ─► Model stack ─► Financial model ─► Final retail price (5) ─► Website pricing page
```

Status on 9 Oct 2026: the demo is in progress. The legal entity is still under discussion. AI cost has not been measured.

## 2. Document order

The current order mostly works. One weak spot: 7 (go-to-market) comes before the docs it depends on (8, 9, 10), and 6 depends on the split in 10.

**Recommendation** (not applied): reorder so each doc depends only on earlier ones. The trade-off is renaming files and fixing every link.

| # | Now | Proposed |
| :-- | :-- | :-- |
| 0–6 | unchanged | unchanged |
| 7 | Go-to-market | Pilot SaaS |
| 8 | Pilot SaaS | Pilot enterprise |
| 9 | Pilot enterprise | Partnership model |
| 10 | Partnership model | Go-to-market |
| 11–14 | unchanged | unchanged |

Unnumbered references: [techstack.md](techstack.md), [ai_cost_simulation.md](ai_cost_simulation.md), [financial_model.md](financial_model.md).

## 3. Missing documents

- [x] **Financial model.** Structure written: [financial_model.md](financial_model.md). Inputs are mostly unknown.
- [x] **Enterprise process flow.** [14_enterprise_process_flow.md](14_enterprise_process_flow.md).
- [x] **AI projects.** [13_ai_project.md](13_ai_project.md). Scope catalogue still to define.
- [ ] **Operations runbook.** For the founder and the backup developer, not for clients. Done when: backup restore, server provisioning, upgrade testing, incident response and data export are written as steps. Needed before the first go-live ([X6](1_challenges.md#2-founder-capacity)).

## 4. Founder decisions, 9 Oct 2026

Applied in the docs:

| Decision | Applied in |
| :-- | :-- |
| AI projects: any system, inside or outside Frappe/ERPNext, within a scope catalogue | [0](0_business_constraint.md) (C4), [13](13_ai_project.md), [1](1_challenges.md) (X5), [3](3_brand_identity.md), [4](4_product_scope.md) (4.1), [6](6_enterprise_pricing_model.md), [7](7_go_to_market.md), CLAUDE.md |
| No cash, runway or geography constraint | [0](0_business_constraint.md#not-constraints) |
| No Navario brand in the product, for retail too | [3](3_brand_identity.md) |
| Separate Referral and Implementation Partner pitches | [3](3_brand_identity.md#partners) |
| Name hosting and AI providers only when asked | [3](3_brand_identity.md#hard-questions), [2](2_legal.md) (L7), [techstack.md](techstack.md#3-hosting) |
| DigitalOcean and Gemini are for now; a move to cheaper providers is planned | [techstack.md](techstack.md), [1](1_challenges.md) (X16) |
| Product scope: data export, multiple warehouses/branches/companies, per-user daily cap, asset question in the demo | [4](4_product_scope.md), [11](11_saas_process_flow.md) |
| New risks X15–X17 | [1](1_challenges.md#6-product-and-technology) |

Still open: legal entity timing (2), PKP (2, leaning non-PKP), pilot terms (8, 9), partner minimum commitment (10, 12).
