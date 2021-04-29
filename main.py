from flask import Flask, jsonify, request

from conexion import crear_usuarios, iniciar_sesion

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

@app.route("/api/v1/sesiones", methods = ["POST"])
def sesion():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            correo = data["correo"]
            contrasenia = data["contrasenia"]
            print(correo, contrasenia)
            identificacion, ok = iniciar_sesion(correo, contrasenia)
            if ok:
                return jsonify({"code": "ok", "id": identificacion})
            else:
                return jsonify({"code": "noexiste"})
        except:
            return jsonify({"code": "error"})

app.run(debug = True) #Para que se recargue la página si modificamos algo
