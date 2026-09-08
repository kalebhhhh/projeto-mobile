from playwright.sync_api import sync_playwright
import re


def obter_token(reel_url: str):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            "https://snapinsta.ai/pt",
            wait_until="networkidle"
        )

        page.fill(
            "#url",
            reel_url
        )

        page.click(
            "#btn-submit"
        )

        page.wait_for_timeout(
            10000
        )

        html = page.eval_on_selector(
            "#download",
            "el => el.innerHTML"
        )

        browser.close()

        tokens = re.findall(
            r"token=([A-Za-z0-9._-]+)",
            html
        )

        if len(tokens) < 2:
            return None

        return tokens[1]


if __name__ == "__main__":

    print(
        obter_token(
            "https://www.instagram.com/reels/Dc4eX9Zxko3/"
        )
    )