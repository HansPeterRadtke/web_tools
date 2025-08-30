from text_browser import TextBrowser

print("[DEBUG] Starting TextBrowser actions test...")

try:
    tb = TextBrowser(headless=True)

    tb.goto("https://practice.expandtesting.com/login")
    tb.dump()

    tb.fill("input[name='username']", "practice")
    tb.fill("input[name='password']", "SuperSecretPassword!")
    tb.click("button[type='submit']")

    tb.dump()

    tb.close()

except Exception as e:
    print(f"[FATAL] Test failed: {e}")

print("[DEBUG] Finished TextBrowser actions test.")