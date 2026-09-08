from playwright.sync_api import sync_playwright


REEL_URL = "https://www.instagram.com/reels/Dc4eX9Zxko3/"


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://snapinsta.ai/pt",
        wait_until="networkidle"
    )

    page.fill(
        "#url",
        REEL_URL
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

    with open(
        "docs/dom_auto.html",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(html)

    print("DOM SALVO")

    token = page.eval_on_selector(
        "#download",
        """
        el => {
            const link = el.querySelector(
                'a[href*="token="]'
            );

            return link
                ? link.href
                : null;
        }
        """
    )

    print("TOKEN URL:")
    print(token)

    input(
        "Pressione ENTER para fechar..."
    )

    browser.close()