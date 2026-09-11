import os
import time
import json
import psutil
import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)
from app.services.tiktok_service import (
    baixar_tiktok_por_url,
)

process = psutil.Process(
    os.getpid()
)

ram_inicial = (
    process.memory_info().rss
    / 1024
    / 1024
)

inicio = time.time()

resultado = baixar_tiktok_por_url(
    "https://www.tiktok.com/@filmes.dub/video/7651256969776401685"
)

fim = time.time()

ram_final = (
    process.memory_info().rss
    / 1024
    / 1024
)

tamanho_json = len(
    json.dumps(
        resultado
    ).encode("utf-8")
)

print("\n============")
print("RESULTADO")
print("============")

print(
    json.dumps(
        resultado,
        indent=2,
        ensure_ascii=False,
    )
)

print("\n============")
print("MÉTRICAS")
print("============")

print(
    f"RAM inicial: {ram_inicial:.2f} MB"
)

print(
    f"RAM final: {ram_final:.2f} MB"
)

print(
    f"Diferença: {ram_final - ram_inicial:.2f} MB"
)

print(
    f"Tempo: {fim - inicio:.2f}s"
)

print(
    f"Resposta JSON: {tamanho_json} bytes"
)