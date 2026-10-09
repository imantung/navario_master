# Market Analysis: Indonesian SMEs

Internal. Who the retail market is, how big it is, who Navario competes with, and how Indonesian business culture shapes the sale. It tests the founder's six hypotheses against sources. Prices are not repeated here; they are in [5_saas_pricing_model.md](5_saas_pricing_model.md#4-benchmark-odoo). Positioning is in [3_brand_identity.md](3_brand_identity.md).

**Bottom line:** the market is big enough for many years of a solo founder's capacity. Demand is not the bottleneck. **Trust and reach are.** The real competitor at the low end is local accounting software (Accurate, Jurnal), not Odoo Community. AI gets the meeting, but control and cash flow close the deal.

## 1. Market size

**MSME** (UMKM, *Usaha Mikro, Kecil dan Menengah*) is the official Indonesian size class. Size is set by business capital (*modal usaha*), excluding land and buildings.

| Class | Business capital | Units (non-agricultural, 31 Dec 2025) | Share |
| :-- | :-- | --: | --: |
| Micro | ≤ IDR 1B | 30,119,928 | 99.70% |
| Small | > IDR 1B – 5B | 73,828 | 0.24% |
| Medium | > IDR 5B – 10B | 15,313 | 0.05% |
| **Total** | | **30,209,069** | |

From [Kadin, UMKM Indonesia](https://kadin.id/en/data-dan-statistik/umkm-indonesia/) (checked 9 Oct 2026), citing the Ministry of MSMEs (SIDT-UMKM database). Annual sales thresholds under PP 7/2021 are **[unverified]**.

**Wholesale and retail trade** is the largest sector: 14.44M of 30.21M units (about 48%), same source.

### From the headline number to Navario's market

| Step | Units | Note |
| :-- | --: | :-- |
| All non-agricultural MSMEs | 30.2M | The "64M UMKM" number often quoted includes agriculture and is almost all micro. Don't use it in a pitch. |
| Small + medium only | ~89,000 | Micro firms rarely have 3+ office users or a budget for an ERP. |
| Of which trading (estimate) | **~43,000** | Assumes the 48% trade share holds for small and medium firms. **Estimate, not a published figure.** |
| Large companies (enterprise track) | Unknown | Not in the MSME data. |

**What it means:** ~43,000 trading companies is a large market for a company that needs tens of clients, not thousands. Revenue per number of clients is in [5 §6, Market potential](5_saas_pricing_model.md#market-potential): 100 clients is under a quarter of one percent of the market. Do not spend time on market size research. Spend it on reaching the first 30 owners ([7_go_to_market.md](7_go_to_market.md#5-channels-in-priority-order)).

### What limits growth: capacity, not demand

| Stage | Realistic paying retail clients | Limited by |
| :-- | :-- | :-- |
| Solo founder | ~10–20 | Founder time: selling, setup and support, with ~50% on AI projects ([C1](0_business_constraint.md#1-founder-and-capacity)) |
| + first support hire | ~30–60 | Setup capacity; hire trigger in [9](9_saas_process_flow.md#support-coverage) |
| + active referral and implementation partners | 100+ | Partner reach and quality ([8](8_partnership_model.md)) |

These ranges are judgement, not data. Replace them with real setup and support hours per client after the pilots.

## 2. The founder's hypotheses, tested

| # | Hypothesis | Verdict | Evidence | What to do |
| :-- | :-- | :-- | :-- | :-- |
| H1 | Many companies don't have an ERP or business system. | **Partly true.** | 99.7% of MSMEs are micro (section 1). No source found for the ERP adoption rate of small and medium firms (**unknown**). Many small traders already use accounting software: Jurnal claims more than 35,000 companies ([jurnal.id](https://www.jurnal.id/id/harga/), checked 9 Oct 2026). | "No ERP" does not mean "no system". Most target firms have spreadsheets, WhatsApp **and** an accounting app. Log the current tools of every prospect in the lead sheet. After 20 demos, the real split is known. |
| H2 | The AI hype makes people want to use AI. | **True for attention, weak for closing.** | Jurnal already sells "AI-supported accounting" on its pricing page, and Odoo Custom includes agentic AI ([5 §4](5_saas_pricing_model.md#4-benchmark-odoo)). AI is becoming a standard feature, not a reason on its own. | Use AI to get the demo booked. Close on outcomes the owner already feels: overdue receivables, dead stock, staff they cannot check. |
| H3 | Economic pressure pushes owners towards productivity. | **Double-edged.** | GDP grew 5.11% in 2025; manufacturing lost an estimated 300,000 jobs since 2023 ([Wikipedia, Economy of Indonesia](https://en.wikipedia.org/wiki/Economy_of_Indonesia), checked 9 Oct 2026). Pressure also makes owners delay new spending. Admin wages are low, so "save staff hours" is a weak argument. | Sell **cash and control**, not productivity: collect receivables faster, cut stock that does not move, see the business without asking staff. |
| H4 | Odoo costs the same per month but implementation is very costly. | **Half true.** | Odoo's licence is **cheaper** per user than Navario's draft price, not the same ([5 §4](5_saas_pricing_model.md#4-benchmark-odoo)). Implementation cost by Indonesian Odoo partners is **unknown**; the task to get 2–3 quotes is open ([5 Tasks](5_saas_pricing_model.md#tasks)). | Never compare monthly licence. Compare **first-year total cost**, after real partner quotes are in hand. |
| H5 | Odoo Community can't compete with us. | **True against Community, but the wrong opponent.** | Community needs self-hosting and a developer, so few small traders run it alone. The low-price opponent is local accounting software: Accurate's base plan and Jurnal's plans are far cheaper for a small team, and Jurnal includes free implementation help ([5 §4](5_saas_pricing_model.md#4-benchmark-odoo)). | Benchmark Accurate and Jurnal, not Odoo Community. Target firms that have **outgrown** them (section 4). |
| H6 | ERPNext is not popular in Indonesia. | **True.** | Frappe lists 3 partners in Indonesia; Odoo lists 67 (7 Gold, 15 Silver, 45 Ready) ([frappe.io](https://frappe.io/partners/regions), [odoo.com](https://www.odoo.com/partners/country/indonesia-98), both checked 9 Oct 2026). | Good: no one sells the same platform locally. Bad: no local ERPNext talent pool for partners or hires ([X18](1_challenges.md#2-founder-capacity)). It does not matter to buyers, since public copy never says ERPNext ([L4](2_legal.md#1-rules)). |

## 3. Competitors

| Competitor | What a trading SME sees | Where they beat Navario |
| :-- | :-- | :-- |
| **Spreadsheets + WhatsApp** | Free, known, flexible | Price, habit |
| **Accurate Online** | Local accounting brand, 1 user in the base plan, cheap add-on users and branches | Price, brand, accountants know it |
| **Jurnal (Mekari)** | Local accounting + inventory, AI claim, free implementation help, part of the Mekari suite (HR, payroll) | Price, brand, free onboarding, payroll in the same vendor |
| **Odoo (via partner)** | Global ERP brand, 67 local partners, many references | Brand, features, partner reach |
| **Odoo Community / local freelancers** | Free licence, cheap developer | Lowest cash price |

Prices for all of these are in [5 §4](5_saas_pricing_model.md#4-benchmark-odoo). Where Navario wins, and what to lead with against each, is in [3 §2 Competitive advantage](3_brand_identity.md#competitive-advantage).

**Weakness to name:** a 3-user trading company will almost always find Accurate or Jurnal cheaper. Navario cannot win the smallest firms on price, and should not try.

## 4. Target segments

| Segment | Typical profile | Pain | Fit |
| :-- | :-- | :-- | :-- |
| **A. Outgrown accounting software** | 10–30 users, 2+ warehouses or branches, uses Accurate/Jurnal + Excel for stock and approvals | Numbers in three places, no approval control, owner asks staff for every figure | **Best.** Already pays for software, pain is clear, setup fee is affordable. |
| **B. Spreadsheet + WhatsApp only** | 5–15 users, owner-run, growing | No control, stock mismatches, overdue receivables | Good, but price-sensitive and may pick Accurate as the "first step". |
| **C. Failed or stalled Odoo project** | 10–50 users, paid a partner, project stuck or over budget | Sunk cost, distrust of vendors | Good, but hard to find and distrustful. Fixed price is the message. |
| **D. Micro traders (1–3 people)** | Owner + family | Bookkeeping | **Not a target.** Price-driven; local apps serve them. |

**Recommendation:** lead retail with **segment A**. Reason: they already accept paying for software and feel the pain of outgrowing it, so the demo answers a question they already have. Trade-off: a smaller pool than "everyone without an ERP", and the brand doc names spreadsheets as the main competitor (open decision below).

## 5. How business works in Indonesia, and what it means for the sale

| Reality | What it means for Navario |
| :-- | :-- |
| **The owner decides alone.** Most trading SMEs are family-owned and owner-run. Managers recommend; the owner signs. | The owner must be in the demo ([pilot rule](5_saas_pricing_model.md#who-qualifies)). Talk to the owner about money and control, not features. |
| **Trust comes through people, not websites.** A referral from a friend, an accountant or a supplier counts more than any ad. | Warm network and referral partners first, as in [7 §5](7_go_to_market.md#5-channels-in-priority-order). Ask every demo for one introduction. |
| **WhatsApp is the business channel.** Orders, approvals, receipts and reminders already run on it. | Follow up on WhatsApp, not email. Proactive WhatsApp summaries ([4.2](4_product_scope.md#4-long-term-sell-only-as-planned-with-a-delivery-date)) fit how owners already work. |
| **Indirect "no".** "*Nanti dulu*", "*saya pikir-pikir dulu*" or no reply usually means no or not now. "*Iya*" can mean "I heard you". | Ask for a concrete next step with a date at the end of each demo. Record "no response after 2 follow-ups" as lost, with the reason. |
| **Negotiation is expected.** "*Bisa kurang?*" (can it be cheaper?) is a normal question, not a rejection. | Keep the fixed price ([C8](0_business_constraint.md#3-commercial-rules)), but prepare non-price concessions in advance: an extra training session, a longer trial, help with data import. |
| **Owners want to pay later; Navario needs cash first.** Payment terms of 30+ days are common between businesses. | Cash first stays. The open decision below tests a two-part setup payment. |
| **Owners worry about staff, not only numbers.** Staff fraud, stock leaks and "only one person knows the system" are common fears. | Access rules and the request log are a selling point: "every question and every action is recorded". Only say this once both are **Works** ([4](4_product_scope.md)). |
| **Staff may resist.** Admin staff fear the system will expose mistakes or replace them. Staff rarely disagree with the owner openly; they slow down quietly. | Name one key user per client during setup. Present the assistant as help for staff, not a check on them. |
| **Tax transparency is sensitive.** Some SMEs keep records loosely to limit tax exposure. A clean ERP makes everything visible. The tax office's Coretax system raises the pressure to digitise **[unverified: rollout status and SME obligations]**. | Never position Navario as tax avoidance or as a tax tool. Say plainly that e-Faktur export is not built ([4.3](4_product_scope.md#4-long-term-sell-only-as-planned-with-a-delivery-date)). Accountant partners handle tax questions. |
| **"ERP" means big company.** Owners don't know the term, and those who do see it as expensive software for large firms (founder's conversations with business-owner friends, Oct 2026; not yet tested in demos). | Don't say "ERP" to SME owners. Say *sistem bisnis* or name the jobs: bookkeeping, stock, buying, selling ([3 §3](3_brand_identity.md#3-words)). Keep "ERP" for enterprise and IT partners. |
| **Bahasa Indonesia first.** Admin staff in many SMEs are not comfortable with English screens. | This is a real edge against Odoo and plain ERPNext. Show it in every demo. |
| **Calendar.** Ramadan and Lebaran (Eid) slow decisions and drain cash (THR, the religious holiday bonus). January is the natural start for a new accounting system. | Don't plan go-lives in the two weeks before Lebaran. Push pilots to go live by January where possible. Lebaran 2027 date **[unverified]**. |

## 6. What this changes in other docs

- **Positioning ([3](3_brand_identity.md#2-positioning)):** lead with AI to book the demo, then sell control and cash. "Main competitor: spreadsheets" understates accounting software (open decision).
- **Pricing ([5 §4](5_saas_pricing_model.md#4-benchmark-odoo)):** Accurate and Jurnal are now in the benchmark, which closes the comparison part of [X12](1_challenges.md#4-competition).
- **Discovery ([9](9_saas_process_flow.md)):** already asks for current tools. Add the reason the prospect is looking now (outgrown tool, failed project, owner wants control).

## Tasks

- [ ] **Test the hypotheses in demos.** Done when: 20 demos are logged with current tools, segment (A–D), reason for looking now, the words the owner uses for their system, and won/lost reason.
- [ ] **Try Jurnal's AI.** Done when: a Jurnal trial has been tested with the same 5 demo questions, and A1 in [3 §2](3_brand_identity.md#competitive-advantage) is confirmed or changed.
- [ ] **Odoo partner quotes.** Same task as [5 Tasks](5_saas_pricing_model.md#tasks). Done when: H4 has a real first-year cost.
- [ ] **Verify open facts.** Done when: PP 7/2021 sales thresholds, Coretax obligations for SMEs and the Lebaran 2027 date are checked and cited, or removed.

## Assumptions

- Small and medium trading firms have the same trade share (~48%) as all MSMEs.
- A typical retail client has 10 paying users (used in the market potential).
- Segment A firms will pay more than their current accounting software for control and AI.
- Owners respond to "control and cash" more than to "AI" when it comes to paying. Not tested with a prospect yet.

## Open decisions

- [ ] **Primary retail segment.** Recommendation: segment A (outgrown Accurate/Jurnal, 10–30 users). Update the positioning in [3](3_brand_identity.md#2-positioning) once decided.
- [ ] **Minimum client size.** A 3-user minimum invites segment D, where Accurate and Jurnal win on price. Recommendation: keep 3 users as the contract minimum, but qualify pilots at 10+ users.
- [ ] **Setup payment terms.** Owners expect to pay later; [C8](0_business_constraint.md#3-commercial-rules) requires cash first. Recommendation: Standard setup in two payments (60% at signing, 40% before go-live). Work still starts only after the first payment clears.
