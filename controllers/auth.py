import bcrypt
from config.db_config import conectarBD

def login(usuario, clave):
    db = conectarBD()
    cursor = db.obtener_cursor()

    cursor.execute(
        "SELECT clave, tipo FROM usuario WHERE nombre_usuario = :1",
        (usuario,)
    )

    row = cursor.fetchone()

    if row is None:
        db.desconectar()
        return None

    clave_db, tipo = row

    if bcrypt.checkpw(clave.encode("utf-8"), clave_db):
        db.desconectar()
        return tipo

    db.desconectar()
    return None


