from playwright.sync_api import sync_playwright

class TextBrowser:
    def __init__(self, headless: bool = True):
        print("[DEBUG] Initializing TextBrowser...")
        self.headless = headless
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.page = self.browser.new_page()

    def goto(self, url: str):
        print(f"[DEBUG] Navigating to {url}...")
        try:
            self.page.goto(url, wait_until="domcontentloaded")
            print(f"[DEBUG] Navigation complete: {self.page.url}")
        except Exception as e:
            print(f"[ERROR] Failed to navigate to {url}: {e}")

    def dump(self):
        print("[DEBUG] Dumping page text and interactable elements...")
        try:
            body_text = self.page.inner_text("body")
            print("[TEXT CONTENT]")
            print(body_text[:2000])  # limit for now

            elements = self.page.query_selector_all("a, button, input, select, textarea")
            print("[INTERACTABLE ELEMENTS]")
            for i, el in enumerate(elements):
                tag    = el.evaluate("el => el.tagName.toLowerCase()")
                text   = el.inner_text() or ""
                name   = el.get_attribute("name") or ""
                typ    = el.get_attribute("type") or ""
                href   = el.get_attribute("href") or ""
                visible= el.is_visible()
                enabled= el.is_enabled()
                print(f"{i} | tag={tag} | text={text} | name={name} | type={typ} | href={href} | visible={visible} | enabled={enabled}")
        except Exception as e:
            print(f"[ERROR] Failed to dump page: {e}")

    def click(self, target: str):
        print(f"[DEBUG] Clicking target: {target}")
        try:
            self.page.click(target)
            print("[INFO] Click successful")
        except Exception as e:
            print(f"[ERROR] Failed to click {target}: {e}")

    def fill(self, target: str, text: str):
        print(f"[DEBUG] Filling target {target} with text: {text}")
        try:
            self.page.fill(target, text)
            print("[INFO] Fill successful")
        except Exception as e:
            print(f"[ERROR] Failed to fill {target}: {e}")

    def press(self, target: str, key: str):
        print(f"[DEBUG] Pressing key {key} on target {target}")
        try:
            self.page.press(target, key)
            print("[INFO] Key press successful")
        except Exception as e:
            print(f"[ERROR] Failed to press {key} on {target}: {e}")

    def select(self, target: str, value: str):
        print(f"[DEBUG] Selecting {value} on {target}")
        try:
            self.page.select_option(target, value=value)
            print("[INFO] Select successful")
        except Exception as e:
            print(f"[ERROR] Failed to select {value} on {target}: {e}")

    def check(self, target: str):
        print(f"[DEBUG] Checking checkbox/radio {target}")
        try:
            self.page.check(target)
            print("[INFO] Check successful")
        except Exception as e:
            print(f"[ERROR] Failed to check {target}: {e}")

    def uncheck(self, target: str):
        print(f"[DEBUG] Unchecking checkbox {target}")
        try:
            self.page.uncheck(target)
            print("[INFO] Uncheck successful")
        except Exception as e:
            print(f"[ERROR] Failed to uncheck {target}: {e}")

    def text(self, selector: str):
        print(f"[DEBUG] Getting text from {selector}")
        try:
            txt = self.page.inner_text(selector)
            print(f"[RESULT] Text: {txt}")
            return txt
        except Exception as e:
            print(f"[ERROR] Failed to get text from {selector}: {e}")
            return None

    def attr(self, selector: str, attribute: str):
        print(f"[DEBUG] Getting attribute {attribute} from {selector}")
        try:
            val = self.page.get_attribute(selector, attribute)
            print(f"[RESULT] {attribute}={val}")
            return val
        except Exception as e:
            print(f"[ERROR] Failed to get attribute {attribute} from {selector}: {e}")
            return None

    def close(self):
        print("[DEBUG] Closing browser...")
        try:
            self.browser.close()
            self.playwright.stop()
        except Exception as e:
            print(f"[ERROR] Failed to close browser: {e}")