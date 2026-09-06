def eh_instagram(url: str) -> bool:
    return "instagram.com" in url

def eh_reel(url: str) -> bool:
    return "/reel/" in url or "/reels/" in url

def obter_plataforma(url: str) -> str:
    if eh_instagram(url):
        return "instagram"
    return "desconhecida"

def extrair_codigo_reel(url: str) -> str:
    try:
        if "/reels/" in url:
            partes = url.split("/reels/")
        else:
            partes = url.split("/reel/")
        return partes[1].split("/")[0]
    except:
        return ""

def obter_tipo(url: str) -> str:
    if eh_reel(url):
        return "reel"
    return "desconhecido"

def limpar_url(url: str) -> str:
    return url.split("?")[0]

def codigo_reel_valido(url: str) -> bool:
    codigo = extrair_codigo_reel(url)
    return codigo !=""

def processar_url_reel(url: str):
    url_limpa = limpar_url(url)
    return {
        "url": url_limpa,
        "codigo": extrair_codigo_reel(url_limpa),
        "plataforma": obter_plataforma(url_limpa),
        "tipo": obter_tipo(url_limpa)
    }
def url_reel_valida(url: str) -> bool:
    url_limpa = limpar_url(url)

    return (
        eh_instagram(url_limpa)
        and eh_reel(url_limpa)
        and codigo_reel_valido(url_limpa)
    )


def validar_reel_completo(url: str):

    url_limpa = limpar_url(url)

    if not eh_instagram(url_limpa):
        return {
            "valido": False,
            "erro": "Não pertence ao Instagram"
        }

    if not eh_reel(url_limpa):
        return {
            "valido": False,
            "erro": "Não é um Reel"
        }

    if not codigo_reel_valido(url_limpa):
        return {
            "valido": False,
            "erro": "Código inválido"
        }

    return {
        "valido": True,
        "url": url_limpa,
        "codigo": extrair_codigo_reel(url_limpa),
        "plataforma": obter_plataforma(url_limpa),
        "tipo": obter_tipo(url_limpa)
    }