from playwright.sync_api import Page, BrowserContext
from typing import List
import traceback


class FoxtelArticlePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.hamburger_menu = '//div[@class="fsui-normalise fnhm"]'
        self.sports_submenu = '//label[contains(text(),"Sports")]'
        self.football_spsubmenu = '//div[@class="fnhmbrl"]//span[contains(text(),"Football")]/ancestor::li[@class="fnhmbsi"]//label'
        self.latest_news ='//a[contains(@href,"/football/latest-news")]/span'
        self.news_page_header = '//h1[contains(text(),"LATEST FOOTBALL NEWS")]'
        self.news_link ='//div[@class="article-snippet__heading-group"]//a'
        self.news_page_title = '//h1'
        self.news_page_desc = '//h1/following-sibling::div[3]'
        self.news_page_heroimg = '//div[@id="primary-video-start-screen"]//amp-img/img'
            
    def click_hamburger_menu(self) -> None:

        assert self.page.locator(self.hamburger_menu).is_enabled()
        self.page.locator(self.hamburger_menu).click()

    def click_sports_submenu(self) -> None:

        assert self.page.locator(self.sports_submenu).is_visible()
        self.page.locator(self.sports_submenu).click()
    
    def click_football_submenu(self) -> None:

        assert self.page.locator(self.football_spsubmenu).is_visible()
        self.page.locator(self.football_spsubmenu).click()
        #self.page.wait_for_timeout(5000)

    def click_football_latest_news(self) -> None:
        
        assert self.page.locator(self.latest_news).is_visible()
        self.page.locator(self.latest_news).click()
        #self.page.wait_for_timeout(15000) 
        self.page.locator(self.news_page_header).wait_for(state="visible")
        assert self.page.locator(self.news_page_header).is_visible()
    
    def click_news(self) -> None:
        self.page.locator(self.news_link).first.click()
        self.page.wait_for_timeout(5000)
        self.page.locator(self.news_page_title).wait_for()
        assert self.page.locator(self.news_page_title).is_visible()
        self.page.locator(self.news_page_heroimg).wait_for()
        assert self.page.locator(self.news_page_heroimg).is_visible()
        self.page.locator(self.news_page_desc).wait_for()
        assert self.page.locator(self.news_page_desc).is_visible()
        self.page.wait_for_timeout(3000)


    
