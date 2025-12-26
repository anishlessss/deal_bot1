from playwright.sync_api import sync_playwright
from config import HEADLESS

def open_page(url):
    p = sync_playwright().start()

    browser = p.chromium.launch(
        headless=HEADLESS,
        args=["--disable-blink-features=AutomationControlled"]
    )

    page = browser.new_page()
    page.goto(url, timeout=60000)
    page.wait_for_timeout(8000)

    return p, browser, page
