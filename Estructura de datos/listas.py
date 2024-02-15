lista = ['La Changa','Sonido pirata','Medio metro']
print(lista[1])
print(f"Wujuuuu {lista[2]}")

#Listas dentro de listas
lista1= ['azul','rojo']
lista2 = [1,2,3,4,['a','b','c','d'],'otro elemento', lista1]

print(lista2)
print(lista2[4][1])
#Imprimir "rojo"
print(lista2[-1][1])

#Imprimir dos elementos de una lista
print(lista2[1:3]) #Seleccionar del índice 1 al 3 (superior no se imprime)
