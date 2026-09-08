import js2py


with open(
    "docs/action2_response.js",
    "r",
    encoding="utf-8"
) as arquivo:

    codigo = arquivo.read()

resultado = js2py.eval_js(
    codigo
)

print(resultado)