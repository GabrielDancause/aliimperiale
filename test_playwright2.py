import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Go to root and test the link directly
        await page.goto('http://localhost:8000/dating-app-analysis-2026.html')

        # Verify page load
        await page.wait_for_selector('h1')
        title = await page.title()

        print(f"Loaded page title: {title}")

        if "The Modern Dating App Landscape" in title:
            print("Successfully loaded the new article.")

            # test FAQ
            await page.wait_for_selector('text="Frequently Asked Questions"')
            print("FAQ section found.")

            # test Chart
            await page.wait_for_selector('table')
            print("Table found.")

            await page.screenshot(path="screenshot.png", full_page=True)
            print("Saved screenshot to screenshot.png")
        else:
            print("Failed to load article.")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
