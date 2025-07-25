from core.base_page import BasePage
from playwright.sync_api import Page, Locator

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_selector = 'input[name="username"]'
        self.password_selector = 'input[name="password"]'
        self.login_button_selector = 'button[type="submit"]'
        self.forgot_password_selector = '.oxd-text.oxd-text--p.orangehrm-login-forgot-header'
        self.error_message_selector = '.oxd-alert-content-text'
        self.required_field_selector = "//div[@class=\"orangehrm-login-slot-wrapper\"]//div[1]//div[1]//span[1]"

    def login(self, username: str, password: str):
        self.fill(self.username_selector, username)
        self.fill(self.password_selector, password)
        self.click(self.login_button_selector)

    def get_error_message(self) -> str:
        self.page.wait_for_timeout(1000)
        return self.get_text(self.error_message_selector)

    def get_required_field_message(self) -> str:
        self.page.wait_for_timeout(1000)
        return self.get_text(self.required_field_selector)

    def click_forgot_password(self):
        with self.page.expect_navigation():
            self.click(self.forgot_password_selector) 