# Challenges

Internal. Obstacles to overcome and risks that may happen, each with a mitigation. Hard limits are in [0_business_constraint.md](0_business_constraint.md). In priority order within each section.

Close a challenge when its mitigation is done or the risk is gone. Add new ones as they appear.

## 1. Sales and trust

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X1 | **The demo is not proven.** The demo is being built (9 Oct 2026); no feature in scope.md is confirmed as **Works** yet. | The demo is the main sales tool. A failure in a live demo loses trust you cannot win back. Until features work, nothing can be claimed ([C6](0_business_constraint.md#2-offer)). | Fill in every status, then rehearse the demo 5 times. Keep a recorded backup video. | [4_product_scope.md](4_product_scope.md#tasks), [9_saas_process_flow.md](9_saas_process_flow.md#stage-1-live-demo-3045-min-online-or-onsite) |
| X2 | **No client portfolio.** | An unknown solo vendor asking an SME to move its accounting is a trust problem first. | Paid pilots ([SaaS](5_saas_pricing_model.md#5-pilot), [enterprise](6_enterprise_pricing_model.md#5-pilot)), public fixed prices, low-risk monthly start. Ask every early client for a testimonial and case study. | [7_go_to_market.md](7_go_to_market.md#3-the-trust-problem-no-portfolio-yet), [9_saas_process_flow.md](9_saas_process_flow.md#stage-7-ongoing-support) |
| X3 | **The proposal claims more than the product may do.** It is read-only, so conflicts stay until it is revised. | Every client who reads a false claim is a trust problem later. | See the table below. Do not show unconfirmed features in demos. | [4_product_scope.md](4_product_scope.md#open-decisions) |

Proposal conflicts (X3):

| Proposal says | Conflicts with | Open decision in |
| :-- | :-- | :-- |
| "No per-user licence fees" | Retail is priced per user | [7_go_to_market.md](7_go_to_market.md#open-decisions) |
| "Other modules … can be switched on as you grow" | [C5](0_business_constraint.md#2-offer) | [4_product_scope.md](4_product_scope.md#open-decisions) |
| Learn, Take action, autocomplete, "only my branch" | [C6](0_business_constraint.md#2-offer) (status unknown) | [4_product_scope.md](4_product_scope.md#open-decisions) |
| "Estimation" as the last step of "Let's Talk" | [C8](0_business_constraint.md#3-commercial-rules) (one fixed price) | [9_saas_process_flow.md](9_saas_process_flow.md#open-decisions) |

## 2. Founder capacity

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X4 | **Building instead of selling.** An engineer-founder's natural pull is to keep building. | The product will not fail for lack of features; it will fail for lack of demos. | Build rule: demo features only, then start demos. Weekly Friday review of the lead sheet. | [4_product_scope.md](4_product_scope.md#build-rule), [7_go_to_market.md](7_go_to_market.md#tasks) |
| X5 | **AI projects take over the week.** | They pay sooner, but turn Navario into a services shop and stall the product. | Cap at ~50% of each week. Quote only project types in the scope catalogue. | [7_go_to_market.md](7_go_to_market.md#tasks), [12_ai_project.md](12_ai_project.md#1-scope-catalogue) |
| X6 | **Key-person risk.** One person runs production for paying clients. | Sickness or travel means no support and no fixes. | A freelance backup developer with server access before the first go-live. | [9_saas_process_flow.md](9_saas_process_flow.md#tasks) |
| X7 | **Support load grows faster than revenue.** | Support time comes out of selling and building. | Video library, the assistant's Learn capability, partners on first line. Hire when the trigger is met. | [9_saas_process_flow.md](9_saas_process_flow.md#support-coverage) |

## 3. Margin

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X8 | **Retail AI cost is unmeasured.** Every cost figure is an estimate. | The retail price and the top-ups may be below cost. | Log 50 real questions with tokens, choose the model stack, then fix prices. | [5_saas_pricing_model.md](5_saas_pricing_model.md#tasks), [ai_cost_simulation.md](ai_cost_simulation.md#next-steps) |
| X9 | **AI prices rise.** The latest Gemini Flash models double in price on 1 Jan 2027. | Contracts signed now run in 2027. | Price retail on 2027 rates. Enterprise and AI projects use BYOK. | [ai_cost_simulation.md](ai_cost_simulation.md#gemini-prices-used), [5_saas_pricing_model.md](5_saas_pricing_model.md#principles), [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#principles) |
| X10 | **Retail AI usage has no ceiling** until the product enforces limits. | One heavy client can erase the margin. | Company pool, per-user daily cap, 80% warning, hard limit, before the first retail client. | [4_product_scope.md](4_product_scope.md#2-first-paid-client) (2.1), [ai_cost_simulation.md](ai_cost_simulation.md#recommendations) |

## 4. Competition

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X11 | **Odoo's licence is cheaper per user, and Odoo Custom includes agentic AI.** | Prospects who compare licence prices pick Odoo. AI alone is not unique. | Compete on first-year total cost and "done for you". Edge: Bahasa Indonesia first, access rules built in, simpler screens, a local person who answers. | [5_saas_pricing_model.md](5_saas_pricing_model.md#4-benchmark-odoo) |
| X12 | **Local products (Accurate Online, Jurnal) are what many SMEs already know.** | Comparison is not done yet. | Include them in the retail price decision. | [5_saas_pricing_model.md](5_saas_pricing_model.md#open-decisions) |

## 5. Partners

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X13 | **Partners learn the system and leave.** It already happened in Sep 2026. | Lost time and know-how given to a possible competitor. | Sign before you teach ([C9](0_business_constraint.md#3-commercial-rules)). Confidentiality and non-solicitation clauses. | [8_partnership_model.md](8_partnership_model.md#rules) |
| X14 | **Retail commission is too small to motivate partners.** No partner has committed yet. | Partners are the main reach a solo founder has. | Focus partners on enterprise, where they keep 100% of their consultancy fees. | [8_partnership_model.md](8_partnership_model.md#why-partners) |

## 6. Product and technology

| # | Challenge | Why it matters | Mitigation | Handled in |
| :-- | :-- | :-- | :-- | :-- |
| X15 | **The assistant gives a wrong number.** | A wrong figure on accounting data, in a demo or to a client, loses trust fast. | Answers come from business tools only, and each links to its source document. A fixed set of 50 test questions runs before every release. | [4_product_scope.md](4_product_scope.md#tasks), [2_legal.md](2_legal.md#open-decisions) (liability) |
| X16 | **One AI provider and one host** (Gemini, DigitalOcean). This is the fastest route now; a move to cheaper providers of the same quality is planned. | Price rises, outages or model retirement hit every client at once. A later move is hard if code depends on one vendor. | Keep all model calls behind one internal interface. Check Gemini prices monthly. Agreements allow a provider change with notice. | [techstack.md](techstack.md#2-nava-ai), [2_legal.md](2_legal.md#open-decisions) |
| X17 | **ERPNext upgrades break Platform Core or Nava AI.** | Every client runs on the same code, so one broken upgrade hits all of them. | Never modify ERPNext. Test each upgrade on the demo instance first. | [techstack.md](techstack.md#4-design-rules) |
