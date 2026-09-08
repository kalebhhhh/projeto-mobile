from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/arquivo/{nome}")
def baixar_arquivo(nome: str):

    return FileResponse(
        path=nome,
        filename=nome,
        media_type="video/mp4"
    )