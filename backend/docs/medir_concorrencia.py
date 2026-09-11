import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

import os
import time
import json
import threading
import psutil

from app.services.tiktok_service import (
    baixar_tiktok_por_url
)

URL = (
    "https://www.tiktok.com/@filmes.dub/video/7651256969776401685"
)

process = psutil.Process(
    os.getpid()
)


def worker(indice):

    inicio = time.time()

    try:

        resultado = baixar_tiktok_por_url(
            URL
        )

        tamanho_json = len(
            json.dumps(
                resultado
            ).encode("utf-8")
        )

        print(
            f"THREAD {indice} OK "
            f"({tamanho_json} bytes)"
        )

    except Exception as erro:

        print(
            f"THREAD {indice} ERRO:"
            f" {erro}"
        )

    fim = time.time()

    print(
        f"THREAD {indice} "
        f"{fim - inicio:.2f}s"
    )


print("\n==============================")
print("TESTE 20 REQUISIÇÕES")
print("==============================")

ram_inicial = (
    process.memory_info().rss
    / 1024
    / 1024
)

print(
    f"RAM inicial: {ram_inicial:.2f} MB"
)

inicio_total = time.time()

threads = []

QUANTIDADE = 20

for i in range(
    QUANTIDADE
):

    t = threading.Thread(
        target=worker,
        args=(i + 1,)
    )

    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

fim_total = time.time()

ram_final = (
    process.memory_info().rss
    / 1024
    / 1024
)

print("\n==============================")
print("RESULTADO FINAL")
print("==============================")

print(
    f"RAM final: {ram_final:.2f} MB"
)

print(
    f"Diferença: "
    f"{ram_final - ram_inicial:.2f} MB"
)

print(
    f"Tempo total: "
    f"{fim_total - inicio_total:.2f}s"
)