from flask import Flask
import webbrowser
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == "__main__":
	webbrowser.open_new_tab("http://localhost:8080")
	app.run(port=8080)
	