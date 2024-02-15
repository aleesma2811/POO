def funcionSaludoSuma(nombre, nombre2, *numeros):
    print(f"Hola {nombre}, tu mejor amigo es {nombre2}")
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado

nombre = input("Nombre: ")
bestie = input("Nombrede tu bestie: ")
print(funcionSaludoSuma(nombre, bestie, 4,5,6))

