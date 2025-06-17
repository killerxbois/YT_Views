
import sys
import asyncio
from playwright.async_api import async_playwright
import random

link = sys.argv[1]
views = int(sys.argv[2])

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)..."
]

async def run(link, views):
    async with async_playwright() as p:
        for i in range(views):
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(user_agent=random.choice(user_agents))
            page = await context.new_page()
            await page.goto(link)
            await page.wait_for_timeout(15 * 60 * 1000)  # 15 minutes
            await browser.close()

asyncio.run(run(link, views))
