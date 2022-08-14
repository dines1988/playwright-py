from playwright.sync_api import Page

class FoxtelHomePage:

    URL = 'https://www.foxsports.com.au/'

    def __init__(self, page: Page) -> None:
        self.page = page
        #self.pop_up = page.locator('button:has-text("No")')
        self.pop_up = page.locator('//button[contains(text(),"No")]')
        self.video_button = page.locator('//li/a[(contains(text(),"Video"))]')

    
    def load(self) -> None:
        try:
            self.page.goto(self.URL)
            self.page.wait_for_timeout(4000)
        except Exception:
            pass

    def close_popup(self) -> None:
        if self.pop_up.is_visible():
            self.pop_up.click()
        assert self.page.title() == 'FOX SPORTS | Live Sports Scores | NRL, AFL, Cricket Scores'
    
    def click_video_link(self) -> None:
        #self.page.on("dialog", lambda dialog: dialog.accept())
        self.video_button.wait_for()
        self.video_button.click()
        self.page.wait_for_load_state()
