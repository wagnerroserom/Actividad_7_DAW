from config import conexion
from werkzeug.security import generate_password_hash, check_password_hash

def registrar_usuario(nombre, correo, contrasena):
    """ Permite registrar un usuario con contraseña hasheada. """

    conn = conexion()
    cur = conn.cursor()
    hash_pass = generate_password_hash(contrasena)
    cur.execute(
        "INSERT INTO usuarios(nombre, correo, contrasena_hash) VALUES (%s, %s, %s)",
        (nombre, correo, hash_pass)
    )
    conn.commit()
    cur.close()
    conn.close()

def obtener_usuario_por_correo(correo):
    conn = conexion()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
    usuario = cur.fetchone()
    cur.close()
    conn.close()
    return usuario

def verificar_usuario(correo, contrasena):
    """ Devuelve el usuario si la contraseña es la correcta. """

    usuario = obtener_usuario_por_correo(correo)
    if usuario and check_password_hash(usuario['contrasena_hash'], contrasena):
        return usuario
    return None