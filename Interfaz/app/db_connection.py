import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        # Crear conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            database="ado",
            user="root",
            password="adosiempreprimera"
        )
        
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
        else:
            print("Error al conectar a la base de datos")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None
