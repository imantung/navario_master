"""AI cost (CoGS) simulation for the Navario AI Business Assistant.

Cost is computed from tokens the way the provider bills them:
uncached input x input price + cached input x cached price + output x output price.
Clients see an AI Quota measured in credits; tokens are never client-facing.

Run: python3 ai_cost_simulation.py
Edit the ASSUMPTIONS section and re-run. Results are explained in ai_cost_simulation.md.
"""

import math

# ---------------------------------------------------------------- ASSUMPTIONS

TAX = 0.11            # PPN on foreign digital services (PMSE), charged on Google invoices
OVERHEAD = 0.20       # retries, failed calls, token estimates being optimistic

# Gemini API paid tier, USD per 1M tokens: (input, cached input, output incl. thinking)
# Source: ai.google.dev/gemini-api/docs/pricing, checked 8 Oct 2026
MODELS = {
    "2.5-flash-lite":  (0.10, 0.01, 0.40),
    "3.1-flash-lite":  (0.25, 0.025, 1.50),
    "2.5-flash":       (0.30, 0.03, 2.50),
    "3.8-flash-2026":  (0.75, 0.075, 3.75),   # until 31 Dec 2026
    "3.8-flash-2027":  (1.50, 0.15, 7.50),    # from 1 Jan 2027 (also 3.6, 3.7 Flash)
}

# Model stacks: (intent classifier, reasoning, execution)
STACKS = {
    "A. Budget (2.5 Lite + 2.5 Flash)":       ("2.5-flash-lite", "2.5-flash", "2.5-flash"),
    "B. Current 2026 (3.1 Lite + 3.8 Flash)": ("3.1-flash-lite", "3.8-flash-2026", "3.8-flash-2026"),
    "C. Current 2027 (3.1 Lite + 3.8 Flash)": ("3.1-flash-lite", "3.8-flash-2027", "3.8-flash-2027"),
}

# Tokens per call
CLASSIFIER_PROMPT = 1_500   # instructions + intent list (static, cacheable)
SYSTEM_PROMPT = 3_000       # assistant instructions, rules, user role (static, cacheable)
TOOL_DEFINITIONS = 4_000    # ~30 tools with JSON schemas (static, cacheable)
HISTORY = 2_000             # earlier turns of the conversation sent again
USER_MESSAGE = 100
TOOL_RESULT = 1_500         # rows / report summary returned by each tool, accumulates
CLASSIFIER_OUTPUT = 50
REASONING_OUTPUT = 800      # plan, incl. thinking
STEP_OUTPUT = 300           # one tool call, incl. thinking
ANSWER_OUTPUT = 600         # final answer (table / summary)
CACHE_HIT_RATE = 0.7        # share of the static prefix actually billed at cached price

# Question mix: name -> (share, tool steps)
QUESTION_MIX = {
    "simple (1 tool)":   (0.50, 1),
    "normal (3 tools)":  (0.35, 3),
    "complex (6 tools)": (0.15, 6),
}

# Credits (the unit of the client's AI Quota)
# credits per message = token cost at the REFERENCE price list / CREDIT_USD, rounded up, minimum 1.
# The reference is frozen, so a question costs the same credits whichever model actually runs it.
CREDIT_USD = 0.01
REFERENCE = "C. Current 2027 (3.1 Lite + 3.8 Flash)"
QUOTA_CREDITS = 700        # retail AI Quota per user per month (draft, 5_saas_pricing_model.md)
USD_IDR = 18_500         # planning rate with a buffer; market ~18,000 (Oct 2026)

WORKING_DAYS = 22
USAGE_PROFILES = {"light": 3, "normal": 6, "heavy": 15}   # questions per user per working day

# ---------------------------------------------------------------- MODEL


def question_calls(stack, steps):
    """Token usage per call: (model, uncached input, cached input, output)."""
    classifier, reasoning, execution = stack
    static = SYSTEM_PROMPT + TOOL_DEFINITIONS

    def call(model, static_in, dynamic_in, out):
        cached = static_in * CACHE_HIT_RATE
        return model, static_in - cached + dynamic_in, cached, out

    calls = [call(classifier, CLASSIFIER_PROMPT, HISTORY + USER_MESSAGE, CLASSIFIER_OUTPUT),
             call(reasoning, static, HISTORY + USER_MESSAGE, REASONING_OUTPUT)]
    # execution loop: one call per tool step plus the final answer; tool results accumulate
    for i in range(steps + 1):
        dynamic = HISTORY + USER_MESSAGE + REASONING_OUTPUT + i * (TOOL_RESULT + STEP_OUTPUT)
        calls.append(call(execution, static, dynamic, ANSWER_OUTPUT if i == steps else STEP_OUTPUT))
    return calls


def tokens_cost_usd(calls):
    cost = 0
    for model, uncached, cached, out in calls:
        price_in, price_cached, price_out = MODELS[model]
        cost += (uncached * price_in + cached * price_cached + out * price_out) / 1e6
    return cost


def question_cost_usd(stack, steps):
    return tokens_cost_usd(question_calls(stack, steps))


def question_credits(steps):
    return max(1, math.ceil(round(question_cost_usd(STACKS[REFERENCE], steps) / CREDIT_USD, 6)))


def average_credits():
    return sum(share * question_credits(steps) for share, steps in QUESTION_MIX.values())


def cost_per_credit_usd(stack):
    """Navario's real AI cost per credit on a stack, incl. overhead and PPN."""
    avg_cost = sum(share * total_usd(question_cost_usd(stack, steps)) for share, steps in QUESTION_MIX.values())
    return avg_cost / average_credits()


def total_usd(usd):
    return usd * (1 + OVERHEAD) * (1 + TAX)


def main():
    ref_in, ref_cached, ref_out = MODELS[STACKS[REFERENCE][2]]
    print(f"Credit: USD {CREDIT_USD} of token cost at the reference price list ({REFERENCE})")
    print(f"  = {CREDIT_USD / ref_in * 1e6:,.0f} input, {CREDIT_USD / ref_cached * 1e6:,.0f} cached input "
          f"or {CREDIT_USD / ref_out * 1e6:,.0f} output tokens on the reference execution model\n")

    print("| Question | Calls | Uncached input | Cached input | Output | Credits |")
    print("| :-- | --: | --: | --: | --: | --: |")
    for q, (share, steps) in QUESTION_MIX.items():
        calls = question_calls(STACKS[REFERENCE], steps)
        unc, cac, out = (sum(c[i] for c in calls) for i in (1, 2, 3))
        print(f"| {q} | {len(calls)} | {unc:,.0f} | {cac:,.0f} | {out:,.0f} | {question_credits(steps)} |")
    avg = average_credits()
    print(f"| **Average (question mix)** | | | | | **{avg:.2f}** |")

    print("\n| Stack | Simple | Normal | Complex | Average / question | Cost / credit (USD) | Cost / credit (IDR) |")
    print("| :-- | --: | --: | --: | --: | --: | --: |")
    for name, stack in STACKS.items():
        costs = [total_usd(question_cost_usd(stack, steps)) for _, steps in QUESTION_MIX.values()]
        mean = sum(share * c for (share, _), c in zip(QUESTION_MIX.values(), costs))
        cpc = cost_per_credit_usd(stack)
        print(f"| {name} | {costs[0]:.3f} | {costs[1]:.3f} | {costs[2]:.3f} | {mean:.3f} | {cpc:.4f} | {cpc * USD_IDR:,.0f} |")

    print("\n| Stack | AI Quota "
          f"({QUOTA_CREDITS} credits) | "
          + " | ".join(f"{p.capitalize()} ({n * WORKING_DAYS * avg:,.0f} cr)" for p, n in USAGE_PROFILES.items()) + " |")
    print("| :-- | --: | --: | --: | --: |")
    for name, stack in STACKS.items():
        cpc = cost_per_credit_usd(stack)
        usage = " | ".join(f"{n * WORKING_DAYS * avg * cpc:.2f}" for n in USAGE_PROFILES.values())
        print(f"| {name[:1]} | {QUOTA_CREDITS * cpc:.2f} | {usage} |")

    print(f"\n100 average questions = {100 * avg:,.0f} credits. AI Quota of {QUOTA_CREDITS} credits "
          f"= about {QUOTA_CREDITS / avg:.0f} average questions.")
    print("Questions to credits: " + ", ".join(f"{q:,} = {q * avg:,.0f}" for q in (30, 200, 500, 1_000, 2_500)))
    print("Top-up floor (2x cost per credit): " + ", ".join(
        f"{n[:1]} IDR {2 * cost_per_credit_usd(st) * USD_IDR:,.0f}" for n, st in STACKS.items()) + " per credit")


if __name__ == "__main__":
    main()
