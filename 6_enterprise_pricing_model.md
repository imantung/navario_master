# Enterprise Pricing Model

Internal. Two offers where the client brings its own AI key (BYOK): **Enterprise** (flat fee, unlimited users, sold through partners, see [10_partnership_model.md](10_partnership_model.md)) and **AI projects** (custom AI work, any industry). Retail is in [5_saas_pricing_model.md](5_saas_pricing_model.md).

## Principles

- **Fixed price** ([C8](0_business_constraint.md#3-commercial-rules)). Every quote is a fixed total agreed before work starts. No hourly billing. The client only ever sees one number.
- **No ERP-only deals** ([C3](0_business_constraint.md#2-offer)). Every enterprise package includes the AI Business Assistant.
- **Flat fee, unlimited users.** Limited by server capacity only. Seats and AI usage never trigger a price change.
- **BYOK (bring your own key).** The client connects its own Gemini API key ([C7](0_business_constraint.md#2-offer)) and pays Google directly for AI usage. Navario charges only for the platform, development and server maintenance. So AI price changes (e.g., the Jan 2027 Gemini increase) do not hit Navario's margin.
- **PPN:** Depends on whether the new entity is PKP (see [2_legal.md](2_legal.md#open-decisions)). If it is, prices exclude PPN.

## 1. Enterprise subscription

| | |
| :-- | :-- |
| **Subscription (client price)** | Flat monthly fee, for example **IDR 12,500,000 / month**. List price for clients who contract with Navario. |
| **Navario's share** | **IDR 7,500,000 / month**, fixed, for the dedicated server and maintenance (hosting, backups, upgrades, second-line support). If the client contracts with the partner, the partner pays this share and sets its own client price. If the client contracts with Navario, the rest of the client price is the partner's share. See [10_partnership_model.md](10_partnership_model.md#2-enterprise-partner-share). Direct deals with no partner: Navario keeps the full client price. |
| **Users** | Unlimited |
| **Server** | Dedicated server, spec *TBD (vCPU / RAM / storage)* |
| **AI Business Assistant** | Included, **BYOK**: the client's own Gemini API key, billed by Google to the client. No AI question limit from Navario. Give the client an estimated AI cost per month from [ai_cost_simulation.md](ai_cost_simulation.md) so they can budget. |
| **Hosting** | Daily backups kept 30 days |
| **Support** | Priority, first response within 6 hours. Partner handles first line, Navario second line. |

When a client outgrows the server, move them to a larger server tier. The server cost comes out of Navario's share, so the server spec sets Navario's margin.

## 2. Enterprise setup

| | |
| :-- | :-- |
| **Navario's technical part** | From IDR 25,000,000 (multi-company, custom workflows, integrations) |
| **Partner consultancy** | Billed separately by the partner, at the partner's own rate |
| **Data migration and customization** | Same price list as retail: [5_saas_pricing_model.md](5_saas_pricing_model.md#3-add-ons) |

## 3. Benchmark: Odoo

At 30+ users, Odoo Custom costs over Rp 7.6M per month in licences alone, before hosting and partner fees (Odoo prices in [5_saas_pricing_model.md](5_saas_pricing_model.md#4-benchmark-odoo)). A flat IDR 12.5M with unlimited users wins as headcount grows.

## 4. AI projects

Custom AI work for any industry, built on the Navario assistant ([C4](0_business_constraint.md#2-offer)).

| | |
| :-- | :-- |
| **Development** | Fixed price per project, quoted after a scoping call. *Price guide TBD.* |
| **Server maintenance** | Monthly fee if Navario hosts and runs it. *Price TBD.* |
| **AI usage** | BYOK: the client's own API key, billed by the provider to the client. Navario does not resell AI usage. |

## Tasks

- [ ] **Enterprise BYOK package.** Done when: the server spec is set and the per-company AI key setting works in a demo.
- [ ] **AI project pricing.** Done when: section 4 has a development price guide and a monthly server maintenance fee.

## Open decisions

- [ ] **Enterprise server spec** (vCPU / RAM / storage) for the enterprise fee. Recommendation: set it from the load of a 30-user demo.
- [ ] **AI project price guide** for development and monthly server maintenance. Recommendation: fixed price per project after a scoping call. Charge for scoping only if it includes a written design.
- [ ] **BYOK providers, and does the product support a per-company key today?** Recommendation: Gemini only for now; the cost model and product are built on it. Do not quote BYOK until the key setting works in a demo.
