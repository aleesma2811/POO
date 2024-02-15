'''
1) Imprimir la frase "Efren es alumno del curso de Python"
'''
alumnos = ['Efren','Sara', 'Carlos','Garza']

'''
2) Crear una lista donde el dato 0 sea el nombre de usuario y el dato 1 sea su edad. 
Los datos deben recolectarse usando "input", la edad debe guardarse como un entero dentro de la lista
Imprimir estructura resultante
'''
#nombre = input("Nombre: ")
#edad = input("Edad: ")
#lista = (nombre, int(edad))
#print(lista)
'''
3) De la lista anterior, cambiar la edad por el doble de su valor. Imprimir estructura resultante
'''
#lista = [nombre, int(edad)]
#lista[1] = lista[1]*2
#print(lista)
'''
4) Indicar cuantos nombres unicos de alumnos existen en la siguiente estructura de datos
'''
alumnos2 = ['Oscar', 'Daniel',' Amiel', 'Alejandra', 'Danna', 'Daniel', 'Danna','Adrian',' Amiel', 
'Danna', 'Daniel',' Amiel',' Amiel', 'Danna','Oscar','Ivan', 'Diego', 'Daniel']
print(f"Hay {len(set(alumnos2))} nombres únicos")

'''
5) Cambiar "Velma" por "The Last of Us" en la siguiente estructura de datos
'''
los_mejores_shows = ('House of the Dragon', 'Rick & Morty', 'Celebrity Deathmatch', 'Velma')

'''
6) Imprimir la frase "La alumna Alejandra tiene 9 de promedio
'''
estudiantes = [('Oscar',9),('Alejandra',9,('matemáticas','biología')),('Ivan',7)]
print(f"La alumna {estudiantes[1][0]} tiene 9 de promedio en {estudiantes[1][2][0]}:)")

'''
7) Imprimir la frase "El Alumno Oscar esta inscrito en Animacion 101
'''
estudiantes2 = [('Oscar',['Animacion 101','Finanzas']),
('Alejandra',['Matematicas Avanzadas','Hackeo Avanzado']),
('Ivan',['Memelogia','Como entrenar a tu dragon'])]
print(f"EL alumno {estudiantes2[0][0]} está inscrito en {estudiantes2[0][1][0]}")

'''
8) Cambiar la materia "Memelogia" a "Teoria Sonidera Aplicada". Imprimir estructura resultante
'''
estudiantes2 = [('Oscar',['Animacion 101','Finanzas']),
('Alejandra',['Matematicas Avanzadas','Hackeo Avanzado']),
('Ivan',['Memelogia','Como entrenar a tu dragon'])]


print(estudiantes2[2][1][0])