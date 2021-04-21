from flask import Flask, jsonify, request

from conexion import crear_usuarios

app = Flask(__name__)

@app.route("/api/v1/usuarios", methods = ["POST"])
def usuario():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)

            if crear_usuarios(data["correo"], data["contrasenia"]):
                return jsonify({"code": "ok"})
            else:
                return jsonify({"code": "existe"})
        except:
            return jsonify({"code": "error"})

app.run(debug = True) #Para que se recargue la página si modificamos algo
