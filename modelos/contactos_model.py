from config import conexion

def listar_contactos(usuario_id):
    conn = conexion()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM contactos WHERE usuario_id = %s ORDER BY fecha_creacion DESC", (usuario_id,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def agregar_contacto(usuario_id, nombre, correo, telefono, detalle):
    conn = conexion()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contactos (usuario_id, nombre, correo, telefono, detalle) VALUES (%s, %s, %s, %s, %s)",
        (usuario_id, nombre, correo, telefono, detalle)
    )
    conn.commit()
    cur.close()
    conn.close()

def obtener_contacto_por_id(id, usuario_id):
    conn = conexion()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT *FROM contactos WHERE id=%s AND usuario_id=%s", (id, usuario_id))
    contacto = cur.fetchone()
    cur.close()
    conn.close()
    return contacto

def actualizar_contacto(id, usuario_id, nombre, correo, telefono, detalle):
    conn = conexion()
    cur = conn.cursor()
    cur.execute(
        "UPDATE contactos SET nombre=%s, correo=%s, telefono=%s, detalle=%s WHERE id=%s AND usuario_id=%s", 
        (nombre, correo, telefono, detalle, id usuario_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def eliminar_contacto(id, usuario_id):
    conn = conexion()
    cur = conn.cursor()
    cur.execute("DELETE FROM contactos WHERE id=%s AND usuario_=%s", (id, usuario_id))
    conn.commit()
    cur.close()
    conn.close()
    