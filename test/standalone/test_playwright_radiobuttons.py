from playwright.sync_api import sync_playwright

print("[DEBUG] Starting Playwright radio buttons test...")

try:
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page    = browser.new_page()

    print("[DEBUG] Navigating to radio buttons page...")
    page.goto("https://practice.expandtesting.com/radio-buttons", wait_until="domcontentloaded")

    print("[RESULT] Initial page text:")
    print(page.inner_text("body")[:500])

    # Find radio buttons
    radios = page.query_selector_all("input[type='radio']")
    print(f"[DEBUG] Found {len(radios)} radio buttons.")

    for i, rb in enumerate(radios):
        value = rb.get_attribute("value")
        name  = rb.get_attribute("name")
        checked = rb.is_checked()
        print(f"Before: {i} | name={name} | value={value} | checked={checked}")

    # Click the first and last radio button
    if radios:
        print("[DEBUG] Clicking first radio button...")
        radios[0].check()
        print(f"After: 0 | checked={radios[0].is_checked()}")

    if len(radios) > 1:
        print("[DEBUG] Clicking last radio button...")
        radios[-1].check()
        print(f"After: {len(radios)-1} | checked={radios[-1].is_checked()}")

    page.wait_for_timeout(1000)

    # Print all states again
    for i, rb in enumerate(radios):
        value = rb.get_attribute("value")
        name  = rb.get_attribute("name")
        checked = rb.is_checked()
        print(f"Final: {i} | name={name} | value={value} | checked={checked}")

    browser.close()

except Exception as e:
  print(f"[FATAL] Playwright radio buttons test failed: {e}")

print("[DEBUG] Finished Playwright radio buttons test.")