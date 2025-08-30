import os
import sys

# Ensure project root is in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from text_browser.core import TextBrowser

print("[DEBUG] Starting test_textbrowser_login_fail...")

try:
    tb = TextBrowser(headless=True)

    tb.goto("https://practice.expandtesting.com/login")
    tb.dump()

    tb.fill("input[name='username']", "wronguser")
    tb.fill("input[name='password']", "wrongpass")
    tb.click("button[type='submit']")

    tb.dump()

    tb.close()

except Exception as e:
    print(f"[FATAL] Test failed: {e}")

print("[DEBUG] Finished test_textbrowser_login_fail.")