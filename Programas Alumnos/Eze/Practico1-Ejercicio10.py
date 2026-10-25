#El juego de Adivinar y las trampas

import random

Numero_aleatorio = random.randint(1, 10)
Usuario = int(input("Ingresa un numero por favor:  "))

if Usuario == Numero_aleatorio:
    print("Felicidades, adivinaste el numero")
if Usuario > 10:
    print("Te has pasado con este numero")
if Usuario < 1:
    print("Te has quedado corto con este numero")
#Bonus
if Usuario == 666:
    print("¡Elegiste el numero de la bestia!")
if Usuario == -666:
    print("¡Eres doblemente maligno por ser negativo!")

print("El numero ganador era: {}".format(Numero_aleatorio))