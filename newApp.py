# importaciones
from flask import Flask, jsonify

# configuracion de la app
app = Flask(__name__)

# endpoints
@app.route("/")
def hello():
    return jsonify({"msg": "Gex esta aqui!!!"})

# ejecucion
app.run(host='0.0.0.0')