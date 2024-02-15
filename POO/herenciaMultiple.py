class Agenda():
    def __init__(self):
        self.lista_contactos = {}
        print("Este teléfono tiene agenda")

    def agregar_contacto(self, nombre, telefono):
        self.lista_contactos[nombre] = telefono


class Camara():
    def __init__(self, megapixeles):
        self.megapixeles = megapixeles
        print(f"Esta cámara toma fotos con {self.megapixeles} megapixeles de resolución")

    def tomar_foto(self):
        print(f"Tomando foto con {self.megapixeles} megapixeles de resolución")


class Reproductor():
    def __init__(self):
        self.lista_canciones = []
        print(f"Este teléfono reproduce")

    def agregar_cancion(self, cancion):
        self.lista_canciones.append(cancion)


class Telefono(Agenda, Camara, Reproductor):
    def __init__(self):
        Agenda.__init__(self)
        Camara.__init__(self, 80)
        Reproductor.__init__(self)


agenda1 = Agenda()
print(agenda1.lista_contactos)
agenda1.agregar_contacto("Ale", 222333)
print(agenda1.lista_contactos)

camara1 = Camara(60)
camara1.tomar_foto()

reproductor1 = Reproductor()
reproductor1.agregar_cancion("Waka waka")
print(reproductor1.lista_canciones)

fono1 = Telefono()
fono1.tomar_foto()
fono1.agregar_contacto("Perla", 122345)
fono1.agregar_cancion("Muffin song")
print(fono1.lista_contactos)


