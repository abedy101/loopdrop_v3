import time
import random
import requests
from playwright.sync_api import sync_playwright

def get_proxy():
    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1000&country=all")
        return random.choice(r.text.strip().split("\n"))
    except:
        return None

def run_bot():
    proxy = get_proxy()
    print(f"[INFO] Using proxy: {proxy}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, proxy={"server": f"socks5://{proxy}"} if proxy else None)
        page = browser.new_page()
        try:
            page.goto("https://abedy101.github.io/loopdrop_v3/")
            time.sleep(random.uniform(5, 10))
            print("[INFO] Page visited successfully.")
        except Exception as e:
            print(f"[ERROR] {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run_bot()