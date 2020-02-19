from conexion import conexion

def atualisar_datos(datos):
    """
    actualiza resultado_op , fecha_op los datos de la tabla resultados
    :param conn:
    :param task:
    :return: project id
    """ 
    database =  r"C:\src\databases\db_Condensadora\Condesadora.db"
    conex = conexion(database)
    con=conex.get_connection()
    sql = ''' UPDATE resultados
              SET resultado_op = ? , 
                  fecha_op = ?
              WHERE id = ? '''
    cur = con.cursor()
    cur.execute(sql, datos)
    con.commit()
 
 
def main():
    atualisar_datos(('8.098765', '2070-02-19' ,8))
 
if __name__ == '__main__':
    main()
