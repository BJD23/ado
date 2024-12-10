from flask import Blueprint, render_template, request
from app.db_connection import get_connection

venta_bp = Blueprint('venta_bp', __name__)

@venta_bp.route('/venta', methods=['GET', 'POST'])
def venta():
    if request.method == 'POST':
        # Recibir datos del formulario
        cliente_nombre = str(request.form.get('nombre'))
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        fecha = request.form.get('fecha')
        asiento_numero = request.form.get('asiento')

        try:
            # Conexión a la base de datos
            connection = get_connection()
            cursor = connection.cursor()

            # Insertar cliente
            cursor.execute("""
                INSERT INTO cliente (nombre) 
                VALUES (%s)
            """, (cliente_nombre))
            connection.commit()

            cliente_id = cursor.lastrowid  # Obtener el ID del cliente

            # Insertar el boleto (aquí los IDs de corrida y descuento son predeterminados)
            cursor.execute("""
                INSERT INTO boleto (nombre, estatus, fecha_hora, metodo_pago, corrida_id, descuento_id, asiento_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (cliente_nombre, "activo", fecha, "efectivo", 1, 1, asiento_numero))
            connection.commit()

            return render_template('venta.html', message="Boleto registrado exitosamente.")
        except Exception as e:
            return render_template('venta.html', message=f"Error al registrar el boleto: {str(e)}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()

    # Obtener las terminales disponibles para origen y destino
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Seleccionar las terminales
        cursor.execute("SELECT nombre, nombre FROM terminal")
        terminales = cursor.fetchall()

    except Exception as e:
        return render_template('venta.html', message=f"Error al cargar terminales: {str(e)}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

    return render_template('venta.html', terminales=terminales)
