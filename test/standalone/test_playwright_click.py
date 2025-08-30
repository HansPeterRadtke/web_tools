from playwright.sync_api import sync_playwright

print("[DEBUG] Starting Playwright click test...")

try:
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page    = browser.new_page()
    print("[DEBUG] Navigating to example.com...")
    page.goto("https://example.com", wait_until="networkidle")

    # Click the link (id=0)
    print("[DEBUG] Clicking link with id=0...")
    page.click("a")
    page.wait_for_load_state("networkidle")

    # Dump new page content
    body_text = page.inner_text("body")
    print("[RESULT] New page text:")
    print(body_text[:1000])

    elements = page.query_selector_all("a, button, input, select, textarea")
    print("[RESULT] Interactable elements on new page:")
    for i, el in enumerate(elements):
      try:
        tag    = el.evaluate("el => el.tagName.toLowerCase()")
        role   = el.get_attribute("role") or ""
        typ    = el.get_attribute("type") or ""
        name   = el.get_attribute("name") or ""
        label  = el.get_attribute("aria-label") or ""
        text   = el.inner_text() or ""
        href   = el.get_attribute("href") or ""
        visible= el.is_visible()
        enabled= el.is_enabled()
        selector = el.evaluate("el => el.outerHTML.slice(0,80)+'...'" )

        print(f"{i} | tag={tag} | role={role} | type={typ} | name={name} | label={label} | text={text} | href={href} | visible={visible} | enabled={enabled} | selector={selector}")
      except Exception as e:
        print(f"[ERROR] Failed to process element {i}: {e}")

    browser.close()

except Exception as e:
  print(f"[FATAL] Playwright click test failed: {e}")

print("[DEBUG] Finished Playwright click test.")