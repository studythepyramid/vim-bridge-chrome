from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # The 'channel' argument tells Playwright to ignore its bundled browser
    # and use the system's actual Google Chrome, which already has its dependencies met!
    browser = p.chromium.launch(channel="chrome", headless=False)
    
    page = browser.new_page()
    page.goto("https://google.com")
    print(f"Success! Booted into: {page.title()}")
    
    browser.close()
