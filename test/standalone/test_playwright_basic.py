from playwright.sync_api import sync_playwright

print("[DEBUG] Starting basic Playwright test...")

try:
  with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
      try:
        print(f"[DEBUG] Launching {browser_type.name}...")
        browser = browser_type.launch(headless=True)
        page = browser.new_page()
        user_agent = page.evaluate("() => navigator.userAgent")
        print(f"[RESULT] {browser_type.name} user-agent: {user_agent}")
        browser.close()
      except Exception as e:
        print(f"[ERROR] Failed on {browser_type.name}: {e}")
except Exception as e:
  print(f"[FATAL] Playwright test failed: {e}")

print("[DEBUG] Finished basic Playwright test.")