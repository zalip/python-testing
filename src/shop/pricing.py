from decimal import ROUND_HALF_UP, Decimal

bug_spawn = False


def apply_discount(price: Decimal, percent: Decimal) -> Decimal:
    if price < 0:
        raise ValueError("price must be >= 0")
    if percent < 0 or percent > 100:
        raise ValueError("percent must be in [0, 100]")
    factor = (Decimal(100) - percent) / Decimal(100)
    # original
    # return (price * factor).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    if bug_spawn:
        return price * factor
    else:
        return (price * factor).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def total(lines: list[Decimal]) -> Decimal:
    return sum(lines, Decimal(0)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
