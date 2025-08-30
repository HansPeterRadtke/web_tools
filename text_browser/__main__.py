import argparse
from .core import TextBrowser


def main():
    parser = argparse.ArgumentParser(description="Text-based headless browser interface")
    parser.add_argument("url", nargs="?", help="Initial URL to open")
    parser.add_argument("--headless", action="store_true", default=True, help="Run browser in headless mode")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive REPL mode")
    args = parser.parse_args()

    print("[DEBUG] Starting text_browser module...")

    tb = TextBrowser(headless=args.headless)

    if args.url:
        tb.goto(args.url)
        tb.dump()

    if args.interactive:
        print("[DEBUG] Entering interactive mode. Type 'help' for commands, 'exit'/'quit'/'q' to quit.")
        while True:
            try:
                cmd = input("text_browser> ").strip()
                if cmd in ("exit", "quit", "q"):
                    print("[DEBUG] Exiting interactive mode.")
                    break
                elif cmd == "help":
                    print("Commands: goto <url>, wait <state>, dump, click <target>, fill <target> <text>, press <target> <key>, select <target> <option>, check <target>, uncheck <target>, text <target>, attr <target> <name>, url, cookies, setcookie <name> <value> <domain>, savestate <path>, loadstate <path>, reload, setua <ua>, viewport <w> <h>")
                elif cmd.startswith("goto "):
                    _, url = cmd.split(" ", 1)
                    tb.goto(url)
                elif cmd.startswith("wait "):
                    _, state = cmd.split(" ", 1)
                    tb.wait(state)
                elif cmd == "dump":
                    tb.dump()
                elif cmd.startswith("click "):
                    _, target = cmd.split(" ", 1)
                    tb.click(target)
                elif cmd.startswith("fill "):
                    parts = cmd.split(" ", 2)
                    if len(parts) == 3:
                        _, target, text = parts
                        tb.fill(target, text)
                    else:
                        print("Usage: fill <target> <text>")
                elif cmd.startswith("press "):
                    parts = cmd.split(" ", 2)
                    if len(parts) == 3:
                        _, target, key = parts
                        tb.press(target, key)
                    else:
                        print("Usage: press <target> <key>")
                elif cmd.startswith("select "):
                    parts = cmd.split(" ", 2)
                    if len(parts) == 3:
                        _, target, option = parts
                        tb.select(target, option)
                    else:
                        print("Usage: select <target> <option>")
                elif cmd.startswith("check "):
                    _, target = cmd.split(" ", 1)
                    tb.check(target)
                elif cmd.startswith("uncheck "):
                    _, target = cmd.split(" ", 1)
                    tb.uncheck(target)
                elif cmd.startswith("text "):
                    _, target = cmd.split(" ", 1)
                    tb.text(target)
                elif cmd.startswith("attr "):
                    parts = cmd.split(" ", 2)
                    if len(parts) == 3:
                        _, target, name = parts
                        tb.attr(target, name)
                    else:
                        print("Usage: attr <target> <name>")
                elif cmd == "url":
                    tb.url()
                elif cmd == "cookies":
                    tb.cookies()
                elif cmd.startswith("setcookie "):
                    parts = cmd.split(" ", 3)
                    if len(parts) == 4:
                        _, name, value, domain = parts
                        tb.set_cookie(name, value, domain)
                    else:
                        print("Usage: setcookie <name> <value> <domain>")
                elif cmd.startswith("savestate "):
                    _, path = cmd.split(" ", 1)
                    tb.savestate(path)
                elif cmd.startswith("loadstate "):
                    _, path = cmd.split(" ", 1)
                    tb.loadstate(path)
                elif cmd == "reload":
                    tb.reload()
                elif cmd.startswith("setua "):
                    _, ua = cmd.split(" ", 1)
                    tb.set_user_agent(ua)
                elif cmd.startswith("viewport "):
                    _, w, h = cmd.split(" ", 2)
                    tb.set_viewport(int(w), int(h))
                else:
                    print("[ERROR] Unknown command.")
            except Exception as e:
                print(f"[FATAL] Exception in interactive mode: {e}")

    tb.close()


if __name__ == "__main__":
    main()