from config import BASE


class AlertsPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE}/javascript_alerts"
        self.js_alert_button = page.get_by_role("button", name="Click for JS Alert")
        self.js_confirm_button = page.get_by_role("button", name="Click for JS Confirm")
        self.js_prompt_button = page.get_by_role("button", name="Click for JS Prompt")
        self.result = page.locator("#result")

    def goto(self):
        self.page.goto(self.url)
