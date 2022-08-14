from playwright.sync_api import Page, BrowserContext
from typing import List


class FoxtelVideoPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.video_link = '//div[@aria-label ="video thumbnail row"][1]/div/div[2]'
        self.play_button = '//button[contains(@class,"StartScreenWrapper")]'
        self.pause_button = '//div[contains(@class,"PlayAndPauseOverlay")]'
        self.ad_link = '//span[contains(@class,"Timer")]'
    
    def launch_video(self) -> None:

        with self.page.expect_popup() as popup_info:
            self.page.locator(self.video_link).click()
        self.page1 = popup_info.value
        print(self.page1.title())
        self.page1.locator(self.play_button).click()
    
    def play_ad(self) -> None:
       
        self.page1.locator(self.ad_link).wait_for()
        assert self.page1.locator(self.ad_link).is_visible()
        #self.page.wait_for_timeout(18000)
    
    def pause_video(self) -> None:
        self.page1.locator(self.ad_link).wait_for(state="hidden")
        self.page1.wait_for_timeout(3000)
        self.page1.locator(self.pause_button).wait_for()
        self.page1.locator(self.pause_button).click()
        #self.page1.wait_for_timeout(5000)