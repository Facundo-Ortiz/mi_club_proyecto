import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from socio import Socio
from persona import Persona
from datetime import date
from datetime import date
from pathlib import Path
from base_de_datos.db import conectar, crear_tabla, guardar_socio


miprueba= Socio(date(2026,5,21),date(2025,7,4),"activo","loco","didimaestro","Lautaro Jordan",21,"DNI","48206231","Argentina","soc")

ruta= Path(__file__).parent / "club.db"

conectar(ruta)

conexion1= conectar(str(ruta))

crear_tabla(conexion1)

guardar_socio(conexion1,miprueba)