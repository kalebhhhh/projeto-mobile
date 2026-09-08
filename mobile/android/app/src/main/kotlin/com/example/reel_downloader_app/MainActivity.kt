package com.example.reel_downloader_app

import android.content.ContentValues
import android.os.Build
import android.os.Environment
import android.provider.MediaStore
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import java.io.File
import java.io.FileInputStream

class MainActivity : FlutterActivity() {

    private val CHANNEL =
        "reel_downloader/downloads"

    override fun configureFlutterEngine(
        flutterEngine: FlutterEngine
    ) {

        super.configureFlutterEngine(
            flutterEngine
        )

        MethodChannel(
            flutterEngine.dartExecutor.binaryMessenger,
            CHANNEL
        ).setMethodCallHandler { call, result ->

            if (
                call.method ==
                "saveToDownloads"
            ) {

                val path =
                    call.argument<String>(
                        "path"
                    )

                if (path == null) {

                    result.error(
                        "PATH_NULL",
                        "Path não informado",
                        null
                    )

                    return@setMethodCallHandler
                }

                try {

                    salvarEmDownloads(
                        path
                    )

                    result.success(
                        true
                    )

                } catch (
                    e: Exception
                ) {

                    result.error(
                        "ERRO",
                        e.message,
                        null
                    )
                }
            }
        }
    }

    private fun salvarEmDownloads(
        caminho: String
    ) {

        val arquivo =
            File(caminho)

        val resolver =
            applicationContext
                .contentResolver

        val values =
            ContentValues().apply {

                put(
                    MediaStore.Downloads.DISPLAY_NAME,
                    arquivo.name
                )

                put(
                    MediaStore.Downloads.MIME_TYPE,
                    "video/mp4"
                )

                if (
                    Build.VERSION.SDK_INT >=
                    Build.VERSION_CODES.Q
                ) {

                    put(
                        MediaStore.Downloads.RELATIVE_PATH,
                        Environment.DIRECTORY_DOWNLOADS
                    )
                }
            }

        val uri =
            resolver.insert(
                MediaStore.Downloads.EXTERNAL_CONTENT_URI,
                values
            ) ?: return

        resolver.openOutputStream(
            uri
        )!!.use { output ->

            FileInputStream(
                arquivo
            ).use { input ->

                input.copyTo(
                    output
                )
            }
        }
    }
}