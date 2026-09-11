import base64
import json

from docs.playwright_token import obter_token


def extrair_dados_token(token: str):

    try:

        payload = token.split(".")[1]

        payload += "=" * (
            -len(payload) % 4
        )

        decoded = base64.urlsafe_b64decode(
            payload
        )

        dados = json.loads(decoded)

        return {
            "url": dados.get("url"),
            "filename": dados.get(
                "filename"
            )
        }

    except Exception as erro:

        return {
            "erro": str(erro)
        }


def baixar_video_do_token(
    token: str
):

    dados = extrair_dados_token(
        token
    )

    video_url = dados.get(
        "url"
    )

    nome_arquivo = dados.get(
        "filename"
    )

    if not video_url:
        return {
            "sucesso": False,
            "mensagem":
                "URL do vídeo não encontrada"
        }

    return {
        "sucesso": True,
        "download_url": video_url,
        "filename": nome_arquivo
    }


def baixar_reel_por_url(
    reel_url: str
):

    token = obter_token(
        reel_url
    )

    if not token:
        return {
            "sucesso": False,
            "mensagem": "Token não encontrado"
        }

    return baixar_video_do_token(
        token
    )