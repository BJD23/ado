from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')  # Configuración desde config.py
    init_routes(app)  # Registrar rutas
    return app
