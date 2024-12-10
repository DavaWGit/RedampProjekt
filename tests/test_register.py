from playwright.sync_api import Page, expect
from pages.page_redamp import DefaultPage

# Try to get to the final registration site
def test_register(page: Page):
    test_page = DefaultPage(page)
    test_page.open_page("https://securitycheck-rc.redamp.eu")

    test_page.click_create_account()

    test_page.click_first_option()

    test_page.click_next_step()

    test_page.click_select_country()

    test_page.click_next_step()

    # final site opens in a new tab
    with page.context.expect_page() as new_tab:
        test_page.click_enter_site()
    
    new_page = new_tab.value
    assert new_page.url == "https://www.cdc.cz/cs/", "Couldn't navigate to the correct page"

    