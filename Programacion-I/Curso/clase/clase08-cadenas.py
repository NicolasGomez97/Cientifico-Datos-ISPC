#nombre = input("Ingrese el nombre: ")

# print("El nombre es: ",nombre.lower())
# print("El nombre es: ",nombre.upper())
# print("El nombre es: ",nombre.capitalize())


edad = input("Ingrese la edad: ")

while(edad.isdigit()==False):

	print("Porfavor ingrese su edad en números.")
	edad = input("Ingrese la edad: ")

	if(int(edad)<18):
		print("Usted no puede ingresar al evento.")
	else: 
		print("Puede Ingresar.")