import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from text_browser.core import TextBrowser

print("[DEBUG] Starting test_textbrowser_dropdowns...")

try:
    tb = TextBrowser(headless=True)

    tb.goto("https://practice.expandtesting.com/dropdown")
    tb.dump()

    tb.select("select", "Option 1")
    tb.select("select[name='country']", "Germany")

    tb.dump()

    tb.close()

except Exception as e:
    print(f"[FATAL] Test failed: {e}")

print("[DEBUG] Finished test_textbrowser_dropdowns.")