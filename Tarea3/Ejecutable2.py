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
