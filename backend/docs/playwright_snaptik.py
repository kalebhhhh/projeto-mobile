from playwright.sync_api import sync_playwright


def obter_download_url(tiktok_url: str):

    resultado = {}

    with sync_playwright() as p:

        browser = p.chromium.launch(
    headless=True,
    args=[
        "--disable-blink-features=AutomationControlled"
    ]
)

        context = browser.new_context(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/139.0.0.0 Safari/537.36"
                ),
                viewport={
                    "width": 1366,
                    "height": 768
                },
                locale="en-US"
            )

        page = context.new_page()
        page.add_init_script("""
                    Object.defineProperty(
                    navigator,
                    'webdriver',
                            {
                                get: () => undefined
                           }
                       );
                """)
        page.goto(
                    "https://snaptik.app/pt3",
                    wait_until="networkidle"
                )
        
        def capturar_resposta(response):
            print(
                "RESPONSE:",
                response.url
            )
            print(
                "STATUS:",
                response.status
            )

            if "/api/extract" in response.url:

                try:

                    dados = response.json()

                    resultado.update(dados)
                    print(
                        "JSON CAPTURADO:"
                    )
                    print(dados)

                except Exception as erro:

                    print(
                        "ERRO AO LER JSON:",
                        erro
                    )

        page.on(
            "response",
            capturar_resposta
        )

        # Aceitar popup de cookies se existir
        try:

            page.locator(
                'button:has-text("Accept")'
            ).click(
                timeout=3000
            )

            print(
                "Cookies aceitos"
            )

        except:

            try:

                page.locator(
                    'button:has-text("Aceitar")'
                ).click(
                    timeout=3000
                )

                print(
                    "Cookies aceitos"
                )

            except:

                print(
                    "Nenhum popup encontrado"
                )

        page.fill(
            "#url-input",
            tiktok_url
        )

        page.locator(
            "#submit-btn"
        ).click(
            force=True
        )

        page.wait_for_timeout(
            20000
        )
        print("\n====================")
        print("TEXTO DA PAGINA")
        print("====================")
        try:
                print(
                   page.locator("body").inner_text()
              )
        except Exception as erro:

            print(
                "ERRO AO CAPTURAR TEXTO:",
                erro
            )
        print(
         "URL ATUAL:",
            page.url
        )
        print("RESULTADO SNAPTIK:")
        print(resultado)
        browser.close()
        return resultado


if __name__ == "__main__":

    resposta = obter_download_url(
        "https://www.tiktok.com/@filmes.dub/video/7651256969776401685"
    )

    print(
        resposta
    )