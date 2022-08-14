import pytest

from pages.home import FoxtelHomePage
from pages.videos import FoxtelVideoPage
from playwright.sync_api import expect, Page, Playwright


@pytest.mark.video
def test_launch_video(
    page: Page,
    home_page: FoxtelHomePage,
    video_page: FoxtelVideoPage) -> None:

    #### Scenario 1: #####

     
    # Given the Foxtel home page is displayed
    home_page.load()

    # Close popup if exists
    home_page.close_popup()

    # When video page is launched
    home_page.click_video_link()

    # When a video is player by the user
    video_page.launch_video()

    # Then ad is played at the start of the video
    video_page.play_ad()
    video_page.pause_video()
    


