from pydantic import BaseModel

class DownloadResponse(BaseModel):
    status: str
    mensagem: str
    url: str | None = None
    plataforma: str | None = None
    tipo: str | None = None
    codigo: str | None = None
