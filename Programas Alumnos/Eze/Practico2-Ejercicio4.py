#Las trampas del azar

import random

Numero = random.randint(1, 10)
Usuario = int(input("Elegi y escribi un numero por favor:  "))

if Usuario == Numero:
    print("Felicidades, ganaste")
if Usuario > 10:
    print("Te has pasado del limite")
if Usuario < 1:
    print("Te has quedado corto con este numero")
#Bonus
if Usuario == 666:
    print("¡Elegiste el numero de la bestia!")
if Usuario == -666:
    print("¡Eres doblemente maligno por ser negativo!")

print("El numero ganador era: {}".format(Numero))