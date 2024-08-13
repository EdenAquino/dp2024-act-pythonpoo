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