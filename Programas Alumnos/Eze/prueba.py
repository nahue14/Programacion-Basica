"""
Edad=30
Saludo="Hola"
Numeropi=3.14
NombreSusana=False

#---------------------------------------------
Resultadodeedad= Edad + 147
Resultadosaludo= print(Saludo, "¿como estas?")
Resultadonumeropi= Numeropi / 2
Resultadonombresusana=NombreSusana and True

print(Resultadodeedad)
print(Resultadonumeropi)
print(Resultadonombresusana)

"""
"""
Resultado1=8
Resultado2=6
Resultado3=3
Total=(Resultado1+Resultado2+Resultado3)
Promedio=Total/3
if Promedio>=6:
  print ("Aprobo")
else:
  print ("No aprobo")
"""

"""
Cualquiercosa=Hola
Apertura=Escribiste
input(Hola)
print(Cualquiercosa)
print(Apertura, Cualquiercosa)

"""
"""
variable=input("Escribi algo: ")
print ("Escribiste esto:" + variable)
#print.......
"""
"""
variable=int(input("Escribi algo: "))
print(max(variable,10))
"""
"""
variable1=int (input("Escriban el 1er numero: "))
variable2=int (input("Escriban el 2do numero: "))
variable3=int (input("Escriban el 3er numero: "))
print (max(variable1,variable2,variable3))
"""
"""
variable1=int (input("Escriban el 1er numero: "))
variable2=int (input("Escriban el 2do numero: "))
variable3=int (input("Escriban el 3er numero: "))
print (min(variable1,variable2,variable3))
"""
"""
Comida="milanesa"
Edad=32
Altura=1.70
Mascota=False
print(Comida)
print(Edad)
print(Altura)
print(Mascota)
print(Comida, Edad, Altura, Mascota)
"""
"""

Primer_numero=int(input("Introduce un primer numero: "))
Segundo_numero=int(input("Introduce un segundo numero: "))
print("La suma es:",Primer_numero+Segundo_numero)
print("La resta es:", Primer_numero-Segundo_numero)
print("El resultado final es:", ((Primer_numero+Segundo_numero)*2))

"""
"""
Nombre=input("¿Cual es tu nombre?: ")
Apellido=input("¿Cual es tu apellido?: ")
print("Tu nombre completo es:", Nombre+ " " + Apellido)
Numero_de_la_suerte=input("¿Cual es tu numero de la suerte?: ")
print("Hola", Nombre + " " + Apellido, "tu numero de la suerte es", Numero_de_la_suerte)

"""
"""
Numeros=15,13,3
Cantidad= len(Numeros)
print(Cantidad)
"""
"""
Palabra='Rosario'
Cantidad=len (Palabra)
print(Cantidad)

"""
"""
variable1=int(input("Introduce el primer numero: "))
variable2=int(input("Introduce el segundo numero: "))
if variable1==variable2:
    print("Son iguales")
elif variable1 != variable2:
    print("Son distintos")
"""
"""
#---Ejemplo: La merienda---
print("Me voy a la cocina")
print("Abro la cocina")

hay_leche = input("Hay leche? (s/n): ")
hay_chocolate = input("Hay chocolate? (s/n): ")

if hay_leche != "s" or hay_chocolate != "s":
    print("Voy hasta el super")
    if hay_leche != "s":
        print("Compro leche")
    if hay_chocolate != "s":
        print("Compro chocolate")

print("Ponemos la leche en el vaso")
print("Ponemos el chocolate en el vaso")
print("Mezclamos")

"""
"""
print("---BIENVENIDO A LA MONTAÑA RUSA---")
#pedimos los datos
edad = int(input("Dime tu edad: "))
altura = int(input("Dime tu altura en centimetros: "))
vip = input("Tienes pase VIP? (S/N): ")

#Bloque 1: 'if' independientes (les sirve para el Ejercicio 1)
if altura>170:
    print ("Aviso del guardia: Cuidado con la cabeza en los tuneles.")

if edad==80:
    print ("Aviso del guardia: ¡Felicidades! Los centenarios entran gratis.")

#Bloque 2: 'if / else' compuesto (les sirve para el ejercicio 2)
if (edad>=12 and altura>=130) or (vip=="S"):
    print ("¡Puedes subir a la atraccion! Que te diviertas.")
else:
    print("Lo siento, por seguridad no cumples con los requisitos para subir.")
"""





