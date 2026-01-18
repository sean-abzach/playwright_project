from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net/")
    bmi_button = page.get_by_role(role="button",name="BMI Calculator")

    bmi_button.click()
    search_button.click()
    # page.keyboard.press("Enter")
    print(page.title())