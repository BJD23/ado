from flask import Flask
from app.routes.module1 import module1
from app.routes.module2 import module2

def create_app():
    app = Flask(__name__)
    app.register_blueprint(module1)
    app.register_blueprint(module2) 
    return app
