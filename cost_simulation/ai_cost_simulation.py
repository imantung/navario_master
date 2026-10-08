"""AI cost (CoGS) simulation for the Navario AI Business Assistant.

Run: python3 ai_cost_simulation.py
Edit the ASSUMPTIONS section and re-run. Results are explained in ai_cost_simulation.md.
"""

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

WORKING_DAYS = 22
USAGE_PROFILES = {"light": 3, "normal": 6, "heavy": 15}   # questions per user per working day

# ---------------------------------------------------------------- MODEL


def call_cost(model, static_in, dynamic_in, out):
    price_in, price_cached, price_out = MODELS[model]
    cached = static_in * CACHE_HIT_RATE
    uncached = static_in - cached + dynamic_in
    return (uncached * price_in + cached * price_cached + out * price_out) / 1e6


def question_cost_usd(stack, steps):
    classifier, reasoning, execution = stack
    static = SYSTEM_PROMPT + TOOL_DEFINITIONS
    cost = call_cost(classifier, CLASSIFIER_PROMPT, HISTORY + USER_MESSAGE, CLASSIFIER_OUTPUT)
    cost += call_cost(reasoning, static, HISTORY + USER_MESSAGE, REASONING_OUTPUT)
    # execution loop: one call per tool step plus the final answer; tool results accumulate
    for i in range(steps + 1):
        dynamic = HISTORY + USER_MESSAGE + REASONING_OUTPUT + i * (TOOL_RESULT + STEP_OUTPUT)
        out = ANSWER_OUTPUT if i == steps else STEP_OUTPUT
        cost += call_cost(execution, static, dynamic, out)
    return cost


def total_usd(usd):
    return usd * (1 + OVERHEAD) * (1 + TAX)


def main():
    for name, stack in STACKS.items():
        print(f"\n{name}")
        avg = 0
        for q, (share, steps) in QUESTION_MIX.items():
            c = total_usd(question_cost_usd(stack, steps))
            avg += share * c
            print(f"  {q:<18} USD {c:>7.4f} / question")
        print(f"  {'weighted average':<18} USD {avg:>7.4f} / question")
        for p, per_day in USAGE_PROFILES.items():
            n = per_day * WORKING_DAYS
            print(f"  {p:<6} user ({n:>3} q/mo)   USD {avg * n:>6.2f} / user / month")
        print(f"  100 questions (retail allowance)  USD {avg * 100:>6.2f}")


if __name__ == "__main__":
    main()
