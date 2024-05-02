import os
from flask import Flask

app = Flask(__name__)


@app.route("/auth/callback")
def auth_callback():
    return "Authentication callback received!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("PORT:", port)
    app.run(debug=True, port=port)
