import base64
import json
from urllib.parse import (
    urlparse,
    parse_qs
)

from docs.playwright_snaptik import (
    obter_download_url
)


def extrair_dados_token(
    token: str
):

    try:

        payload = token.split(".")[1]

        payload += "=" * (
            -len(payload) % 4
        )

        decoded = (
            base64.urlsafe_b64decode(
                payload
            )
        )

        dados = json.loads(
            decoded
        )

        return {
            "url": dados.get(
                "url"
            ),
            "filename": dados.get(
                "filename"
            )
        }

    except Exception as erro:

        return {
            "erro": str(erro)
        }


def baixar_tiktok_por_url(
    tiktok_url: str
):

    resposta = obter_download_url(
        tiktok_url
    )

    if not resposta.get(
        "success"
    ):

        return {
            "sucesso": False,
            "mensagem":
                "Não foi possível obter dados do vídeo"
        }

    download_url = (
        resposta["data"].get(
            "downloadUrl"
        )
    )

    if not download_url:

        return {
            "sucesso": False,
            "mensagem":
                "downloadUrl não encontrado"
        }

    query = parse_qs(
        urlparse(
            download_url
        ).query
    )

    token = query.get(
        "token",
        [None]
    )[0]

    if not token:

        return {
            "sucesso": False,
            "mensagem":
                "Token JWT não encontrado"
        }

    dados = extrair_dados_token(
        token
    )

    video_url = dados.get(
        "url"
    )

    filename = dados.get(
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
        "filename": filename
    }