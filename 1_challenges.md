# Challenges

Internal. Obstacles to overcome and risks that may happen, each with a mitigation. Hard limits are in [0_business_constraint.md](0_business_constraint.md). In priority order within each section.

Close a challenge when its mitigation is done or the risk is gone. Add new ones as they appear.

## 1. Sales and trust

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X1 | **The demo is not proven.** No feature in scope.md is confirmed as **Works** yet. | The demo is the main sales tool. A failure in a live demo loses trust you cannot win back. Until features work, nothing can be claimed ([C6](0_business_constraint.md#2-offer)). | Fill in every status, then rehearse the demo 5 times. Keep a recorded backup video. | [scope.md](scope.md#tasks), [process_flow.md](process_flow.md#stage-1-live-demo-3045-min-online-or-onsite) |
| X2 | **No client portfolio.** | An unknown solo vendor asking an SME to move its accounting is a trust problem first. | Founding client program, public fixed prices, low-risk monthly start. Ask every early client for a testimonial and case study. | [marketing_strategy.md](marketing_strategy.md#2-the-real-problem-no-portfolio-yet), [process_flow.md](process_flow.md#stage-7-ongoing-support) |
| X3 | **The proposal claims more than the product may do.** It is read-only, so conflicts stay until it is revised. | Every client who reads a false claim is a trust problem later. | See the table below. Do not show unconfirmed features in demos. | [scope.md](scope.md#open-decisions) |

Proposal conflicts (X3):

| Proposal says | Conflicts with | Open decision in |
| :-- | :-- | :-- |
| "No per-user licence fees" | Retail is priced per user | [marketing_strategy.md](marketing_strategy.md#open-decisions) |
| "Other modules … can be switched on as you grow" | [C5](0_business_constraint.md#2-offer) | [scope.md](scope.md#open-decisions) |
| Learn, Take action, autocomplete, "only my branch" | [C6](0_business_constraint.md#2-offer) (status unknown) | [scope.md](scope.md#open-decisions) |
| "Estimation" as the last step of "Let's Talk" | [C8](0_business_constraint.md#3-commercial-rules) (one fixed price) | [process_flow.md](process_flow.md#open-decisions) |

## 2. Founder capacity

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X4 | **Building instead of selling.** An engineer-founder's natural pull is to keep building. | The product will not fail for lack of features; it will fail for lack of demos. | Build rule: demo features only, then start demos. Weekly Friday review of the lead sheet. | [scope.md](scope.md#build-rule), [marketing_strategy.md](marketing_strategy.md#tasks) |
| X5 | **AI projects take over the week.** | They pay sooner, but turn Navario into a services shop and stall the product. | Cap at ~50% of each week. Make every AI project reuse the Navario assistant. | [marketing_strategy.md](marketing_strategy.md#tasks), [scope.md](scope.md#4-long-term-do-not-sell-yet) (4.1) |
| X6 | **Key-person risk.** One person runs production for paying clients. | Sickness or travel means no support and no fixes. | A freelance backup developer with server access and a runbook before the first go-live. | [process_flow.md](process_flow.md#tasks) |
| X7 | **Support load grows faster than revenue.** | Support time comes out of selling and building. | Video library, the assistant's Learn capability, partners on first line. Hire when the trigger is met. | [process_flow.md](process_flow.md#support-coverage) |

## 3. Margin

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X8 | **Retail AI cost is unmeasured.** Every cost figure is an estimate. | The retail price and the top-ups may be below cost. | Log 50 real questions with tokens, choose the model stack, then fix prices. | [pricing_model.md](pricing_model.md#tasks), [ai_cost_simulation.md](ai_cost_simulation.md#next-steps) |
| X9 | **AI prices rise.** The latest Gemini Flash models double in price on 1 Jan 2027. | Contracts signed now run in 2027. | Price retail on 2027 rates. Enterprise and AI projects use BYOK. | [ai_cost_simulation.md](ai_cost_simulation.md#gemini-prices-used), [pricing_model.md](pricing_model.md#principles) |
| X10 | **Retail AI usage has no ceiling** until the product enforces limits. | One heavy client can erase the margin. | Company pool, per-user daily cap, 80% warning, hard limit, before the first retail client. | [scope.md](scope.md#2-first-paid-client) (2.1), [ai_cost_simulation.md](ai_cost_simulation.md#recommendations) |

## 4. Competition

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X11 | **Odoo's licence is cheaper per user, and Odoo Custom includes agentic AI.** | Prospects who compare licence prices pick Odoo. AI alone is not unique. | Compete on first-year total cost and "done for you". Edge: Bahasa Indonesia first, access rules built in, simpler screens, a local person who answers. | [pricing_model.md](pricing_model.md#4-benchmark-odoo) |
| X12 | **Local products (Accurate Online, Jurnal) are what many SMEs already know.** | Comparison is not done yet. | Include them in the retail price decision. | [pricing_model.md](pricing_model.md#open-decisions) |

## 5. Partners

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X13 | **Partners learn the system and leave.** It already happened in Sep 2026. | Lost time and know-how given to a possible competitor. | Sign before you teach ([C9](0_business_constraint.md#3-commercial-rules)). Confidentiality and non-solicitation clauses. | [partnership_model.md](partnership_model.md#rules) |
| X14 | **Retail commission is too small to motivate partners.** No partner has committed yet. | Partners are the main reach a solo founder has. | Focus partners on enterprise, where they keep 100% of their consultancy fees. | [partnership_model.md](partnership_model.md#why-partners) |
