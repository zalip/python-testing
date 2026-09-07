from config import BASE


class UploadPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE}/upload"
        self.upload_file = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.uploaded_file = page.locator("#uploaded-files")

    def goto(self):
        self.page.goto(self.url)

    def upload(self, file_path):
        self.upload_file.set_input_files(file_path)
