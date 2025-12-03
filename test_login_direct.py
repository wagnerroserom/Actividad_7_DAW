from app import app
from controladores import usuario_controller

with app.test_request_context('/login'):
    try:
        salida = usuario_controller.login()
        print("OK - login() ejecutado, tipo:", type(salida))
    except Exception as e:
        import traceback
        traceback.print_exc()
