from flask import Flask,request,render_template,redirect,url_for, send_file
import youtube_dl

app = Flask(__name__)
path = "H:\Assets\Music_for_download\\"
def download_vid(url, method='mp3'):
    with youtube_dl.YoutubeDL() as ydl:
        l = ydl.extract_info(url, download = False)
        dl = l["formats"][-1]["url"]
        return (dl)
@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        global link
        link = request.form["youtube_link"]
        link_ = download_vid(link)
        return redirect(link_+"&dl=1")
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True, port = 8000)
pri()



    