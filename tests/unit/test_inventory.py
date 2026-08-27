import pytest

from shop.inventory import Inventory, OutOfStockError


def test_reserve_ok():
    inv = Inventory()
    inv.set_stock("SKU1", 5)

    inv.reserve("SKU1", 2)

    assert inv.available("SKU1") == 3


def test_reserve_out_of_stock():
    inv = Inventory()
    inv.set_stock("SKU1", 1)

    with pytest.raises(OutOfStockError):
        inv.reserve("SKU1", 2)


def test_stock_bad_qty():
    inv = Inventory()

    with pytest.raises(ValueError):
        inv.set_stock("SKU1", -1)


def test_reserve_bad_qty():
    inv = Inventory()
    inv.set_stock("SKU1", 1)

    with pytest.raises(ValueError):
        inv.reserve("SKU1", 0)

    with pytest.raises(ValueError):
        inv.reserve("SKU1", -1)
