from fastapi import APIRouter
from app.models.video_request import VideoRequest
from app.repositories.download_repository import (listar_downloads, buscar_download_por_id)
from app.services.reel_service import (validar_reel, obter_info_reel)
from app.services.download_service import (processar_download,iniciar_download)

router = APIRouter()

@router.post("/reel")
def reel(video: VideoRequest):
    return processar_download(video.url)

@router.post("/reel/validar")
def validar(video: VideoRequest):
    return validar_reel(video.url)

@router.get("/downloads")
def downloads():
    return listar_downloads()

@router.get("/downloads/{id}")
def download_por_id(id: int):
    download = buscar_download_por_id(id)
    if download is None:
            return {
                "erro":"Download não encontrado" 
        }
    return download
@router.post("/reel/info")
def info(video: VideoRequest):

    return obter_info_reel(video.url)

#recebera url compartilhada
@router.post("/reel/share")
def reel_share(video: VideoRequest):
    return processar_download(video.url)

@router.post("/reel/download")
def reel_download(video: VideoRequest):

    return iniciar_download(video.url)