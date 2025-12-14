from config.db_config import conectarBD

def crear_insumo(nombre, tipo, stock, costo_usd):
    db = conectarBD()
    cursor = db.obtener_cursor()

    cursor.execute(
        "INSERT INTO insumo (nombre, tipo, stock, costo_usd) VALUES (:1, :2, :3, :4)",
        (nombre, tipo, stock, costo_usd)
    )

    db.connection.commit()
    db.desconectar()
