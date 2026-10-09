# Business Constraints

Internal. The hard limits Navario works within: facts we cannot change now, and rules we chose to keep. Every other doc must respect them. Challenges and risks are in [1_challenges.md](1_challenges.md). Legal rules are in [2_legal.md](2_legal.md).

When a constraint changes, update this file first, then the docs in the "Handled in" column.

## 1. Founder and capacity

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C1 | **Solo founder.** One person sells, builds, implements and supports. | Build and sell in parallel: demo while the product is built, never wait for a finished product. At most ~50% of each week on AI projects. Partners bring reach and first-line support. | [4_product_scope.md](4_product_scope.md#build-rule), [7_go_to_market.md](7_go_to_market.md#tasks), [8_partnership_model.md](8_partnership_model.md) |

## 2. Offer

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C3 | **AI first. No ERP-only deals.** | Every package includes the AI Business Assistant. Decline ERP-only prospects politely. | [5_saas_pricing_model.md](5_saas_pricing_model.md#principles), [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#principles), [3_brand_identity.md](3_brand_identity.md#2-positioning) |
| C4 | **Retail market: trading companies only.** Enterprise: any industry. AI projects: any industry, any system, inside or outside Frappe/ERPNext, within the scope catalogue. | Public marketing and retail messaging use trading examples only. Other industries appear only in enterprise and AI project conversations. AI projects are quoted only for types in the catalogue. | [3_brand_identity.md](3_brand_identity.md#2-positioning), [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#who-qualifies), [12_ai_project.md](12_ai_project.md#1-scope-catalogue) |
| C5 | **Retail: five modules only:** Accounting, Buying, Selling, Stock, Asset Management. Selling more is too much for one person. Enterprise: any ERPNext module, configured by the partner. | Retail: if asked for another module, answer "not offered now". Enterprise: other modules run on standard ERPNext screens. The assistant and Platform Core cover only what is **Works** in [4_product_scope.md](4_product_scope.md). | [4_product_scope.md](4_product_scope.md#3-claimed-in-the-proposal-likely-weak) (3.5), [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#who-qualifies) |

## 3. Commercial rules

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C8 | **Fixed price, cash first.** | One fixed total per quote. Work starts after payment clears. Anything extra is a change request with its own fixed quote. Commissions are paid only after the client pays. | [9_saas_process_flow.md](9_saas_process_flow.md#stage-3-fixed-price-quote--contract), [8_partnership_model.md](8_partnership_model.md#rules) |
| C9 | **Partners do sales and ERP functional work only. Technical details stay with Navario.** | Partners get demos, functional training and a demo instance, before or after signing. Never: source code, server access, architecture, AI design (prompts, tools, model stack). | [8_partnership_model.md](8_partnership_model.md#rules) (rule 0), [10_partner_onboarding_process.md](10_partner_onboarding_process.md) |
| C10 | **Navario owns Platform Core and Nava AI, keeps them closed source, and hosts them itself** ([L6](2_legal.md#1-rules)). No services that compete with partners (bookkeeping, tax filing, audit, consultancy). | Partners never modify core code. Billing depends on who signs with the client: the partner (partner sets the price, pays Navario's share) or Navario (Navario bills, pays the partner share). | [8_partnership_model.md](8_partnership_model.md#2-enterprise-partner-share) |

## Not constraints

Checked with the founder on 9 Oct 2026. Don't add them as constraints unless this changes.

- **Cash and runway.** No limit for now.
- **Geography.** No limit. Sell anywhere in Indonesia.

Removed or moved by the founder on 9 Oct 2026. The codes stay unused.

- **C6, claim only what works in a demo today.** Build and sell run in parallel (C1). Honesty still holds: only **Works** features are shown or described as working. A feature not built yet may be sold only as planned, with a delivery date in the quote.
- **C7, Gemini only.** Any AI model or provider is allowed. For now, retail and BYOK stay on one model (Gemini) until a client opportunity needs another.
- **C2, no ERP or accounting background.** Moved to challenges as [X18](1_challenges.md#2-founder-capacity).

## Assumptions

- The founder can spend ~50% of the week on AI projects and still finish the demo and sell (C1).
- Partners will supply ERP and accounting know-how ([X18](1_challenges.md#2-founder-capacity)). No partner has committed yet.
