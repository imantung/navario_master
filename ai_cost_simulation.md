# AI Cost Simulation (CoGS)

Internal. The cost of the AI Business Assistant per question and per user, used to set AI limits and prices in [5_saas_pricing_model.md](5_saas_pricing_model.md). To change assumptions, edit [ai_cost_simulation.py](script/ai_cost_simulation.py) and re-run it.

**Status:** These are estimates; no real token data has been measured yet. Replace the assumptions with measured averages once the demo logs token counts (see "Next steps").

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

Server cost is **not** included; this is AI cost only.

## Results

All costs in USD, including the 20% overhead and 11% PPN.

### Cost per question

| Stack (classifier + reasoning/execution) | Simple | Normal | Complex | **Average** |
| :-- | --: | --: | --: | --: |
| A. Budget: 2.5 Flash-Lite + 2.5 Flash | 0.013 | 0.023 | 0.043 | **0.021** |
| B. 3.1 Flash-Lite + 3.8 Flash, 2026 price | 0.027 | 0.050 | 0.098 | **0.046** |
| C. 3.1 Flash-Lite + 3.8 Flash, **2027 price** | 0.053 | 0.099 | 0.195 | **0.090** |

### Cost per user per month

| Stack | 100 questions (retail allowance) | Light (66) | Normal (132) | Heavy (330) |
| :-- | --: | --: | --: | --: |
| A. Budget | 2.11 | 1.39 | 2.78 | 6.95 |
| B. 2026 price | 4.56 | 3.01 | 6.02 | 15.05 |
| C. 2027 price | 9.02 | 5.95 | 11.91 | 29.77 |

## What this means

Our prices are in IDR. For comparison, USD 1 ≈ IDR 16,500.

1. **AI cost per user ranges from USD 2 to 9 for 100 questions, depending on the model.** Model choice changes CoGS by more than 4x, so it is the biggest pricing decision.
2. **Current top-up prices lose money on stack C.** Stack C costs ~USD 0.09 (~IDR 1,500) per question; the top-ups in [5_saas_pricing_model.md](5_saas_pricing_model.md) sell for less. Even on stack A the margin is thin once you take the server into account.
3. **Retail with 100 questions per user:** AI cost is USD 2.11 (stack A) to USD 9.02 (stack C) per user per month (table above). Compare it with the retail price per user in [5_saas_pricing_model.md](5_saas_pricing_model.md). On stack C, AI takes too large a share of the price to leave room for server, support and partner commission.
4. **Enterprise uses BYOK** (see [6_enterprise_pricing_model.md](6_enterprise_pricing_model.md)), so AI cost is the client's, not ours. Use the "Cost per user per month" table as the client's budget estimate: cost per user for their usage level × number of users. Example: an enterprise client with 50 normal users asks ~6,600 questions a month.
5. **Complex questions cost 3–4x a simple one**, because tool results pile up in the context on every step. Capping tool steps and trimming tool results are the cheapest optimizations.

## Recommendations

1. **Route by intent.** Let the classifier send simple lookups (the "find", "open", "print" intents) straight to execution on a cheaper model, and use the strongest Flash only for analysis and multi-step questions. Test whether 2.5 Flash (or 3.1 Flash-Lite) is good enough for execution: if quality holds, cost drops close to stack A.
2. **Cut the tokens that repeat on every call:**
   - Send only the tools relevant to the classified intent, not all ~30.
   - Keep history short (last 3–4 turns, or a summary).
   - Return compact tool results: top 20 rows plus totals, and a link to the full list.
   - Cap the execution loop at ~6 tool steps.
3. **Set prices from stack C until quality tests prove a cheaper stack.** Then lower prices or raise limits. Raising AI limits later is easy; cutting them is not.
4. **Re-price top-ups** at ≥ 2x the cost per question of the chosen stack. On stack C that is ~USD 0.18 (~IDR 3,000) per question; on stack A ~USD 0.045 (~IDR 700–800).
5. **Enforce limits in the product:** a company pool, a per-user daily cap (for example 30 questions), a warning at 80%, and a clear message when the pool runs out.

## Next steps

- [ ] Log per question: model, number of calls, input / cached / output tokens, and intent. Gemini returns these in `usage_metadata`.
- [ ] Run 50 realistic questions on the demo data and replace the assumptions with measured averages.
- [ ] Test answer quality on 2.5 Flash versus 3.8 Flash for the execution step.
- [ ] Choose the stack, then update AI allowances and top-up prices in [5_saas_pricing_model.md](5_saas_pricing_model.md).
