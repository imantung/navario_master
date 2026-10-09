# Partnership Model

Internal. This is the basis for the partner agreement, which will be written in Bahasa Indonesia when the first partner commits ([2_legal.md](2_legal.md#2-documents-needed)). No partner has committed yet. Prices are in [5_saas_pricing_model.md](5_saas_pricing_model.md) and [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md); this doc only sets the split.

## Why partners

- **Retail (SaaS):** Commission on a low list price is small, so retail referrals are a bonus for partners, not a business ([X14](1_challenges.md#5-partners)).
- **Enterprise:** This is where partners earn. **Navario builds and runs the platform (ERP, AI assistant, hosting, technical customization) for a fixed monthly share. The partner owns the client relationship, keeps the rest of the subscription, and charges the client for consultancy.**
- For Navario, partners provide what a solo founder lacks ([C1, C2](0_business_constraint.md#1-founder-and-capacity)): sales reach, business process know-how, and capacity for training and first-line support.

## Partner types

| | **Referral Partner** | **Implementation Partner** |
| :-- | :-- | :-- |
| **Deals** | SaaS and enterprise | Enterprise (SaaS allowed) |
| **Typical profile** | Accountants, tax consultants (*konsultan pajak*), bookkeepers, business consultants, IT freelancers | IT/ERP consulting firms, KAP/KKP firms with a consulting arm, system integrators, ERPNext implementers |
| **Partner does** | Introduces the client | Sells, runs discovery, designs processes, configures, trains, first-line support |
| **Navario does** | Demo, quote, setup, training, support | Platform, hosting, AI assistant, upgrades, custom code, second-line support, demo support for the first deals |
| **Partner earns** | SaaS commission (section 1) | Enterprise partner share (section 2) + **100% of their own consultancy fees** |

## 1. SaaS commission

Based on the retail subscription in [5_saas_pricing_model.md](5_saas_pricing_model.md#1-subscription). Decide before signing the first partner. Options so far:

| Option | Subscription commission | Setup fee share |
| :-- | :-- | :-- |
| A. Simple | 15% of subscription, as long as the client pays | None |
| B. Old Tier 1 (Referral) | 10% of subscription, lifetime | IDR 500,000 flat bonus |
| C. Old Tier 2 (Co-selling) | 15% in year 1, 10% from year 2 | 20% of Standard setup; IDR 500,000 flat for Fast-Track |

Whatever is chosen:
- **Not included in the base:** AI question top-ups, other add-ons, customization, trial extensions and PPN.
- Paid within 7 days after the client's payment clears.

## 2. Enterprise partner share

Based on the enterprise subscription in [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#1-enterprise-subscription). **Navario's share** is fixed per client per month, for the dedicated server and maintenance. It does not change with users or AI usage, only when the client moves to a larger server tier. AI usage is billed by Google to the client (BYOK) and is outside every split.

The model depends on **which company signs the agreement with the client**:

| | **A. Client contracts with the partner** | **B. Client contracts with Navario** |
| :-- | :-- | :-- |
| **Client price** | Set by the partner | Navario's list price |
| **Who bills the client** | Partner (subscription, setup, consultancy, everything) | Navario bills the subscription and technical customization. Partner bills its own consultancy. |
| **Navario earns** | Navario's share, billed to the partner | The client price |
| **Partner earns** | Client price − Navario's share, plus its own fees | Client price − Navario's share (paid by Navario), plus its own consultancy fees |
| **Setup and customization** | Navario bills its technical work to the partner at Navario's price. The partner prices it to the client. | Navario bills its technical work to the client at a fixed quote. |
| **Cash first** ([C8](0_business_constraint.md#3-commercial-rules)) | Partner pays Navario's share monthly in advance, whether or not the client has paid the partner | Navario pays the partner share within 7 days after the client's payment clears |
| **If the partner leaves** | Navario has no obligation to the client. The partner's contract with the client is the partner's responsibility. Only exception: client data (rule 5). | Navario keeps serving the client and keeps the full client price. |

- **Referral Partner on an enterprise deal:** always model B. Navario does the implementation, so the referral partner gets the SaaS commission rate on the client price, not the partner share.
- **Direct deals with no partner:** Navario keeps the full client price.

### Principal or subcon (model A)

In model A, Navario can act as either, deal by deal:

| | **Principal** | **Subcon** |
| :-- | :-- | :-- |
| **Meaning** | Navario is the product owner; the partner resells the product | Navario does work inside the partner's project |
| **Use when** | The partner sells the product as a product, to several clients | A system integrator or consultancy has one project and wants one vendor for its client |
| **Navario earns** | Navario's share every month | Navario's share every month, plus fixed quotes for technical work |

Same in both:
- **No Navario brand in the ERP.** The client sees the partner's or the client's own brand. Navario stays behind the scenes unless the partner chooses to mention it.
- **No source code** for Platform Core or Nava AI, to the partner or the client. Only the client's own customization (Company_Custom) is handed over, to the client ([L6](2_legal.md#3-code-ownership-ip)).
- **Navario hosts.** No on-premise install, because handing over the code may make it open source under GPL v3 ([L6](2_legal.md#1-rules)).

### Support split (enterprise)

| Level | Who | Examples |
| :-- | :-- | :-- |
| First line | Partner | "How do I…?", configuration changes, user training, process questions |
| Second line | Navario | Bugs, server, backups, upgrades, AI assistant behavior, custom code |

## 3. Pilots

Pilots referred by a partner ([5_saas_pricing_model.md](5_saas_pricing_model.md#5-pilot), [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#5-pilot)) follow the same split. If the pilot discounts stay on setup only (open decisions in 5 and 6), the subscription split does not change.

## 4. What Navario gives partners

Step by step, from first contact to active partner: [10_partner_onboarding_process.md](10_partner_onboarding_process.md).

- The proposal (English, plus Bahasa Indonesia when ready) and a one-page partner summary
- A demo instance with the trading company dataset and the demo script from [9_saas_process_flow.md](9_saas_process_flow.md)
- A product training session (Implementation Partners: enough to configure and train clients), **only after the partner agreement is signed**
- The retail price list, and for Implementation Partners, the enterprise split

## Rules

0. **Sign before you teach** ([C9](0_business_constraint.md#3-commercial-rules)). Before signing, a prospective partner gets only the proposal, a live demo run by Navario, and the partner summary. No system access, no architecture or AI walkthroughs, no hands-on ERPNext training. Training starts after the agreement (with confidentiality and non-solicitation clauses) is signed. Lesson from Sep 2026: a prospective partner with ERP implementation experience learned ERPNext and the AI approach from the founder, then left without an agreement. *Note: The enforceability of confidentiality and non-solicitation clauses must be validated with a certified Indonesian tax consultant or notary.*
1. **Lead registration.** Partners register a lead (company name and contact) by WhatsApp or the web form. Attribution is locked for **60 days** and extended while a deal is active. The first registration wins.
2. **Cash first.** Commissions and partner shares are paid only after the client's money clears.
3. **Technical ownership.** Navario owns Platform Core and Nava AI, and never shares their source code ([2_legal.md](2_legal.md#3-code-ownership-ip)). Partners don't modify core code; custom code goes through Navario. The client owns its Company_Custom code and gets it on request.
4. **No competition on services.** Navario doesn't offer bookkeeping, tax filing, audit or business consultancy that competes with partners, and doesn't take over a partner's client for consulting.
5. **Client data.** The client owns its data. Partners get system access only with the client's approval, under the client's data protection terms (UU PDP). Model A: if the partner stops paying Navario's share, the client gets 30 days' notice and a full data export before the server is shut down. This is written into the partner agreement. *Note: This must be validated with a certified Indonesian tax consultant or notary.*
6. **Commission and partner share end** when the client stops paying, or when the partner is terminated for breach. Model B: if an Implementation Partner leaves, Navario keeps serving the client and takes over first-line support. Model A: see section 2.

## Later: reciprocal referrals

Once Navario has direct clients (around 10 or more), refer clients who need bookkeeping, tax filing or audit to partner firms in exchange for referrals back. This isn't worth offering yet; there is nothing to swap.

## Tasks

- [ ] **Partner summary.** Done when: a one-page partner summary exists, with the enterprise split and BYOK explained.
- [ ] **Partner outreach.** Depends on: partner summary. Done when: 15 accountants, tax consultants or IT consultants in Jabodetabek have been contacted. Follow rule 0: sign before you teach.

Partner agreement draft: see [2_legal.md](2_legal.md#tasks).

## Assumptions

- Accountants refer clients even with a small commission.
- Implementation Partners accept a fixed Navario share and no source code.

## Open decisions

Decide before signing the first partner.

- [ ] **Which Implementation Partners to target first.** An ERPNext implementer can run plain ERPNext without paying Navario, and is the X13 risk. Recommendation: target accountants and IT consultancies with no ERP of their own first.
- [ ] **Model A undercutting retail.** In model A the partner sets the price, and could sell below retail to small clients. Recommendation: model A only for clients above the retail user range.

- [ ] **SaaS commission option** (A, B or C above), lifetime or capped (for example 24 months). Recommendation: option A. It is simple, and AI top-ups stay outside the base.
- [ ] **Commission on AI projects** a partner refers. Recommendation: a one-time share of the development fee only.
- [ ] **Reference rights in white-label deals.** With no Navario brand, these clients add nothing to the portfolio. Recommendation: the partner agreement lets Navario cite the client anonymously ("a distributor in Surabaya, 40 users"), and by name only with the client's written consent.
- [ ] **Minimum commitment** for Implementation Partners (for example 1 deal per 6 months) to keep the "partner" status.
