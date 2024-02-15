class MedioMetroRobot():
    def __init__(self,nombre_usuario,procedencia): #Constructor: Define valores a los atributos
        self.nombre_usuario = nombre_usuario
        self.procedencia = procedencia
        self.color = input("Color: ")
        print(f"Ha nacido un nuevo medio metro robot que viene de {self.procedencia}")
        
    altura = 0.5
    material = 'aluminio'

    def saludo(self): #Se usa self para "amarrar" la clase con los atributos (funciones dentro de clases)
        print(f'Holi. Te quiero {self.nombre_usuario} :)')

robot1 = MedioMetroRobot('Ale','Corea')
robot1.saludo()
print(isinstance(robot1,MedioMetroRobot)) 

robot2 = MedioMetroRobot('Perla','CN')
robot2.saludo()