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
    base_de_datos = r"C:\src\databases\db_Condensadora\Condesadora.db"
    

    crear_tabla_resultados_sql = """  CREATE TABLE IF NOT EXISTS resultados(
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            resultado_op FLOAT(100) NOT NULL,
                            fecha_op DATE NOT NULL );  """

    conectar = crear_conexion(base_de_datos)
    if conectar is not None:
        crear_tablas(conectar,crear_tabla_resultados_sql)
    else:
        print("Error! No se puede crear la conexión de la base de datos.")

if __name__ == "__main__":
    principal()