import random
import string
from faker import Faker
import datetime

fake = Faker('es_MX')  # Configurar Faker para generar datos de México

# Generar RFC en el formato: ABCD123456EFG
rfc_usados = set()  # Set para almacenar los RFCs generados

def generar_rfc(nombre, paterno, materno, fecha_nacimiento):
    # Primeras 2 letras del primer nombre y apellido paterno
    rfc_base = (nombre[:2] + paterno[:2]).upper()
    
    # Fecha de nacimiento: año (2 dígitos), mes (2 dígitos), día (2 dígitos)
    anio = fecha_nacimiento.year % 100
    mes = fecha_nacimiento.month
    dia = fecha_nacimiento.day
    fecha = f"{anio:02d}{mes:02d}{dia:02d}"
    
    # Tres caracteres aleatorios (letras o números)
    caracteres_aleatorios = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    
    # Generar RFC completo
    rfc = f"{rfc_base}{fecha}{caracteres_aleatorios}"
    
    # Verificar que el RFC sea único
    while rfc in rfc_usados:
        rfc = f"{rfc_base}{fecha}{caracteres_aleatorios}"
    rfc_usados.add(rfc)
    
    return rfc

# Generar NSS de 11 dígitos
def generar_nss():
    return ''.join([str(random.randint(0, 9)) for _ in range(11)])

# Generar número de teléfono de 10 dígitos
def generar_telefono():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

# Función para generar el número de licencia con letra aleatoria seguida de 8 dígitos
def generar_numero_licencia():
    letra = random.choice(string.ascii_uppercase)  # Genera una letra aleatoria
    numeros = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # Genera 8 dígitos aleatorios
    return letra + numeros  # Une la letra y los números

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
    
    # Fecha de nacimiento aleatoria
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=65)

    # Generar RFC basado en los nombres y la fecha de nacimiento
    rfc = generar_rfc(nombre, paterno, materno, fecha_nacimiento)
    
   
    ocupaciones = {
        'Asesor de ventas': 0.04,   
        'Mecánico': 0.06,           
        'Auxiliar': 0.06,            
        'Analista': 0.04,            
        'Gerente': 0.03,             
        'Conductor': 0.80,           
        'Controlador': 0.03          
    }   

    ocupacion = random.choices(list(ocupaciones.keys()), weights=list(ocupaciones.values()), k=1)[0]

    # Generar empleado
    empleado = {
        'rfc': rfc,
        'nombres': nombre[:30],
        'paterno': paterno[:30],
        'materno': materno,
        'telefono': telefono,
        'calle': fake.street_name()[:30],
        'numero': fake.building_number()[:30],
        'colonia': fake.city()[:30],
        'cp': random.choice(codigos_postales),  # Selecciona un código postal aleatorio
        'cuenta_bancaria': cuenta_bancaria,
        'sueldo_diario': random.randint(150, 1000),  # Sueldo diario aleatorio
        'ocupacion': ocupacion
    }
    
    return empleado, fecha_nacimiento

def generar_chofer(empleado, empleado_id):
    if empleado['ocupacion'] == 'Conductor':
        # Generar fecha de vigencia de licencia entre 2029 y 2035 usando datetime
        vigencia_licencia = fake.date_between(start_date=datetime.date(2029, 1, 1), end_date=datetime.date(2035, 12, 31))

        numero_licencia = generar_numero_licencia()  # Usar la función modificada para el número de licencia

        chofer = {
            'empleado_id': empleado_id,  # Relacionar con el empleado_id
            'vigencia_licencia': vigencia_licencia,
            'numero_licencia': numero_licencia
        }
        return chofer
    return None



# Crear 1000 empleados y choferes
empleados = []
choferes = []
for _ in range(20000):
    empleado, fecha_nacimiento = generar_empleado()
    # Simular auto-incremento del ID del empleado
    empleado_id = len(empleados) + 1
    chofer = generar_chofer(empleado, empleado_id)
    empleados.append(empleado)
    if chofer:
        choferes.append(chofer)

# Crear archivo SQL de inserción
with open('empleados_insert.sql', 'w') as f:
    f.write("USE ado;\n\n")  # Usar la base de datos 'ado'

    # Insertar empleados
    for empleado in empleados:
        f.write(f"INSERT INTO empleado (rfc, nombres, paterno, materno, telefono, calle, numero, colonia, cp, cuenta_bancaria, sueldo_diario, ocupacion) VALUES (")
        f.write(f"'{empleado['rfc']}', '{empleado['nombres']}', '{empleado['paterno']}', '{empleado['materno']}', '{empleado['telefono']}', ")
        f.write(f"'{empleado['calle']}', '{empleado['numero']}', '{empleado['colonia']}', '{empleado['cp']}', '{empleado['cuenta_bancaria']}', ")
        f.write(f"{empleado['sueldo_diario']}, '{empleado['ocupacion']}');\n")

    # Insertar choferes
    for chofer in choferes:
        f.write(f"INSERT INTO conductor (empleado_id, vigencia_licencia, numero_licencia) VALUES (")
        f.write(f"{chofer['empleado_id']}, '{chofer['vigencia_licencia']}', '{chofer['numero_licencia']}');\n")

print("Archivo SQL generado exitosamente como 'empleados_insert.sql'")
