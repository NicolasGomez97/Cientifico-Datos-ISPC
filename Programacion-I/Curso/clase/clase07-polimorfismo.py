
class Gerente():

	def marcacion(self):
		print("Marca asistencia solo una vez.")

class Subgerente():

	def marcacion(self):
		print("Marca asistencia solo 2 veces.")

class Jefearea():

	def marcacion(self):
		print("Marca asistencia 4 veces.")

class Asistente():

	def marcacion(self):
		print("Marca asistencia 4 veces y firma en el padrón.")


def marcacionTrabajador(trabajador):
	trabajador.marcacion()


mTrabajador = Subgerente() 
marcacionTrabajador(mTrabajador)


mTrabajador2 = Gerente()
marcacionTrabajador(mTrabajador2)