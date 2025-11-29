from flask import Flask
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'clave_super_secreta_123'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# importar las rutas
from controladores import usuario_controller, contactos_controller

if __name__ == "__main__":
    app.run(debug=True, port=5000)