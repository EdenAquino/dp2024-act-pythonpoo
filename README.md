# dp2024-act-pythonpoo
Ejemplos de POO con Python

Nombre: Eden Dario Aquino Méndez
Carnet: 200615537
Solución de los siguientes problemas:
1. Solicitar 3 textos y realizar lo siguiente:
• Mostrar el promedio de las longitudes de los textos.
• Concatenar los textos e indicar si el largo es mayor, menor o igual a 15.
• Indicar cuál de los textos posee más caracteres.
• Concatenar los textos e indicar la cantidad de caracteres numéricos existentes.

class Calculos:
    #atributos
    texto1=""
    texto2=""
    texto3=""
    resultado=0.0
    rev=0
    a=0
    b=0
    c=0
    z=0
    #métodos
    def obtenerLongitudes(self):
        a=(len(self.texto1))
        b=(len(self.texto2))
        c=(len(self.texto3))
        print("\nLa longitud de ", self.texto1," es ", a)
        print("La longitud de ", self.texto2," es ", b)
        print("La longitud de ", self.texto3," es ", c,"\n")

    def promediar(self):
        a=(len(self.texto1))
        b=(len(self.texto2))
        c=(len(self.texto3))
        self.resultado=(a + b + c)/3
        print("El promedio de las 3 longitudes es:", self.resultado," \n")

    def verificarLongitudes(self):
        self.resultado2=self.texto1+self.texto2+self.texto3
        self.rev=(len(self.resultado2))
        if self.rev > 15: print("El largo de la concatenación de caracteres es mayor que 15 \n")
        if self.rev < 15: print("El largo de la concatenación de caracteres es menor que 15 \n")
        if self.rev==15: print("El largo de la concatenación de caracteres es igual que 15 \n")
    
    def mayorLongitud(self):
        a=(len(self.texto1))
        b=(len(self.texto2))
        c=(len(self.texto3))
        print("El texto con mayor longitud tiene:",max(a,b,c),"caracteres, y es:")
        if a==max(a,b,c):print(self.texto1)
        if b==max(a,b,c):print(self.texto2)
        if c==max(a,b,c):print(self.texto3)

    def verificarCaracteres(self):
        for y in self.resultado2:
            print("La cantidad de números en la concatenación es ", y) 


#referencia al archivo y clase
from Programa1 import Calculos
x = Calculos()
print("Manejo de datos")
x.texto1=input("ingrese un texto:\t")
x.texto2=input("ingrese un texto:\t")
x.texto3=input("ingrese un texto:\t")
x.obtenerLongitudes()
x.promediar()
x.verificarLongitudes()
x.mayorLongitud()
x.verificarCaracteres()



2. Realizar los siguientes cálculos para un empleado del departamento de ventas:
• Comisión por ventas (10% del total vendido)
• Monto para pagar de IGSS (4.83% del sueldo base)
• Ahorro (7% del total ganado)
• Total ganado = sueldo base + comisión por ventas + bonificación.
• Total descuentos = ahorro + IGSS.
• Sueldo liquido = Total ganado – total descuentos.

class Planilla:
    #atributos
    sueldo=0.0
    ventas=0.0
    bonificacion=0.0
    comision=0.0
    igss=0.0
    ahorro=0.0
    total=0.0
    descuentos=0.0
    liquido=0.0
    #métodos
    def calcularComision(self):
        self.comision=self.ventas*0.1
        print("La comisión por el total vendido es ", self.comision,"\n")
    def calcularIgss(self):
        self.igss=self.sueldo*0.0483
        print("El valor del IGSS es:", self.igss," \n")
    def calcularAhorro(self):
        self.ahorro=(self.sueldo + self.ventas + self.comision)*0.07
        print("El ahorro es de ",self.ahorro, "\n")
    def calcularTotal(self):
        self.total=self.sueldo+self.comision+self.bonificacion
        print("El total ganado es: ",self.total,"\n")
    def calcularDescuentos(self):
        self.descuentos=self.ahorro+self.igss
        print("El total de descuentos es: ", self.descuentos)
    def calcularLiquido(self):
        self.liquido=self.total-self.descuentos
        print("El sueldo líquido es: ", self.liquido)


#referencia al archivo y clase
from Programa2 import Planilla
x = Planilla()
print("Planilla")
x.sueldo=float(input("ingrese el sueldo base:\t"))
x.ventas=float(input("ingrese el total de ventas:\t"))
x.bonificacion=float(input("ingrese la bonificación:\t"))
x.calcularComision()
x.calcularIgss()
x.calcularAhorro()
x.calcularTotal()
x.calcularDescuentos()
x.calcularLiquido()



3. Solicitar 1 valor numérico de base 10 y realizar lo siguiente: • Calcular y mostrar factorial del valor
ingresado
• Indicar si el número es primo.
• Indicar si el número es perfecto.
• Convertir el número a binario
• Mostrar la serie de Fibonacci hasta el valor ingresado.

class Numero:
    #atributos
    num=0
    factorial=0
    binario=0
    #métodos
    def calcularFactorial(self):
        factorial = 1
        i = 1
        while (i <= self.num):
            factorial = factorial * i
            i = i + 1
        print ("El factorial de " + str(self.num) + " es " + str(factorial))
    def verificarPrimo(self):
        for n in range(2, self.num):
            if self.num % n == 0:
                print("No es primo porque tiene más de dos divisores")
                return False
        print("Es primo")
        return True
    def convertirBinario(self):
        self.binario=bin(int(self.num))[2:]
        print("En binario es: ", self.binario,"\n")


#referencia al archivo y clase
from Programa3 import Numero
x = Numero()
print("Números")
x.num=int(input("ingrese un número de base 10:\t"))
x.calcularFactorial()
x.verificarPrimo()
x.convertirBinario()



4. Ejemplo de Herencia

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

              
#referencia al archivo y clase
from Programa4 import Bicicleta
objeto=Bicicleta()
objeto.ingreso()
objeto.mostrar()
