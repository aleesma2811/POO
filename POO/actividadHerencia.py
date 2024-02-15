class Vehiculo():
    def __init__(self, numero_ruedas, velocidad):
        self.numero_ruedas = numero_ruedas
        self.velocidad = velocidad
        print(f"Vehiculo creado!")

    def desplazarse(self):
        print(f"Vehiculo desplazandose!")


class Avion(Vehiculo):
    def __init__(self, numero_ruedas, velocidad):
        super().__init__(numero_ruedas, velocidad)

    def sonar_claxon(self):
        print(f"My sonic claxon goes NOOT NOOT")

    def desplazarse(self):
        print(f"Volando sin llantas")


class Microbus(Vehiculo):
    def __init__(self, numero_ruedas, velocidad):
        super().__init__(numero_ruedas, velocidad)

    def sonar_claxon(self):
        print(f"Grito de tarzan bien macizo")

    def desplazarse(self):
        print(f"Rodando en 4 ruedas, o a veces 3")


class Automovil(Vehiculo):
    def __init__(self, numero_ruedas, velocidad):
        super().__init__(numero_ruedas, velocidad)

    def sonar_claxon(self):
        print(f"MIC MIC")
    
    def desplazarse(self):
        print(f"Rodando en 4 llantas")


class Bicicleta (Vehiculo):
    def __init__(self, numero_ruedas, velocidad):
        super().__init__(numero_ruedas, velocidad)

    def sonar_claxon(self):
        print(f"Sonido de corneta")

    def desplazarse(self):
        print(f"Rodando en 2 llantas")



'''
A partir de la clase padre, crear las siguientes clases hijas
Avion
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "My sonic claxon goes NOOT NOOT"
Microbus
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "Grito de tarzan bien macizo"
Automovil
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "MIC MIC"
Bicicleta
    Metodos
        sonar_claxon
            Argumentos: Nada
            Comportamiento: Imprimir "Sonido de corneta"

Usando polimorfismo, crear un metodo "desplazarse" con los siguientes comportamientos para las clases hijas:
    Clase Avion: Imprimir "Volando sin llantas"
    Clase Microbus: Imprimir "Rodando en 4 llantas, o a veces 3"
    Clase Automovil: Imprimir "Rodando en 4 llantas"
    Clase Bicicleta: Imprimir "Rodando en 2 llantas"
'''

avion1 = Avion(6, 1000)
avion1.desplazarse()
avion1.sonar_claxon()

auto1 = Automovil(4, 90)
auto1.sonar_claxon()

bici1 = Bicicleta(2, 20)
bici1.desplazarse()

micro1 = Microbus(3, 50)
micro1.desplazarse()