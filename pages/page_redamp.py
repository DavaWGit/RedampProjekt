from playwright.sync_api import Page

# Test class for filling out login form
class DefaultPage:
    def __init__(self, page: Page):
        self.page = page
    
    def open_page(self, url: str):
        self.page.goto(url)

    def fill_login(self, email: str, password: str):
        self.page.get_by_label("email").fill(email)
        self.page.locator("input[name='password']").fill(password)
    
    def click_signin_button(self):
        self.page.get_by_role("button", name="PŘIHLÁSIT").click()

    def get_signin_error(self):
        return self.page.locator("div[data-test='signin-error']")

    def click_create_account(self):
        self.page.get_by_role("button", name="VYTVOŘIT ÚČET").click()

    def click_back(self):
        self.page.get_by_role("button", name="Zpět na přihlášení").click()

    def toggle_darkmode(self):
        self.page.locator("label.css-us5h9s").click()