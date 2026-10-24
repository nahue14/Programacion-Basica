#Buscando extremos con multiples variables

edad1=int(input("Ingrese la edad de la primera persona: "))
edad2=int(input("Ingrese la edad de la segunda persona: "))
edad3=int(input("Ingrese la edad de la tercera persona: "))
edad4=int(input("Ingrese la edad de la cuarta persona: "))

print("La edad mas grande es: {}".format(max(edad1, edad2, edad3, edad4)))
print("La edad mas pequeña es: {}".format(min(edad1, edad2, edad3, edad4)))

print("Las edades ingresadas son: {}. El mayor tiene {} años y el menor tiene {} años.".format([edad1, edad2, edad3, edad4], max(edad1, edad2, edad3, edad4), min(edad1, edad2, edad3, edad4)))
