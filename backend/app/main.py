from fastapi import FastAPI;

from app.api.health import router as health_router;
from app.api.download import router as download_router


app = FastAPI()

app.include_router(health_router)
app.include_router(download_router)


@app.get("/")
def home():
    return {
        "message": "Servidor Funcionando"
    }