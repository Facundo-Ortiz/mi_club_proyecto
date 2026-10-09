import sqlite3

def conectar(ruta):
    conexion= sqlite3.connect(ruta)
    return conexion

def crear_tabla(conexion):
    cursor= conexion.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS socios(id INTEGER PRIMARY KEY AUTOINCREMENT, ultimo_login TEXT, fecha_inscripcion TEXT, estado TEXT DEFAULT 'Activo', nombre_completo TEXT NOT NULL, edad INTEGER NOT NULL, tipo_identificacion TEXT, identificacion TEXT, nacionalidad TEXT, rol TEXT DEFAULT 'socio', usuario TEXT UNIQUE NOT NULL, contrasenia TEXT NOT NULL)")

    cursor.execute("CREATE TABLE IF NOT EXISTS cuotas(cuota_id INTEGER PRIMARY KEY AUTOINCREMENT, monto FLOAT NOT NULL, estado TEXT DEFAULT 'Pendiente',fecha_de_vencimiento TEXT NOT NULL,metodo_de_pago TEXT NOT NULL,id_socio INTEGER NOT NULL, FOREIGN KEY (id_socio) REFERENCES socios(id))")

    conexion.commit()


def guardar_socio(conexion,socio):
    cursor= conexion.cursor()
    cursor.execute("INSERT INTO socios(ultimo_login,fecha_inscripcion,estado,usuario,contrasenia,nombre_completo,edad,tipo_identificacion,identificacion,nacionalidad,rol)" 
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
    
def guardar_cuota(conexion,usuario,cuota):

    cursor= conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario=?",(usuario,))

    fila= cursor.fetchone()

    if fila is None:
        raise ValueError("El socio no existe")
    else:
        id_socio= fila[0]

        cursor.execute("INSERT INTO cuotas(monto, estado, fecha_de_vencimiento, metodo_de_pago,id_socio) " "VALUES(?,?,?,?,?)",(
            cuota.monto,
            cuota.get_estado(),
            cuota.fecha__de_vencimiento,
            cuota.metodo_de_pago,
            id_socio,
            )



    )


    conexion.commit()

def listar_cuotas_de_socio(conexion,usuario):
    cursor= conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario=?", (usuario,))

    fila= cursor.fetchone()

    if fila is None:
        return []
    else:
        id_socio= fila[0]

        cursor.execute("SELECT monto,estado,fecha_de_vencimiento,metodo_de_pago FROM cuotas WHERE id_socio=?", (id_socio,))
    
        return cursor.fetchall()