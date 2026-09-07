from config import BASE


class DynamicLoadingPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE}/dynamic_loading/1"
        self.url_2 = f"{BASE}/dynamic_loading/2"
        self.start_button = page.locator("button:has-text('Start')")
        self.loading_indicator = page.locator("#loading")
        self.finish = page.locator("#finish")

    def goto(self):
        self.page.goto(self.url)

    def goto_v2(self):
        self.page.goto(self.url_2)
