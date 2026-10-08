# Business Constraints

Internal. The hard limits Navario works within: facts we cannot change now, and rules we chose to keep. Every other doc must respect them. Challenges and risks are in [1_challenges.md](1_challenges.md). Legal rules are in [3_legal.md](3_legal.md).

When a constraint changes, update this file first, then the docs in the "Handled in" column.

## 1. Founder and capacity

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C1 | **Solo founder.** One person sells, builds, implements and supports. | Build only the demo features, then sell. At most ~50% of each week on AI projects. Partners bring reach and first-line support. | [scope.md](scope.md#build-rule), [marketing_strategy.md](marketing_strategy.md#tasks), [partnership_model.md](partnership_model.md) |
| C2 | **No ERP or accounting background.** | Business process know-how comes from partners, a fixed discovery checklist, and later an accounting-background support hire. | [partnership_model.md](partnership_model.md#why-partners), [process_flow.md](process_flow.md#stage-2-needs-discussion-4590-min-included-in-setup) |

## 2. Offer

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C3 | **AI first. No ERP-only deals.** | Every package includes the AI Business Assistant. Decline ERP-only prospects politely. | [pricing_model.md](pricing_model.md#principles), [marketing_strategy.md](marketing_strategy.md#1-positioning) |
| C4 | **Product market: trading companies only.** AI projects: any industry, but they must reuse the Navario assistant. | No manufacturing, retail chain or services examples in product messaging. | [marketing_strategy.md](marketing_strategy.md#1-positioning), [scope.md](scope.md#4-long-term-do-not-sell-yet) (4.1) |
| C5 | **Five modules only:** Accounting, Buying, Selling, Stock, Asset Management. Not offered: Manufacturing, Projects, HR/Payroll, Finance/budgeting. | If asked for another module, answer "not offered now". | [scope.md](scope.md#3-claimed-in-the-proposal-likely-weak) (3.5) |
| C6 | **Claim only what works in a demo today.** | Unbuilt features (e.g., e-Faktur export) are stated as not included. | [scope.md](scope.md) |
| C7 | **Gemini only.** The product and the cost model are built on it. | BYOK means a Gemini key for now. | [pricing_model.md](pricing_model.md#open-decisions) |

## 3. Commercial rules

| # | Constraint | What it forces | Handled in |
| :-- | :-- | :-- | :-- |
| C8 | **Fixed price, cash first.** | One fixed total per quote. Work starts after payment clears. Anything extra is a change request with its own fixed quote. Commissions are paid only after the client pays. | [process_flow.md](process_flow.md#stage-3-fixed-price-quote--contract), [partnership_model.md](partnership_model.md#rules) |
| C9 | **Sign before you teach.** | Before signing, a prospective partner gets only the proposal, a live demo and the partner summary. No system access or training. | [partnership_model.md](partnership_model.md#rules) (rule 0) |
| C10 | **Navario owns the platform and the recurring billing.** No services that compete with partners (bookkeeping, tax filing, audit, consultancy). | Partners bill consultancy; Navario bills subscription and custom code. | [partnership_model.md](partnership_model.md#implementation-partner-who-bills-what) |
