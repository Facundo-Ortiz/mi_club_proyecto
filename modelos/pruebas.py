import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from socio import Socio
from persona import Persona
from cuotas import Cuotas
from actividad import Actividad
from club import Club
from datetime import date
from pathlib import Path
from base_de_datos.db import conectar, crear_tabla, guardar_socio,guardar_cuota,listar_cuotas_de_socio,buscar_socio_por_usuario,guardar_actividad,guardar_club,listar_actividades_de_socio,anotar_socio_actividad,desanotar_socio_actividad
from servicios.servicio_autenticacion import autenticar,RUTA_DB

ruta = RUTA_DB

if ruta.exists():
    ruta.unlink()

conexion1 = conectar(str(ruta))
crear_tabla(conexion1)

if ruta.exists():
    ruta.unlink()

conexion1= conectar(str(ruta))
crear_tabla(conexion1)



miprueba= Socio(date(2026,5,25),date(2025,7,4),"activo","loco","didimaestro","Lautaro Jordan",21,"DNI","48206231","Argentina","socio")

miprueba1= Socio(date(2023,6,22),date(2025,7,4),"activo","oi","deah","Fede Comunica",21,"DNI","48206531","Argentina","socio")

miprueba2= Socio(date(2022,1,21),date(2025,7,4),"activo","queque","ertete","Kayla Mcqueen",21,"DNI","42206231","Argentina","socio")

miactividad1= Actividad("Fulbo",22,2332521)

miactividad2= Actividad("voaley",12,2332523)

miactividad3= Actividad("teni",14,2252351)

miclub= Club("agea","afweaaete0","laesquina","chavo",date(2026,2,21))





for usuario in ("loco","oi","queque"):
    buscar_socio_por_usuario(conexion1,usuario)



# Guardar Socios
guardar_socio(conexion1,miprueba)
guardar_socio(conexion1,miprueba1)
guardar_socio(conexion1,miprueba2)


# Guardar Cuotas
guardar_cuota(conexion1,miprueba.get_usuario(),Cuotas(123124,"Pendiente",date(2026,12,14),"mercado libre"))
guardar_cuota(conexion1,miprueba1.get_usuario(),Cuotas(1124,"Pendiente",date(2026,11,12),"mercado libre"))
guardar_cuota(conexion1,miprueba2.get_usuario(),Cuotas(124,"Pendiente",date(2026,11,13),"mercado libre"))


# Guardar actividades 
guardar_actividad(conexion1,miactividad1)
guardar_actividad(conexion1,miactividad2)
guardar_actividad(conexion1,miactividad3)

# Guardar clubes

guardar_club(conexion1,miclub)

conexion1.commit()

print(autenticar("oi","deah"))

conexion1.close()