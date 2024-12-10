from playwright.sync_api import Page, expect
from pages.page_redamp import DefaultPage

# Wrong credentials error message
def test_form_validation(page: Page):
    test_page = DefaultPage(page)
    test_page.open_page("https://securitycheck-rc.redamp.eu")

    test_page.fill_login("tester@gmail.com", "password")

    test_page.click_signin_button()

    
    expect(test_page.get_signin_error()).to_be_visible()

    