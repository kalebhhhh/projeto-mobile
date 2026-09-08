import base64
import json
import re

import requests

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


def consultar_reel(reel_url: str):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; "
            "Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/152.0.0.0 Safari/537.36"
        ),
        "Referer": "https://snapinsta.ai/",
        "Origin": "https://snapinsta.ai"
    }

    response = requests.post(
        "https://snapinsta.ai/action2.php",
        headers=headers,
        data={
            "url": reel_url,
            "action": "post",
            "lang": "pt"
        }
    )

    return response.text


def baixar_video(
    video_url: str,
    nome_arquivo: str,
):

    response = requests.get(
        video_url,
        headers={
            "User-Agent":
                "TelegramBot (like TwitterBot)"
        },
        stream=True
    )

    if response.status_code != 200:
        return {
            "sucesso": False,
            "mensagem":
                f"Erro ao baixar vídeo: "
                f"{response.status_code}"
        }

    with open(
        nome_arquivo,
        "wb"
    ) as arquivo:

        for chunk in response.iter_content(
            chunk_size=8192
        ):
            if chunk:
                arquivo.write(chunk)

    return {
        "sucesso": True,
        "arquivo": nome_arquivo
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

    return baixar_video(
        video_url,
        nome_arquivo
    )


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