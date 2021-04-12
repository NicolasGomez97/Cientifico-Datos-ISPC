

class Persona():

	def __init__(self, nombre, apellido, sexo):
		self.nombre = nombre
		self.apellido =apellido
		self.sexo = sexo

		self.hablar = False

	def hablar(self):
		self.hablar=True


	def estado(self):
		print("Nombre: ",self.nombre,
			  "\nApellido: ",self.apellido,
			  "\nSexo: ",self.sexo,
			  "\nHablar: ",self.hablar)


class Supervisor(Persona):
	objetivo=""

	def objetivos(self):
		self.objetivo="Tiene que cumplir con las metas mensuales."

	def estado(self):
		print("Nombre: ",self.nombre,
			  "\nApellido: ",self.apellido,
			  "\nSexo: ",self.sexo,
			  "\nHablar: ",self.hablar,
			  "\nObjetivo: ",self.objetivo)



class Obrero(Persona):
	manejarmaq=""

	def manejar(self):
		self.manejarmaq="Tiene que descargar 80 containers al mes."

	def estado(self):
		print("Nombre: ",self.nombre,
			  "\nApellido: ",self.apellido,
			  "\nSexo: ",self.sexo,
			  "\nHablar: ",self.hablar,
			  "\nObjetivo: ",self.manejarmaq)


print("******************DATOS SUPERVISOR*********************")
miSupervisor=Supervisor("Juan","Gonzalez","Masculino")
miSupervisor.objetivos()
miSupervisor.estado()

print("******************DATOS OBRERO*********************")
miObrero=Obrero("Jose","Amaranto","Masculino")
miObrero.manejar()
miObrero.estado()