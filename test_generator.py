from playwright.sync_api import sync_playwright

def test_generator():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000/relationship-boundaries-generator.html')

        # Verify title
        assert "Relationship Boundaries Generator" in page.title()

        # Select "Open / Polyamorous"
        page.click('button[data-style="open"]')

        # Take a screenshot before generating
        page.screenshot(path="screenshot_before_generate.png")

        # Generate boundaries
        page.click('button:has-text("Generate My Boundaries")')

        # Wait for results to be visible
        page.wait_for_selector('#results-screen', state='visible')

        # Verify text in results
        assert page.locator('#results-screen').is_visible()

        # Take a screenshot after generating
        page.screenshot(path="screenshot_after_generate.png")

        print("Tests passed successfully.")
        browser.close()

if __name__ == '__main__':
    test_generator()