from playwright.sync_api import sync_playwright

print("[DEBUG] Starting Playwright login test...")

try:
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page    = browser.new_page()

    print("[DEBUG] Navigating to practice login page...")
    page.goto("https://practice.expandtesting.com/login", wait_until="domcontentloaded")

    # Dump initial interactables
    elements = page.query_selector_all("a, button, input, select, textarea")
    print("[RESULT] Initial interactable elements:")
    for i, el in enumerate(elements):
      tag    = el.evaluate("el => el.tagName.toLowerCase()")
      text   = el.inner_text() or ""
      name   = el.get_attribute("name") or ""
      typ    = el.get_attribute("type") or ""
      href   = el.get_attribute("href") or ""
      visible= el.is_visible()
      enabled= el.is_enabled()
      print(f"{i} | tag={tag} | text={text} | name={name} | type={typ} | href={href} | visible={visible} | enabled={enabled}")

    # Fill in login form
    print("[DEBUG] Filling username and password...")
    page.fill("input[name='username']", "practice")
    page.fill("input[name='password']", "SuperSecretPassword!")

    print("[DEBUG] Submitting form...")
    page.click("button[type='submit']")
    page.wait_for_load_state("domcontentloaded")

    # Dump resulting page text and interactables
    print("[RESULT] Page text after login:")
    print(page.inner_text("body")[:1000])

    elements = page.query_selector_all("a, button, input, select, textarea")
    print("[RESULT] Interactable elements after login:")
    for i, el in enumerate(elements):
      tag    = el.evaluate("el => el.tagName.toLowerCase()")
      text   = el.inner_text() or ""
      name   = el.get_attribute("name") or ""
      typ    = el.get_attribute("type") or ""
      href   = el.get_attribute("href") or ""
      visible= el.is_visible()
      enabled= el.is_enabled()
      print(f"{i} | tag={tag} | text={text} | name={name} | type={typ} | href={href} | visible={visible} | enabled={enabled}")

    browser.close()

except Exception as e:
  print(f"[FATAL] Playwright login test failed: {e}")

print("[DEBUG] Finished Playwright login test.")