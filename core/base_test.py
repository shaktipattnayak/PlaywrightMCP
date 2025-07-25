import pytest
from playwright.sync_api import sync_playwright
import datetime

@pytest.fixture(scope="function", autouse=True)
def setup_page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        request.cls.page = page
        yield page
        context.close()
        browser.close()

class BaseTest:
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        rep = outcome.get_result()
        if rep.when == "call" and rep.failed:
            page = getattr(item.instance, 'page', None)
            if page:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                page.screenshot(path=f"screenshots/{item.name}_{timestamp}.png") 