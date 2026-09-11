import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:app_links/app_links.dart';

import 'screens/home_screen.dart';
import 'theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(
    const ReelDownloaderApp(),
  );
}

class ReelDownloaderApp extends StatefulWidget {
  const ReelDownloaderApp({
    super.key,
  });

  @override
  State<ReelDownloaderApp> createState() =>
      _ReelDownloaderAppState();
}

class _ReelDownloaderAppState
    extends State<ReelDownloaderApp> {

  static const MethodChannel _channel =
      MethodChannel(
    'reel_downloader/downloads',
  );

  late final AppLinks _appLinks;

  String? _initialUrl;

  @override
  void initState() {
    super.initState();

    _initDeepLinks();

    _obterTextoCompartilhado();
  }

  Future<void> _obterTextoCompartilhado() async {

    try {

      final texto =
          await _channel.invokeMethod<String>(
        'getSharedText',
      );

      if (
          texto != null &&
          texto.isNotEmpty
      ) {

        debugPrint(
          'TEXTO COMPARTILHADO: $texto',
        );

        setState(() {
          _initialUrl = texto;
        });
      }

    } catch (e) {

      debugPrint(
        'Erro ao obter texto compartilhado: $e',
      );
    }
  }

  void _initDeepLinks() {

    _appLinks = AppLinks();

    _appLinks.uriLinkStream.listen(
      (uri) {

        debugPrint(
          'DEEP LINK RECEBIDO: ${uri.toString()}',
        );

        _handleDeepLink(uri);
      },
      onError: (err) {

        debugPrint(
          'Erro ao processar deep link: $err',
        );
      },
    );

    _appLinks.getInitialLink().then(
      (uri) {

        if (uri != null) {
          _handleDeepLink(uri);
        }
      },
    ).catchError(
      (error) {

        debugPrint(
          'Erro ao obter link inicial: $error',
        );
      },
    );
  }

  void _handleDeepLink(
    Uri uri,
  ) {

    final url =
        uri.toString();

    debugPrint(
      'DEEP LINK RECEBIDO: $url',
    );

    if (
        url.contains(
          'instagram.com',
        ) ||
        url.contains(
          'tiktok.com',
        )
    ) {

      setState(() {
        _initialUrl = url;
      });
    }
  }

  @override
  Widget build(
    BuildContext context,
  ) {

    return MaterialApp(
      debugShowCheckedModeBanner:
          false,
      theme: AppTheme.theme,
      home: HomeScreen(
        initialUrl: _initialUrl,
      ),
    );
  }
}