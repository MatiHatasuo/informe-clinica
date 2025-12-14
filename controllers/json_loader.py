import json
import bcrypt
from config.db_config import conectarBD

def cargar_usuarios_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    db = conectarBD()
    cursor = db.obtener_cursor()

    for u in usuarios:
        clave = bcrypt.hashpw("1234".encode(), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO usuario (nombre_usuario, clave, tipo) VALUES (:1, :2, 'PACIENTE')",
            (u["username"], clave)
        )

    db.connection.commit()
    db.desconectar()
