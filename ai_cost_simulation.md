# AI Cost Simulation (CoGS)

Internal. The cost of the AI Business Assistant in tokens, per question, per credit and per user, used to set the AI Quota and prices in [5_saas_pricing_model.md](5_saas_pricing_model.md). To change assumptions, edit [ai_cost_simulation.py](script/ai_cost_simulation.py) and re-run it.

**Status:** These are estimates of tokens per call; no real token data has been measured yet. Replace the assumptions with measured averages once the demo logs token counts (see "Next steps").

## Workflow being costed

```
User question
   │
   ▼
1. Intent classifier (Flash-Lite)          1 call
   │
   ▼
2. Reasoning layer (Flash)                 1 call, makes a plan
   │
   ▼
3. Execution & tool calling (Flash)        1 call per tool step + 1 call for the final answer
                                           tool results pile up in the context each step
```

## How cost is calculated

The same way the provider bills it, per call, then summed over all calls in a message:

```
cost = uncached input tokens × input price
     + cached input tokens   × cached input price
     + output tokens         × output price (incl. thinking)
```

Then +20% overhead and +11% PPN for Navario's real cost.

## Gemini prices used

USD per 1M tokens, paid tier, from [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) (checked 8 Oct 2026).

| Model | Input | Cached input | Output (incl. thinking) |
| :-- | --: | --: | --: |
| 2.5 Flash-Lite | 0.10 | 0.01 | 0.40 |
| 3.1 Flash-Lite | 0.25 | 0.025 | 1.50 |
| 2.5 Flash | 0.30 | 0.03 | 2.50 |
| 3.8 Flash, until 31 Dec 2026 | 0.75 | 0.075 | 3.75 |
| **3.8 Flash, from 1 Jan 2027** (also 3.6, 3.7) | **1.50** | **0.15** | **7.50** |

**The latest Flash models double in price on 1 Jan 2027.** Client contracts signed now will run in 2027, so use the 2027 price (stack C) for pricing decisions.

## Assumptions

| | Value | Notes |
| :-- | :-- | :-- |
| Static prompt (cacheable) | 3,000 system prompt + 4,000 tool definitions | ~30 tools with JSON schemas |
| Classifier prompt | 1,500 | |
| Conversation history | 2,000 | Sent again on every call |
| Tool result | 1,500 per step | Accumulates in the execution loop |
| Output | Classifier 50, plan 800, tool step 300, final answer 600 | Includes thinking tokens |
| Cache hit rate | 70% of the static prompt | Gemini context caching, as configured |
| Question mix | 50% simple (1 tool), 35% normal (3 tools), 15% complex (6 tools) | |
| Overhead | +20% | Retries, failed calls, optimistic estimates |
| Tax | +11% PPN | Google charges PPN on digital services to Indonesian buyers |
| Usage | Light 3, normal 6, heavy 15 questions per user per working day; 22 working days | |
| Credit | USD 0.01 of token cost at the reference price list, rounded up per message, minimum 1 | Section "Credits" |
| AI Quota | 700 credits per user per month (draft) | [5_saas_pricing_model.md](5_saas_pricing_model.md#1-subscription) |

Server cost is **not** included; this is AI cost only.

## Credits

Clients see an **AI Quota** measured in **credits**. Tokens stay internal.

**Conversion:** credits per message = token cost of the message at the **reference price list**, divided by USD 0.01, rounded up, minimum 1.

- **Reference price list:** stack C prices (3.1 Flash-Lite + 3.8 Flash at 2027 rates), frozen. Credits are always metered against it, whichever model actually runs. So a question costs the client the same credits even when we route it to a cheaper model or change provider. The saving is Navario's margin, or a bigger AI Quota later.
- **Why cost-weighted tokens, not raw tokens:** output tokens cost 5x input and cached input costs 0.1x input. Counting raw tokens would charge a long cached prompt like a long answer.
- **In tokens:** 1 credit = 6,667 input, 66,667 cached input or 1,333 output tokens on the reference execution model.
- **Why USD 0.01:** fine enough that rounding up adds little, and a simple question still comes out at a small, readable number.

| Question | Calls | Uncached input | Cached input | Output | Credits |
| :-- | --: | --: | --: | --: | --: |
| simple (1 tool) | 4 | 18,550 | 15,750 | 1,750 | 4 |
| normal (3 tools) | 6 | 37,550 | 25,550 | 2,350 | 8 |
| complex (6 tools) | 9 | 79,550 | 40,250 | 3,250 | 15 |
| **Average (question mix)** | | | | | **7.05** |

Tokens are totals over all calls in the message. 100 average questions = 705 credits; the 700-credit AI Quota is about 99 average questions.

## Results

All costs in USD, including the 20% overhead and 11% PPN.

### Cost per question and per credit

| Stack | Simple | Normal | Complex | Average / question | Cost / credit (USD) | Cost / credit (IDR) |
| :-- | --: | --: | --: | --: | --: | --: |
| A. Budget (2.5 Lite + 2.5 Flash) | 0.013 | 0.023 | 0.043 | 0.021 | 0.0030 | 55 |
| B. Current 2026 (3.1 Lite + 3.8 Flash) | 0.027 | 0.050 | 0.098 | 0.046 | 0.0065 | 120 |
| C. Current 2027 (3.1 Lite + 3.8 Flash) | 0.053 | 0.099 | 0.195 | 0.090 | 0.0128 | 237 |

### Cost per user per month

| Stack | AI Quota (700 credits) | Light (465 cr) | Normal (931 cr) | Heavy (2,326 cr) |
| :-- | --: | --: | --: | --: |
| A | 2.09 | 1.39 | 2.78 | 6.95 |
| B | 4.53 | 3.01 | 6.02 | 15.05 |
| C | 8.96 | 5.95 | 11.91 | 29.77 |

Questions to credits: 30 = 212, 200 = 1,410, 500 = 3,525, 1,000 = 7,050, 2,500 = 17,625.

## What this means

Our prices are in IDR. For comparison, we plan with USD 1 = IDR 18,500: the market rate is about IDR 18,000 (Oct 2026), plus a buffer.

1. **AI cost per user ranges from USD 2 to 9 for a full AI Quota, depending on the model.** Model choice changes CoGS by more than 4x, so it is the biggest pricing decision.
2. **A credit costs Navario IDR 55 (stack A) to IDR 237 (stack C).** The top-ups in [5_saas_pricing_model.md](5_saas_pricing_model.md) sell below cost on stacks B and C.
3. **Credits fix the flat-question risk.** A complex question uses about 4x the credits of a simple one, matching its cost. Heavy analysis users run out sooner instead of eating the margin.
4. **Enterprise uses BYOK** (see [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md)), so AI cost is the client's, not ours. Use the "Cost per user per month" table as the client's budget estimate: cost per user for their usage level × number of users.
5. **Complex questions cost 3–4x a simple one**, because tool results pile up in the context on every step. Capping tool steps and trimming tool results are the cheapest optimizations.

## Recommendations

1. **Route by intent.** Let the classifier send simple lookups (the "find", "open", "print" intents) straight to execution on a cheaper model, and use the strongest Flash only for analysis and multi-step questions. Test whether 2.5 Flash (or 3.1 Flash-Lite) is good enough for execution: if quality holds, cost drops close to stack A while credits stay the same.
2. **Cut the tokens that repeat on every call:**
   - Send only the tools relevant to the classified intent, not all ~30.
   - Keep history short (last 3–4 turns, or a summary).
   - Return compact tool results: top 20 rows plus totals, and a link to the full list.
   - Cap the execution loop at ~6 tool steps.
3. **Set prices from stack C until quality tests prove a cheaper stack.** Then raise the AI Quota rather than cut prices. Raising AI limits later is easy; cutting them is not.
4. **Re-price top-ups** at ≥ 2x the cost per credit of the chosen stack: IDR 473 per credit on stack C, IDR 111 on stack A.
5. **Enforce the AI Quota in the product:** credits per message shown under each answer, a company pool, a per-user daily cap (for example 212 credits, about 30 questions), a warning at 80%, and a clear message when the quota runs out.

## Next steps

- [ ] Log per message: model, number of calls, input / cached / output tokens, intent, and credits charged. Gemini returns the tokens in `usage_metadata`.
- [ ] Run 50 realistic questions on the demo data and replace the assumptions with measured averages.
- [ ] Test answer quality on 2.5 Flash versus 3.8 Flash for the execution step.
- [ ] Choose the stack, then update the AI Quota and top-up prices in [5_saas_pricing_model.md](5_saas_pricing_model.md).

## Open decisions

- [ ] **AI Quota vs normal usage.** A "normal" user (931 credits) uses more than the 700-credit AI Quota. Is that intended, to drive top-ups? Recommendation: confirm it, and make the 80% warning and the top-up flow smooth.
- [ ] **Exchange rate review.** Planning rate is IDR 18,500 per USD (set 9 Oct 2026). Recommendation: review quarterly; re-run both scripts if the market rate passes IDR 18,500.
- [ ] **Reference price list when providers change.** Recommendation: keep stack C 2027 prices as the frozen reference for the whole contract term; review it only at the yearly price review, with 30 days' notice.
