# Requisição Reel

POST /reel

{
    "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/"
}
# Resposta Reel

{
    "status": "concluido",
    "mensagem": "URL válida",
    "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/",
    "plataforma": "instagram",
    "tipo": "reel",
    "codigo": "Dc7YfBnCKIZ"
}
# Resposta Inválida
{
    "status": "erro",
    "mensagem": "Não pertence ao Instagram"
}
# POST /reel/validar

{
  "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/"
}
# POST /reel/info

{
  "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/"
}
# POST /reel/download


{
  "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/"
}
# Compartilhamento Instagram

POST /reel/share

{
    "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/"
}
# Validar Reel

POST /reel/validar

{
    "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/"
}
# Informações do Reel

POST /reel/info

{
    "url": "https://www.instagram.com/reels/Dc7YfBnCKIZ/"
}
# Fluxo Mobile
Instagram
↓ Compartilhar
↓
Flutter
↓
POST /reel/share
↓
POST /reel/info
↓
POST /reel/download
↓
Salvar no dispositivo

