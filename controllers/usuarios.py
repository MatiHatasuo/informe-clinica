import bcrypt
from config.db_config import conectarBD

def crear_usuario(nombre_usuario, clave, tipo):
    db = conectarBD()
    cursor = db.obtener_cursor()

    clave_encriptada = bcrypt.hashpw(
        clave.encode("utf-8"),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO usuario (nombre_usuario, clave, tipo)
        VALUES (:1, :2, :3)
        """,
        (nombre_usuario, clave_encriptada, tipo)
    )

    db.connection.commit()
    db.desconectar()

    print("Usuario creado correctamente")
