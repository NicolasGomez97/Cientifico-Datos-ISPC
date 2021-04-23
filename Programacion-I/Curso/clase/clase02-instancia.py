class Carro():

	#Atributos
	marca="Audi"
	longitud=2.8
	ruedas=4
	motor=2.5
	color="negro"
	modelo="Q5"

	#Propiedades
	arrancar=True
	frenar= False

	#Metodo
	def enmarcha(self):
		self.arrancar= False

	def estado(self):
		if(self.arrancar):
			
			return"El auto esta en arranque."
		else:
			
			return "El auto esta detenido."

#Instancia de clase  --> nombre_instancia = clase()
auto = Carro()
 
print("La marca del auto: ",Carro.marca)
print("Longitud: ",auto.longitud)
print("Número de Ruedas: ",auto.ruedas)
print("Motor: ",auto.motor)
print("Color del auto: ",auto.color)
print("Modelo del auto: ",auto.modelo)

auto.enmarcha()
print(auto.estado())