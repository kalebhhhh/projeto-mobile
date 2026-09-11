from fastapi import APIRouter
from app.services.tiktok_service import (
    baixar_tiktok_por_url,
)
from app.models.video_request import VideoRequest

from app.repositories.download_repository import (
    listar_downloads,
    buscar_download_por_id,
)

from app.services.reel_service import (
    validar_reel,
    obter_info_reel,
)

from app.services.download_service import (
    processar_download,
    iniciar_download,
)

from app.services.instagram_service import (
    baixar_reel_por_url,
)

router = APIRouter()


@router.post("/tiktok/download-real")
def tiktok_download_real(
    video: VideoRequest
):
    return baixar_tiktok_por_url(
        video.url
    )

@router.post("/reel/download-real")
def reel_download_real(
    video: VideoRequest
):

    return baixar_reel_por_url(
        video.url
    )


@router.post("/reel")
def reel(video: VideoRequest):

    return processar_download(
        video.url
    )


@router.post("/reel/validar")
def validar(video: VideoRequest):

    return validar_reel(
        video.url
    )


@router.post("/reel/info")
def info(video: VideoRequest):

    return obter_info_reel(
        video.url
    )


@router.post("/reel/share")
def reel_share(video: VideoRequest):

    return processar_download(
        video.url
    )


@router.post("/reel/download")
def reel_download(video: VideoRequest):

    return iniciar_download(
        video.url
    )


@router.get("/downloads")
def downloads():

    return listar_downloads()
##rotafinal

@router.get("/downloads/{id}")
def download_por_id(id: int):

    download = buscar_download_por_id(
        id
    )

    if download is None:
        return {
            "erro": "Download não encontrado"
        }

    return download