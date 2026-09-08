import 'package:flutter/material.dart';

import 'screens/home_screen.dart';

void main() {
  runApp(
    const ReelDownloaderApp(),
  );
}

class ReelDownloaderApp
    extends StatelessWidget {

  const ReelDownloaderApp({
    super.key,
  });

  @override
  Widget build(
    BuildContext context,
  ) {

    return const MaterialApp(
      debugShowCheckedModeBanner:
          false,

      home: HomeScreen(),
    );
  }
}