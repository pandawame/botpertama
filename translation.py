class Translation(object):

    START_TEXT = """Halo,

Aku dapat melakukan banyak hal yang tidak dijelaskan oleh Penciptaku.

<b>Tidak semua orang dapat menjalankan fiturku!</b>

Ketik /help untuk fitur dasarku.
"""

    HELP_USER = """Fitur dasarku..
    
1. Untuk mengganti nama berkas kirim (Tautan | Nama Baru beserta Ekstensi).
2. Thumbnail bersifat permanen.
   Untuk menghapus Thumbnail ketik /deletethumbnail
   Kamu hanya perlu mengirim Thumbnail baru untuk menimpanya!
3. Penjelasan <b>Button</b>:
   SVideo - Kirim video asli serta tangkapan layar.
   DFile  - Kirim berkas serta tangkapan layar.
   Video  - Kirim berkas video tanpa tangkapan layar.
   DFile  - Kirim berkas tanpa tangkapan layar.
   
   <i>Fitur tangkapan layar secara default tidak diaktifkan oleh Penciptaku.</i>
"""

    FORMAT_SELECTION = """Pilih format yang diinginkan: <a href='{}'>perkiraan ukuran berkas</a>"""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    DOWNLOAD_START = "Sedang mengunduh berkasmu..."
    
    UPLOAD_START = "Sedang mengunggah..."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Diundah dalam {} detik. \n\nDiunggah dalam {} detik."

    RCHD_TG_API_LIMIT = "Diunduh {} detik.\nUkuran Berkas Terdeteksi : {}\nMaaf. Tetapi, Aku tidak dapat mengunggah berkas yang lebih besar dari 1,95GB karena keterbatasan API Telegram."

    SAVED_CUSTOM_THUMB_NAIL = "Thumbnail telah disimpan."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail telah dihapus."

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."    
