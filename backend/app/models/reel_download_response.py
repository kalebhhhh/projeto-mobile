from pydantic import BaseModel

class ReelDownloadResponse(BaseModel):
    sucesso: bool
    codigo: str
    mensagem: str
    