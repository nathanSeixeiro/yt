from pytube import YouTube

video_urls = [
    "https://www.youtube.com/watch?v=-dQ55jupCVk",
    "https://www.youtube.com/watch?v=ZQ1UUHe2C_0",
]

caminho_destino = "./download/"

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print(f'Download: {percent:.2f}%')

def baixar_videos(urls, caminho):
    for url in urls:
        try:
            yt = YouTube(url, on_progress_callback=progress_callback)
            video_stream = yt.streams.get_highest_resolution()
            print(f"Baixando: {yt.title}")
            video_stream.download(output_path=caminho)
            print("Download completo!")
        except Exception as e:
            print(f"Ocorreu um erro ao baixar o vídeo {url}: {e}")

baixar_videos(video_urls, caminho_destino)
