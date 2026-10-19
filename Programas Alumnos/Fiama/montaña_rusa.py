print("--- BIENVENIDO A LA MONTAÑA RUSA ---")

#Pedimos los datos
edad = int(input("Dime tu edad: "))
altura= int(input("Dime tu altura en centímetros: "))
vip = input("¿Tienes pase VIP? (S/N): ")

#Bloque 1: 'if' independientes (les sirve para el Ejercicio 1)
if altura > 170:
    print("Aviso del guardia: CUidado con la cabeza en los túneles.")

if edad == 80:
    print("Aviso del guardia: ¡Felicidades! Los octagenarios entran gratis")

#Bloque 2: 'if / else' compuesto (les sirve para el Ejercicio)
if (edad >= 12 and altura >= 130) or (vip == "S"):
    print("¡Puedes subir a la atracción! Que te diviertas")
else:
    print("Lo siento, por seguirdad no cumples con los requisitos para subir.")    