import sqlite3
from sqlite3 import Error
 
 
def crear_conexion(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 
 
def inserta_datos(conn, resultados):
    """
    Crear un nuevo dato en la tabla resultado
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO resultados(id, resultado_op, fecha_op)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, resultados)
    return cur.lastrowid
 
 
def main():
    base_de_datos =  r"C:\src\databases\db_Condensadora\Condesadora.db"
 
    # create a database connection
    conn = crear_conexion(base_de_datos)
    with conn:
        # create a new project
        nuevo_dato = ('4', '8.44444','2020-02-17')
        datos_id = inserta_datos(conn, nuevo_dato)

 
if __name__ == '__main__':
    main()