class Computadora():

	def __init__(self):
		self.__marca = "Toshiba"
		self.__procesador = "Intel"
		self.__mouse = 1
		self.__teclado = 1
	
		self.__ejecutar = False

	def ejecucion(self,ejecuciones):
		self.__ejecutar=ejecuciones

		if(self.__ejecutar):
			update=self.__actualizacion_automatica()		

		if(self.__ejecutar and update):
			
			print("El equipo esta en ejecucion.")
		else:
			print("El equipo esta suspendido.")

	def __actualizacion_automatica(self):
		print("El equipo se esta actualizando.")

		self.servupdate="Activado"

		if(self.servupdate=="Activado"):
			return True
		else:
			return False


	def estado(self):
		print("La marca de PC es ",self.__marca,"tiene un ",self.__procesador,"cuenta con ",self.__mouse,"mouse y un ",self.__teclado,"teclado.")



pc = Computadora()

print(pc.ejecucion(True))
print(pc.estado())

print("*************************************************")

pc2 = Computadora()

# pc2.teclado=2
print(pc2.ejecucion(False))
print(pc2.estado())