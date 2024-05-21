import requests 
from flask import Flask, render_template, url_for
from flask import request as req

app = Flask(__name__)

# Define your API token
api_token = "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"

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": f"Bearer {api_token}"}

        data = req.form["data"]

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
        })

        return render_template("index.html", result=output[0]["summary_text"])
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
