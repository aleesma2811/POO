alumnos = [
    {
        'nombre':'Ale',
        'calificacion':89
    },
    {
        'nombre':'Perla',
        'calificacion':100
    },
    {
        'nombre':'Meh',
        'calificacion':45
    },
]

#Calcular promedio utilizando ciclos for y descomprimiendo

suma = 0
for elementos in alumnos:
    print(elementos['calificacion'])
    suma = suma + elementos['calificacion']
print(f"Promedio general: {suma/len(alumnos)}")
