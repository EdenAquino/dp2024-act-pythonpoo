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