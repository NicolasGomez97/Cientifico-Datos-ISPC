class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)


class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
         return super().__str__() + " Velocidad km/hr: " +str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
         return super().__str__() + " tipo: " + self.tipo 


vehiculo = Vehiculo("Rojo",4)
print(vehiculo)

auto = Coche("Rojo",4,150)
print(auto)

bicicleta = Bicicleta("Blanca", 2, "Urbana")
print(bicicleta)    

