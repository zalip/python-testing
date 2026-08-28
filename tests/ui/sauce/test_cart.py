from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_cart_and_check_info(page):
    cart_page = CartPage(page)
    inventory_page = InventoryPage(page)
    login_page = LoginPage(page)
    login_page.goto().login_standart()

    assert inventory_page.title.inner_text() == "Products"

    inventory_page.add_to_cart_backpack.click()

    inventory_page.inventory_item_name.filter(has_text="Sauce Labs Onesie").click()

    assert (
        "Rib snap infant onesie for the junior automation engineer"
        in inventory_page.inventory_item_desc.inner_text()
    )
    assert "7.99" in inventory_page.inventory_item_price.inner_text()

    inventory_page.shopping_cart_link.click()

    assert cart_page.cart_items.count() == 1
    assert "Sauce Labs Backpack" in cart_page.cart_item_name.inner_text()
