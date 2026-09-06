from pydantic import BaseModel

class DownloadInfo(BaseModel):
    id: int
    url: str
    codigo: str
    status: str