from training_playwright.foot_locker_uk_project.pages.find_a_store_page import FindStorePage


class TestFindAStore:
    def test_search_store_in_london(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.footlocker.co.uk/", wait_until="domcontentloaded")

        store_page = FindStorePage(page)
        store_page.accept_cookies_if_present()

        store_page.open_find_store_dropdown()
        store_page.choose_preferred_store_option()
        store_page.enter_location("London")
        store_page.submit_search()
        store_page.wait_for_store_results()