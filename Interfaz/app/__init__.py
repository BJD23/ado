from flask import Flask
from app.routes.module1 import module1
from app.routes.module2 import module2
from app.routes.venta import venta_bp  # Importar la nueva ruta

def create_app():
    app = Flask(__name__)
    app.register_blueprint(module1)
    app.register_blueprint(module2)
    app.register_blueprint(venta_bp)  # Registrar la nueva ruta
    return app
