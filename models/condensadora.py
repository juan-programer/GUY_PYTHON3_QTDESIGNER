class condensadora:
    def __init__(self):
        self.id = None
        self.nombre = "Anonymous"
        self.longitud = 0.0
        self.cantidad = 1
        self.resultado = 0

    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
        
    def set_nombre(self, e):
        self.nombre = e

    def get_longitud(self):
        return self.longitud

    def set_longitud(self, e):
        self.longitud = e

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, e):
        self.cantidad = e

    def get_resultado(self):
        return self.resultado

    def set_resultado(self, e):
        self.resultado = e