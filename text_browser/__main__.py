import argparse
import sys
from .core import TextBrowser

def main():
    parser = argparse.ArgumentParser(description="Text-based headless browser interface")
    parser.add_argument("url", nargs="?", help="Initial URL to open")
    parser.add_argument("--headless", action="store_true", default=True, help="Run browser in headless mode")
    args = parser.parse_args()

    print("[DEBUG] Starting text_browser module...")

    tb = TextBrowser(headless=args.headless)
    if args.url:
        tb.goto(args.url)
        tb.dump()

if __name__ == "__main__":
    main()