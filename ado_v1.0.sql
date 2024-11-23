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
    estatus ENUM("Disponible", "No disponible") NOT NULL 
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

CREATE TABLE autobus (
    autobus_id INT(5) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    matricula CHAR(7) NOT NULL,
    tipo VARCHAR(15) NOT NULL,
    marca VARCHAR(15) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    total_asiento INT(2) NOT NULL,
    num_columna INT(2) NOT NULL,
    num_fila INT(2) NOT NULL
);

CREATE TABLE asiento (
    num_asiento INT(2) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    fila INT(2) NOT NULL,
    FOREIGN KEY (corrida_id) REFERENCES corrida(corrida_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    FOREIGN KEY (folio) REFERENCES boleto(folio)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    FOREIGN KEY (autobus_id) REFERENCES autobus(autobus_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE localidad (
    localidad_id INT(4) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(25) NOT NULL,
    clave CHAR(3) NOT NULL,
    estado VARCHAR(25) NOT NULL 
);

CREATE TABLE terminal (
    terminal_id INT(4) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    cp INT(5) NOT NULL
    calle VARCHAR(40) NOT NULL,
    telefono CHAR(10) NOT NULL,
    estatus ENUM("Activa", "Inactiva") NOT NULL,
    localidad_id INT(4) NOT NULL, --llave foranea
    FOREIGN KEY (localidad_id) REFERENCES localidad(localidad_id)
);

CREATE TABLE ruta (
    ruta_id INT(5) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    origen VARCHAR(30) NOT NULL,
    destino VARCHAR(30) NOT NULL,
    estatus ENUM("Disponible", "No disponible") NOT NULL,
    terminal_id INT(4) NOT NULL,
    FOREIGN KEY (terminal_id) REFERENCES terminal(terminal_id)
);

CREATE TABLE subruta (
    subruta_id INT(5) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    origen VARCHAR(30) NOT NULL,
    destino VARCHAR(30) NOT NULL,
    distancia INT(4) NOT NULL,
    tiempo_aprox TIME NOT NULL,
    estatus ENUM("Disponible", "No disponible") NOT NULL,
    ruta_id INT(5) NOT NULL,
    FOREIGN KEY (ruta_id) REFERENCES ruta(ruta_id)
);

CREATE TABLE amenidad (
    amenidad_id INT(4) PRIMARY KEY NOT NULL,--duda del tamaño 4
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR NOT NULL
);

CREATE TABLE marca (
    marca_id INT(1) PRIMARY KEY NOT NULL,
    marca VARCHAR(30) NOT NULL,
    servicio VARCHAR(15) NOT NULL
);

CREATE TABLE factura (
    folio_fiscal CHAR(36) PRIMARY KEY NOT NULL,
    rfc VARCHAR(13) NOT NULL,
    razon_social VARCHAR(100) NOT NULL,
    reg_fiscal VARCHAR(100) NOT NULL,
    domicilio VARCHAR(200) NOT NULL,
    subtotal INT(5) NOT NULL,
    impuestos INT(5) not NULL,
    total INT(5) NOT NULL
);

CREATE TABLE saldo_max (
    numero_tarjeta INT(16) PRIMARY KEY NOT NULL,
    nombre_titular VARCHAR(60) NOT NULL,
    saldo INT(5) NOT NULL,
    ultimo_movimiento INT(5) NOT NULL,
    final_vigencia DATE(10),
    estatus ENUM("Activa", "Inactiva") NOT NULL--cambio de varchar a enum
);