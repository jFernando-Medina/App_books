from flask import Flask
from decoradores import check_for_token

app = Flask(__name__)


@app.route("/login", methods = ["POST"])
def Login():
    recibido = {"Success": True}
    return recibido

@app.route("/")
@check_for_token
def Index():
    return "success!"

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
