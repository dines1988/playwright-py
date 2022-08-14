"""
This module contains shared fixtures.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import os
import pytest

from pages.home import FoxtelHomePage
from pages.videos import FoxtelVideoPage
from pages.article import FoxtelArticlePage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator
import sys
import asyncio


@pytest.fixture
def video_page(page: Page) -> FoxtelVideoPage:
    return FoxtelVideoPage(page)


@pytest.fixture
def home_page(page: Page) -> FoxtelHomePage:
    return FoxtelHomePage(page)


@pytest.fixture
def article_page(page: Page) -> FoxtelArticlePage:
    return FoxtelArticlePage(page)

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     screen_file = ''
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         if report.failed and "page" in item.funcargs:
#             page = item.funcargs["page"]
#             screenshot_dir = Path("screenshots")
#             screenshot_dir.mkdir(exist_ok=True)
#             screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
#             page.screenshot(path=screen_file)
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # add the screenshots to the html report
#             extra.append(pytest_html.extras.png(screen_file))
#         report.extra = extra