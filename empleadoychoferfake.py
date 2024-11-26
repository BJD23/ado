import random
from faker import Faker
import string

fake = Faker('es_MX')  # Configurar Faker para generar datos de México

# Generar RFC único de 11 caracteres
rfc_usados = set()  # Set para almacenar los RFCs generados

def generar_rfc():
    while True:
        rfc = fake.random_number(digits=11)  # Genera un número aleatorio de 11 dígitos
        rfc_str = str(rfc)
        if len(rfc_str) == 11 and rfc_str not in rfc_usados:
            rfc_usados.add(rfc_str)
            return rfc_str

# Generar NSS de 11 dígitos
def generar_nss():
    return str(fake.random_number(digits=11))

# Generar número de teléfono de 10 dígitos
def generar_telefono():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

# Función para generar el número de licencia con letra aleatoria seguida de 8 dígitos
def generar_numero_licencia():
    letra = random.choice(string.ascii_uppercase)  # Genera una letra aleatoria
    numeros = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # Genera 8 dígitos aleatorios
    return letra + numeros  # Une la letra y los números

# Lista de códigos postales de México (solo algunos ejemplos)
codigos_postales = ['01000', '02000', '03000', '04000', '05000', '06000', '07000', '08000', '09000', '10000', '11000', '12000', '13000', '14000', '15000', '16000', '17000', '18000', '19000', '20000', '21000', '22000', '23000', '24000', '25000', '26000', '27000', '28000', '29000', '30000', '31000', '32000', '33000', '34000', '35000', '36000', '37000', '38000', '39000', '40000', '41000', '42000', '43000', '44000', '45000', '46000', '47000', '48000', '49000', '50000', '51000', '52000', '53000', '54000', '55000', '56000', '57000', '58000', '59000', '60000', '61000', '62000', '63000', '64000', '65000', '66000', '67000', '68000', '69000', '70000', '71000', '72000', '73000', '74000', '75000', '76000', '77000', '78000', '79000', '80000', '81000', '82000', '83000', '84000', '85000', '86000', '87000', '88000', '89000', '90000', '91000', '92000', '93000', '94000', '95000', '96000', '97000', '98000', '99000', '18300', '27400', '96500', '07130']

# Generar datos de empleados
def generar_empleado():
    nombre = fake.first_name()
    paterno = fake.last_name()
    materno = fake.last_name() if random.choice([True, False]) else None
    telefono = generar_telefono()
    correo = fake.email()
    cuenta_bancaria = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    ciudad = fake.city()

    # Ocupación aleatoria
    ocupaciones = {
        'Asesor de ventas': 0.07,
        'Mecánico': 0.12,
        'Auxiliar': 0.12,
        'Analista': 0.08,
        'Gerente': 0.06,
        'Conductor': 0.40,
        'Controlador': 0.05
    }
    ocupacion = random.choices(list(ocupaciones.keys()), weights=list(ocupaciones.values()), k=1)[0]
    
    # Generar empleado
    rfc = generar_rfc()
    nss = generar_nss()

    empleado = {
        'rfc': rfc,
        'nombres': nombre,
        'paterno': paterno,
        'materno': materno,
        'nss': nss,
        'telefono': telefono,
        'calle': fake.street_name(),
        'numero': fake.building_number(),
        'colonia': fake.city(),
        'cp': random.choice(codigos_postales),  # Selecciona un código postal aleatorio
        'ciudad': ciudad,
        'cuenta_bancaria': cuenta_bancaria,
        'sueldo_diario': random.randint(150, 1000),  # Sueldo diario aleatorio
        'ocupacion': ocupacion
    }
    
    return empleado

# Generar chofer para empleados que sean conductores
def generar_chofer(empleado):
    if empleado['ocupacion'] == 'Conductor':
        vigencia_licencia = fake.date_this_century()
        numero_licencia = generar_numero_licencia()  # Usar la función modificada para el número de licencia
        chofer = {
            'rfc': empleado['rfc'],
            'vigencia_licencia': vigencia_licencia,
            'numero_licencia': numero_licencia
        }
        return chofer
    return None

# Crear 1000 empleados y choferes
empleados = []
choferes = []
for _ in range(1000):
    empleado = generar_empleado()
    chofer = generar_chofer(empleado)
    empleados.append(empleado)
    if chofer:
        choferes.append(chofer)

# Crear archivo SQL de inserción
with open('empleados_insert.sql', 'w') as f:
    f.write("USE ado;\n\n")  # Usar la base de datos 'ado'

    for empleado in empleados:
        f.write(f"INSERT INTO empleado (rfc, nombres, paterno, materno, nss, telefono, calle, numero, colonia, cp, ciudad, cuenta_bancaria, sueldo_diario, ocupacion) VALUES (")
        f.write(f"'{empleado['rfc']}', '{empleado['nombres']}', '{empleado['paterno']}', '{empleado['materno']}', '{empleado['nss']}', '{empleado['telefono']}', ")
        f.write(f"'{empleado['calle']}', '{empleado['numero']}', '{empleado['colonia']}', '{empleado['cp']}', '{empleado['ciudad']}', ")
        f.write(f"'{empleado['cuenta_bancaria']}', {empleado['sueldo_diario']}, '{empleado['ocupacion']}');\n")

    for chofer in choferes:
        f.write(f"INSERT INTO chofer (rfc, vigencia_licencia, numero_licencia) VALUES (")
        f.write(f"'{chofer['rfc']}', '{chofer['vigencia_licencia']}', '{chofer['numero_licencia']}');\n")

print("Archivo SQL generado exitosamente como 'empleados_insert.sql'")
