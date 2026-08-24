from datetime import datetime
from datetime import date

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
        fecha_actual = date.today()

        if self.fecha_de_vencimiento < fecha_actual:
            print("Esta cuota está vencida y ya van", (fecha_actual-self.fecha_de_vencimiento).days,"Dias sin pagar.")
        else:
            
            print("Esta cuota no está vencida y faltan",(self.fecha_de_vencimiento-fecha_actual).days, "días para vencer")

    def mostrar_dias_vencimiento(self):
        fecha_actual= date.today()
        
        print("Faltan",(self.fecha_de_vencimiento-fecha_actual).days, "dais para vencer.")

    def cambiar_fecha_de_vencimiento(self):
        print("Cambiando fecha de vencimiento.")
        fecha_actual = date.today()

        if self.fecha_de_vencimiento < fecha_actual:
            print("Esta cuota está vencida y no se puede cambiar.")
        else:
            anio = int(input("Ingrese el año (ej: 2026): "))

            mes = int(input("Ingrese el mes (1-12): "))

            dia = int(input("Ingrese el día: "))
            self.fecha_de_vencimiento = date(anio, mes, dia)
            print("La fecha de vencimiento fue actualizada a:", self.fecha_de_vencimiento)

micuota= Cuotas("True",2154,"sin pagar", date(2027,2,12),"debito")

micuota.verificar_vencimiento()

micuota.mostrar_dias_vencimiento()

micuota.cambiar_fecha_de_vencimiento()