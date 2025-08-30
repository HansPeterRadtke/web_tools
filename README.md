# Web Tools

A **text-based headless browser** powered by Playwright.
It executes real JavaScript, interacts with DOM elements, and outputs only **plain text**.

## Features
- Full DOM discovery and interaction
- Supports links, buttons, inputs, textareas, radios, checkboxes, dropdowns
- Executes JavaScript (SPAs, AJAX, dynamic menus all work)
- Text-only I/O: no images, no video, no screenshots
- Usable both as CLI tool and as Python module

## Installation
```bash
pip install playwright
playwright install chromium
```

## Usage

### One-shot CLI mode (default)
Run a single command and exit.
```bash
python3 -m text_browser https://example.com
```
This will open the page, dump text + interactables, then exit.

### Interactive mode
Stay in the same browser session and issue multiple commands step by step.
```bash
python3 -m text_browser --interactive
```

You’ll enter a REPL prompt:
```
text_browser>
```
Use commands to interact with the live page. Type `quit`, `exit`, or `q` to leave.

## Command Reference

### Navigation
- `goto <url>` — navigate to a URL
- `wait <state>` — wait for load state (`load`, `domcontentloaded`, `networkidle`)
- `reload` — reload current page
- `url` — print current URL

### Discovery
- `dump` — dump all visible text + interactable elements with numeric IDs

### Interactions
- `click <target>` — click by numeric ID, CSS selector, or `text=...`
- `fill <target> <text>` — fill text input
- `press <target> <key>` — press a key (e.g. Enter)
- `select <target> <option>` — select dropdown option by text or value
- `check <target>` — check a checkbox
- `uncheck <target>` — uncheck a checkbox

### Reading
- `text <target>` — read visible text of element
- `attr <target> <name>` — read attribute value (e.g. href)

### State & Cookies
- `cookies` — list current cookies
- `setcookie <name> <value> <domain>` — set a cookie manually
- `savestate <path>` — save session (cookies, storage) to JSON file
- `loadstate <path>` — restore session from JSON file

### Settings
- `setua <ua_string>` — change user agent
- `viewport <w> <h>` — set viewport size

### Exit
- `quit`, `exit`, or `q` — exit interactive mode and close browser

## Examples
```bash
python3 -m text_browser --interactive

text_browser> goto https://finance.yahoo.com
text_browser> dump
text_browser> click 9
text_browser> wait load
text_browser> dump
text_browser> fill 479 AAPL
text_browser> press 479 Enter
text_browser> wait load
text_browser> dump
text_browser> cookies
text_browser> savestate session.json
text_browser> quit
```

## Module Usage (Python)
```python
from text_browser import TextBrowser

browser = TextBrowser()
browser.goto("https://example.com")
browser.dump()
browser.click("text=Login")
browser.fill(3, "user@example.com")
browser.press(3, "Enter")
browser.close()
```

## License
MIT