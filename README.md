# Web Tools

A text-based headless browser powered by Playwright.

## Features
- Full DOM discovery and interaction
- Text-only output (no images, no video)
- Supports links, buttons, inputs, textareas, radios, checkboxes, dropdowns
- Executes JavaScript just like a real browser
- Usable via CLI or as a Python module

## Structure
```
text_browser/       # Main module
  ├── __init__.py
  ├── __main__.py   # CLI entry
  └── core.py       # TextBrowser class

test/
  ├── standalone/   # Direct Playwright tests
  └── test_textbrowser/ # Tests using TextBrowser module
```

## Usage
### CLI
```bash
python3 -m text_browser https://example.com
```

### Python
```python
from text_browser import TextBrowser

browser = TextBrowser()
browser.goto("https://example.com")
browser.dump()
browser.close()
```

## License
MIT