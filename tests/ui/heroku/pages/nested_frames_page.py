from config import BASE


class NestedFramesPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE}/nested_frames"
        self.frame_top = page.frame_locator("frame[name='frame-top']")
        self.frame_middle = self.frame_top.frame_locator("frame[name='frame-middle']")

    def goto(self):
        self.page.goto(self.url)
