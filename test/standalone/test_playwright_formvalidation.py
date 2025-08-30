from playwright.sync_api import sync_playwright

print("[DEBUG] Starting Playwright form validation test...")

try:
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page    = browser.new_page()

    print("[DEBUG] Navigating to form validation page...")
    page.goto("https://practice.expandtesting.com/form-validation", wait_until="domcontentloaded")

    print("[RESULT] Initial page text:")
    print(page.inner_text("body")[:500])

    # Click submit without filling anything
    print("[DEBUG] Submitting empty form...")
    page.click("button[type='submit']")
    page.wait_for_timeout(1000)

    print("[RESULT] Page text after submitting empty form:")
    print(page.inner_text("body")[:500])

    # Fill partial form (only Contact Name)
    print("[DEBUG] Filling only Contact Name...")
    page.fill("#validationCustom01", "Test User")
    page.click("button[type='submit']")
    page.wait_for_timeout(1000)

    print("[RESULT] Page text after submitting partial form:")
    print(page.inner_text("body")[:500])

    # Fill full form with valid data
    print("[DEBUG] Filling complete form...")
    page.fill("#validationCustom01", "Test User")
    page.fill("#validationCustom02", "1234567890")
    page.fill("#validationCustomUsername", "pickup-username")
    page.fill("#validationCustom03", "2025-08-30")
    page.select_option("#validationCustom04", label="cash on delivery")
    page.click("button[type='submit']")
    page.wait_for_timeout(1000)

    print("[RESULT] Page text after valid form submission:")
    print(page.inner_text("body")[:500])

    browser.close()

except Exception as e:
  print(f"[FATAL] Playwright form validation test failed: {e}")

print("[DEBUG] Finished Playwright form validation test.")