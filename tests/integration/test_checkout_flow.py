from decimal import Decimal

import pytest

from shop import payment
from shop.cart import Cart, CartItem
from shop.inventory import Inventory


class FakeGateway:
    def charge(self, amount, currency="USD"):
        return {"ok": True, "id": "pay_1"}


class FakeFailGateway:
    def charge(self, amount, currency="USD"):
        return {"ok": False}


@pytest.mark.integration
def test_checkout_reserves_stock_and_totals():
    inv = Inventory()
    inv.set_stock("TEE", 10)

    cart = Cart(discount_percent=Decimal(0))
    cart.add(CartItem("TEE", Decimal("25.00"), qty=3))
    inv.reserve("TEE", 3)

    assert cart.grand_total() == Decimal("75.00") and inv.available("TEE") == 7


@pytest.mark.integration
def test_checkout_reserve_payment_seccess():
    inv = Inventory()
    inv.set_stock("BREAD", 15)

    cart = Cart()
    cart.add(CartItem("BREAD", Decimal("1.00"), qty=Decimal("5.00")))
    grand_total = cart.grand_total()

    inv.reserve("BREAD", 5)

    fake_gateway = FakeGateway()
    pay_id = payment.pay_order(grand_total, fake_gateway)

    assert (
        inv.available("BREAD") == 10
        and grand_total == Decimal("5.00")
        and pay_id == "pay_1"
    )


@pytest.mark.integration
def test_checkout_reserve_payment_failure_no_restock():
    inv = Inventory()
    inv.set_stock("BREAD", 15)

    cart = Cart()
    cart.add(CartItem("BREAD", Decimal("1.00"), qty=Decimal("5.00")))
    grand_total = cart.grand_total()

    inv.reserve("BREAD", 5)
    assert inv.available("BREAD") == 10

    fake_gateway = FakeFailGateway()
    with pytest.raises(RuntimeError):
        payment.pay_order(grand_total, fake_gateway)

    assert inv.available("BREAD") == 10
