from playwright.sync_api import sync_playwright

class TextBrowser:
    def __init__(self, headless: bool = True, user_agent: str = None, viewport: tuple = (1280, 800)):
        print("[DEBUG] Initializing TextBrowser...")
        self.headless = headless
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless, args=["--disable-blink-features=AutomationControlled"])
        context_args = {}
        if user_agent:
            context_args["user_agent"] = user_agent
        if viewport:
            context_args["viewport"] = {"width": viewport[0], "height": viewport[1]}
        self.context = self.browser.new_context(**context_args)
        self.page = self.context.new_page()
        self.elements = []  # cache from last dump
        print("[DEBUG] Browser initialized with UA:", user_agent or "default")

    def goto(self, url: str):
        print(f"[DEBUG] Navigating to {url}...")
        try:
            self.page.goto(url, wait_until="domcontentloaded")
            print(f"[DEBUG] Navigation complete: {self.page.url}")
        except Exception as e:
            print(f"[ERROR] Failed to navigate to {url}: {e}")

    def wait(self, state: str = "networkidle"):
        print(f"[DEBUG] Waiting for state: {state}")
        try:
            self.page.wait_for_load_state(state)
            print(f"[INFO] Waited for {state}")
        except Exception as e:
            print(f"[ERROR] Wait for {state} failed: {e}")

    def dump(self):
        print("[DEBUG] Dumping page text and interactable elements...")
        try:
            body_text = self.page.inner_text("body")
            print("[TEXT CONTENT]")
            print(body_text[:2000])  # limit for now

            self.elements = self.page.query_selector_all("a, button, input, select, textarea")
            print("[INTERACTABLE ELEMENTS]")
            for i, el in enumerate(self.elements):
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

    def _resolve_target(self, target):
        # Numeric ID
        if isinstance(target, int) or (isinstance(target, str) and target.isdigit()):
            idx = int(target)
            if 0 <= idx < len(self.elements):
                return self.elements[idx]
            else:
                raise ValueError(f"Invalid element index {idx}")
        # text= match
        if isinstance(target, str) and target.startswith("text="):
            textval = target.split("=", 1)[1]
            return self.page.get_by_text(textval)
        # raw CSS selector
        return self.page.query_selector(target)

    def click(self, target):
        print(f"[DEBUG] Clicking {target}...")
        try:
            el = self._resolve_target(target)
            if el:
                el.click()
                print("[INFO] Click successful")
            else:
                print("[ERROR] No element found to click")
        except Exception as e:
            print(f"[ERROR] Click failed: {e}")

    def fill(self, target, text):
        print(f"[DEBUG] Filling {target} with '{text}'...")
        try:
            el = self._resolve_target(target)
            if el:
                el.fill(text)
                print("[INFO] Fill successful")
            else:
                print("[ERROR] No element found to fill")
        except Exception as e:
            print(f"[ERROR] Fill failed: {e}")

    def press(self, target, key):
        print(f"[DEBUG] Pressing {key} on {target}...")
        try:
            el = self._resolve_target(target)
            if el:
                el.press(key)
                print("[INFO] Press successful")
            else:
                print("[ERROR] No element found to press on")
        except Exception as e:
            print(f"[ERROR] Press failed: {e}")

    def select(self, target, option):
        print(f"[DEBUG] Selecting '{option}' on {target}...")
        try:
            el = self._resolve_target(target)
            if el:
                el.select_option(option)
                print("[INFO] Select successful")
            else:
                print("[ERROR] No element found to select")
        except Exception as e:
            print(f"[ERROR] Select failed: {e}")

    def check(self, target):
        print(f"[DEBUG] Checking {target}...")
        try:
            el = self._resolve_target(target)
            if el:
                el.check()
                print("[INFO] Check successful")
            else:
                print("[ERROR] No element found to check")
        except Exception as e:
            print(f"[ERROR] Check failed: {e}")

    def uncheck(self, target):
        print(f"[DEBUG] Unchecking {target}...")
        try:
            el = self._resolve_target(target)
            if el:
                el.uncheck()
                print("[INFO] Uncheck successful")
            else:
                print("[ERROR] No element found to uncheck")
        except Exception as e:
            print(f"[ERROR] Uncheck failed: {e}")

    def text(self, target):
        print(f"[DEBUG] Reading text from {target}...")
        try:
            el = self._resolve_target(target)
            if el:
                print(el.inner_text())
            else:
                print("[ERROR] No element found to read text")
        except Exception as e:
            print(f"[ERROR] Text read failed: {e}")

    def attr(self, target, name):
        print(f"[DEBUG] Reading attribute '{name}' from {target}...")
        try:
            el = self._resolve_target(target)
            if el:
                print(el.get_attribute(name))
            else:
                print("[ERROR] No element found to read attribute")
        except Exception as e:
            print(f"[ERROR] Attr read failed: {e}")

    def url(self):
        print(f"[DEBUG] Current URL: {self.page.url}")

    def cookies(self):
        print("[DEBUG] Reading cookies...")
        try:
            print(self.context.cookies())
        except Exception as e:
            print(f"[ERROR] Failed to get cookies: {e}")

    def set_cookie(self, name, value, domain):
        print(f"[DEBUG] Setting cookie {name}={value} for {domain}")
        try:
            self.context.add_cookies([{ "name": name, "value": value, "domain": domain, "path": "/" }])
            print("[INFO] Cookie set successfully")
        except Exception as e:
            print(f"[ERROR] Failed to set cookie: {e}")

    def savestate(self, path):
        print(f"[DEBUG] Saving browser state to {path}")
        try:
            self.context.storage_state(path=path)
            print("[INFO] State saved")
        except Exception as e:
            print(f"[ERROR] Failed to save state: {e}")

    def loadstate(self, path):
        print(f"[DEBUG] Loading browser state from {path}")
        try:
            self.context = self.browser.new_context(storage_state=path)
            self.page = self.context.new_page()
            print("[INFO] State loaded")
        except Exception as e:
            print(f"[ERROR] Failed to load state: {e}")

    def reload(self):
        print("[DEBUG] Reloading page...")
        try:
            self.page.reload()
            print("[INFO] Reload successful")
        except Exception as e:
            print(f"[ERROR] Reload failed: {e}")

    def set_user_agent(self, ua_string: str):
        print(f"[DEBUG] Setting user agent to {ua_string}")
        try:
            self.context.set_extra_http_headers({"User-Agent": ua_string})
            print("[INFO] User agent updated")
        except Exception as e:
            print(f"[ERROR] Failed to set user agent: {e}")

    def set_viewport(self, width: int, height: int):
        print(f"[DEBUG] Setting viewport to {width}x{height}")
        try:
            self.page.set_viewport_size({"width": width, "height": height})
            print("[INFO] Viewport updated")
        except Exception as e:
            print(f"[ERROR] Failed to set viewport: {e}")

    def close(self):
        print("[DEBUG] Closing browser...")
        try:
            self.browser.close()
            self.playwright.stop()
        except Exception as e:
            print(f"[ERROR] Failed to close browser: {e}")