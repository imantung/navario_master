# AI Projects

Internal. The second offer: custom AI work for any industry, on any system, inside or outside Frappe/ERPNext ([C4](0_business_constraint.md#2-offer)). Prices are in [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#4-ai-projects). Wording for the startup network is in [3_brand_identity.md](3_brand_identity.md#ai-projects-startup-network-linkedin).

## Principles

- **Every project includes AI** ([C3](0_business_constraint.md#2-offer)). No plain software work without an AI part.
- **Fixed price** ([C8](0_business_constraint.md#3-commercial-rules)). One fixed total after scoping. Anything extra is a change request with its own fixed quote.
- **BYOK.** The client pays the AI provider directly. Navario does not resell AI usage.
- **Capped time.** At most ~50% of each week ([C1](0_business_constraint.md#1-founder-and-capacity), [X5](1_challenges.md#2-founder-capacity)).

## 1. Scope catalogue

The project types Navario offers. Only types listed here are quoted.

| Type | What it is | Status |
| :-- | :-- | :-- |
| **MCP server** | Connects a client's system to AI assistants through the Model Context Protocol, so an assistant can read and act on that system | To define |
| **Automation** | AI steps inside a business workflow, e.g. reading incoming documents and creating records | To define |
| *More types* | To be added by the founder | — |

## 2. Process

Standard custom software delivery.

```
1 Scoping call → 2 Written scope & fixed quote → 3 Contract & payment → 4 Build → 5 UAT → 6 Handover → 7 Maintenance (optional)
```

| Stage | You give | You receive |
| :-- | :-- | :-- |
| 1. Scoping call | Questions on goal, systems, data, users | The problem, the systems involved, a decision maker |
| 2. Written scope & fixed quote | Scope (in and out), milestones, fixed total, AI provider and estimated AI cost | Approval |
| 3. Contract & payment | AI project agreement in Bahasa Indonesia ([L2](2_legal.md#1-rules)) | Signature, payment per the agreed schedule |
| 4. Build | Progress demo at each milestone | Access to the client's systems and an AI key (BYOK) |
| 5. UAT | A test checklist from the written scope | Signed UAT acceptance |
| 6. Handover | Deployment, documentation, the code the client owns (see open decisions) | Handover sign-off |
| 7. Maintenance | Hosting and fixes, if Navario runs it | Monthly fee |

## Assumptions

- The founder's 15+ years in software are enough proof for AI project buyers, without an AI project portfolio.
- The startup network is the first channel ([7_go_to_market.md](7_go_to_market.md#tasks)).

## Tasks

- [ ] **Scope catalogue.** Done when: each type in section 1 has a one-paragraph description, what is out of scope, and one example.
- [ ] **AI project offer.** See [7_go_to_market.md](7_go_to_market.md#tasks).
- [ ] **Pricing.** See [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#tasks).

## Open decisions

- [ ] **Final scope catalogue.** Recommendation: start with MCP server and automation only. Add a type after a real prospect asks for it twice.
- [ ] **Payment schedule.** C8 says work starts after payment clears. Recommendation: 50% at signing, 50% at UAT acceptance. Larger projects: per milestone.
- [ ] **AI provider.** The product is Gemini only ([C7](0_business_constraint.md#2-offer)), but AI projects run on the client's key. Recommendation: the client's choice of provider. Navario recommends one in the written scope.
- [ ] **Code ownership.** See [2_legal.md](2_legal.md#open-decisions).
- [ ] **Reusing Nava AI code.** May a project reuse parts of Nava AI? Recommendation: yes, but only while Navario hosts the project. Never hand the code over ([L6](2_legal.md#1-rules)).
