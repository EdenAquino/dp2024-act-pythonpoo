class Vehiculo:
    color = ""
    ruedas = 0
    def ingreso(self):
        self.color = input("ingrese el color\t")
        self.ruedas = int(input("ingrese las ruedas\t"))
    def mostrar (self):
        print("color: " , self.color)
        print("ruedas: " , self.ruedas)

class Coche(Vehiculo):
    velocidad = 0
    def ingreso (self):
        super().ingreso()
        self.valocidad = int(input("ingrese la velocidad\t"))
    def mostrar(self):
        super().mostrar()
        print("velocidad: " , self.velocidad)

class Camioneta(Coche):
    carga = 0
    def ingreso(self):
        super().ingreso()
        self.carga = int(input("ingrese la carga\t"))
    def mostrar(self):
        super().mostrar()
        print("carga: " , self.carga)

class Motocicleta(Camioneta):
    velocidad = 0
    def mostrar(self):
        super().mostrar()
        print("velocidad: " , self.velocidad)

class Bicicleta(Motocicleta):
    tipo = ""
    def ingreso(self):
        super().ingreso()
        self.tipo = input("ingrese el tipo\t")
    def mostrar(self):
        super().mostrar()
        print("tipo: " , self.tipo)
              
