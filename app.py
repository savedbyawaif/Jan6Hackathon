
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "welcome"

@app.route("/registration")
def reg():
    return "Registration details"

if __name__ == "__main__":
    app.run(debug=True)