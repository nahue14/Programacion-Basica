"""Ejercicio 4: Buscando extremos con múltiples variables
1. Solicita al usuario que introduzca las edades de 4 personas distintas (conviértelas a variables enteras).
2. Utilizando las funciones max y min, averigua cuál es la edad más grande y cuál es la más pequeña entre las cuatro.
3. Imprime el resultado en un solo renglón utilizando .format(), de manera que el texto final diga algo
como: "Las edades ingresadas son [edad1], [edad2], [edad3] y [edad4]. El mayor tiene [maximo] años y 
el menor [minimo] años."."""

print("*_ BIENVENIDO _* \n")

edad1 = int(input("Ingrese la edad de la primer persona: "))
edad2 = int(input("Ingrese la edad de la sagunda persona: "))
edad3 = int(input("Ingrese la edad de la tercer persona: "))
edad4 = int(input("Ingrese la edad de la cuarta persona: "))

mayor = max(edad1, edad2, edad3, edad4)
menor = min(edad1, edad2, edad3, edad4)

print("\n Las edades ingresadas son {}, {}, {} y {}. El mayor tiene {} años y el menor {} años.".format(edad1,edad2,edad3,edad4,mayor,menor))