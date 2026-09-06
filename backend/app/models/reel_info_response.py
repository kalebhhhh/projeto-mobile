from pydantic import BaseModel


class ReelInfoResponse(BaseModel):
    valido: bool
    url: str | None = None
    codigo: str | None = None
    plataforma: str | None = None
    tipo: str | None = None
    erro: str | None = None