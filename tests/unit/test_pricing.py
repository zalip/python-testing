from decimal import Decimal

import pytest

from shop.pricing import apply_discount, total


def test_apply_discount_basic():
    assert apply_discount(Decimal("100.00"), Decimal("10")) == Decimal("90.00")


@pytest.mark.parametrize(
    "price,percent,expected",
    [
        (Decimal("10.00"), Decimal("0"), Decimal("10.00")),
        (Decimal("10.00"), Decimal("100"), Decimal("0.00")),
        (Decimal("19.99"), Decimal("25"), Decimal("14.99")),
    ],
)
def test_apply_discount_cases(price, percent, expected):
    assert apply_discount(price, percent) == expected


def test_apply_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(Decimal("10"), Decimal("101"))


def test_total_empty():
    assert total([]) == Decimal("0.00")