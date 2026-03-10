from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:8000/safer-sex-complete-guide.html')
    page.wait_for_selector('h1')
    page.screenshot(path='screenshot_safer_sex.png', full_page=True)
    browser.close()