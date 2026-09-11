from playwright.sync_api import sync_playwright


def obter_download_url(tiktok_url: str):

    resultado = {}

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        def capturar_resposta(response):

            if "/api/extract" in response.url:

                try:

                    dados = response.json()

                    resultado.update(dados)

                except Exception as erro:

                    print(
                        "ERRO AO LER JSON:",
                        erro
                    )

        page.on(
            "response",
            capturar_resposta
        )

        page.goto(
            "https://snaptik.app/pt3",
            wait_until="networkidle"
        )

        page.fill(
            "#url-input",
            tiktok_url
        )

        page.click(
            "#submit-btn"
        )

        page.wait_for_timeout(
            10000
        )

        browser.close()

        return resultado


if __name__ == "__main__":

    resposta = obter_download_url(
        "https://www.tiktok.com/@filmes.dub/video/7651256969776401685"
    )
