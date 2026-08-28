class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = self.page.locator(".title")
        self.add_to_cart_backpack = self.page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.add_to_cart_tshirt_red = self.page.locator(
            "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']"
        )
        self.inventory_item_name = self.page.locator(".inventory_item_name")
        self.inventory_item_desc = self.page.locator(
            '[data-test="inventory-item-desc"]'
        )
        self.inventory_item_price = self.page.locator(
            '[data-test="inventory-item-price"]'
        )
        self.shopping_cart_link = self.page.locator("[data-test='shopping-cart-link']")

        def add_backpack(self):
            self.add_to_cart_backpack.click()

        def add_red_tshirt(self):
            self.add_to_cart_tshirt_red.click()
