#HERENCIA: Heredar atributos y métodos de una clase padre a una clase hija
#POLIMORFISMO: Cuando el mismo método está en distintas clases pero tienen funcionamiento distinto

class Persona():
    def __init__(self, nombre, matricula, fecha_alta):
        self.nombre = nombre
        self.matricula = matricula
        self.fecha_alta = fecha_alta
    
    def saludo(self):
        print(f"La persona {self.nombre} ha sido creada con la matrícula {self.matricula} en {self.fecha_alta}")

class Estudiante(Persona):
    def __init__(self, nombre, matricula, fecha_alta, promedio):
        super().__init__(nombre, matricula, fecha_alta)
        self.promedio = promedio

class Profesor(Persona):
    def __init__(self, nombre, matricula, fecha_alta, sueldo):
        super().__init__(nombre, matricula, fecha_alta)
        self.sueldo = sueldo

    def saludo(self):
        print(f"Hola, soy el profesor {self.nombre}, tengo la matrícula {self.matricula} y fui creado en {self.fecha_alta}")

import datetime
fecha = datetime.datetime.now()

estudiante1 = Estudiante("Carlos", 192, fecha, 8.5)
estudiante1.saludo()
print(estudiante1.promedio)

profesor1 = Profesor("Ivan", 234, fecha, 20)
profesor1.saludo()