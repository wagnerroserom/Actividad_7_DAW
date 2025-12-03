# inspeccionar_login.py
from app import app

print("RUTAS REGISTRADAS:")
for rule in sorted(app.url_map.iter_rules(), key=lambda r: str(r)):
    print(f"{rule} -> endpoint: {rule.endpoint}")

# Información detallada para /login
for rule in app.url_map.iter_rules():
    if str(rule) == '/login':
        ep = rule.endpoint
        func = app.view_functions.get(ep)
        print("\nINFO de /login:")
        print("endpoint:", ep)
        print("view function object:", func)
        if func:
            try:
                print("module:", func.__module__)
                print("function name:", func.__name__)
                print("source file:", func.__code__.co_filename)
                print("line:", func.__code__.co_firstlineno)
            except Exception as e:
                print("No fue posible introspectar más:", e)
