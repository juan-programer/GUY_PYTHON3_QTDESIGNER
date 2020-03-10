import sqlite3 , datetime      
from sqlite3 import Error   

def crear_conexion(db_file):
    conectar = None
    try:                  
        conectar = sqlite3.connect(db_file)
        return conectar
    except Error as e:
        print(e)
    return conectar

def crear_tablas(conectar, create_table_sql):
    try:
        consulta = conectar.cursor()
        consulta.execute(create_table_sql)
    except Error as e:
        print(e)

def principal():
    base_de_datos = r"/home/juan/Documentos/databases/bd_condensadora/Condesadora.db"
    
    crear_tabla_Condensadora_sql = """ CREATE TABLE "condensadora" (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                "nombre"	TEXT,
                                                "longitud"	REAL,
                                    "cantidad"	INTEGER DEFAULT 0,
                                    "resultado"	REAL DEFAULT 0.0); """

    conectar = crear_conexion(base_de_datos)
    if conectar is not None:
        crear_tablas(conectar,crear_tabla_Condensadora_sql)
    else:
        print("Error! No se puede crear la conexión de la base de datos.")

if __name__ == "__main__":
    principal()