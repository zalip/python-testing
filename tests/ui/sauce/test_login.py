from pages.login_page import LoginPage


def test_locked_user(page):

    login_page = LoginPage(page)

    login_page.goto()
    login_page.login_locked_out()

    assert (
        login_page.error_message.inner_text()
        == "Epic sadface: Sorry, this user has been locked out."
    )
