from flask import Blueprint, render_template
from app.db_connection import get_connection

module1 = Blueprint('module1', __name__, template_folder="../templates")

@module1.route('/module1')
def index():
    connection = get_connection()
    if connection:
        return render_template('module1.html', message="Conexión exitosa a la base de datos.")
    else:
        return render_template('module1.html', message="Error al conectar a la base de datos.")
