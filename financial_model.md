# Financial Model

Internal. Whether the prices cover the costs, and how many clients Navario needs. Prices are not repeated here; they come from [5_saas_pricing_model.md](5_saas_pricing_model.md) and [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md). AI cost comes from [ai_cost_simulation.md](ai_cost_simulation.md).

**Status:** Structure only. Most inputs are unknown. No cash or runway constraint for now ([0_business_constraint.md](0_business_constraint.md)).

## 1. Inputs

| Input | Source | Value |
| :-- | :-- | :-- |
| Retail price per user, setup fees | [5_saas_pricing_model.md](5_saas_pricing_model.md) | Draft |
| Enterprise client price and Navario's share | [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md) | Draft |
| AI cost per retail user | [ai_cost_simulation.md](ai_cost_simulation.md) | Estimate |
| Server cost per retail client (shared cloud) | [techstack.md](techstack.md#open-decisions) | Unknown |
| Dedicated server cost per enterprise client | [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#open-decisions) | Unknown |
| Partner commission and partner share | [10_partnership_model.md](10_partnership_model.md#open-decisions) | Open decision |
| Support hire cost | [11_saas_process_flow.md](11_saas_process_flow.md#support-coverage) | Estimate |
| Payment processing and bank fees | — | Unknown |
| Fixed costs: tools, domain, backup developer retainer, notary and lawyer, bookkeeping | — | Unknown |

## 2. Outputs

| Output | Formula |
| :-- | :-- |
| Margin per retail user per month | price per user − AI cost − server cost per user − partner commission (if referred) |
| Margin per enterprise client per month | Navario's share (model A) or client price − partner share (model B) − dedicated server cost |
| Margin per AI project | development price − founder days × a target day rate |
| Break-even | monthly fixed costs ÷ average margin per client |
| Support hire trigger | Check against [11_saas_process_flow.md](11_saas_process_flow.md#support-coverage) |

## Assumptions

- Founder time is not a cost line. It is limited by [C1](0_business_constraint.md#1-founder-and-capacity), not by money.
- One shared server holds many retail clients.

## Tasks

- [ ] **Fixed costs.** Done when: every monthly fixed cost is listed with its real amount.
- [ ] **Server cost.** Done when: the cost per retail client and per enterprise server is measured ([techstack.md](techstack.md#open-decisions)).
- [ ] **Script.** Depends on: fixed costs and server cost. Done when: `script/financial_model.py` computes section 2 from the inputs, and its output is copied here. Never calculate by hand, the same rule as the AI cost simulation.

## Open decisions

- [ ] **Target margin per retail user.** Recommendation: set it once the inputs are measured, before the retail price is final.
- [ ] **12-month revenue target.** Recommendation: set it from break-even, and use it in [7_go_to_market.md](7_go_to_market.md).
