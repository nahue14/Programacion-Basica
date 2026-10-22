#----------------------------------------------------------------------------------------------------------------------------
"""comida_favorita = "asado"
edad = 20
altura = 1.70
mascotas = True
print("tu comida favorita es:",comida_favorita,"tu edad es:",edad,"tu altura es:",altura,"tienes mascotas", mascotas)"""
#-------------------------------------------------------------------------------------------------------------------------
"""comida_favorita = input("cual es tu comida favorita?:")
edad = int(input("cual es tu edad?:"))
altura = float(input("cual es tu altura?:"))
mascotas = bool(input("tienes mascotas?:"))
print("tu comida favorita es:",comida_favorita,"tu edad es:",edad,"tu altura es:",altura,"tienes mascotas:",mascotas)"""
#---------------------------------------------------------------------------------------------------------------------------
"""comida_favorita = input("cual es tu comida favorita?:")
edad = int(input("cual es tu edad?:"))
altura = float(input("cual es tu altura?:"))
respuesta = input("¿tienes mascotas?")
if respuesta == "si" or respuesta == "Si" or respuesta =="SI":
    print("tu comida favorita:",comida_favorita,"tu edad:",edad,"tu altura",altura,"si tienes mascotas")
else: print("tu comida favorita:",comida_favorita,"tu edad:",edad,"tu altura",altura,"no tienes mascotas")"""
#-----------------------------------------------------------------------------------------------------------------------------
"""s = 'septimo'
a = s
print(len(a))"""
#------------------------------------------------------------------------------------------------------------------------
"""nombre = input("cual es tu nombre?")
apellido = input("cual es tu apellido?")
print("tu nombre completo es:",nombre,apellido)"""
#--------------------------------------------------------------------------------------------------------------------------
"""v1 = int(input("introduce un primer num:"))
v2 = int(input("introduce un segundo num:"))
v3 = int(input("introduce un tercer num:"))
v4 = int(input("introduce cualquier num:"))
print(max(v1,v2,v3,v4))
print(min(v1,v2,v3,v4))
print("numero mayor ej:{}".format(100))
print("numero min ej:{}".format(1))"""
#-------------------------------------------------------------------------------------------------------------------------------
"""v1 = int(input("numero 1:"))
v2 = int(input("numero 2:"))
print("numero mayor :{}".format(max(v1,v2)),"numero min:{}".format(min(v1,v2)"""
#--------------------------------------------------------------------------------------------------------------------------
"""num1 = int(input("numero1: "))
if num1%2 == 0 :
    print("par")
elif num1%2 != 0:
    print("impar")"""
#-------------------------------------------------------------------------------------------------------------------------------
"""num1 = int(input("numero1: "))
num2 = int(input("numero2: "))
suma = num1 + num2
resta = num1 - num2 
sumamul = suma*2
print("suma",suma,"resta",resta,"multiplicacion",sumamul) """
#-----------------------------------------------------------------------------------------------------------------------------
"""nombre = input("tu nombre: ")
apellido = input("tu apellido: ")
suerte = int(input("tu numero de la suerte: ")) 
print("hola, {}, {},".format(nombre,apellido) , "tu numero de la suerte es:  {}".format(suerte))"""
#-------------------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------------
"""edad1 = int(input("pers1: "))
edad2 = int(input("pers2: "))
edad3 = int(input("pers3: "))
edad4 = int(input("pers4: "))
edadmax = max(edad1,edad2,edad3,edad4)
edadmin = min(edad1,edad2,edad3,edad4)
print("las edades son, {}, {}, {}, {}, ".format(edad1,edad2,edad3,edad4) , "edad mayor ,{}, ".format(edadmax) , "edad menor, {}".format(edadmin))"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------
"""producto = float(input("precio del producto: "))
cantidad = int(input("cantidad producto: "))
precio_final = producto*cantidad
if precio_final >= 15000 :
    print("total a pagar, {}, y envio gratis".format(precio_final))
else:
    print("total a pagar, {}, sin envio gratis".format(precio_final))"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""print("--- BIENVENIDO A LA MONTAÑA RUSA ---")

#PEDIMOS DATOS
edad = int(input("dime tu edad: "))
altura = int(input("dime tu altura en cm: "))
vip = input("¿tienes pase vip? (s/n): ")

# bloque 1: "if" independientes(les sirve para el ejercicio 1)
if altura > 170:
    print("aviso del guardia: cuidado con la cabeza en los tuneles.")

if edad == 80 : 
    print("aviso del guardia: ¡felicidades! los centenarios entran gratis.")


#bloque 2: "if / else" compuesto (les sirve para el ejercicio 2)
if (edad>= 12 and altura>= 130) or (vip == "s"): 
    print("¡puedes subir a la atraccion! que te diviertas")
else:
    print("lo siento, por seguridad no cumples los requisitos para subir")"""
"""peso_corporal = float(input("peso corporal: "))
altura = float(input("tu altura: "))
masa_corp = (peso_corporal/altura)**2
if masa_corp <=25.00 :
    print("peso saludable, IMC : {}".format(masa_corp))
else: 
    print("peso no saludable, IMC: {}".format(masa_corp))"""
#------------------------------------------------------------------------------------------------------------------------------------------------------
# validador de edad:
"""edad = int(input("tu edad: "))
if edad >= 18:
    print("puede acceder al permiso")
else:
    print("no puedes acceder al permiso")"""
#-----------------------------------------------------------------------------------------------------
nota = int(input("tu nota del 1 al 100: "))
nombre = input("tu nombre: ")
if nota >= 90 and nota < 100:
    print("{}, excelente tu nota es (A)".format(nombre))
elif nota >= 80 and nota < 90:
    print("{}, tu nota es (B)".format(nombre))
elif nota >= 70 and nota < 80 :
    print("{}, tu nota es (C)".format(nombre))
elif nota >= 60 and nota < 70:
    print("{}, aprobado rasante, tu nota es (D)".format(nombre))
elif nota< 60 and nota > 0:
    print("{}, has reprobado tu nota es (F)".format(nombre))
else:
    print("invalido")
    