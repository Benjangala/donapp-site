
from flask import Flask, render_template
import webbrowser
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

def menu():
	return render_template("menu.html")

@app.route("/")
@app.route("/menu")
def hello():
	return "Bonjour"

@app.route('/contact')
def contact():
	return render_template("contact.html")

if __name__ == "__main__":
	# webbrowser.open_new("http://127.0.0.1:5000")
	app.debug = True
	app.run("0.0.0.0", port=5001)




