import pytest

from pages.home import FoxtelHomePage
from pages.article import FoxtelArticlePage
from playwright.sync_api import expect, Page, Playwright


@pytest.mark.article
def test_launch_article(
    page: Page,
    home_page: FoxtelHomePage,
    article_page: FoxtelArticlePage) -> None:

    #### Scenario 1: #####

    # Given the Foxtel home page is displayed
    home_page.load()

    # Close popup if exists
    home_page.close_popup()
   
    # When hamburger menu is invoked
    article_page.click_hamburger_menu()

    # When navigated to sports submenu
    article_page.click_sports_submenu()

    # When navigated to football sports submenu
    article_page.click_football_submenu()

    # Then
    article_page.click_football_latest_news()
    article_page.click_news()
    

    


