class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = self.page.locator(".cart_item")
        self.cart_item_name = self.page.locator(".inventory_item_name")
        self.checkout = self.page.locator('[data-test="checkout"]')
