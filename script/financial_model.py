"""
Navario potential profit per client: python3 script/financial_model.py
Edit the ASSUMPTIONS section and re-run. Results are copied into the
"Financial model" sections of 5_saas_pricing_model.md and 6_enterprise_pricing_model.md.
Prices here must match those two docs; they are the source of truth.
"""

from ai_cost_simulation import QUESTION_MIX, STACKS, question_cost_usd, total_usd

# ---------------------------------------------------------------- ASSUMPTIONS

USD_IDR = 16_500  # same rate as ai_cost_simulation.md

# Retail, from 5_saas_pricing_model.md (draft)
PRICE_PER_USER = 400_000  # IDR / user / month
ANNUAL_DISCOUNT = 0.15
SETUP = {"Fast-Track": 3_500_000, "Standard": 8_500_000}
ALLOWANCE = 100  # AI questions / user / month, assume the pool is fully used
RETAIL_CLIENTS = {"3 users": (3, "Fast-Track"), "10 users": (10, "Fast-Track"), "30 users": (30, "Standard")}
PARTNER_COMMISSION = 0.15  # option A in 8_partnership_model.md, only if a partner referred the client

# Enterprise, from 6_enterprise_pricing_model.md (draft)
ENTERPRISE_CLIENT_PRICE = 12_500_000  # IDR / month
NAVARIO_SHARE = 7_500_000  # IDR / month
ENTERPRISE_SETUP = 25_000_000  # Navario's technical part, "from"

# Market potential, from market_analysis.md (Kadin, 31 Dec 2025, non-agricultural)
SMALL_MEDIUM_FIRMS = 73_828 + 15_313
TRADE_SHARE = 14.44 / 30.21  # trade share of all MSMEs; assumed to hold for small + medium
USERS_PER_CLIENT = 10  # assumption: typical segment A client, matches the 10+ user pilot rule
CLIENT_SCENARIOS = [10, 30, 100, 300]  # paying retail clients

# Unknown: server cost per client and per dedicated server, support, fixed costs.
# Results are before these costs.

# ---------------------------------------------------------------- MODEL


def ai_cost_per_question_idr(stack):
    usd = sum(share * total_usd(question_cost_usd(stack, steps)) for share, steps in QUESTION_MIX.values())
    return usd * USD_IDR


def idr(x):
    return f"{x / 1e6:.2f}M"


def retail():
    print("Retail AI cost per user per month, IDR, full allowance used\n")
    print("| Stack | AI cost | Share of price |")
    print("| :-- | --: | --: |")
    for stack_name, stack in STACKS.items():
        ai_user = ai_cost_per_question_idr(stack) * ALLOWANCE
        print(f"| {stack_name} | {ai_user:,.0f} | {ai_user / PRICE_PER_USER:.0%} |")

    print("\nRetail profit per client, IDR, before server, support and fixed costs\n")
    print("| Stack | Client | Revenue / month | Profit / month, direct | Profit / month, referred "
          "| Year 1, direct, incl. setup | Year 1, annual prepaid, incl. setup |")
    print("| :-- | :-- | --: | --: | --: | --: | --: |")
    for stack_name, stack in STACKS.items():
        ai_user = ai_cost_per_question_idr(stack) * ALLOWANCE
        for name, (users, setup) in RETAIL_CLIENTS.items():
            revenue = PRICE_PER_USER * users
            ai = ai_user * users
            direct = revenue - ai
            referred = direct - revenue * PARTNER_COMMISSION
            year1 = direct * 12 + SETUP[setup]
            year1_annual = (revenue * (1 - ANNUAL_DISCOUNT) - ai) * 12 + SETUP[setup]
            print(f"| {stack_name[:1]} | {name}, {setup} | {idr(revenue)} | {idr(direct)} | {idr(referred)} "
                  f"| {idr(year1)} | {idr(year1_annual)} |")


def enterprise():
    print("\nEnterprise profit per client, IDR, AI is BYOK, before dedicated server cost\n")
    print("| Deal | Profit / month | Year 1, incl. setup |")
    print("| :-- | --: | --: |")
    print(f"| Through a partner (Navario's share) | {idr(NAVARIO_SHARE)} | {idr(NAVARIO_SHARE * 12 + ENTERPRISE_SETUP)} |")
    print(f"| Direct, no partner | {idr(ENTERPRISE_CLIENT_PRICE)} | {idr(ENTERPRISE_CLIENT_PRICE * 12 + ENTERPRISE_SETUP)} |")


def idr_b(x):
    return f"{x / 1e9:,.1f}B"


def market():
    firms = SMALL_MEDIUM_FIRMS * TRADE_SHARE
    revenue_client = PRICE_PER_USER * USERS_PER_CLIENT * 12
    ai_client = ai_cost_per_question_idr(STACKS[list(STACKS)[-1]]) * ALLOWANCE * USERS_PER_CLIENT * 12
    print(f"\nRetail market potential, {USERS_PER_CLIENT} users per client, list price, stack C, direct\n")
    print(f"Trading small + medium firms (estimate): {firms:,.0f}")
    print(f"If every one were a client: {idr_b(firms * revenue_client)} subscription revenue / year\n")
    print("| Paying clients | Share of trading firms | Subscription revenue / year | Profit / year, before server, support, fixed |")
    print("| --: | --: | --: | --: |")
    for n in CLIENT_SCENARIOS:
        print(f"| {n} | {n / firms:.2%} | {idr_b(n * revenue_client)} | {idr_b(n * (revenue_client - ai_client))} |")


if __name__ == "__main__":
    retail()
    enterprise()
    market()
