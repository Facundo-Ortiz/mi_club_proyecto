
from datetime import date

class Cuotas:
    def __init__(self,numero_cuota, monto,  estado, fecha_de_vencimiento, metodo_de_pago):
        self.numero_cuota = numero_cuota
        self.monto = monto
        self.__estado = estado
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.metodo_de_pago = metodo_de_pago


    def get_estado (self):
        return self.__estado
    def set_estado (self, estado_modificado):
        self.__estado = estado_modificado
    
    def verificar_vencimiento(self):
        fecha_actual = date.today()

        if self.fecha_de_vencimiento > fecha_actual:
            print("Esta cuota está vencida y ya van", (fecha_actual-self.fecha_de_vencimiento).days,"Dias sin pagar.")
        else:
            
            print("Esta cuota no está vencida y faltan",(self.fecha_de_vencimiento-fecha_actual).days, "días para vencer")
        

# abs()= convierte valores negativos a postivos :)

micuota= Cuotas("True",2154,"sin pagar", date(2027,2,12),"debito")

micuota.verificar_vencimiento()