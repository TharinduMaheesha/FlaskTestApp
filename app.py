from flask import Flask, render_template, request, flash
from pytube import YouTube

app = Flask(__name__, static_folder='static')
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	link = str(request.form['name_input'])
	yt = YouTube(link)
	yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("static")
	test = yt.title
	flash(test+".mp4")
	return render_template("video.html")