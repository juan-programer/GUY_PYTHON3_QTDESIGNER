import sqlite3
from sqlite3 import Error
 
 
def crear_conexion(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conectar = None
    try:
        conectar = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conectar
 
 
def inserta_datos(conectar, resultados):
    """
    Crear un nuevo dato en la tabla resultado
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO resultados(id, resultado_op, fecha_op)
              VALUES(?,?,?) '''
    cur = conectar.cursor()
    cur.execute(sql, resultados)
    return cur.lastrowid
 
 
def main():
    base_de_datos =  r"C:\src\databases\db_Condensadora\Condesadora.db"
 
    # create a database connection
    conectar = crear_conexion(base_de_datos)
    with conectar:
        # create a new project
        nuevo_dato = ('8', '8.44444','2021-02-19')
        datos_id = inserta_datos(conectar, nuevo_dato)

 
if __name__ == '__main__':
    main()