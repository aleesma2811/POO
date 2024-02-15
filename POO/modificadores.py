class Automovil():
    def __init__(self, modelo, color):
        self.__modelo = modelo #Atributo privado
        self.__kilometraje = 0
        self.__color = color
        print(self.__modelo)

    def set_kilometraje(self, kilometraje):
        self.__kilometraje += kilometraje

    def get_kilometraje(self):
        print(f"Este auto ha recorrido {self.__kilometraje} kilómetros.")


auto1 = Automovil("Nissan", "rojo")
auto1.set_kilometraje(20)
auto1.set_kilometraje(14)
auto1.set_kilometraje(30)
auto1.set_kilometraje(19)
auto1.get_kilometraje()

print(auto1.__color)

