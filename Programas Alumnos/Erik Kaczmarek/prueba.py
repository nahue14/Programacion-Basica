"""print("abierto")
#comentario
#https://www.datacamp.com/es/tutorial/python-block-comment
#el print muestra un texto o palabra 
print ("this is a coment")
'''comentario multilinea: es para un comentario mas largo de lo habitual'''
https://mimo-org.translate.goog/glossary/python/comment?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc&_x_tr_hist=true
print ("abierto\n cerrado")

#------------------------------------------------------------------

Edad=31
Saludo="hola"
Numero pi=3.14
NombreErik=False
ResultadoEdad=30+147
ResultadoSaludo=("Hola. Como estas?")
ResulultadoNumeroPi= 3.14/2
ResultadoNombreErik=False and True

#----------------------------------------------------------------------------

N1=10
N2=8
N3=4
Promedio=(N1+N2+N3)/3
print ('promedio final':, promedio)
print ('¿aprobo?', promedio >=6)

variable1=int(input("escribe el 1er nro: "))
variable2=int(input("escribe el 2do nro: "))
variable3=int(input("escribe el 3er nro: "))
"""
#-----------------------------------

#print("escribiste esto: " + variable)
#print (min(variable1,variable2))

#------------------------------------

"""comida_favorita = "milanesa"
edad = 31
altura = 1.64
mascotas = True
print(comida_favorita)
print(edad)
print(altura)
print(mascotas)
print(comida_favorita, edad, altura, mascotas)"""

#--------------------------------------

"""N1 = int(input("Introduce el N1: "))
N2 = int(input("Introduce el N2: "))

print("Suma:", N1 + N2)
print("Resta:", N1 - N2)
print("Suma multiplicada por 2:", (N1 + N2) * 2)"""

#------------------------------------------

"""palabra='una palabara de 7 letras'
cantidad= len(palabra)
print (cantidad)"""

#------------------------------------------ pedir nombre y apellido y mostrar por pantalla (ejemplo de ejecucion)

"""nombre=input("tu nombre:")
apellido=input("tu apeliido:")
print("tu nombre es: " + nombre + apellido)"""

#------------------------------------------------ agregar una 4ta variable un nro cualquiera que analice

"""variable1=int(input("1er nro:"))
variable2=int(input("2do nro:"))
variable3=int(input("3er nro:"))
variable4=int(input("cualquier nro:"))
print("el nro max es:", max (variable1, variable2, variable3, variable4))
print("el nro min es:", min (variable1, variable2, variable3, variable4))
print("los nros son {},{},{} y {}. el nro max es {} y el nro min es {}. " .format #format"""

#------------------------------------------------- comprimir la funcion max y min usando print y format en un solo renglon

"""variablex=int(input(5))
print("el usuario escribio: {}".format (variablex))"""

#-------------- 2 variables 2 if (operador basico ==) imprime igual y elif(10!=8) imprime que son distintos

"""num1 = int(input("Ingresa el primer número: ")); num2 = int(input("Ingresa el segundo número: ")); num3 = int(input("Ingresa el tercer número: ")); print("Son iguales (==)" if num1 == num2 else "Son distintos (!=)"); print("El primer número es mayor" if num1 > num2 else "El segundo número es mayor" if num1 < num2 else "Los dos números son iguales")
print("adivina un nro del 1 al 10")

a = int(input("ingresa un nro:"))
if a != 8:
    print("no es correcto")
if a == 8:
    print("joya!")"""

#------------------------------------------------

"""print("me voy a la cocina")
print("abro la heladera")
hay_leche = input("hay leche? (s/n): ")
hay_chocolate = input("hay chocolate? s/n): ")
if hay_leche != "s" or hay_chocolate != "s":
    print("voy hasta el super")
    if hay_leche != "s":
        print("compro leche")
    if hay_chocolate != "s":
        print("compro chocolate")

print("ponemos la leche en el vaso")
print("ponemos el chocolate en el vaso")
print("mezclamos")"""

#------------------------------------------------

print("---- Bienvenidos a la montaña rusa ----")
#pedimos los datos al usuario
edad = int(input("Por favor, ingresa tu edad: "))
altura = int(input("Por favor, ingresa tu altura en centimetros: "))
vip = input("tiene pase vip? (s/n): ")
#Bloque 1: 'if' independientes (les sirve para el ejercicio 1)
if altura >= 170:
    print("Aviso del guardia: cuidado con la cabeza en los tuneles")
if edad == 80:
    print("Aviso del guardia: felicidades! los centenarios entran gratis")
#Bloque 2: 'if / else' compuesto (les sirve para el ejercicio 2)
if (edad >= 12 and altura >= 130) or (vip == "s"):
    print("los siento, por seguridad no cumples con los requisitos para subir")