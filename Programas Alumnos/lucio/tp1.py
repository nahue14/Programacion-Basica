# ejercicio 1 tp1 -------------------------------------------------------------------
"""comida_favorita = "asado"
edad = 20
altura = 1.70
mascotas = True
print("tu comida favorita es:",comida_favorita,"tu edad es:",edad,"tu altura es:",altura,"tienes mascotas", mascotas)"""
# ejercicio 2 ---------------------------------------------------------------------------------------------------------------
"""num1 = int(input("numero1: "))
num2 = int(input("numero2: "))
suma = num1 + num2
resta = num1 - num2 
sumamul = suma*2
print("suma",suma,"resta",resta,"multiplicacion",sumamul) """
# ejercicio 3 ------------------------------------------------------------------------------------------------------------------------
"""nombre = input("tu nombre: ")
apellido = input("tu apellido: ")
suerte = int(input("tu numero de la suerte: ")) 
print("hola, {}, {},".format(nombre,apellido) , "tu numero de la suerte es:  {}".format(suerte))"""
# ejercicio 4 ---------------------------------------------------------------------------------------------------------------------------------
"""edad1 = int(input("pers1: "))
edad2 = int(input("pers2: "))
edad3 = int(input("pers3: "))
edad4 = int(input("pers4: "))
edadmax = max(edad1,edad2,edad3,edad4)
edadmin = min(edad1,edad2,edad3,edad4)
print("las edades son, {}, {}, {}, {}, ".format(edad1,edad2,edad3,edad4) , "edad mayor ,{}, ".format(edadmax) , "edad menor, {}".format(edadmin))"""
# ejercicio 5 ---------------------------------------------------------------------------------------------------------------------------------------------
"""producto = float(input("precio del producto: "))
cantidad = int(input("cantidad producto: "))
precio_final = producto*cantidad
if precio_final >= 15000 :
    print("total a pagar, {}, y envio gratis".format(precio_final))
else:
    print("total a pagar, {}, sin envio gratis".format(precio_final))"""
#ejercicio 10 ---------------------------------------------------------------------------------------------------------------------------------------------------------
"""import random
numero_secreto = random.randint(1,10)
jugador = int(input("ingresa tu numero: "))
while jugador != numero_secreto :
    int(input("vuelve a intentarlo: "))

print("numero correcto")"""
# ejercicio 11 ---------------------------------------------------------------------------------------------------------------------------------------------------------------
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