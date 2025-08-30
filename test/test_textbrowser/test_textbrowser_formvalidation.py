import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from text_browser.core import TextBrowser

print("[DEBUG] Starting test_textbrowser_formvalidation...")

try:
    tb = TextBrowser(headless=True)

    tb.goto("https://practice.expandtesting.com/form-validation")
    tb.dump()

    # Empty submit
    tb.click("button[type='submit']")
    tb.dump()

    # Partial form (only name)
    tb.fill("input[name='ContactName']", "Test User")
    tb.click("button[type='submit']")
    tb.dump()

    # Full form with placeholder phone number format (012-3456789)
    tb.fill("input[name='ContactName']", "Test User")
    tb.fill("input[name='contactnumber']", "012-3456789")
    tb.fill("input[name='pickupdate']", "2025-08-30")
    tb.select("select[name='payment']", "cash on delivery")
    tb.click("button[type='submit']")
    tb.dump()

    tb.close()

except Exception as e:
    print(f"[FATAL] Test failed: {e}")

print("[DEBUG] Finished test_textbrowser_formvalidation.")