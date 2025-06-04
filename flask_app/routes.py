from flask_app import app

@app.route("/saludo", methods=["GET"])
def saludo():
    return "Hola, mundo"
