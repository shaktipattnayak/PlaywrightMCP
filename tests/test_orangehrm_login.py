import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datetime
from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from config import ORANGEHRM_URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
from core.base_test import BaseTest
import csv

load_dotenv()

def load_login_test_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_users.csv')
    with open(data_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['username'], row['password'], row['expected']) for row in reader]

class TestLogin(BaseTest):
    def setup_method(self, method):
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=False)
        self._context = self._browser.new_context()
        self.page = self._context.new_page()
        self.login_page = LoginPage(self.page)
        self.page.goto(ORANGEHRM_URL)

    def teardown_method(self, method):
        self._context.close()
        self._browser.close()
        self._playwright.stop()

    @pytest.mark.mcp
    def test_login_success(self):
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        print('URL after login:', self.page.url)
        self.page.wait_for_selector('.oxd-topbar-header-title', timeout=10000)
        assert "dashboard" in self.page.url.lower()

    @pytest.mark.mcp
    @pytest.mark.parametrize("username, password, expected_error", load_login_test_data())
    def test_login_from_csv(self, username, password, expected_error):
        self.login_page.login(username, password)
        actual_error = self.login_page.get_error_message().strip()
        required_field = self.login_page.get_required_field_message().strip()
        assert expected_error.strip() in actual_error or expected_error.strip() in required_field

    @pytest.mark.mcp
    def test_login_empty_fields(self):
        self.login_page.login("", "")
        assert "Required" in self.login_page.get_required_field_message()

    @pytest.mark.mcp
    def test_forgot_password_link(self):
        self.login_page.click_forgot_password()
        assert "requestPasswordResetCode" in self.page.url 