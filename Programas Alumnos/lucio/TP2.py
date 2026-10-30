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
"""print( "                      Bienvenido al juego                  ")
import random
choice = input("elige (A) o (B): ")
objeto = True
quest = random.randint(1,6)
if choice == "A":
    print("puerta verde")
    choice = input("A o B: ")
    if choice == "A":
        print("encuentras un cofre verde, dentro habia una espada verde, sigues avanzando?")
        choice = input("(A) o (B): ")
        if choice == "A" and objeto == True:
            print("derrotas un slime y subes de nivel")
        elif choice == "B":
            print("tomas un atajo y te encuentras un mago enemigo, te dice que adivines un numero para sobrevivir")
            jugador = int(input("tu numero:"))
            if jugador == quest :
                print("ganaste")
            else: 
                print("fin del juego")

    elif choice =="B":
        print("avanzas por un camino y te derrotan")
elif choice == "B":
    print("no entras a la mazmorra")"""
#ejercicio 13 --------------------------------------------------------------------------------------------------------------------------
"""kilometraje = int(input("numero enter: "))
if kilometraje <= 300 :
    monto = 500
else: 
    excedente = kilometraje - 300
    if kilometraje <= 1000:
        monto = 500 + 3 * excedente
    else: 
        monto = 500 + 1.5 * excedente

print("el importe a pagar es {}".format(monto))"""
# ejercicio 6 -----------------------------------------------------------------------------------------------------------------------------------
"""print( "  CONVERSOR DE MONEDA        ")
dolar_euro = 0,90
peso_dolar = 1.535,52
libra_euro = 1,20
dolar_yen = 157,53
operacion = input("que desea hacer? (A) dolar,euro (B) peso,dolar (C) libra_euro (D) dolar_yen: ")
if operacion == "A":
    monto = int(input("tu monto: "))
    final = (dolar_euro * monto)
    final_final = final
    print("monto final {}".format(final_final) )"""
# ejercicio 14 -----------------------------------------------------------------------------------------------------------------------------------------------
print(" batalla pokemon")
import random
pikachu = 80
squirtle = 90
while pikachu > 0 and squirtle > 0 :
    ataque = random.randint(1,2)
    if ataque == 1 :
        squirtle -=11
        print("pikachu usa bola voltio, squirtle pierde 10 hp")
    elif ataque == 2 :
        squirtle -=11
        print("pikachu usa trueno, squirtle pierde 11 hp")
print(squirtle)
turno_jugador = input("(P),(A),(B): ")
while turno_jugador != "P" and turno_jugador !="A" and turno_jugador !="B":
    turno_jugador = input("(P),(A),(B): ")
    if turno_jugador == "A":
        pikachu -=10
        print("squirtle usa hidropulso, pikachu pierde 10 hp")
    elif turno_jugador == "B":
        pikachu -=11
        print("squirtle usa hidrobomba, pikachu pierde 11 hp")
    elif turno_jugador == "P":
        pikachu -=5
        print("squirtle usa patada, pikachu pierde 5 hp")
print(pikachu) 
