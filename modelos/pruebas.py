import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from socio import Socio
from persona import Persona
from cuotas import Cuotas
from datetime import date
from pathlib import Path
from base_de_datos.db import conectar, crear_tabla, guardar_socio,guardar_cuota,listar_cuotas_de_socio,buscar_socio_por_usuario

ruta= Path(__file__).parent / "club.db"

if ruta.exists():
    ruta.unlink()

conexion1= conectar(str(ruta))
crear_tabla(conexion1)



miprueba= Socio(date(2026,5,25),date(2025,7,4),"activo","loco","didimaestro","Lautaro Jordan",21,"DNI","48206231","Argentina","socio")

miprueba1= Socio(date(2023,6,22),date(2025,7,4),"activo","oi","deah","Fede Comunica",21,"DNI","48206531","Argentina","socio")

miprueba2= Socio(date(2022,1,21),date(2025,7,4),"activo","queque","ertete","Kayla Mcqueen",21,"DNI","42206231","Argentina","socio")

# Guardar Socios
guardar_socio(conexion1,miprueba)
guardar_socio(conexion1,miprueba1)
guardar_socio(conexion1,miprueba2)


# Guardar Cuotas
guardar_cuota(conexion1,miprueba.get_usuario(),Cuotas(123124,"Pendiente",date(2026,12,14),"mercado libre"))
guardar_cuota(conexion1,miprueba1.get_usuario(),Cuotas(1124,"Pendiente",date(2026,11,12),"mercado libre"))
guardar_cuota(conexion1,miprueba2.get_usuario(),Cuotas(124,"Pendiente",date(2026,11,13),"mercado libre"))

#for usuario in ("loco","oi","queque"):
#    print(f"Cuotas de {usuario}:")
#    for cuota in listar_cuotas_de_socio(conexion1,usuario):
#        print("",cuota)


print(buscar_socio_por_usuario(conexion1,miprueba1.get_usuario()))

conexion1.close()