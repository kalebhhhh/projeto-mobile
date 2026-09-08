from app.models.download_response import DownloadResponse
from app.models.video_info import VideoInfo
from app.models.download_info import DownloadInfo
from app.models.reel_download_response import (
    ReelDownloadResponse
)

from app.repositories.download_repository import (
    salvar_download
)

from app.utils.url_utils import (
    validar_reel_completo
)

from app.config.status import (
    STATUS_PRONTO,
    STATUS_VALIDADO,
    STATUS_ERRO
)

from app.services.instagram_service import (
    baixar_video_do_token
)


def processar_download(url: str):

    if not url:
        return DownloadResponse(
            status=STATUS_ERRO,
            mensagem="URL não informada"
        )

    resultado = validar_reel_completo(url)

    if not resultado["valido"]:
        return DownloadResponse(
            status=STATUS_ERRO,
            mensagem=resultado["erro"]
        )

    video = VideoInfo(
        url=resultado["url"],
        codigo=resultado["codigo"],
        plataforma=resultado["plataforma"],
        tipo=resultado["tipo"],
        status=STATUS_PRONTO
    )

    download = DownloadInfo(
        id=0,
        url=video.url,
        codigo=video.codigo,
        status=STATUS_PRONTO
    )

    salvar_download(download)

    return DownloadResponse(
        status=STATUS_VALIDADO,
        mensagem="URL válida",
        url=video.url,
        plataforma=video.plataforma,
        tipo=video.tipo,
        codigo=video.codigo
    )

def iniciar_download(url: str):

    resultado = validar_reel_completo(url)

    if not resultado["valido"]:
        return ReelDownloadResponse(
            sucesso=False,
            codigo="",
            mensagem=resultado["erro"]
        )

    return ReelDownloadResponse(
        sucesso=True,
        codigo=resultado["codigo"],
        mensagem="Download iniciado"
    )