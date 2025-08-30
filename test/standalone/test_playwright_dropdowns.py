from playwright.sync_api import sync_playwright

print("[DEBUG] Starting Playwright dropdowns test...")

try:
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page    = browser.new_page()

    print("[DEBUG] Navigating to dropdown page...")
    page.goto("https://practice.expandtesting.com/dropdown", wait_until="domcontentloaded")

    print("[RESULT] Initial page text:")
    print(page.inner_text("body")[:500])

    # Find all selects
    dropdowns = page.query_selector_all("select")
    print(f"[DEBUG] Found {len(dropdowns)} dropdowns.")

    for i, dd in enumerate(dropdowns):
        options = dd.query_selector_all("option")
        print(f"Dropdown {i} has {len(options)} options:")
        for j, opt in enumerate(options[:10]):  # only print first 10 for brevity
            val = opt.get_attribute("value")
            text= opt.inner_text()
            selected = opt.is_checked() if val else False
            print(f"  {j} | value={val} | text={text} | selected={selected}")

    # Try selecting values
    if dropdowns:
        print("[DEBUG] Selecting first option in first dropdown...")
        dropdowns[0].select_option(index=1)
        print("[DEBUG] Selected option index 1 in dropdown 0")

    if len(dropdowns) > 2:
        print("[DEBUG] Selecting Germany in country dropdown...")
        dropdowns[2].select_option(label="Germany")
        print("[DEBUG] Selected Germany in dropdown 2")

    page.wait_for_timeout(1000)

    browser.close()

except Exception as e:
  print(f"[FATAL] Playwright dropdowns test failed: {e}")

print("[DEBUG] Finished Playwright dropdowns test.")