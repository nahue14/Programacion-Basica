"""
#Opcion 1
Nombre=input("¿Cual es tu nombre?: ")
Apellido=input("¿Cual es tu apellido?: ")
print("Tu nombre completo es:", Nombre+ " " + Apellido)
Numero_de_la_suerte=input("¿Cual es tu numero de la suerte?: ")
print("Hola", Nombre + " " + Apellido, "tu numero de la suerte es", Numero_de_la_suerte)
"""

#Opcion 2 usando .format
Nombre = input("¿Cual es tu nombre?: ")
Apellido = input("¿Cual es tu apellido?: ")
print("Tu nombre completo es: {} {}".format (Nombre, Apellido))
Numero_de_la_suerte = input("¿Cual es tu numero de la suerte?: ")
print("Hola {} {}, tu numero de la suerte es {}".format (Nombre, Apellido, Numero_de_la_suerte))






