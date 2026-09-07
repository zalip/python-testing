from config import BASE


class DynamicControlsPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE}/dynamic_controls"
        self.message = page.locator("#message")
        self.checkbox = page.locator("#checkbox")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.add_button = page.get_by_role("button", name="Add")
        self.enable_button = page.get_by_role("button", name="Enable")
        self.disable_button = page.get_by_role("button", name="Disable")

    def goto(self):
        self.page.goto(self.url)
