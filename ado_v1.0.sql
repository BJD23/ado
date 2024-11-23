DROP DATABASE IF EXISTS ado;
CREATE DATABASE ado;
USE ado;

CREATE TABLE cliente(
    cliente_id INT(6) PRIMARY KEY NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    paterno VARCHAR(15) NOT NULL,
    materno VARCHAR(15),
    telefono VARCHAR(10), NOT NULL,
    correo VARCHAR(60) NOT NULL,
    contraseña VARCHAR(256) NOT NULL 
);

CREATE TABLE descuento(
    descuento_id INT(3) PRIMARY KEY NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    cantidad_max INT(2) NOT NULL,
    porcentaje_descuento INT(2) NOT NULL,
    fin_vigencia DATETIME NOT NULL
);

CREATE TABLE Empleado (
    rfc VARCHAR(13) PRIMARY KEY NOT NULL,
    nombres VARCHAR(30) NOT NULL,
    paterno VARCHAR(30) NOT NULL,
    materno VARCHAR(30),
    nss VARCHAR(11),NOT NULL
    telefono VARCHAR(20), NOT NULL
    calle VARCHAR(30),
    numero VARCHAR(4),
    colonia VARCHAR(30),
    cp VARCHAR(5),
    cuenta_bancaria VARCHAR(11) NOT NULL,
    sueldo_diario INT(5) NOT NULL,
    ocupacion VARCHAR(25) NOT NULL,
);

CREATE TABLE chofer (
    chofer_id INT(5) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    vigencia_licencia DATE NOT NULL,
    numero_licencia VARCHAR(20) NOT NULL,
    FOREIGN KEY (rfc) REFERENCES Empleado(rfc)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE corrida (
    corrida_id INT(6) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    precio_corrida DECIMAL(8,2) NOT NULL,
    estatus ENUM --que es esto?? 
);

CREATE TABLE boleto (
    folio INT(12) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estatus VARCHAR(15) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    metodo_pago VARCHAR(30) NOT NULL,
    FOREIGN KEY (corrida_id) REFERENCES corrida(corrida_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE 