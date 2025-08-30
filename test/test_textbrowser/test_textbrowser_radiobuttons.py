import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from text_browser.core import TextBrowser

print("[DEBUG] Starting test_textbrowser_radiobuttons...")

try:
    tb = TextBrowser(headless=True)

    tb.goto("https://practice.expandtesting.com/radio-buttons")
    tb.dump()

    tb.check("input[value='blue']")
    tb.check("input[value='tennis']")

    tb.dump()

    tb.close()

except Exception as e:
    print(f"[FATAL] Test failed: {e}")

print("[DEBUG] Finished test_textbrowser_radiobuttons.")