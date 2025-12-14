import oracledb

class ConexionOracle:
    def __init__(self, user, password, dsn):
        self.user = user
        self.password = password
        self.dsn = dsn
        self.connection = None

    def conectar(self):
        self.connection = oracledb.connect(
            user=self.user,
            password=self.password,
            dsn=self.dsn
        )

    def obtener_cursor(self):
        return self.connection.cursor()

    def desconectar(self):
        if self.connection:
            self.connection.close()
