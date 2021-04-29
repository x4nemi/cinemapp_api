import mysql.connector
import hashlib #para hasheo

bd = mysql.connector.connect(
    user = 'ximena', password = '123',
    database = 'cinemapp'
)

cursor = bd.cursor() #lo que hará la conexión del
                     #script y la base de datos

def get_usuarios():
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {
            "id": row[0],
            "correo": row[1],
            "contrasenia": row[2]
        }
        usuarios.append(usuario)
    return usuarios

def existe_usuario(correo):
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,)) #tupla de un elemento

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False


def crear_usuarios(correo, contrasenia):
    if existe_usuario(correo):
        return False
    else:
        h = hashlib.new("sha256", bytes(contrasenia, "utf-8")) 
        h = h.hexdigest() #cadena
        insertar = "INSERT INTO usuario(correo, contrasenia) VALUES(%s, %s)"
        cursor.execute(insertar, (correo, h))

        bd.commit()
        return True

def iniciar_sesion(correo, contrasenia):
    h = hashlib.new("sha256", bytes(contrasenia, "utf-8")) 
    h = h.hexdigest() #cadena
    query = "SELECT id FROM usuario WHERE correo = %s AND contrasenia = %s"
    cursor.execute(query, (correo, h))
    identificacion = cursor.fetchone()
    if identificacion:
        return identificacion[0], True
    else:
        return None, False