# ejercicio 1 del tp2 -------------------------------------------------------------------------------------------------------------------------------------
"""print("me voy a la cocina")
print("abro la nevera")

hay_leche = input("hay leche? (s/n): ")
hay_chocolate =  input("hay chocolate?(s/n): ")

if hay_leche != "s" or hay_chocolate != "s" :
    print("voy hasta el super")
    if hay_leche != "s" :
        print("compro leche")
    if hay_chocolate != "s" :
        print("compro chocolate")

print("ponemos la leche en el vaso")
print("ponemos el chocolate en el vaso")
print("mezclamos")"""
# ejercicio 2 -------------------------------------------------------------------------------------------------------------------------------------------
"""edad = int(input("tu edad: "))
if edad >= 18 and <= 90:
    print("tiene acceso")
else: 
    print("no tiene acceso")"""
# ejercicio 3 ----------------------------------------------------------------------------------------------------------------------------------
"""edad = int(input("tu edad: "))
carnet = input("tipo de carnet: E(estudiante), P(pensionista), F(familia numerosa), N(ninguno)")
if (edad >= 25 and edad <= 35 and carnet == "E") or (edad < 10 and carnet == "N") or (edad >= 65 and carnet == "P") or (carnet == "F"):
    print("tiene descuento")
else: 
    print("no tiene descuento")"""
"""if edad < 10 and carnet == "N" :
        print("tiene descuento menor")
        if edad >= 65 and carnet == "P" :
            print("tiene descuento p")
            if carnet == "F":
                print("tiene descuento f")"""
#ejercicio 4 -----------------------------------------------------------------------------------------------------------------------------------------
"""import random
numero_secreto = random.randint(1,10)
jugador = int(input("ingresa tu numero: "))
if jugador == numero_secreto :
    print("has acertado")
if jugador > 10 :
    print("te has pasado del limite")
if jugador < 1 :
    print("te has quedado corto")
if jugador == 666 :
    print("elegiste el numero de la bestia")
if jugador == -666 :
    print("doblemente maligno por ser negativo")

print("numero ganador: {}".format(numero_secreto))"""
#ejercicio 5 -------------------------------------------------------------------------------------------------------------------
"""print("                            BIENVENIDO                        ")

puntuacion = 0
resp_1 = input("¿te gusta realizar actividades al aire libre? (A) de acuerdo, (B) mas o menos (C) en desacuerdo")
resp_2 = input("¿te gusta conocer gente nueva? (A) de acuerdo, (B) mas o menos, (C) en desacuerdo ")
resp_3 = input("¿eres de muchos amigos o de amigos contados? (A) de acuerdo, (B) mas o menos, (C) en desacuerdo")
if resp_1 = "A": 
    puntuacion + 10
if resp_2 = "A": 
    puntuacion + 10
if resp_3 = "A":
    puntuacion + 10
elif resp_1 = "B":
    puntuacion + 5
elif resp_2 = "B":
    puntuacion +5
elif resp_3 = "B":
    puntuacion + 5
elif resp_1 = "C":
    puntuacion + 0
elif resp_2 = "C":
    puntuacion + 0
elif resp_3 = "C":
    puntuacion + 0
else:
    print("las opciones posibles son A, B Y C")

if puntuacion = 30 :
    print("eres sociable")
elif puntuacion = 15 :
    print ("eres reservado")
elif pntuaciond = 0 :
    print ("eres timido")"""
#ejercicio 11 -------------------------------------------------------------------------------------------------------------------
"""print(" ¿el primero es el mayor de todos?")

n1 = int(input("numero 1 :"))
n2 = int(input("numero 2 :"))
n3 = int(input("numero 3: "))
if n1 > n2 and n1 > n3 :
    mensaje = "el primero es el mayor"
else :
    mensaje = "el primero no es el mayor"

print("conclusion : {}".format(mensaje))"""
# ejercicio 12 -------------------------------------------------------------------------------------------------------------------
print( "                      Bienvenido al juego                  ")
choice = input("elige (A) o (B): ")

if choice == "A" :
    print("puerta roja, carmesi")
    choice = input(" (A) o (B)")
    if choice == "A" :
        print("encuentras cofre carmesi, obtienes espada carmesi, sigues avanzando o sales?")
        """if choice == "A" :
            print("aparecio un enemigo! jabali carmesi")
            if choice == "A" : 
                print(" derrotaste jabali carmesi ¡felicidades subes de nivel!")
elif choice == "B":
    print("puerta verde")
     elif choice == "B":
        print("encontraste cofre del bosque, obtienes baculo naturaleza, sigues avanzando o te quedas?")
        elif choice == "B":
            print(" aparecio un slime!")
            elif choice == "B":
                print(" derrotaste al slime, subes de nivel!")"""