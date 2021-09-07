import os

run = True

path = 'G:\Music'

while run:
    ask = input("[Y]outube Link or [Q]uit :")
    if ask.upper() == 'Y':
        url = input("YOUTUBE URL :  ")
        f_url = (f"youtube-dl -o {path}\%(title)s.%(ext)s -x --audio-format mp3 " + url)
        os.system(f_url)
    else:
        run = False

