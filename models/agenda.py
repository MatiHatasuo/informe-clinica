from config.db_config import conectarBD

def crear_agenda(id_paciente, id_medico, fecha_consulta, estado):
    db = conectarBD()
    cursor = db.obtener_cursor()

    cursor.execute(
        "INSERT INTO agenda (id_paciente, id_medico, fecha_consulta, estado) VALUES (:1, :2, :3, :4)",
        (id_paciente, id_medico, fecha_consulta, estado)
    )

    db.connection.commit()
    db.desconectar()
