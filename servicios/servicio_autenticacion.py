import tkinter as tk #traigo la biblioteca de TKINTER
from base_de_datos.db import conectar, buscar_socio_por_usuario
from pathlib import Path
from modelos.socio import Socio

RUTA_DB = Path(__file__).parent.parent / "club.db"


# Crear una pequeña app con etiqueta de texto 
# que sea un saludo integrando el nombre que ingrese el usuario,
#  entrada para que el usuario ingrese nombre y botón que sea que cuando lo 
# presiones obtenga el nombre y devuelva el saludo completo . 



def autenticar(usuario, contrasenia):
    conexion = conectar(str(RUTA_DB))
    socio = buscar_socio_por_usuario(conexion, usuario)
    conexion.close()

    if socio is None:
        return None
    if contrasenia == socio.get_contrasenia():
        return socio
    return None

