import asyncio
import sys
from playwright.async_api import async_playwright

async def run():
    # 1. Grab text from stdin (piped from tmux/vim)
    input_text = sys.stdin.read().strip()
    if not input_text:
        print("No input text detected.")
        return

    try:
        # 2. Start Playwright and Connect to the Bunker's Chrome
        async with async_playwright() as p:
            # We access connect_over_cdp through p.chromium
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")

            # Most Chrome sessions have only one context
            context = browser.contexts[0]

            # 3. Find the Gemini Tab (using a more robust check)
            target_page = None
            for page in context.pages:
                if "gemini.google.com" in page.url:
                    target_page = page
                    break

            if not target_page:
                print("Error: Gemini tab not found in Chrome.")
                return

            # 4. Bring to front so you can see it happen
            await target_page.bring_to_front()

            # 5. Locate the input (Gemini uses a div with role='textbox')
            textbox = target_page.get_by_role("textbox")

            # 6. Clear and Paste
            # .fill() automatically focuses and clears the field
            await textbox.fill(input_text)

            print(f"Successfully pasted {len(input_text)} characters into Gemini.")
            print("Waiting for internet... Hit Enter in Chrome when ready.")

    except Exception as e:
        print(f"Bunker Error: {e}")

if __name__ == "__main__":
    asyncio.run(run())
