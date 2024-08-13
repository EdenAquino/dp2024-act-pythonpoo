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