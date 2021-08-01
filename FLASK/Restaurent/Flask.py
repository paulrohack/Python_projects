from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)
@app.route("/")
def page():
    return redirect(url_for("home"))
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/menu")
def menu():
    return render_template("menu.html")
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
if __name__ == "__main__":
    app.run(debug=True)
    



    