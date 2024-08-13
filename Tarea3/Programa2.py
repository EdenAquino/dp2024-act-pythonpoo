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