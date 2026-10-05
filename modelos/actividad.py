from datetime import date

class Actividad:
    def __init__(self,nombre,dia,horario):
        self.nombre= nombre
        self.dia= dia
        self.horario= horario
    
    def informacion_de_actividad(self):

        return f'Actividad: {self.nombre} , en el dia: {self.dia}, su horario es de: {self.horario}'