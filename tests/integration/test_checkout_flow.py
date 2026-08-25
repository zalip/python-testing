from decimal import Decimal

from shop.cart import Cart, CartItem
from shop.inventory import Inventory


def test_checkout_reserves_stock_and_totals():
    inv = Inventory()
    inv.set_stock("TEE", 10)

    cart = Cart(discount_percent=Decimal("0"))
    cart.add(CartItem("TEE", Decimal("25.00"), qty=3))
    inv.reserve("TEE", 3)

    assert cart.grand_total() == Decimal("75.00")
    assert inv.available("TEE") == 7