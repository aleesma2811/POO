'''
Crear un programa que pregunte al usuario su nombre , edad ,
dia de nacimiento , mes de nacimiento , año de nacimiento ,
CURP y código postal>
<Calcular el folio a partir de la multiplicación del dia, mes,
año de nacimiento y código postal>
<Mostrar en pantalla los datos proporcionados por el usuario así
como el folio generado. Todos los datos deben mostrarse en
MAYÚSCULAS sin importar si el usuario las escribió con
minúsculas originalmente>
'''

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
dia = int(input("Ingrese su día de nacimiento: "))
mes = int(input("Ingrese el número de mes de nacimiento: "))
year = int(input("Ingrese su año de nacimiento: "))
curp = input("Ingrese su CURP: ")
CodigoPostal = (input("Por último, ingrese su código de postal: "))

folio = dia*mes*year*CodigoPostal

print(f'''
Nombre: {nombre.upper()}
Edad: {edad}
Día de nacimiento: {dia}
Mes de nacimiento: {mes}
Año de nacimiento: {year}
CURP: {curp.upper()}
Código postal: {CodigoPostal}

Folio generado: {folio}

''')