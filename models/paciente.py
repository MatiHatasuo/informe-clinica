from config.db_config import conectarBD

def crear_paciente(id_usuario, comuna, fecha_primera_visita):
    db = conectarBD()
    cursor = db.obtener_cursor()

    cursor.execute(
        "INSERT INTO paciente (id_usuario, comuna, fecha_primera_visita) VALUES (:1, :2, :3)",
        (id_usuario, comuna, fecha_primera_visita)
    )

    db.connection.commit()
    db.desconectar()
