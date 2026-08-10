from datetime import datetime

class Cuotas:
    def __init__(self,numero_cuota, monto,  estado, fecha_de_vencimiento, metodo_de_pago):
        self.numero_cuota = numero_cuota
        self.monto = monto
        self.estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.metodo_de_pago = metodo_de_pago


    def get_estado (self):
        return self.__estado
    def set_estado (self, estado_modificado):
        self.__estado = estado_modificado
    
    def verificar_vencimiento(self):
        fecha_actual= datetime.now().date

        if self.fecha_de_vencimiento<fecha_actual:
            print("esta cuota no esta vencida y faltan", fecha_actual-self.fecha_de_vencimiento, "dias para vencer")
        
        else:
            print("Esta cuota si esta vencida")
        

micuota= Cuotas("True",2021,"veranpo")

micuota.verificar_vencimiento()