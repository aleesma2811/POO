'''
Instrucciones:
Su mision es crear la clase Alumno, la cual esta definida de la siguiente manera
    Atributos:
        nombre -> String ---------- Obtener su valor como argumento del constructor de la clase
        matricula -> String ---------- Obtener su valor como argumento del constructor de la clase
        materias -> diccionario vacio ---------- Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)
        costo_credito = 2500 ----------Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)

        NOTA: Al crear un objeto, debe imprmirse la frase "Alumn@ {nombre del alumno} ha sido creado con la matricula {matricula del alumno}"
    
    Metodos:
        inscribir_materia
            Argumentos: Recibe un diccionario con los datos corresponientes a cada materia (los diccionarios de estas materias se encuentran mas abajo 
                        en este mismo documento)
            Funcionamiento: El formato del diccionario puede verse en las 3 materias incluidas en este archivo
                            Al inscribri una materia, se debe agregar la informacion correspondiente al diccionario que
                            originalmente estaba vacio dentro de la clase
                            {
                            'nombre de la materia 1': 'datos de la materia 1',
                            'nombre de la materia 2': 'datos de la materia 2',
                            etc
                            }
        
        
        desinscribir_materia
            Argumentos: Nombre de la materia a desinscribir
            Funcionamiento: Borrar el key correspondiente a la materia por desinscribrir
                            (busquen en internet como funciona "del" para diccionarios)
                            Usen un bloque try except para evitar que el programa crashee al intentar
                            desinscribir una materia no existente en el diccionario
        
        
        calcular_colegiatura
            Argumentos: Nada
            Funcionamiento: Calcula el costo total de la colegiatura sumando los creditos de las materias
                            inscritas y multiplicando el resultado por el costo del credito.
                            La suma de creditos inscritos debe hacerse con ciclos for
        
        
        aplicar_beca
            Argumentos: Porcentaje (en flotante. ejemplo: 0.30 es una beca del 30%)
            Funcionamiento: Actualiza el costo por credito de la clase haciendo el descuento correspondiente
        
        
        calificar_materia    
            Argumentos: Nombre de la materia a calificar y calificacion
            Funcionamiento: Asigna la calificacion a la materia correspondiente
                            Y cambia la bandera "Materia Cursada" a True
        
        
        calcular_promedio
            Argumentos: Nada
            Funcionamiento: Usando ciclos for, calcula y devuelve el promedio del alumno
                            El programa debe generar una excepcion (el programa debe crashear)
                            si se intenta sacar el promedio de una materia que aun no ha sido cursada

'''


#Estas son las materias a inscribir
programacion = {
        'nombre':'POO',
        'datos':{
                'Salon':'A',
                'Dias':'Lunes, Martes, Jueves',
                'Creditos':5,
                'Calificacion':0,
                'Materia Cursada':False
           }
           }

animacion = {
        'nombre':'Animacion y jueguitos',
        'datos':{
                'Salon':'B',
                'Dias':' Martes, Jueves',
                'Creditos':'6',
                'Calificacion':0,
                'Materia Cursada':False
           }
           }

algebra = {
        'nombre':'Algebra',
        'datos':{
                'Salon':'D',
                'Dias':'Jueves',
                'Creditos':'4',
                'Calificacion':0,
                'Materia Cursada':False
           }
           }

class Alumno():
    def __init__(self, nombre, matricula, materias, costo_credito):
        self.nombre = nombre
        self.matricula = matricula
        self.materias = {}
        self.costo_credito = 2500

        print(f"Alumn@ {self.nombre} ha sido creado con la matricula {self.matricula}")
        pass

    def inscribir_materia (self, **materia):
        self.materias[materia['nombre']] = materia['datos']

    def desinscribir_materia (self, nombre):
        try:
            del self.materias[nombre]
        except KeyError:
            print(f"La materia {nombre} no existe")

    def calcular_colegiatura (self):
        suma_creditos = 0
        for materia in self.materias:
            suma_creditos += int(self.materias[materia]['Creditos'])
        return suma_creditos*self.costo_credito

        



alumno1 = Alumno('Ale', 555 , 'programacion', 233)
print(alumno1.materias)
alumno1.inscribir_materia(**programacion)

print(alumno1.materias)

alumno1.desinscribir_materia(**programacion)

