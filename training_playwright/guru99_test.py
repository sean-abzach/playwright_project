from playwright.sync_api import sync_playwright

with (((sync_playwright() as playwright))):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/#google_vignette")
    user = page.locator("[name='userName']")
    user.fill("Tutorial")
    password = page.locator("[name='password']")
    password.type("tutorial")
    submit_button= page.locator("[name='submit']")
    submit_button.click()
    current_url= page.url
    page.close()
    browser.close()
    print("### Test end ###")