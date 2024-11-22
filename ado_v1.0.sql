DROP DATABASE IF EXISTS ado;
CREATE DATABSE ado;
USE ado;

CREATE TABLE IF NOT EXISTS cliente(
    cliente_id INT NOT NULL,
    nombre VARCHAR(40) NOT NULL,
    paterno VARCHAR(40) NOT NULL,
    materno VARCHAR(40),
    telefono VARCHAR(10), NOT NULL,
    correo VARCHAR(80) NOT NULL,
    contraseña VARCHAR(255) NOT NULL 
);