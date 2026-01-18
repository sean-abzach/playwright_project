

class Test_calculator:

    def test_interest_drop_down(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net")
        interest = page.locator("[href='/interest-calculator.html']").click()
        dropdown = page.locator("[id='compound']")
        dropdown.select_option("weekly")
        dropdown.select_option(index=4)
        radio = page.locator("[id='codditionat2']")
        radio.click()
        print ("test end")