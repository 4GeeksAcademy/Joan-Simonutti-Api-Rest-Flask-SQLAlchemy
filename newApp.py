# importaciones
from flask import Flask, jsonify

# configuracion de la app
app = Flask(__name__)

# endpoints


@app.route("/")
def hello():
    return jsonify({"msg": "Gex esta aqui!!!"}), 200

@app.route("/numero1", methods=['GET'])
def handle_numero1():
    return jsonify({
        "msg": "numero1 esta aqui, en su endpoint!!!", 
        "success": True
        }), 200


# ejecucion
app.run(host='0.0.0.0')
