from persona import Persona

from datetime import datetime

class Socio(Persona):
    def __init__(self,ultimo_login,fecha_inscripcion, estado, usuario, contrasenia, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad,rol):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
        self.lista_clubes = []
        self.lista_cuotas = []
        self.lista_socios_totales= []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado = estado
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.ultimo_login= ultimo_login
        self.rol= rol


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
            self.estado= "suspendido"
            return f'Esta cuenta ha estado:, {dias_inactividad}, Dias inactivos. Suspendiendo cuenta...)'
            

    def agregar_socio(self,socio):
        self.lista_socios_totales.append(socio)

    def activar_socios(self):
        
        nombre_scio= input("Ingrese el nombre del socio que desee activar: ")

        for i in self.lista_socios_totales:

            if self.nombre_completo==nombre_scio:
                
                self.estado="activo"

                return f'La cuenta de', {self.nombre_completo} ,'ha sido activada.'
    
                
            else:
                return f'No hay ningun socio que corresponda con el nombre buscado'
            
    def verficar_rol(self):
        if self.rol=="admin":
            return f'La cuenta de {self.nombre_completo}, tiene rol de administrador.'
        elif self.rol=="socio":
            return f'La cuenta de {self.nombre_completo},tiene rol de socio.'
       