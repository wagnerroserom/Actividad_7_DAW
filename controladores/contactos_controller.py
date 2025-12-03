
from flask import render_template, request, redirect, session, flash
from app import app
from modelos.contactos_model import (
    listar_contactos, agregar_contacto, obtener_contacto_por_id,
    actualizar_contacto, eliminar_contacto
)

@app.route('/contactos')
def contactos():
    # Verificar sesión
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
        # Usar 'correo' para mantener consistencia con el resto del proyecto
        correo = request.form.get('correo', '').strip()
        telefono = request.form.get('telefono', '').strip()
        notas = request.form.get('notas', '').strip()

        # Validación: nombre obligatorio
        if not nombre:
            flash('El nombre es obligatorio.', 'danger')
            return render_template('formulario_contacto.html', accion='Agregar')

        # Agregar contacto en la BD
        agregar_contacto(session['usuario_id'], nombre, correo, telefono, notas)
        flash('Contacto agregado correctamente.', 'success')
        return redirect('/contactos')

    return render_template('formulario_contacto.html', accion='Agregar')


@app.route('/contactos/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'usuario_id' not in session:
        return redirect('/login')

    contacto = obtener_contacto_por_id(id, session['usuario_id'])
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
        flash('Contacto actualizado correctamente.', 'success')
        return redirect('/contactos')

    return render_template('formulario_contacto.html', accion='Editar', contact=contacto)


@app.route('/contactos/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    if 'usuario_id' not in session:
        return redirect('/login')

    # Si la petición es POST, proceder a eliminar
    if request.method == 'POST':
        eliminar_contacto(id, session['usuario_id'])
        flash('Contacto eliminado.', 'success')
        return redirect('/contactos')

    # Si se accede por GET, mostrar confirmación simple
    return render_template('confirmar_eliminar.html', id=id)
