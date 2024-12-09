from .module1 import module1
from .module2 import module2  # Otros módulos

def init_routes(app):
    app.register_blueprint(module1, url_prefix='/module1')
    app.register_blueprint(module2, url_prefix='/module2')
