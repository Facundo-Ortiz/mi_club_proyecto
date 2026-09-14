from socio import Socio
from persona import Persona
from datetime import date


miprueba= Socio(date(2026,5,21),date(2025,7,4),"activo","loco","didimaestro","Lautaro Jordan",21,"DNI","48206231","Argentina","soc")

print(miprueba.verficar_rol())