# Partner Onboarding Process

Internal. A partner from first contact to active partner. The model, split and rules are in [8_partnership_model.md](8_partnership_model.md). The key rule: **sign before you teach** ([C9](0_business_constraint.md#3-commercial-rules)).

```
1 Outreach → 2 Intro & demo → 3 Fit check → 4 Agreement → 5 Onboarding → 6 First deal → 7 Active partner
             └──────── no system access, no training ────────┘
```

| Stage | Referral Partner | Implementation Partner | Exit document |
| :-- | :-- | :-- | :-- |
| 1. Outreach | ✓ | ✓ | Contact logged in the lead sheet |
| 2. Intro & demo | ✓ | ✓ | — |
| 3. Fit check | Short | Full | Fit check filled in |
| 4. Agreement | ✓ | ✓ (model A or B, principal or subcon) | Signed partner agreement |
| 5. Onboarding | Short: price list, lead registration | Full: training, demo instance | Training done |
| 6. First deal | Navario runs it | Navario supports it | First client signed |
| 7. Active partner | ✓ | ✓ | Quarterly review |

## Stage 1: Outreach

* **Who:** Referral: accountants, tax consultants, bookkeepers, business consultants, IT freelancers. Implementation: IT/ERP consulting firms, KAP/KKP firms with a consulting arm, system integrators.
* **You give:** A short message using the partner pitch in [3_brand_identity.md](3_brand_identity.md#partners), and an invitation to a 30-min call.
* **You receive:** Interest and a meeting time.

## Stage 2: Intro & Demo (45–60 min)

* **You give:** The live demo run by Navario ([9_saas_process_flow.md](9_saas_process_flow.md#stage-1-live-demo-3045-min-online-or-onsite)), the proposal and the one-page partner summary.
* **You receive:** Their client base (industries, company sizes, how many trading companies), their services, and what they want: referral income or implementation work.
* **Do not give:** System access, architecture or AI walkthroughs, hands-on training, or the enterprise split details beyond the partner summary ([8_partnership_model.md](8_partnership_model.md#rules), rule 0).

## Stage 3: Fit Check

| Check | Referral | Implementation |
| :-- | :-- | :-- |
| Has trading companies among its clients or network | ✓ | ✓ |
| No competing ERP they push by default (or willing to offer Navario next to it) | ✓ | ✓ |
| Has staff who can configure, train and do first-line support | — | ✓ |
| Has a legal entity that can sign and invoice (needed for model A) | — | ✓ |
| Has a real prospect in mind | Nice to have | ✓ |

* **Decide with the partner:** partner type; for Implementation Partners, model A or B, and principal or subcon ([8_partnership_model.md](8_partnership_model.md#2-enterprise-partner-share)).
* **Stop here** if the fit is weak. Keep them as an informal referrer with no training.

## Stage 4: Agreement

* **You give:** The partner agreement in Bahasa Indonesia ([L2](2_legal.md#1-rules)) with: partner type, commission or partner share, model A or B, lead registration, confidentiality and non-solicitation, no source code ([L6](2_legal.md#1-rules)), client data rules (30-day notice and data export for model A), and reference rights.
* **You receive:** The signed agreement, company documents (NIB, NPWP) and bank details for commission payments.
* **Rule:** Nothing in stage 5 starts before the signature. No agreement before Navario's legal entity exists ([L1](2_legal.md#1-rules)).

## Stage 5: Onboarding

| | Referral Partner | Implementation Partner |
| :-- | :-- | :-- |
| **Materials** | Partner summary, retail price list, pilot offers ([5 §5](5_saas_pricing_model.md#5-pilot), [6 §5](6_enterprise_pricing_model.md#5-pilot)), the brand wording ([3_brand_identity.md](3_brand_identity.md)) | Same, plus the enterprise split |
| **Lead registration** | How to register a lead by WhatsApp or web form | Same |
| **Demo** | None; Navario runs demos | Own demo instance with the trading dataset, and the demo script |
| **Training** | 30-min product overview | Product training: configuration, user training, first-line support. Enough to run stages 2, 5 and 7 of the client process. |
| **Support channel** | WhatsApp with Navario | Second-line channel: how to raise bugs, server and AI issues |

* **You receive:** A completed training (Implementation) and the partner's contact list for leads.
* **Never given:** Source code, server access or architecture details for Platform Core and Nava AI ([techstack.md](techstack.md#4-design-rules), rule 5).

## Stage 6: First Deal

* **Referral:** The partner registers the lead and introduces it. Navario runs the full client process. Commission is paid after the client's payment clears.
* **Implementation:** Navario joins the demo and the needs discussion, and reviews the partner's setup before go-live. The partner leads training and first-line support. From the second deal, Navario steps back to second line.
* **You receive:** The first signed client, and feedback on what the partner needed but did not have.

## Stage 7: Active Partner

* **Every month:** Pay commission or partner share after the client's payment clears (model B), or invoice Navario's share in advance (model A).
* **Every quarter:** 30-min review: leads registered, deals closed, support issues, product feedback.
* **Status (proposed, not decided):** A partner with no registered lead in 6 months goes back to informal referrer ([open decision](8_partnership_model.md#open-decisions) on minimum commitment).

## Tasks

- [ ] **Partner summary.** Done when: a one-page partner summary exists ([8_partnership_model.md](8_partnership_model.md#tasks)).
- [ ] **Fit check form.** Done when: the stage 3 checklist exists as a one-page form.
- [ ] **Partner agreement.** Done when: the draft in [2_legal.md](2_legal.md#tasks) is checked by a notary or lawyer.
- [ ] **Implementation training kit.** Depends on: a signed Implementation Partner. Done when: a training agenda, a configuration guide and a first-line support guide exist. Don't build it before the first partner signs.
- [ ] **Partner demo instance.** Done when: a demo instance can be created per partner from the trading dataset in under an hour.

## Open decisions

- [ ] **Onboarding fee for Implementation Partners.** Recommendation: none at first. Ask for a real prospect instead (stage 3); it costs them nothing and proves commitment.
- [ ] **Who pays for the partner's demo instance.** Recommendation: Navario pays for it while the partner is active, and shuts it down after 6 months with no registered lead.
