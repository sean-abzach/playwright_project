

class FindStorePage:
    def __init__(self, page):
        self.page = page
        self.find_a_store_button = page.get_by_role("button", name="Find a Store")
        self.choose_preferred_store = page.get_by_text("Choose a preferred store to make shopping easier.")
        self.search_input = page.locator("[id='StoreLocator_search_query']")
        self.search_button = page.get_by_role("button", name="Search for Stores")
        self.store_items = page.locator("li.col")

    def accept_cookies_if_present(self):
        accept_button = self.page.get_by_role("button", name="Accept All Cookies")
        try:
            accept_button.click(timeout=3000)
        except Exception:
            pass

    def open_find_store_dropdown(self):
        self.find_a_store_button.click()

    def choose_preferred_store_option(self):
        self.choose_preferred_store.click()

    def enter_location(self, location):
        self.search_input.wait_for(state="visible")
        self.search_input.fill(location)

    def submit_search(self):
        self.search_input.press("Enter")

    def wait_for_store_results(self):
        self.store_items.first.wait_for(state="visible", timeout=20000)