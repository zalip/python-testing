from pages.dynamic_loading import DynamicLoadingPage
from playwright.sync_api import expect


def test_dynamic_loading(page):
    dynamic_loading_page = DynamicLoadingPage(page)
    dynamic_loading_page.goto_v2()

    dynamic_loading_page.start_button.click()

    # expect(dynamic_loading_page.loading_indicator).to_be_visible()
    # загрузка может быть слишком быстрой - начнет флакать
    expect(dynamic_loading_page.finish).to_be_visible()
    expect(dynamic_loading_page.finish).to_have_text("Hello World!")
