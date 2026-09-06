from app.utils.url_utils import validar_reel_completo
from app.models.reel_validation_response import ReelValidationResponse
from app.models.reel_info_response import ReelInfoResponse

def validar_reel(url: str):

    resultado = validar_reel_completo(url)

    if not resultado["valido"]:
        return ReelValidationResponse(
            valido=False,
            mensagem=resultado["erro"]
        )

    return ReelValidationResponse(
        valido=True,
        mensagem="Reel válido",
        codigo=resultado["codigo"]
    )

def obter_info_reel(url: str):
    resultado = validar_reel_completo(url)
    if not resultado["valido"]:

        return ReelInfoResponse(
            valido=False,
            erro=resultado["erro"]
        )
    return ReelInfoResponse(
        valido=True,
        url=resultado["url"],
        codigo=resultado["codigo"],
        plataforma=resultado["plataforma"],
        tipo=resultado["tipo"]
    )