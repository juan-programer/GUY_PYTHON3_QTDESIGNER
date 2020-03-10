import sqlite3
from sqlite3 import Error

class conexion:
    def __init__(self, database = r"/home/juan/Documentos/databases/bd_condensadora/Condesadora.db"):
        self.conectar = None
        try:
            self.conectar = sqlite3.connect(database)
        except Error as e:
            print(e)

    def get_connection(self):
        return self.conectar