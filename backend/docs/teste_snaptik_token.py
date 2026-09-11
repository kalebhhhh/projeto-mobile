import base64
import json

token = """
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJodHRwczovL3YxNm1lLnRpa3Rva2Nkbi5jb20vM2RiZDUxNTM5MTVkOTk1OTIxN2VhN2IxY2E2YjMxMzAvNmFhNDk0N2EvdmlkZW8vdG9zL2FsaXNnL3Rvcy1hbGlzZy1wdmUtMDAzN2MwMDEvb2thVkJjaWc2T0JSaU92SU00dlR6QXliRURGRUF2aVlxWENPNC8_YT0xMzQwJmJ0aT1iR1J1Wkh4dk1YSXhjbTUzWm0xY1lGOWViV0Z6YUhGbU9nJTNEJTNEJiZidD03NTcmZnQ9QkloQTdWMHh3d0NSZmpDRWRiT3gya0VHQ2dwaWdtWlVRaktKNk40TEVOMFAzLUkmbWltZV90eXBlPXZpZGVvX21wNCZyYz1OV2M2YURVMk16VXpPV2RrWm1ScFpVQnBhalZtYld3NWNtaGxPek16T0Rjek5FQTBMbUF2TVRJek5URXhZRE5nTkRFdFlTTmhNMm8yTW1SclpHdGhMUzFrTVdCemN3JTNEJTNEJnZ2cGw9MSZsPTIwMjYwOTExMDY1MzMxOTFDMTFERTk0MTdBQTYyNzlCNTEmYnRhZz1lMDAwNjgwMDAiLCJmaWxlbmFtZSI6InNuYXB0aWtfNzY1MTI1Njk2OTc3NjQwMTY4NV92My5tcDQiLCJoZWFkZXJzIjp7InVzZXItYWdlbnQiOiJUZWxlZ3JhbUJvdCAobGlrZSBUd2l0dGVyQm90KSJ9LCJpYXQiOjE3ODkwODA4MTF9.KBjbG-j9adXmcKTeSrpsa7efKVE_V_Tcv1J7bXAmjFA
""".strip()

payload = token.split(".")[1]

payload += "=" * (-len(payload) % 4)

dados = json.loads(
    base64.urlsafe_b64decode(payload)
)

print(
    json.dumps(
        dados,
        indent=4,
        ensure_ascii=False
    )
)