# Enterprise Process Flow

Internal. An enterprise client from first contact to ongoing support. Retail is in [9_saas_process_flow.md](9_saas_process_flow.md); stages that work the same way link there. Prices are in [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md). Partner models A and B are in [8_partnership_model.md](8_partnership_model.md#2-enterprise-partner-share). Pilot clients follow the same stages with the terms in [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#5-pilot).

```
1 Live demo → 2 Discovery → 3 Quote & contract → 4 Server & AI key → 5 Setup & migration → 6 Training & UAT → 7 Go-live → 8 Support
```

## Who does what

| Stage | Direct (no partner) | Model A (client contracts with partner) | Model B (client contracts with Navario) | Exit document |
| :-- | :-- | :-- | :-- | :-- |
| 1. Live demo | Navario | Partner, Navario joins the first deals | Partner, Navario joins the first deals | Lead registered |
| 2. Discovery | Navario | Partner leads, Navario covers technical scope | Partner leads, Navario covers technical scope | Discovery checklist filled in |
| 3. Quote & contract | Navario | Partner quotes the client; Navario quotes the partner | Navario quotes the client; partner quotes its consultancy | Signed agreement, payment cleared |
| 4. Server & AI key | Navario | Navario | Navario | Server live, client's AI key connected |
| 5. Setup & migration | Navario | Partner configures, Navario does technical work | Partner configures, Navario does technical work | Master data sign-off |
| 6. Training & UAT | Navario | Partner | Partner | UAT acceptance |
| 7. Go-live | Navario | Partner, Navario reviews | Partner, Navario reviews | Go-live sign-off |
| 8. Support | Navario | Partner first line, Navario second | Partner first line, Navario second | — |

Direct deals are allowed in any industry. Navario looks for a partner to help, mainly with functional work outside trading ([8_partnership_model.md](8_partnership_model.md#2-enterprise-partner-share)).

Stage durations: unknown. Measure them on the first enterprise pilot.

## Stage 1: Live Demo

Same script as retail ([9_saas_process_flow.md](9_saas_process_flow.md#stage-1-live-demo-3045-min-online-or-onsite)). Also show multiple branches or companies, if they are **Works** in [4_product_scope.md](4_product_scope.md).

* **Qualify:** above the retail user range, multiple branches or companies, a budget, a decision maker in the demo ([6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#who-qualifies)).

## Stage 2: Discovery

* **You give:** The retail discovery checklist ([9](9_saas_process_flow.md#stage-2-needs-discussion-included-in-setup)), plus:
  * Companies, branches and warehouses, and the transactions between them
  * Integrations with other systems
  * Custom workflows and approval rules
  * Number of users per department, expected AI usage (for the AI cost estimate)
  * Data location requirements ([L7](2_legal.md#1-rules))
  * Whether the client has a Google Cloud billing account
* **You receive:** Answers, sample documents and a user list.
* **Decide:** model A or B, principal or subcon ([8](8_partnership_model.md#principal-or-subcon-model-a)), and server size.

## Stage 3: Quote & Contract

* **You give:** A quotation in Bahasa Indonesia with one fixed total for setup and the monthly fee, a monthly AI cost estimate from [ai_cost_simulation.md](ai_cost_simulation.md), and the service agreement (or the partner agreement, in model A).
* **You receive:** The signed agreement and payment.
* **Rule:** Same as retail: no quotation before the legal entity exists, work starts after payment clears ([L1](2_legal.md#1-rules), [C8](0_business_constraint.md#3-commercial-rules)).

## Stage 4: Server & AI Key

* **You give:** A dedicated server, and a guide for the client to create a Gemini API key (the one model for now) on its own paid Google Cloud billing account.
* **You receive:** The client's AI key, connected to its instance ([4_product_scope.md](4_product_scope.md#2-first-paid-client), 2.2).

## Stages 5–7: Setup, Training, Go-Live

Same as retail stages 4–6 ([9](9_saas_process_flow.md#stage-4-setup--data-import)), with the partner doing configuration and training where there is one. Navario reviews the partner's setup before go-live.

## Stage 8: Support

* Support split: [8_partnership_model.md](8_partnership_model.md#support-split-enterprise). Response time: [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#1-enterprise-subscription).
* **Every month:** check server load. Move the client to a larger server tier when needed.
* **One month after go-live:** ask for a testimonial, logo permission and a case study. In white-label deals, see the reference rights decision in [8](8_partnership_model.md#open-decisions).

## Assumptions

- The client can create and pay for its own Gemini key.
- A partner can run discovery, training and first-line support after the training in [10_partner_onboarding_process.md](10_partner_onboarding_process.md#stage-5-onboarding).

## Tasks

- [ ] **Enterprise discovery checklist.** Done when: the stage 2 additions exist as a one-page Bahasa Indonesia form.
- [ ] **AI key guide.** Depends on: BYOK is **Works**. Done when: a one-page Bahasa Indonesia guide walks a client through creating a paid Gemini API key.

## Open decisions

- [ ] **Client asks for data in Indonesia.** Recommendation: quote a different hosting setup at a fixed price, as [L7](2_legal.md#1-rules) says. Don't promise it before a client asks.
