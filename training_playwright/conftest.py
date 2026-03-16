

class SearchProductPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("[id='HeaderSearch--desktop_search_query']")

    def search_product(self,text):
        self.search_input.click()
        self.search_input.fill(text)
        self.search_input.press("Enter")