'''
Instrucciones:
Su mision es crear la clase Alumno, la cual esta definida de la siguiente manera
    Atributos:
        nombre -> String ---------- Obtener su valor como argumento del constructor de la clase
        matricula -> String ---------- Obtener su valor como argumento del constructor de la clase
        materias -> lista vacia ---------- Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)
        costo_credito = 2500 ----------Preinicializado dentro del constructor (No toma su valor con el argumento del constructor)

        NOTA: Al crear un objeto, debe imprmirse la frase "Alumn@ {nombre del alumno} ha sido creado con la matricula {matricula del alumno}"
    
    Metodos:
        inscribir_materia
            Argumentos: Recibe el nombre de una materia, la cual se añade a la lsita de materias del alumno
            Funcionamiento: Al inscribir la materia, debe imprimirse la frase "la materia {materia} ha sido inscrita correctamente"
        
        
        calcular_colegiatura
            Argumentos: Nada
            Funcionamiento: Calcula el costo total de la colegiatura multiplicando el costo del credito X el numero de materias X 5
              (asumamos que cada materia tiene una carga de 5 creditos)
        
        
        aplicar_beca
            Argumentos: Porcentaje (en flotante. ejemplo: 0.30 es una beca del 30%)
            Funcionamiento: Actualiza el costo por credito de la clase haciendo el descuento correspondiente
        
'''

class Alumno():
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.materias = []
        self.costo_credito = 2500

        print(f"Alumno {self.nombre} ha sido creado con la matricula {self.matricula}.")


    def inscribir_materia(self, materia):
        self.materias.append(materia)
        print(f"La materia {materia} ha sido inscrita correctamente")

    def desinscribir_materia(self, materia):
        self.materias.remove(materia)
        print(f"La materia {materia} ha sido eliminada")

    
    def calcular_colegiatura(self):
        colegiatura = self.costo_credito * 5 * len(self.materias)
        return colegiatura


    def calcular_beca(self, porcentaje):
        total_colegiatura = 0
        total_colegiatura = self.calcular_colegiatura()
        self.costo_credito = total_colegiatura - (total_colegiatura * porcentaje)
        print(f"Colegiatura con beca: {self.costo_credito}")


alumno1 = Alumno('Ale', 2345)
alumno1.inscribir_materia('Algebra')
alumno1.desinscribir_materia('Algebra')

print(alumno1.calcular_colegiatura())
alumno1.calcular_beca(0.5)

print(vars(alumno1))