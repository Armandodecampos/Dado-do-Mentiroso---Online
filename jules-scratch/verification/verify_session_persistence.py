import asyncio
from playwright.async_api import async_playwright, expect
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context() # Use a context to preserve localStorage
        page = await context.new_page()

        file_path = "file://" + os.path.abspath("index.htm")
        await page.goto(file_path)

        # Simulate the UI change to the "logged-in" state
        await page.evaluate("""() => {
            localStorage.setItem('sb-oyeqychxfnyhthoygtob-auth-token', JSON.stringify({
                "access_token": "mock_token",
                "user": { "id": "mock_id", "email": "test@example.com" }
            }));
            document.getElementById('logged-in-app').classList.remove('hidden');
            document.getElementById('main-container').classList.add('hidden');
            document.body.classList.remove('bg-gray-100');
        }""")

        await page.wait_for_timeout(1000)

        # Verify the logged-in view is visible
        await expect(page.locator("#profile-button")).to_be_visible(timeout=10000)

        # Take a screenshot before reload
        await page.screenshot(path="jules-scratch/verification/before_reload.png")

        # Reload the page
        await page.reload()

        await page.wait_for_timeout(1000)

        # Verify that the logged-in view is still visible
        await expect(page.locator("#profile-button")).to_be_visible(timeout=10000)

        # Take a screenshot after reload
        await page.screenshot(path="jules-scratch/verification/after_reload.png")

        await browser.close()
        print("Script finished successfully.")

if __name__ == "__main__":
    asyncio.run(main())
