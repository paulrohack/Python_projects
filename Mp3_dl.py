import youtube_dl
while True:
    url = input("URL for the Video to Download: ")
    try:
        with youtube_dl.YoutubeDL() as ydl:
            ydl.download([url])
    except KeyboardInterrupt:
        quit()