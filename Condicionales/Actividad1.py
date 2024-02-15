#Pida al usuario su edad. Si tiene 18 anios o mas, imprimir "Eres mayor de edad"
#En caso contrario, imprimir "eres menor de edad"

#En el mismo programa, indique si la edad del usuario es un numero par o
#un numero impar 

#Si la edad esta entre 30 y 40, imprimir "Ya sientese, senior(a)"

edad = int(input("Ingrese su edad: "))


if (edad >= 18):
    print("Eres mayor de edad. ")
    if (edad % 2 == 0):
        print("Su edad es par")
    else:
        print("Su edad es impar")
else:
    print("Eres menor de edad. ")
    
    
if (edad >= 30 and edad <= 40):
    print("Ya siéntese senior")