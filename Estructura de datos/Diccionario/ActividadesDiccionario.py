
alumno = {
    "nombre": "Amapolo",
    "edad": 23,
    "situacion": "regular",
    "hobbies": ["nadar", "correr", "hacer el paso del pinguino"],
    "materias": {
        "historia": {
            "profesor": {
                "nombre": "Juan Carlos Bodoque",
                "universidad": "UNAM",
                "año egreso": 1982
            },
            "calificacion": "10"
        },
        "algebra": {
            "profesor": {
                "nombre": "Salgado Macedonio",
                "universidad": "SINATRACA",
                "año egreso": 1988
            },
            "calificacion": "7.2"
        },
        "programacion": {
            "profesor": {
                "nombre": "Peter Parker",
                "universidad": "IPN",
                "año egreso": 2012
            },
            "calificacion": "8.9"
        },
    }
}

#Imprimir el nombre y la edad del alumno -> El alumno X tiene Y años
print(f"El alumno {alumno['nombre']} tiene {alumno['edad']} años")

#Imprimir el tercer hobby del alumno
print(f"El tercer hobby del alumno {alumno['nombre']} es {alumno['hobbies'][2]}")

#Obtener el promedio del alumno

#Indicar el nombre, institución y año de egreso del profesor de programación
#El profesor X egresó en Y del Z
print(f"El profesor {alumno['materias']['programacion']['profesor']['nombre']} egresó en {alumno['materias']['programacion']['profesor']['universidad']} del {alumno['materias']['programacion']['profesor']['año egreso']}")

#Cambiar el tercer hobby del alumno por “ir a misa”
hobby= alumno["hobbies"][2]= "ir a misa"
print(f"EL tercer hobby favorito de {alumno['nombre']} es: {hobby}")

#Cambiar la calificación de algebra a 9.2
calificacion = alumno["materias"]["algebra"]["calificacion"]=9.2
print(calificacion)

#Obtener el promedio del alumno

#Cambiar el nombre, institución y año de egreso del profesor de programacion–