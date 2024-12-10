from flask import Blueprint, render_template
from app.db_connection import get_connection  # Asegúrate de que esta función esté configurada correctamente

module1 = Blueprint('module1', __name__)

@module1.route('/module1')
def verificar_conexion():
    # Intentar conectar a la base de datos
    connection = get_connection()
    if connection:
        message = "Conexión exitosa a la base de datos."
        connection.close()  # Cerrar la conexión después de usarla
    else:
        message = "Error al conectar a la base de datos."
    
    return render_template('module1.html', message=message)
