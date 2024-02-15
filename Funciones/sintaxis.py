def decirHola(nombre):
    print(f"Hola {nombre}")

decirHola("Ale")
decirHola("Yo")

def sumarDos(n1, n2):
    resultado = float(n1) + float(n2)
    return(resultado)

miresultado = sumarDos(4, 8)
print(miresultado)    

#Hola Tal, tu tienes tantos años
def presentacion():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    print(f"Hola {nombre}, tú tienes {edad} años de edad.")

presentacion()

