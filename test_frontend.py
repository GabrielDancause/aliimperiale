from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000/sexual-health-tracker.html')
        page.click('text="Accept"') # close consent bar
        page.click('text="10"') # click on the 10th day
        page.wait_for_timeout(1000)

        # Select the modal section and screenshot it directly to make sure we see it
        modal = page.locator('#logging-section')
        modal.screenshot(path='screenshot_modal_only.png')
        browser.close()

run()
