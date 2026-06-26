import yt_dlp

def download_video(url):
    opsi = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'noplaylist': True,  # hanya 1 video
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(opsi) as ydl:
        print("⏳ Download video...")
        ydl.download([url])
        print("✅ Selesai!")


def download_playlist(url):
    opsi = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'noplaylist': False,  # aktifkan playlist
        'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(opsi) as ydl:
        print("⏳ Download playlist...")
        ydl.download([url])
        print("✅ Playlist selesai!")


if __name__ == "__main__":
    print("=== YT Downloader (yt-dlp) ===")
    url = input("Masukkan URL: ")

    print("\nPilih mode:")
    print("1. Download Video")
    print("2. Download Playlist")

    pilihan = input("Pilih (1/2): ")

    if pilihan == "2":
        download_playlist(url)
    else:
        download_video(url)
