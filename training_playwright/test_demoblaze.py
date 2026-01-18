

class TestDemoblaze:

    def test_demoblaze_correct_login(self, setup_playwright):
        print("into test_demoblaze_correct_login")
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")

        # user = page.locator("#user-name")
        # user.fill("standard_user")
        # password = page.locator("#password")
        # password.fill("secret_sauce")
        # login_btn = page.get_by_text("login")
        # login_btn.click()
        # current_url = page.url
        # assert current_url == "https://www.saucedemo.com/inventory.html", "current URL is not as expected"