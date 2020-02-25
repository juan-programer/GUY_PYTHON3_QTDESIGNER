import sqlite3 
from sqlite3 import Error 
def crear_conexion(db_file): 
    """ crear una conecion a la base de datos """ 
    conectar = None
    try :
        conectar = sqlite3.connect(db_file)
        print( sqlite3.version )
    except Error as e:
        print (e)
    finally:
        if conectar:
            conectar.close()
if __name__   ==   '__main__' :
    crear_conexion(r"C:\src\databases\db_Condensadora\Condesadora.db")