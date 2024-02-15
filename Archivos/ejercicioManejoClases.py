'''
Crear clase Alumno
    usando constructor de la clase
        atributo privado nombre
        atributo privado matricula
    
    Al crear un un alumno, deberá de imprimir en un txt llamado logs.txt
    "Alumno X" creado en "fecha"

    METODOS
        inscribir_materia(nombre_materia, creditos)
            añadir un key al diccionario de materias cuyo value sean los créditos
            Materia X inscrita en "fecha"

        desinscribir_materia (nombre_materia)
            borrar el key correspondiente
            Materia X dada de baja
'''

class Alumno():
    def __init__(self, nombre, matricula, materias):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__materias = {}

        import datetime
        fecha = datetime.datetime.now()
        with open('logsactovidad','a') as file:
            file.write(f"{fecha} ---- El alumno {self.__nombre} ha sido inscrito \n")

    def inscribir_maeria(self, materia, creditos):
        self.__materias[materia] = creditos

        import datetime
        fecha = datetime.datetime.now()
        with open('logsactovidad','a') as file:
            file.write(f"{fecha} ---- La materia {materia} ha sido creada \n")


alumno1 = Alumno('Ale',444, 'POO')
alumno1.inscribir_maeria('PA',777)