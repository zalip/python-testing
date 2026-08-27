from decimal import Decimal

import pytest

from shop.cart import Cart, CartItem
from shop.inventory import Inventory, OutOfStockError


@pytest.fixture
def inventory():
    return Inventory()


@pytest.fixture
def inventory_with_stock(inventory):
    inventory.set_stock("SKU1", 5)
    return inventory


@pytest.fixture
def cart():
    return Cart()


@pytest.fixture
def cart_with_item(cart):
    cart.add(CartItem(sku="SKU1", price=Decimal("10.00"), qty=1))
    return cart


@pytest.fixture
def cart_with_discount():
    cart = Cart(discount_percent=Decimal("10.00"))
    cart.add(CartItem(sku="SKU1", price=Decimal("10.00"), qty=1))
    return cart


def test_reserve_ok(inventory_with_stock):
    inventory_with_stock.reserve("SKU1", 1)
    assert inventory_with_stock.available("SKU1") == 4


def test_reserve_out_of_stock(inventory_with_stock):
    inventory_with_stock.set_stock("SKU2", 1)
    with pytest.raises(OutOfStockError):
        inventory_with_stock.reserve("SKU2", 2)


def test_cart_grand_total(cart_with_item):
    assert cart_with_item.grand_total() == Decimal("10.00")
    cart_with_item.add(CartItem(sku="SKU1", price=Decimal("10.00"), qty=8))
    assert cart_with_item.grand_total() == Decimal("90.00")


def test_cart_grand_total_discount(cart_with_discount):
    assert cart_with_discount.grand_total() == Decimal("9.00")
    cart_with_discount.add(CartItem(sku="SKU1", price=Decimal("10.00"), qty=8))
    assert cart_with_discount.grand_total() == Decimal("81.00")


def test_cart_grand_total_aaa(cart):
    cart.add(CartItem("SKU2", Decimal("10.00"), Decimal("1.00")))

    total = cart.grand_total()

    assert total == Decimal("10.00")


def test_cart_grand_total_with_10_percent_discount_aaa(cart):
    cart.discount_percent = 10
    cart.add(CartItem("SKU1", price=Decimal("10.00"), qty=Decimal("1.00")))

    total = cart.grand_total()

    assert total == Decimal("9.00")
