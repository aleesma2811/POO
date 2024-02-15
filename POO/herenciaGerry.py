class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre 
        self.sonido = sonido

    def emitir_sonido(self):
        print(self.sonido)


class Perro(Animal):
    def __init__(self, nombre, sonido, color, patas):
        super().__init__(nombre, sonido)
        self.color = color
        self.patas = patas
    
class Gato(Animal):
    def __init__(self, nombre, sonido, color, patas):
        super().__init__(nombre, sonido)
        self.color = color
        self.patas = patas

perro = Perro("LIA", "gua", "blanco", 4)
gato = Gato("Michi","miau", "blanco", 4)

lista = [perro, gato]

for i in lista:
    i.emitir_sonido()
