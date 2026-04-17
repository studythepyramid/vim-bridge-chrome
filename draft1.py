import asyncio
from playwright.async_api import connect_over_cdp

async def send_to_gemini(text):
    # Connect to your already-open Chrome
    browser = await connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]

    # 1. Choose the Tab (find the one with Gemini)
    page = next(p for p in context.pages if "gemini.google.com" in p.url)
    await page.bring_to_front()

    # 2. Find the input field (Gemini uses a contenteditable div)
    input_selector = "div[contenteditable='true']"

    # 3. Clear and Paste
    await page.focus(input_selector)
    # Clear by selecting all and deleting
    await page.keyboard.press("Control+A")
    await page.keyboard.press("Backspace")
    await page.keyboard.type(text)

    # 4. Stay and wait for Enter (manual or scripted)
    # To auto-hit enter: await page.keyboard.press("Enter")
    print("Content pasted into Gemini. Waiting for your signal...")

# Trigger this from a tmux buffer or clipboard
