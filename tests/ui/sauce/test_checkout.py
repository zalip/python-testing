from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_items_to_cart_and_checkout(page):
    checkout_page = CheckoutPage(page)
    cart_page = CartPage(page)
    inventory_page = InventoryPage(page)
    login_page = LoginPage(page)
    login_page.goto().login_standart()

    inventory_page.add_to_cart_backpack.click()
    inventory_page.add_to_cart_tshirt_red.click()

    inventory_page.shopping_cart_link.click()

    assert cart_page.cart_items.count() == 2
    assert cart_page.cart_item_name.filter(has_text="Sauce Labs Backpack").count() == 1
    assert cart_page.cart_item_name.filter(has_text="T-Shirt (Red)").count() == 1

    cart_page.checkout.click()

    checkout_page.fill_info("Jurra", "Qqwrd", "220025").click_continue()

    assert checkout_page.title.inner_text() == "Checkout: Overview"

    checkout_page.finish_button.click()
    assert checkout_page.complete_header.inner_text() == "Thank you for your order!"
