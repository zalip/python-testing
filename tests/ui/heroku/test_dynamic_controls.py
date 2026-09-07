from pages.dynamic_controls import DynamicControlsPage
from playwright.sync_api import expect


def test_dynamic_controls(page):
    dynamic_controls_page = DynamicControlsPage(page)
    dynamic_controls_page.goto()

    # It's gone!/It's back!
    expect(dynamic_controls_page.checkbox).to_have_count(1)
    dynamic_controls_page.remove_button.click()
    expect(dynamic_controls_page.message).to_have_text("It's gone!")
    expect(dynamic_controls_page.checkbox).to_have_count(0)
    dynamic_controls_page.add_button.click()
    expect(dynamic_controls_page.message).to_have_text("It's back!")
    expect(dynamic_controls_page.checkbox).to_have_count(1)

    # It's enabled!/It's disabled!
    dynamic_controls_page.enable_button.click()
    expect(dynamic_controls_page.message).to_have_text("It's enabled!")
    dynamic_controls_page.disable_button.click()
    expect(dynamic_controls_page.message).to_have_text("It's disabled!")
