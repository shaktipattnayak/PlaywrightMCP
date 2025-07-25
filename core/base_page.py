from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str, timeout: int = 5000):
        self.page.locator(selector).click(timeout=timeout)

    def fill(self, selector: str, value: str, timeout: int = 5000):
        self.page.locator(selector).fill(value, timeout=timeout)

    def wait_for_selector(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def get_text(self, selector: str, timeout: int = 5000) -> str:
        try:
            return self.page.locator(selector).inner_text(timeout=timeout)
        except Exception:
            return "" 