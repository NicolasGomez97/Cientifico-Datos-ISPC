class Computadora():

	def __init__(self):
		self.marca = "Toshiba"
		self.procesador = "Intel"
		self.mouse = 1
		self.teclado = 1
	
		self.suspendido = False

	def ejecucion(self,suspension):
		self.suspendido=suspension

		if(self.suspendido):
			print("El equipo esta suspendido.")
		else:
			print("El equipo esta en ejecucion.")

	def estado(self):
		print(self.marca,self.procesador,self.mouse,self.teclado)


pc = Computadora()

print("Marca: ",pc.marca)
print("Procesador: ",pc.procesador)
print("Mouse: ",pc.mouse)
print("Teclado: ",pc.teclado)

print(pc.ejecucion(True))
print(pc.estado())

print("*************************************************")

pc2 = Computadora()
print("Marca: ",pc2.marca)
print("Procesador: ",pc2.procesador)
print("Mouse: ",pc2.mouse)
print("Teclado: ",pc2.teclado)

print(pc2.ejecucion(False))
print(pc2.estado())