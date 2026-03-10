import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 2000})
        await page.goto("http://localhost:8000/sex-education-study-2026.html")

        # Wait for fonts to load
        await page.evaluate("document.fonts.ready")

        # Take a screenshot
        await page.screenshot(path="screenshot-desktop.png", full_page=True)

        # Also test blog index
        await page.goto("http://localhost:8000/blog/index.html")
        await page.evaluate("document.fonts.ready")
        await page.screenshot(path="screenshot-blog.png", full_page=False)

        await browser.close()

asyncio.run(run())
