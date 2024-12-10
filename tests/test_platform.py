from playwright.sync_api import sync_playwright, expect
from pages.page_redamp import DefaultPage

# Viewport test on multiple devices
def test_devices():
    devices = [
        "iPhone 15",
        "Galaxy Note 3",
        "iPad Pro 11",
    ]

    with sync_playwright() as p:
        for device_name in devices:
            device = p.devices[device_name]
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(**device)
            page = context.new_page()

            test_page = DefaultPage(page)
            test_page.open_page("https://securitycheck-rc.redamp.eu")
            test_page.click_create_account()

            expect(page.get_by_role("button", name="Zpět na přihlášení")).to_be_visible()
            test_page.click_back()

            expect(page.locator("label.css-us5h9s")).to_be_visible()
            test_page.toggle_darkmode()

            context.close()
            browser.close()
