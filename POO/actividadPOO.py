'''
Crear la clase Medio Metro Robot
La misma estara compuestas de los siguientes metodos y atributos
Atributos:
    -anio de fabricacion  ->int
    -lote  ->int 
    -material  ->string
    -altura  ->float
    -coeficiente intelectual  ->float
    -pasos  -> list 2 pasos
'''

class MedioMetroRobot():
    def __init__(self, anio, lote, material, altura, coefIntelectual, pasos):
        self.anio = anio
        self.lote = lote
        self.material = material
        self.altura = altura
        self.coefIntelectual = coefIntelectual
        self.pasos = pasos

        print (f"Hola jaja, me fabricaon en el año {self.anio} y soy parte del lote {self.lote}")
        pass
    '''
        anio = 2012
        lote = 5432
        material = 'oro'
        altura = 1.5
        coefIntelectual = 100
        pasos = ['a','b','c']
    '''

    def saludar(self):
        print(f"Holi, seamos cubiamigos :)")

    def coeficiente(self):
        print(f"Mi coeficiente es de {self.coefIntelectual}")

    def listarPasos(self):
        for pasos in self.pasos:
            print(pasos)

robot1 = MedioMetroRobot(2012, 5432, 'oro',1.5, 100, ['Helicoptero','Pinguino'])
robot1.saludar()
robot1.listarPasos

            

'''
Al ser instanciado un objeto de esta clase, debe imprimirse "Hola. Me fabricaron en {anio de fabricacion} y soy 
parte del lote {lote}

Metodos:
    -saludar
        Debe imprimir "Hola, seamos cumbiamigos"
    -decir coeficiente
        Debe imprimir "Mi coeficiente es de {coeficiente}"
    -listar pasos
        Debe imprimir los pasos que conoce el medio metro (usar ciclos for pa imprimirlos)
    - aprender pasos
        Debe recibir como argumento el nombre de un paso, que sera agregado a la lista de pasos 
        que se sabe

'''