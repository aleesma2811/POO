#1 De la siguiente lista, imprima el resultado de elevar cada elemento al cuadrado:
mi_lista = [1,3,9,7,11]

for num in mi_lista:
    print(num**2)

#2 De la siguiente lista, imprima el resultado de elevar cada elemento al cuadrado:
mi_lista_2 = [1,'3',9,'7','11']

for num in mi_lista_2:
    print(int(num)**2)

#3 De la siguiente lista, imprima el resultado de elevar cada elemento al cuadrado. Solo castear 
#tipo de datos cuando se requiera. No castear todo el tiempo
mi_lista_2 = [2,'4',10,'8','12']

print(type(mi_lista_2))

for n in mi_lista_2:
    if(type(n) == str):
        print(f"{int(n)**2}")
    else:
        print(f"{int(n)**2}")

#4 Recorrer con un for la siguiente lista de nombres, imprimir "Hola nombre_en_la lista" por cada nombre
nombres =['Cheems','Cholondrina','Medio Metro']

for names in nombres:
    print(f"Hola {names}")

#5 Pedir al usuario un valor inicial, un valor final y el tipo de cambio
#Realizar un conversor de divisas donde se imprima el resultado de multiplicar desde al valor
#inicial al valor final por el tipo de cambio.
#Ejemplo, si el valor inicial es 1 y el final es 3, con un tipo de cambio de 10, debera mostrarse:
#1 dolar son 10 pesos
#2 dolar son 20 pesos
#3 dolares son 30 pesos
'''
vi = int(input("Ingrese el primer valor a convertir: "))
vf = int(input("Ingrese el último valor a convertir: "))
cambio = int(input("Por último, ingrese el tipo de cambio: "))

valores = range(vi,vf+1,cambio)

for n in range(vi,vf+1):
    print(f"{n} dolares son {n*cambio} pesos")
'''
    
#6 Pedir al usuario un valor inicial y un valor final, devolver una lista con un rango de valores
#entre esos numeros que contenga el valor al cubo de los mismos, por ejemplo, si 1 es inicial y 
#3 es final, la lista resultante debe ser [1,8,27]

lista = []
vi = int(input("Valor inicial: "))
vf = int(input("Valor final: "))


for valores in range(vi,vf+1):
    lista.append(valores**3)
print(lista)