from decimal import Decimal

import pytest

from shop.cart import Cart, CartItem


def test_cart_grand_total_with_discount():
    cart = Cart(discount_percent=Decimal(10))
    cart.add(CartItem("A", Decimal("50.00"), qty=2))
    assert cart.grand_total() == Decimal("90.00")


def test_cart_item_rejects_zero_qty():
    with pytest.raises(ValueError):
        CartItem("A", Decimal("1.00"), qty=0)


def test_cart_item_rejects_negative_qty():
    with pytest.raises(ValueError):
        CartItem("A", Decimal("1.00"), qty=-1)


def test_cart_item_rejects_negative_price():
    with pytest.raises(ValueError):
        CartItem("A", Decimal("-1.00"), qty=1)
