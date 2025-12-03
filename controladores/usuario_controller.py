from flask import render_template, request, redirect, session, flash
from app import app
from modelos.usuario_model import registrar_usuario, verificar_usuario, obtener_usuario_por_correo

@app.route('/')
def raiz():
    return redirect('/login')

# Registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        correo = request.form.get('correo', '').strip()
        contrasena = request.form.get('contrasena', '')

        # Validaciones de formato de correo, contraseña >= 8 caracteres
        if len(contrasena) < 8:
            flash('La contraseña debe tener al menos 8 caracteres.', 'danger')
            return render_template('registro.html')
        
        # Se verificará correo único
        if obtener_usuario_por_correo(correo):
            flash('El correo ya se encuentra registrado.', 'danger')
            return render_template('registro.html')
        
        # Registro de ususario
        registrar_usuario(nombre, correo, contrasena)
        flash('El usuario ha sido registrado correctamente.', 'success')
        return redirect('/login')

    return render_template('registro.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo', '').strip()
        contrasena = request.form.get('contrasena', '')
        usuario = verificar_usuario(correo, contrasena)
        if usuario:
            session['usuario_id'] = usuario['id']
            session['nombre'] = usuario['nombre']
            return redirect('/contactos')
        flash('Las credenciales son incorrectas.', 'danger')
    return render_template('login.html')

    # Salir
    @app.route('/salir')
    def salir():
        session.clear()
        return redirect('/login')
    