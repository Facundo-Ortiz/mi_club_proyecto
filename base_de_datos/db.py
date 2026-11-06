import sqlite3
from modelos.socio import Socio
from datetime import date

def conectar(ruta):
    conexion= sqlite3.connect(ruta)
    return conexion

def crear_tabla(conexion):
    cursor= conexion.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS socios(id INTEGER PRIMARY KEY AUTOINCREMENT, ultimo_login TEXT, fecha_inscripcion TEXT, estado TEXT DEFAULT 'Activo', nombre_completo TEXT NOT NULL, edad INTEGER NOT NULL, tipo_identificacion TEXT, identificacion TEXT, nacionalidad TEXT, usuario TEXT UNIQUE NOT NULL, contrasenia TEXT NOT NULL, rol TEXT DEFAULT 'socio')")

    cursor.execute("CREATE TABLE IF NOT EXISTS cuotas(cuota_id INTEGER PRIMARY KEY AUTOINCREMENT, monto FLOAT NOT NULL, estado TEXT DEFAULT 'Pendiente',fecha_de_vencimiento TEXT NOT NULL,metodo_de_pago TEXT NOT NULL,id_socio INTEGER NOT NULL, FOREIGN KEY (id_socio) REFERENCES socios(id))")

    cursor.execute("CREATE TABLE IF NOT EXISTS clubes(club_id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT, ubicacion TEXT NOT NULL, presidente TEXT NOT NULL, fecha_fundacion TEXT NOT NULL)")

    cursor.execute("CREATE TABLE IF NOT EXISTS actividades(actividad_id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, dia TEXT NOT NULL, horario TEXT NOT NULL)")

    cursor.execute("CREATE TABLE IF NOT EXISTS socio_actividad( id_socio INTEGER, id_actividad INTEGER, PRIMARY KEY (id_socio,id_actividad), FOREIGN KEY (id_socio) REFERENCES socios(id), FOREIGN KEY (id_actividad) REFERENCES actividades(actividad_id))")

    conexion.commit()


def guardar_socio(conexion,socio):
    cursor= conexion.cursor()
    cursor.execute("INSERT INTO socios(ultimo_login,fecha_inscripcion,estado,nombre_completo,edad,tipo_identificacion,identificacion,nacionalidad,usuario,contrasenia,rol)" 
                   "VALUES(?,?,?,?,?,?,?,?,?,?,?)",(
      socio.ultimo_login.isoformat(),
      socio.fecha_inscripcion.isoformat(), 
      socio.estado,
      socio.nombre_completo,
      socio.edad,
      socio.get_tipo_identificacion(),
      socio.get_identificacion(),
      socio.get_nacionalidad(),
      socio.get_usuario(),
      socio.get_contrasenia(),
      socio.rol ))
    
    conexion.commit()
    
def guardar_cuota(conexion,usuario1,cuota):

    cursor= conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario=?",(usuario1,))

    fila= cursor.fetchone()

    if fila is None:
        raise ValueError("El socio no existe")
    else:
        id_socio= fila[0]

        cursor.execute("INSERT INTO cuotas(monto, estado, fecha_de_vencimiento, metodo_de_pago,id_socio) " "VALUES(?,?,?,?,?)",(
            cuota.monto,
            cuota.get_estado(),
            cuota.fecha_de_vencimiento,
            cuota.metodo_de_pago,
            id_socio,
            )



    )
    conexion.commit()



def obtener_club(conexion):
    cursor= conexion.cursor()

    cursor.execute("SELECT nombre, descripcion, ubicacion, presidente, fecha_fundacion FROM clubes LIMIT 1")
    fila = cursor.fetchone()
    if fila is None:
        return None
    else: 
        nombre, descripcion, ubicacion, presidente, fecha_fundacion = fila
        from modelos.club import Club
        return Club(nombre, descripcion, ubicacion, presidente, fecha_fundacion)



def guardar_club(conexion,club):
    cursor= conexion.cursor()
    cursor.execute("INSERT INTO clubes(nombre,descripcion,ubicacion,presidente,fecha_fundacion)" 
                   "VALUES(?,?,?,?,?)",(
        club.nombre,
        club.descripcion,
        club.ubicacion,
        club.get_presidente(),
        club.get_fecha()
     
                   )
    )
    conexion.commit()
    

def guardar_actividad(conexion,actividad):
    cursor= conexion.cursor()
    cursor.execute("INSERT INTO actividades(nombre, dia, horario)" 
                   "VALUES(?,?,?)",(
      actividad.nombre,
      actividad.dia,
      actividad.horario))
    
    conexion.commit()

def listar_cuotas_de_socio(conexion,usuario1):
    cursor= conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario=?", (usuario1,))

    fila= cursor.fetchone()

    if fila is None:
        return []
    else:
        id_socio= fila[0]

        cursor.execute("SELECT monto,estado,fecha_de_vencimiento,metodo_de_pago FROM cuotas WHERE id_socio=?", (id_socio,))
    
        return cursor.fetchall()
    

def buscar_socio_por_usuario(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return None
    
    socio = Socio(
        date.fromisoformat(fila[1]), 
        date.fromisoformat(fila[2]),
        fila[3],
        fila[4],
        fila[5],
        fila[6],
        fila[7],
        fila[8],
        fila[9],
        fila[10],
        fila[11]
    )
    return socio

def anotar_socio_actividad(conexion,usuario,nombre):
    cursor= conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario=?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
            return "El socio no existe."
    else:
        id_socio= fila[0]

    cursor.execute("SELECT actividad_id FROM actividades WHERE nombre = ?", (nombre,))
    fila = cursor.fetchone()
    if fila is None:
        return f"La actividad {nombre} no existe."
    actividad_id = fila[0]

    cursor.execute("INSERT OR IGNORE INTO socio_actividad(id_socio,id_actividad) VALUES (?,?)", (id_socio,actividad_id,)
    )
    conexion.commit()
    return f'Te anotaste en {nombre}.'

def desanotar_socio_actividad(conexion,usuario,nombre_actividad):
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    else:
        id_socio= fila[0]

    cursor.execute("SELECT actividad_id FROM actividades WHERE nombre = ?", (nombre_actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return "La actividad no existe."
    else:
        actividad_id= fila[0]

    cursor.execute("DELETE FROM socio_actividad WHERE id_socio = ? AND id_actividad= ? ", (id_socio,actividad_id,))
    conexion.commit()
    return f'Te desanotaste de {nombre_actividad}'

def listar_actividades_de_socio(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT a.nombre, a.dia, a.horario FROM actividades AS a JOIN socio_actividad AS sa ON sa.id_actividad = a.actividad_id JOIN socios s ON s.id = sa.id_socio WHERE s.usuario = ?",
        (usuario,),
    )
    return cursor.fetchall()
