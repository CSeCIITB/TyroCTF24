from flask import Flask, request, render_template
import csv
import requests

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6500, debug=True)