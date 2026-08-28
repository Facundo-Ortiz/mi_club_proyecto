from persona import Persona

from datetime import datetime

class Socio(Persona):
    def __init__(self,ultimo_login,fecha_inscripcion, estado, usuario, contrasenia, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
        self.lista_clubes = []
        self.lista_cuotas = []
        self.lista_socios_totales= []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.ultimo_login= ultimo_login


    def get_usuario(self):
        return self.__usuario
    def set_usuario (self, usuario_nuevo):
        self.__usuario = usuario_nuevo


    def get_contrasenia(self):
        return self.__contrasenia
    def set_contrasenia(self, contrasenia_nueva):
        self.__contrasenia = contrasenia_nueva
    
    def verificar_inactividad(self):

        fecha_actual= datetime.now()

        dias_inactividad= (fecha_actual-self.ultimo_login).days

        if dias_inactividad>=90:
            print("Esta cuenta ha estado:", dias_inactividad, "Dias inactivos. Suspendiendo cuenta...")
            self.estado= "suspendido" 

    def agregar_socio(self,socio):
        self.lista_socios_totales.append(socio)

    def activar_socios(self):
        
        nombre_scio= input("Ingrese el nombre del socio que desee activar: ")

        for i in self.lista_socios_totales:

            if self.nombre_completo==nombre_scio:
                
                print("La cuenta de",self.nombre_completo,"ha sido activada.")
            
                self.estado="activo"
            else:
                print("No hay ningun socio que corresponda con el nombre buscado")


misocio1= Socio(datetime(2025,3,2),datetime(2025,3,2),"inactivo","sospechoso","aewghts","pablo medina",20,"DNI",48321354,"Argentina")

misocio2= Socio(datetime(2025,3,2),datetime(2025,3,2),"activo","azsa","456456","Alani Rodriguez",22,"DNI",4221314,"Argentina")

misocio3= Socio(datetime(2025,3,2),datetime(2025,3,2),"activo","logan","123789","Logan Suarez",20,"DNI",48621314,"Argentina")

misocio4= Socio(datetime(2025,3,2),datetime(2025,3,2),"suspendido","lolanisa","789963","Lola Salazar",20,"DNI",48421314,"Argentina")


misocio1.agregar_socio(misocio1)
misocio2.agregar_socio(misocio2)
misocio3.agregar_socio(misocio3)
misocio4.agregar_socio(misocio4)

misocio1.activar_socios()
