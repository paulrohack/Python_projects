import youtube_dl
url = input("URL for the Video to Download: ")
with youtube_dl.YoutubeDL() as ydl:
    ydl.download([url])