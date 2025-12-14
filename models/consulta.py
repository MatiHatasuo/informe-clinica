from config.db_config import conectarBD

def crear_consulta(id_paciente, id_medico, id_receta, fecha, comentarios, valor):
    db = conectarBD()
    cursor = db.obtener_cursor()

    cursor.execute(
        "INSERT INTO consulta (id_paciente, id_medico, id_receta, fecha, comentarios, valor) VALUES (:1, :2, :3, :4, :5, :6)",
        (id_paciente, id_medico, id_receta, fecha, comentarios, valor)
    )

    db.connection.commit()
    db.desconectar()
