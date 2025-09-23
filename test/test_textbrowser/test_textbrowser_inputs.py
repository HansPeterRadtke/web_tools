import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from hpr.webtools.text_browser.core import TextBrowser

print("[DEBUG] Starting test_textbrowser_inputs...")

try:
    tb = TextBrowser(headless=True)

    tb.goto("https://practice.expandtesting.com/inputs")
    tb.dump()

    tb.fill("input[type='number']", "123")
    tb.fill("input[type='text']", "Hello")
    tb.fill("input[type='password']", "secretpass")
    tb.fill("input[type='date']", "2025-08-30")

    tb.dump()

    tb.close()

except Exception as e:
    print(f"[FATAL] Test failed: {e}")

print("[DEBUG] Finished test_textbrowser_inputs.")