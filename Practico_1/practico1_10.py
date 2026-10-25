"""Ejercicio 10: El Juego de Adivinar y las Trampas
1. Importa la librería random para que la computadora pueda generar números al azar.
2. Crea una variable que guarde un número aleatorio generado entre el 1 y el 10.
3. Solicita al usuario que elija un número y conviértelo a un valor entero (int).
4. Utilizando únicamente condicionales if, evalúa los siguientes escenarios e imprime un mensaje para cada uno:
.Si el usuario adivina el número exacto, infórmale que ha ganado.
.Si el número ingresado es mayor a 10, avísale que se ha pasado.
.Si el número ingresado es menor a 1, indícale que se ha quedado corto.
.Bonus (Easter Eggs): Agrega dos condiciones secretas. Si el usuario ingresa 666, dile que eligió el número de la bestia. 
Si ingresa -666, dile que es doblemente maligno por ser negativo.
5. Al final del programa, imprime siempre cuál era el número ganador utilizando la función .format()."""

import random

print(" *ADIVINA EL NÚMERO*\n")
azar = random.randint (1,10)
num = int(input("Ingresa un número: "))

if num == azar:
    print("\n¡Adivinaste! {} es el número correcto".format(num))
elif num == 666:
    print("\nElegiste el número de la bestia.\nEl número correcto es {}".format(azar))
elif num == -666:
    print("\nInvocaste a la bestia X2.\nEl número correcto es {}".format(azar))    
elif num > 10:
    print("¡Te pasaste! El número correcto es {}".format(azar))
elif num < 1:
    print("\nTe quedaste corto.\nEl número correcto es {}".format(azar))
else:
    print("El número correcto es {}".format(azar))