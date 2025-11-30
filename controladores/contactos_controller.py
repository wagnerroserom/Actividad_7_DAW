from flask import render_template, request, redirect, session, flash
from app import app
from modelos.contactos_model import (
    listar_contactos, agregar_contacto, obtener_contacto_por_id, actualizar_contacto, eliminar_contacto
)

@app.route('/contactos')
def contactos():
    if 'usuario_id' not in session:
        return redirect('/login')
    data = listar_contactos(session['usuario_id'])
    return render_template('contactos.html', contactos=data)

@app.route('/contactos/agregar', methods=['GET', 'POST'])
def agregar():
    if 'usuario_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        correo = request.form.get('email', '').strip()
        telefono = request.form.get('telefono', '').strip()
        notas = request.form.get('notas', '').strip()

        # Para la validación el nombre debe ser obligatorio, el correo es opcional
        if not nombre:
            flash('El nombre es obligatorio.', 'danger')
            return render_template('formulario_contacto.html', accion='Agregar')
        
        agregar_contacto(session['usuario_id'], nombre, correo, telefono, notas)
        return redirect('/contactos')
    return render_template('formulario_contacto.html', accion='Agregar')

@app.route('/contactos/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    contacto = obtener_contacto_por_id(id, session['usuario:id'])
    if not contacto:
        flash('Contacto no encontrado.', 'danger')
        return redirect('/contactos')
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        correo = request.form.get('correo', '').strip()
        telefono = request.form.get('telefono', '').strip()
        notas = request.form.get('notas', '').strip()
        if not nombre:
            flash('El nombre es obligatorio.', 'danger')
            return render_template('formulario_contacto.html', accion='Editar', contact=contacto)
        actualizar_contacto(id, session['usuario_id'], nombre, correo, telefono, notas)
        return redirect('/contactos')
    return render_template('formulario_contacto.html', accion='Editar', contact=contacto)

@app.route('/contactos/eliminar/<int:id>')
def eliminar(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    eliminar_contacto(id, session['usuario_id'])
    return redirect('/contactos') 
