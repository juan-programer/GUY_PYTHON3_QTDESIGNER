from conexion import conexion
from models.condensadora import condensadora
class condensadoraController:
    def __init__(self):
        conex = conexion()
        self.con=conex.get_connection()

    def insertar(self,conde):
        consulta = "INSERT INTO condensadora (nombre, longitud, cantidad, resultado) VALUES ( '{}', {} , {}, {} )".format(conde.get_nombre(), conde.get_longitud(), conde.get_cantidad(), conde.get_resultado())
        try:
            self.con.execute(consulta)
            self.con.commit()
            print("Registro Completado")
        except Exception as e:
            print(str(e)+"\n\nError Al Registrar")

    
    def get_all(self):
        consulta = "SELECT * FROM condensadora"
        return self.con.execute(consulta)


    def update(self, conde):
        consulta = "UPDATE condensadora SET nombre = '{}' , longitud = {}, cantidad = {}, resultado = {} WHERE id = {}".format(conde.get_nombre(), conde.get_longitud(), conde.get_cantidad(), conde.get_resultado(), conde.get_id())
        try:    
            self.con.execute(consulta)
            self.con.commit()
            print("Actualización Exitosa")
        except Exception as e:
            print(str(e)+"\n\nError Al Actulizar Datos")
        