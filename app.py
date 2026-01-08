from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Assignment 4 Flask App Running"

@app.route("/api")
def api():
    with open("data.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
