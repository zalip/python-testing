from pages.nested_frames_page import NestedFramesPage
from playwright.sync_api import expect


def test_nested_frames(page):
    nested_frames_page = NestedFramesPage(page)
    nested_frames_page.goto()

    expect(nested_frames_page.frame_middle.locator("body")).to_have_text("MIDDLE")
