import yt_dlp

def download_youtube_video(video_url):
    # Konfigurasi untuk pengunduhan
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Pilih kualitas terbaik
        'outtmpl': '%(title)s.%(ext)s',       # Format nama file
        'noplaylist': True,                   # Unduh hanya video, bukan playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Mengunduh video...")
            ydl.download([video_url])
            print("Video berhasil diunduh!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Masukkan URL video
video_url = input("Masukkan URL video YouTube: ")
download_youtube_video(video_url)
