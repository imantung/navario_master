# Legal

Internal. Legal entity, tax registration, contracts, data protection, trademark and code ownership (IP). Other docs link here and do not repeat these rules.

## 1. Rules

| # | Rule | What it forces | Applied in |
| :-- | :-- | :-- | :-- |
| L1 | **No legal entity yet.** The name *PT Upaya Teknologi Sejahtera* is reserved, not registered. | No quotation or agreement until the entity is registered. Until then, no document uses the company name as if it exists. | [9_saas_process_flow.md](9_saas_process_flow.md#stage-3-fixed-price-quote--contract), [website/requirement.md](website/requirement.md) |
| L2 | **Agreements with Indonesian parties must be in Bahasa Indonesia** (Law No. 24/2009, Art. 31). | Quotations, service and partner agreements, Terms and Privacy Policy in Bahasa Indonesia (bilingual is fine). | Section 2 below |
| L3 | **Client data protection (UU PDP No. 27/2022).** The client owns its data. | Partners get system access only with the client's approval. Client data inside the product, including AI processing, is covered by the service agreement. | [8_partnership_model.md](8_partnership_model.md#rules) (rule 5) |
| L4 | **"ERPNext" is a Frappe trademark.** | Don't use it in brand-like phrases. Name it only when asked. | [3_brand_identity.md](3_brand_identity.md#3-words) |
| L5 | **Partners never get technical details** ([C9](0_business_constraint.md#3-commercial-rules)). | Functional training can start before signing. Partner agreement includes confidentiality and non-solicitation clauses. Their enforceability must be checked. | [8_partnership_model.md](8_partnership_model.md#rules) (rule 0) |
| L6 | **Closed source only while Navario hosts it.** ERPNext is GPL v3. Platform Core and Nava AI run on top of it. | Platform Core and Nava AI are never handed over as code: no on-premise install, no copy to partners or clients. Hosting as a service keeps them closed; handing over the code may oblige Navario to release it under GPL v3. | Section 3 below, [8_partnership_model.md](8_partnership_model.md#rules) (rule 3) |
| L7 | **Client data is hosted outside Indonesia** (DigitalOcean, Singapore), and AI processing is done by Google. UU PDP has rules on transferring personal data abroad. | State the server location and the AI processing in the service agreement and the Privacy Policy, and get the client's agreement. Sales material does not name the providers; answer if a client asks ([3_brand_identity.md](3_brand_identity.md#hard-questions)). If an enterprise client requires data in Indonesia, quote a different hosting setup. | [techstack.md](techstack.md#3-hosting) |

## 2. Documents needed

All in Bahasa Indonesia (L2), checked by a notary or lawyer before first use.

| Document | Used in | Status |
| :-- | :-- | :-- |
| Quotation template | [9_saas_process_flow.md](9_saas_process_flow.md#stage-3-fixed-price-quote--contract), stage 3 | Not drafted |
| Service agreement (including client data and AI processing) | [9_saas_process_flow.md](9_saas_process_flow.md#stage-3-fixed-price-quote--contract), stage 3 | Not drafted |
| Partner agreement: model A (client contracts with the partner; Navario supplies the partner, as principal or subcon; no source code to the partner; client gets 30 days' notice and a data export if the partner stops paying) and model B (client contracts with Navario; Navario pays the partner share) | [8_partnership_model.md](8_partnership_model.md#2-enterprise-partner-share) | Not drafted |
| AI project agreement (scope, fixed price, payment schedule, code ownership, BYOK) | [12_ai_project.md](12_ai_project.md#2-process), stage 3 | Not drafted |
| Terms of Service and Privacy Policy (website) | [website/requirement.md](website/requirement.md) (P-10) | Boffon version exists; needs Navario update |

## 3. Code ownership (IP)

```
Frappe (open source, MIT)
└── ERPNext (open source, GPL v3)
    └── Platform Core (closed source)
        ├── Nava AI (closed source)
        └── Company_Custom (client proprietary)
```

| Layer | What it is | Owner | Licence | Who gets the source |
| :-- | :-- | :-- | :-- | :-- |
| Frappe | Web framework | Frappe Technologies | MIT | Public |
| ERPNext | ERP | Frappe Technologies | GPL v3 | Public |
| Platform Core | UI/UX improvements, Indonesian localization, etc. | PT Upaya Teknologi Sejahtera | Closed source | Nobody outside Navario |
| Nava AI | The AI Business Assistant | PT Upaya Teknologi Sejahtera | Closed source | Nobody outside Navario |
| Company_Custom | One client's customization | The client | Client proprietary | The client, on request |

Licences checked on GitHub: [Frappe](https://github.com/frappe/frappe/blob/develop/LICENSE) (MIT) and [ERPNext](https://github.com/frappe/erpnext/blob/develop/license.txt) (GPL v3, not AGPL) (checked 9 Oct 2026). GPL v3 is triggered by handing over copies, not by running the software as a hosted service.

**If a client leaves**, they keep their data, ERPNext and their Company_Custom code, so there is no vendor lock-in. They lose Platform Core and Nava AI. Details and the design rules that keep this true: [techstack.md](techstack.md#5-if-a-client-leaves).

## Tasks

- [ ] **Legal entity.** Done when: *PT Upaya Teknologi Sejahtera* is registered and has a business bank account.
- [ ] **IP assignment.** Depends on: legal entity. Done when: a signed deed transfers Platform Core and Nava AI, written by the founder before registration, to *PT Upaya Teknologi Sejahtera*.
- [ ] **Cross-border data check.** Done when: a lawyer has confirmed what UU PDP requires for client data hosted in Singapore and AI processing by Google (L7), and the service agreement and Privacy Policy include it.
- [ ] **GPL check.** Done when: a lawyer has confirmed that Platform Core and Nava AI can stay closed source while hosted by Navario (L6), and what changes if a client asks for on-premise.
- [ ] **Sales documents.** Depends on: legal entity and final retail pricing. Done when: the quotation template, service agreement, and Terms/Privacy exist in Bahasa Indonesia and have been checked by a notary or lawyer.
- [ ] **Partner agreement draft.** Depends on: the commission decision in [8_partnership_model.md](8_partnership_model.md#open-decisions). Done when: a Bahasa Indonesia draft with confidentiality and non-solicitation clauses exists, checked by a notary or lawyer.

## Assumptions

- A PT Perorangan fits a solo founder at this size **[unverified]**.
- Running Platform Core and Nava AI as a hosted service does not trigger GPL v3 (lawyer check is a task above).

## Open decisions

- [ ] **Whether and when to register the legal entity.** The founder is still unsure and wants to discuss it further (9 Oct 2026). It blocks every quotation, pilot and partner agreement (L1). Recommendation: set a target date before the first demo to a warm contact, so a "yes" can turn into a quote right away.
- [ ] **Legal entity type.** Register *PT Upaya Teknologi Sejahtera* as a *PT Perorangan* or a regular PT (a new entity, not PT Inovasi Teknologi Terintegrasi)? Recommendation: PT Perorangan first, before the first quotation; convert to a regular PT when an investor or co-founder joins.
- [ ] **PKP (PPN registration).** Mandatory only above IDR 4.8 billion turnover per year **[unverified]**. The founder leans towards non-PKP (9 Oct 2026). Recommendation: stay non-PKP at first. Revisit when an enterprise client needs a *faktur pajak*. Decides whether prices in [5_saas_pricing_model.md](5_saas_pricing_model.md#principles) and [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md#principles) include PPN.
- [ ] **Code ownership in AI projects.** Company_Custom covers ERP clients only. Recommendation: the client owns project-specific code. Nava AI and reusable parts stay with Navario and are used only while Navario hosts them.
- [ ] **Liability for AI answers** ([X15](1_challenges.md#6-product-and-technology)). Recommendation: the service agreement limits liability to the fees paid in the last 12 months, and says AI answers must be checked against the linked documents.
- [ ] **Provider changes** ([X16](1_challenges.md#6-product-and-technology)). Hosting and AI providers may change later. Recommendation: the agreement and Privacy Policy describe providers by role (cloud host, AI service) with their current names in an annex, and allow a change with 30 days' notice.

*Note: This must be validated with a certified Indonesian tax consultant or notary.*
