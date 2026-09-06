from pydantic import BaseModel


class ReelValidationResponse(BaseModel):
    valido: bool
    mensagem: str | None = None
    codigo: str | None = None