
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ASDD Practical 07 - Docker Image Built Using GitHub Actions!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
