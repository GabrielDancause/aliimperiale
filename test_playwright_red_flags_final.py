import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 1024})

        # Load the page
        await page.goto("http://localhost:8000/relationship-red-flags.html")
        await page.wait_for_load_state("networkidle")

        # Set some slider values to get a red/yellow state
        await page.evaluate("""
            const sliders = document.querySelectorAll('input[type="range"]');
            sliders.forEach((slider, i) => {
                if (i >= 0 && i < 50) {
                    slider.value = 85;
                    slider.dispatchEvent(new Event('input', { bubbles: true }));
                }
            });
        """)

        # Click the submit button using its ID
        await page.click('#calculate-btn')

        # Wait for the results to appear
        await page.wait_for_selector("#results-section", state="visible")

        # Scroll to results
        await page.evaluate("document.getElementById('results-section').scrollIntoView()")

        # Give it a tiny bit of time to settle the scroll
        await page.wait_for_timeout(500)

        # Take screenshot
        await page.screenshot(path="screenshot_red_flags_results.png", full_page=True)
        print("Captured screenshot_red_flags_results.png")

        await browser.close()

asyncio.run(main())
