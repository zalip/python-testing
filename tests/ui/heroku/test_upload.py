from pages.upload import UploadPage
from playwright.sync_api import expect


def test_upload(page):
    upload_page = UploadPage(page)
    upload_page.goto()

    upload_page.upload_file.set_input_files("tests/ui/heroku/test_upload.py")
    upload_page.upload_button.click()

    expect(upload_page.uploaded_file).to_have_text("test_upload.py")
