import random
from faker import Faker

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

# Lista de códigos postales de México (solo algunos ejemplos)
codigos_postales = ['01000', '01010', '01100', '01200', '03100', '03110', '03300', '03810', '05000', '05010']

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
        numero_licencia = fake.uuid4()[:20]  # Simula un número de licencia aleatorio
        chofer = {
            'rfc': empleado['rfc'],
            'vigencia_licencia': vigencia_licencia,
            'numero_licencia': numero_licencia
        }
        return chofer
    return None

# Crear empleados y choferes (por ejemplo, 10 empleados)
empleados = []
choferes = []
for _ in range(10):
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
