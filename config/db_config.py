from config.conexion_oracle import ConexionOracle

def conectarBD():
    db = ConexionOracle("system", "mati", "localhost:1521/xe")
    db.conectar()
    return db
