# projeto-flutter
Reel Downloader
*
Aplicativo Flutter para download de Reels do Instagram e vídeos do TikTok utilizando um backend FastAPI.

Funcionalidades
Instagram
Download de Reels
Validação automática de URLs
Extração automática de vídeo
Salvamento na pasta Downloads
TikTok
Download de vídeos TikTok
Compartilhamento direto do TikTok
Download automático após compartilhamento
Salvamento na pasta Downloads
Aplicativo Mobile
Interface Material 3
Barra de progresso em tempo real
Histórico de downloads da sessão
Compartilhamento de app
Deep Linking
Compartilhamento direto Instagram → App
Compartilhamento direto TikTok → App
Backend
FastAPI
Playwright
SnapInsta
SnapTik
Retorno apenas da URL real do vídeo
Download realizado diretamente pelo celular


cd backend

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

cd mobile

flutter pub get

flutter run


configurar:
mobile/lib/services/api_service.dart
static const String baseUrl =
    'http://192.168.0.3:8000';



testes feitos de consumo api
Tiktok:
RAM adicional: 6.52 MB
Tempo médio: 17.86s
Resposta API: 527 bytes

Instagram:
RAM adicional: 3.93 MB
Tempo médio: 17.62s
Resposta API: 1151 bytes

projeto-flutter\backend\docs\medir_concorrencia.py
20 requisições simultâneas: 
RAM inicial: 32.33 MB
RAM final:   98.35 MB
Diferença:   66.02 MB
20/20 concluídas com sucesso











flutter create reel_downloader_app
python -m uvicorn app.main:app --reload
flutter run
flutter build apk --release
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload (subir servidor)

Próximo grande passo importante, reduzir drásticamente o consumo do backend. 08/09/2026
