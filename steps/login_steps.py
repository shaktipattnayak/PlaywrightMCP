from pytest_bdd import scenarios, given, when, then, parsers
from config import ORANGEHRM_URL
from pages.login_page import LoginPage
import pytest

scenarios('../features/login.feature')

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@given('I am on the login page')
def go_to_login_page(page):
    page.goto(ORANGEHRM_URL)

@when(parsers.parse('I fill "{field}" with "{value}"'))
def fill_field(page, field, value):
    selector = f'input[name="{field}"]'
    page.fill(selector, value)

@when(parsers.parse('I click "{button}"'))
def click_button(page, button):
    page.click(f'button:has-text("{button}")')

@then(parsers.parse('I should see "{text}"'))
def should_see_text(page, text):
    assert text.lower() in page.content().lower() 