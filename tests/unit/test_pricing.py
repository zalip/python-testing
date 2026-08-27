from decimal import Decimal

import pytest

from shop.pricing import apply_discount, total

# apply_discount(price, percent) -> Decimal


def test_apply_discount_basic():
    # Arrange
    price = Decimal("100.00")
    percent = Decimal("10.00")

    # Act
    result = apply_discount(price, percent)

    # Assert
    assert result == Decimal("90.00")


def test_total_sums_lines():
    lines = [Decimal("10.50"), Decimal("1.25")]
    assert total(lines) == Decimal("11.75")


def test_total_empty():
    assert total([]) == Decimal("0.00")


def test_apply_discount_reject_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(Decimal(10), Decimal("101.00"))


def test_apply_discount_reject_bad_price():
    with pytest.raises(ValueError, match="price"):
        apply_discount(Decimal(-1), Decimal("100.00"))


def test_apply_discount_reject_negative_percent():
    with pytest.raises(ValueError):
        apply_discount(Decimal(10), Decimal(-10))


def test_apply_discount_reject_negative_percent_message():
    with pytest.raises(ValueError, match="percent must be in"):
        apply_discount(Decimal(10), Decimal("101.00"))


# regression
def test_apply_discount_half_up_on_odd_cent():
    """Regression: 19.99 @ 25% must be 14.99, not 14.9925 truncated."""
    assert apply_discount(Decimal("19.99"), Decimal("25.00")) == Decimal("14.99")
