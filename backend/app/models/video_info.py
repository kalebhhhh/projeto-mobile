from pydantic import BaseModel

class VideoInfo(BaseModel):
    url: str
    codigo: str
    plataforma: str
    tipo: str
    status: str
