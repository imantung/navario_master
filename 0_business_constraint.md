# Business Constraints

Internal. The hard limits Navario works within: facts we cannot change now, and rules we chose to keep. Every other doc must respect them. Challenges and risks are in [1_challenges.md](1_challenges.md). Legal rules are in [2_legal.md](2_legal.md).

When a constraint changes, update this file first, then the docs in the "Handled in" column.

## 1. Founder and capacity

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C1 | **Solo founder.** One person sells, builds, implements and supports. | Build only the demo features, then sell. At most ~50% of each week on AI projects. Partners bring reach and first-line support. | [4_product_scope.md](4_product_scope.md#build-rule), [7_go_to_market.md](7_go_to_market.md#tasks), [10_partnership_model.md](10_partnership_model.md) |
| C2 | **No ERP or accounting background.** | Business process know-how comes from partners, a fixed discovery checklist, and later an accounting-background support hire. | [10_partnership_model.md](10_partnership_model.md#why-partners), [process_flow.md](process_flow.md#stage-2-needs-discussion-4590-min-included-in-setup) |

## 2. Offer

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C3 | **AI first. No ERP-only deals.** | Every package includes the AI Business Assistant. Decline ERP-only prospects politely. | [5_saas_pricing_model.md](5_saas_pricing_model.md#principles), [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#principles), [3_brand_identity.md](3_brand_identity.md#2-positioning) |
| C4 | **Product market: trading companies only.** AI projects: any industry, but they must reuse the Navario assistant. | No manufacturing, retail chain or services examples in product messaging. | [3_brand_identity.md](3_brand_identity.md#2-positioning), [4_product_scope.md](4_product_scope.md#4-long-term-do-not-sell-yet) (4.1) |
| C5 | **Five modules only:** Accounting, Buying, Selling, Stock, Asset Management. Not offered: Manufacturing, Projects, HR/Payroll, Finance/budgeting. | If asked for another module, answer "not offered now". | [4_product_scope.md](4_product_scope.md#3-claimed-in-the-proposal-likely-weak) (3.5) |
| C6 | **Claim only what works in a demo today.** | Unbuilt features (e.g., e-Faktur export) are stated as not included. | [4_product_scope.md](4_product_scope.md) |
| C7 | **Gemini only.** The product and the cost model are built on it. | BYOK means a Gemini key for now. | [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#open-decisions) |

## 3. Commercial rules

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C8 | **Fixed price, cash first.** | One fixed total per quote. Work starts after payment clears. Anything extra is a change request with its own fixed quote. Commissions are paid only after the client pays. | [process_flow.md](process_flow.md#stage-3-fixed-price-quote--contract), [10_partnership_model.md](10_partnership_model.md#rules) |
| C9 | **Sign before you teach.** | Before signing, a prospective partner gets only the proposal, a live demo and the partner summary. No system access or training. | [10_partnership_model.md](10_partnership_model.md#rules) (rule 0) |
| C10 | **Navario owns Platform Core and Nava AI, keeps them closed source, and hosts them itself** ([L6](2_legal.md#1-rules)). No services that compete with partners (bookkeeping, tax filing, audit, consultancy). | Partners never modify core code. Billing depends on who signs with the client: the partner (partner sets the price, pays Navario's share) or Navario (Navario bills, pays the partner share). | [10_partnership_model.md](10_partnership_model.md#2-enterprise-partner-share) |
