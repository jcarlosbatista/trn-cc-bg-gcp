import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def get():
    name = os.environ.get("NAME", "Data")
    return "{}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))