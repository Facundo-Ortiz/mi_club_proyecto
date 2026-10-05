import sqlite3

def conectar(ruta):
    conexion= sqlite3.connect(ruta)
    return conexion

def crear_tabla(conexion):
    cursor= conexion.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS socio(id INTEGER PRIMARY KEY AUTOINCREMENT, ultimo_login TEXT, fecha_inscripcion TEXT, estado TEXT DEFAULT 'Activo', nombre_completo TEXT NOT NULL, edad INTEGER NOT NULL, tipo_identificacion TEXT, identificacion TEXT, nacionalidad TEXT, rol TEXT DEFAULT 'socio', usuario TEXT UNIQUE NOT NULL, contrasenia TEXT NOT NULL)")

    conexion.commit()


def guardar_socio(conexion,socio):
    cursor= conexion.cursor()
    cursor.execute("INSERT INTO socio(ultimo_login,fecha_inscripcion,estado,usuario,contrasenia,nombre_completo,edad,tipo_identificacion,identificacion,nacionalidad,rol)" 
                   "VALUES(?,?,?,?,?,?,?,?,?,?,?)",(
      socio.ultimo_login,
      socio.fecha_inscripcion.isoformat(), 
      socio.estado,
      socio.get_usuario(),
      socio.get_contrasenia(),
      socio.nombre_completo,
      socio.edad,
      socio.get_tipo_identificacion(),
      socio.get_identificacion(),
      socio.get_nacionalidad(),
      socio.rol ))

    conexion.commit()