# Summary

Internal. How the Navario business model fits together. Start here. Prices are not repeated here; they are in [5_saas_pricing_model.md](5_saas_pricing_model.md) and [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md). Assumptions and open decisions live in each doc, under `## Assumptions` and `## Open decisions`.

**Codes used across docs:** C = constraints ([0](0_business_constraint.md)), X = challenges ([1](1_challenges.md)), L = legal rules ([2](2_legal.md#1-rules)).

## 1. The business model

**In one line:** Navario sells an AI Business Assistant with a complete ERP to Indonesian trading companies. It is hosted by Navario and sold at one fixed price. A second offer, AI projects, is custom AI work on any system and brings cash in sooner.

### What is sold

| | **Retail (SaaS)** | **Enterprise** | **AI projects** |
| :-- | :-- | :-- | :-- |
| **Buyer** | Trading SMEs, about 3–30 users | Larger companies in any industry: many users, branches or companies | Any industry |
| **What** | ERP (five modules) + AI assistant | Same, any ERPNext module, unlimited users | Types in the scope catalogue (MCP server, automation, …) |
| **Price shape** | Per user per month + one-time setup + add-ons | Flat monthly fee + setup | Fixed price per project + monthly maintenance if Navario hosts it |
| **Who pays for AI** | Navario (AI question pool with a hard limit) | Client (BYOK, own AI key) | Client (BYOK) |
| **Hosting** | Shared cloud | Dedicated server | Navario, if maintained |
| **Channel** | Direct, Referral Partners | Implementation Partners (model A or B), or direct | Founder's startup network |
| **Docs** | [5](5_saas_pricing_model.md) (incl. pilot), [9](9_saas_process_flow.md) | [6](6_enterprise_pricing_model.md) (incl. pilot), [11](11_enterprise_process_flow.md) | [12](12_ai_project.md), [6 §4](6_enterprise_pricing_model.md#4-ai-projects) |

### Where the money comes from

| | Recurring | One-time |
| :-- | :-- | :-- |
| **Retail** | Subscriptions, AI question top-ups | Setup, data migration, customization, training, trial extensions |
| **Enterprise** | Navario's share (model A) or the client price minus the partner share (model B) | Navario's technical setup and customization |
| **AI projects** | Server maintenance | Development |

In the short term, most cash comes from AI projects and setup fees. In the long term, the company's value is its recurring revenue. Whether the prices cover the costs is checked in the financial model ([5 §6](5_saas_pricing_model.md#6-financial-model), [6 §6](6_enterprise_pricing_model.md#6-financial-model)).

### Why a client picks Navario

Lead with the AI assistant: ask in plain Bahasa Indonesia, get answers from the company's own live data. No single advantage is unique; the edge is the combination plus "done for you". The full list, and which to lead with per competitor, is in [3 §2 Competitive advantage](3_brand_identity.md#competitive-advantage).

### How Navario protects itself

- Platform Core and Nava AI stay closed source and are only ever hosted by Navario ([L6](2_legal.md#1-rules)).
- The client keeps its data, ERPNext and its own Company_Custom code, so "no vendor lock-in" is true while Navario keeps its IP ([techstack.md](techstack.md#5-if-a-client-leaves)).
- Retail AI cost is capped by the question pool. Enterprise and AI project AI cost is the client's (BYOK).
- Partners do sales and ERP functional work only; technical details stay with Navario ([C9](0_business_constraint.md#3-commercial-rules)).
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

| # | Doc |
| :-- | :-- |
| 0–4 | Constraints, challenges, legal, brand, product scope |
| 5 | SaaS pricing, incl. pilot and financial model |
| 6 | Enterprise and AI project pricing, incl. pilot and financial model |
| 7 | Go-to-market |
| 8 | Partnership model |
| 9 | SaaS process flow |
| 10 | Partner onboarding process |
| 11 | Enterprise process flow |
| 12 | AI project |

One weak spot: 7 (go-to-market) comes before the partnership model (8) it depends on, and 6 depends on the split in 8.

Unnumbered references: [market_analysis.md](market_analysis.md), [techstack.md](techstack.md), [ai_cost_simulation.md](ai_cost_simulation.md), [financial_model.py](script/financial_model.py).

## 3. Missing documents

- [x] **Financial model.** Profit per client in [5 §6](5_saas_pricing_model.md#6-financial-model) and [6 §6](6_enterprise_pricing_model.md#6-financial-model). Server, support and fixed costs are still unknown.
- [x] **Enterprise process flow.** [11_enterprise_process_flow.md](11_enterprise_process_flow.md).
- [x] **AI projects.** [12_ai_project.md](12_ai_project.md). Scope catalogue still to define.

## 4. Founder decisions, 9 Oct 2026

Applied in the docs:

| Decision | Applied in |
| :-- | :-- |
| AI projects: any system, inside or outside Frappe/ERPNext, within a scope catalogue | [0](0_business_constraint.md) (C4), [12](12_ai_project.md), [1](1_challenges.md) (X5), [3](3_brand_identity.md), [4](4_product_scope.md) (4.1), [6](6_enterprise_pricing_model.md), [7](7_go_to_market.md), CLAUDE.md |
| No cash, runway or geography constraint | [0](0_business_constraint.md#not-constraints) |
| No Navario brand in the product, for retail too | [3](3_brand_identity.md) |
| Separate Referral and Implementation Partner pitches | [3](3_brand_identity.md#partners) |
| Name hosting and AI providers only when asked | [3](3_brand_identity.md#hard-questions), [2](2_legal.md) (L7), [techstack.md](techstack.md#3-hosting) |
| DigitalOcean and Gemini are for now; a move to cheaper providers is planned | [techstack.md](techstack.md), [1](1_challenges.md) (X16) |
| Product scope: data export, multiple warehouses/branches/companies, per-user daily cap, asset question in the demo | [4](4_product_scope.md), [9](9_saas_process_flow.md) |
| New risks X15–X17 | [1](1_challenges.md#6-product-and-technology) |
| Enterprise: any industry; direct or with a partner, Navario looks for partners to help | [0](0_business_constraint.md) (C4), [1](1_challenges.md) (X18), [3](3_brand_identity.md), [6](6_enterprise_pricing_model.md#who-qualifies), [8](8_partnership_model.md), [10](10_partner_onboarding_process.md#stage-3-fit-check), [11](11_enterprise_process_flow.md), CLAUDE.md |
| Constraints changed: C5 is retail only (enterprise: any ERPNext module); C6 and C7 removed (build and sell in parallel, any AI model); C9 is now "functional yes, technical never"; C2 moved to X18 | [0](0_business_constraint.md), [1](1_challenges.md) (X1, X4, X13, X16, X19), [2](2_legal.md) (L5), [4](4_product_scope.md), [6](6_enterprise_pricing_model.md), [8](8_partnership_model.md#rules), [10](10_partner_onboarding_process.md), [11](11_enterprise_process_flow.md), [techstack.md](techstack.md), CLAUDE.md |
| All messaging says "growing companies", not "trading companies"; retail sales still target trading first. The proposal is for enterprise, so "ERP" stays in it. | [0](0_business_constraint.md) (C4), [3](3_brand_identity.md#2-positioning), CLAUDE.md |

Still open: legal entity timing (2), PKP (2, leaning non-PKP), pilot terms (5, 6), partner minimum commitment (8, 10).
