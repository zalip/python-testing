from config import BASE, PASSWORD, USER_LOCKED_OUT, USER_STANDARD


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = self.page.locator("[data-test='username']")
        self.password = self.page.locator("[data-test='password']")
        self.login_button = self.page.locator("[data-test='login-button']")
        self.error_message = self.page.locator('[data-test="error"]')

    def goto(self):
        self.page.goto(BASE)
        return self

    def login(self, user, password):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

    def login_standart(self):
        self.login(USER_STANDARD, PASSWORD)

    def login_locked_out(self):
        self.login(USER_LOCKED_OUT, PASSWORD)
