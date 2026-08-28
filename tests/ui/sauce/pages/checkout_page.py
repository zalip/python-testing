class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = self.page.locator('[data-test="firstName"]')
        self.last_name = self.page.locator('[data-test="lastName"]')
        self.postal_code = self.page.locator('[data-test="postalCode"]')
        self.continue_button = self.page.locator('[data-test="continue"]')
        self.title = self.page.locator('[data-test="title"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = self.page.locator('[data-test="complete-header"]')

    def fill_info(self, firstname, lastname, postal):
        self.first_name.fill(firstname)
        self.last_name.fill(lastname)
        self.postal_code.fill(postal)
        return self

    def click_continue(self):
        self.continue_button.click()
