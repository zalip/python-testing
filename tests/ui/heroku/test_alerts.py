from pages.alerts import AlertsPage
from playwright.sync_api import expect


def test_alert(page):
    alerts_page = AlertsPage(page)
    alerts_page.goto()

    page.once("dialog", lambda dialog: dialog.accept())
    alerts_page.js_alert_button.click()

    expect(alerts_page.result).to_have_text("You successfully clicked an alert")


def test_confirm_two_options(page):
    alerts_page = AlertsPage(page)
    alerts_page.goto()

    page.once("dialog", lambda dialog: dialog.accept())
    alerts_page.js_confirm_button.click()

    expect(alerts_page.result).to_have_text("You clicked: Ok")

    page.once("dialog", lambda dialog: dialog.dismiss())
    alerts_page.js_confirm_button.click()

    expect(alerts_page.result).to_have_text("You clicked: Cancel")


def test_prompt(page):
    alerts_page = AlertsPage(page)
    alerts_page.goto()

    page.once("dialog", lambda dialog: dialog.accept("test prompt"))
    # сразу слушатель диалога, иначе плейврайт все алерты отклоняет автоматически
    alerts_page.js_prompt_button.click()

    expect(alerts_page.result).to_have_text("You entered: test prompt")
