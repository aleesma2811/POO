alumno = {
    'nombre':'Eduardo',
    'edad':20,
    'nacionalidad':'MX'
}
def desempaqueDict(**diccionario):
    for llave, valor in alumno.items():
        print(f"{llave} --- {valor}")

desempaqueDict(**alumno)
