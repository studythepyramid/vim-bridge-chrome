
# uv run python bridge.py
from playwright.sync_api import sync_playwright

def send_vim_buffer_to_chrome(text_to_paste: str):
    with sync_playwright() as p:
        # 1. Connect to your existing Chrome instance
        print("[+] Connecting to Chrome on port 9222...")
        browser = p.chromium.connect_over_cdp("http://localhost:9222")

        # 2. Grab the active tab
        default_context = browser.contexts[0]
        page = default_context.pages[0]
        print(f"[+] Active Tab: {page.title()}")

        # 3. Locate the input box and paste
        # (You will need to inspect the target website to get the right selector)
        chat_box = page.locator("textarea")
        chat_box.fill(text_to_paste)

        # 4. Hit Enter or click the send button
        chat_box.press("Enter")
        print("[+] Payload delivered.")

        browser.disconnect()


def mis():

    # A,
    """
    Scraping Tokens in the AI Age
When you say "scrape tokens," there are two massive use cases here that Playwright handles beautifully:

A. Scraping Auth Tokens (Cookies / LocalStorage)
If you want to use a CLI tool to talk to an AI API, but the API requires a web-login, you can use the bridge to steal your own browser's session tokens.
    """
    # Inside your Playwright script...
    # 1. Steal all cookies (Session IDs, JWTs)
    cookies = default_context.cookies()
    for cookie in cookies:
        if cookie['name'] == '__Secure-next-auth.session-token':
            print(f"Found Auth Token: {cookie['value']}")

    # 2. Steal LocalStorage (Many modern AI UIs store access tokens here)
    local_storage = page.evaluate("() => JSON.stringify(window.localStorage)")
    print(local_storage)


    ## 2
    """
B. Scraping Streamed Response Tokens (Text)
If the GFW makes an AI web UI unstable, you can use Playwright to watch the DOM network traffic and "scrape" the LLM response tokens as they stream in, writing them directly back to a Tmux pane or Neovim buffer.
    """
    # Wait for the AI's response paragraph to appear and grab the text
    response_locator = page.locator(".ai-response-container").last
    # Playwright automatically waits for the element to be stable!
    full_response = response_locator.inner_text()

    # Append it to the terminal log for double_chop to ingest later
    with open("/tmp/olddog.terminal.md", "a") as f:
        f.write(f"\n## AI_Response\n{full_response}\n")




if __name__ == "__main__":
    # In reality, you would read this from a temp file or stdin from Neovim
    send_vim_buffer_to_chrome("Hello from the Neovim bunker.")
