
class Persona():

	def __init__(self, nombre, edad, residencia):

		self.nombre = nombre
		self.edad = edad
		self.residencia = residencia


	def estado(self):

		print("Nombre: ",self.nombre,
			  "\nEdad: ",self.edad,
			  "\nLugar de Residencia: ",self.residencia )



class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre, edad, residencia):

		super().__init__(nombre, edad, residencia)

		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):

		super().estado()
		print("Salario: ",self.salario,
			  "\nAntiguedad: ",self.antiguedad,"años.")

emp = Empleado(3000, 5, "Juan", 23, "Peru")
emp.descripcion()

print(isinstance(emp,Empleado))