from playwright.sync_api import sync_playwright

print("[DEBUG] Starting Playwright inputs test...")

try:
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page    = browser.new_page()

    print("[DEBUG] Navigating to inputs page...")
    page.goto("https://practice.expandtesting.com/inputs", wait_until="domcontentloaded")

    print("[RESULT] Initial page text:")
    print(page.inner_text("body")[:500])

    # Fill each input type
    print("[DEBUG] Filling number input...")
    page.fill("input[type='number']", "123")

    print("[DEBUG] Filling text input...")
    page.fill("input[type='text']", "Hello")

    print("[DEBUG] Filling password input...")
    page.fill("input[type='password']", "secretpass")

    print("[DEBUG] Filling date input...")
    page.fill("input[type='date']", "2025-08-30")

    # Click Display button (catch various possible selectors)
    print("[DEBUG] Clicking Display button...")
    try:
      page.click("button[type='submit']")
    except:
      try:
        page.click("input[value='Display']")
      except:
        page.click("button:has-text('Display')")

    page.wait_for_timeout(1000)

    print("[RESULT] Page text after Display:")
    print(page.inner_text("body")[:500])

    browser.close()

except Exception as e:
  print(f"[FATAL] Playwright inputs test failed: {e}")

print("[DEBUG] Finished Playwright inputs test.")