from decimal import Decimal

import pytest

from shop.pricing import apply_discount

# apply_discount(price, percent) -> Decimal


@pytest.mark.parametrize(
    "price, percent, expected",
    [
        (Decimal("10.00"), Decimal("0.00"), Decimal("10.00")),
        (Decimal("10.00"), Decimal("100.00"), Decimal("0.00")),
        (Decimal("19.99"), Decimal("25.00"), Decimal("14.99")),
        (Decimal("100.00"), Decimal("10.00"), Decimal("90.00")),
        (Decimal("50.00"), Decimal("0.00"), Decimal("50.00")),
    ],
)
def test_apply_discount_cases(price, percent, expected):
    assert apply_discount(price, percent) == expected


@pytest.mark.parametrize(
    "price, percent",
    [
        (Decimal("-10.00"), Decimal("0.00")),
        (Decimal("-1.00"), Decimal("100.00")),
        (Decimal("-0.00001"), Decimal("100.00")),
    ],
)
def test_apply_discount_reject_bad_price(price, percent):
    with pytest.raises(ValueError, match="price"):
        apply_discount(price, percent)


@pytest.mark.parametrize(
    "price, percent",
    [
        (Decimal("10.00"), Decimal("-10.00")),
        (Decimal("0.00"), Decimal("-10.00")),
        (Decimal("1110.00"), Decimal("-1.00")),
        (Decimal("1110.00"), Decimal("100500.00")),
        (Decimal("1110.00"), Decimal("100.00001")),
    ],
)
def test_apply_discount_reject_bad_percent(price, percent):
    with pytest.raises(ValueError, match="percent"):
        apply_discount(price, percent)
