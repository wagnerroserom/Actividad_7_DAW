# listar_rutas.py
from app import app

print("RUTAS REGISTRADAS:")
for rule in sorted(app.url_map.iter_rules(), key=lambda r: str(r)):
    print(f"{rule} -> {sorted(rule.methods)}")
