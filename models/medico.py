from config.db_config import conectarBD

def crear_medico(id_usuario, especialidad, horario, fecha_ingreso):
    db = conectarBD()
    cursor = db.obtener_cursor()

    cursor.execute(
        "INSERT INTO medico (id_usuario, especialidad, horario_atencion, fecha_ingreso) VALUES (:1, :2, :3, :4)",
        (id_usuario, especialidad, horario, fecha_ingreso)
    )

    db.connection.commit()
    db.desconectar()
