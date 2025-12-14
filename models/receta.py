from config.db_config import conectarBD

def crear_receta(id_paciente, id_medico, descripcion, medicamentos, costo_clp):
    db = conectarBD()
    cursor = db.obtener_cursor()

    cursor.execute(
        "INSERT INTO receta (id_paciente, id_medico, descripcion, medicamentos, costo_clp) VALUES (:1, :2, :3, :4, :5)",
        (id_paciente, id_medico, descripcion, medicamentos, costo_clp)
    )

    db.connection.commit()
    db.desconectar()
