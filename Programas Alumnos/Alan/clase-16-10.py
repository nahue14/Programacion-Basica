#--- Ejemplo: la merienda---
"""print("me voy a la cocina")
print("Abro la heladera")

hay_leche = input("hay leche? (s/n): ")
hay_chocolate = input("hay chocolate? (s/n): ")

if hay_leche != "s" or hay_chocolate != "s":
    print("voy hasta el supermeracado")
    if hay_leche != "s":
        print("compro leche")
    if hay_chocolate != "s":
        print("compro chocolate")

print("ponemos la leche en el vaso")
print("ponemos el chocolate en el vaso")
print("mezclamos")"""


print("---BIENVENIDO A LA MONTAÑA RUSA")

#Pedimos datos
edad = int(input("dime tu edad: "))
altura = int(input("dime tu altura en centímetros: "))
vip = input("Tienes pase VIP? (S/N): ")

#Bloque 1: 'if' independientes (les sirve para el ejercicio 1)
if altura>170:
    print("aviso del guardia: Cuidado con la cabeza en los tuneles.")

if edad == 80:
    print("Aviso del guarda: ¡Felicidades! Los centenarios entran gratis.")

#Bloque 2: 'if / else' compuesto (les sirve para el Ejercicio 2)
if (edad>= 12 and altura >= 130) or (vip == "S"):
    print("¡puedes subir a la atraccion! Que te diviertas.")
else:
    print("Lo siento, por seguridad no cumples los requisitos para subir.")