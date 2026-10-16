"""
nota1 =10
nota2 =8
nota3 =9
Resultado1 =(nota1 + nota2 + nota3)
promedio =(Resultado1) /3
print("Promedio final", promedio)
print("¿APROBADO?:", promedio>=6)
imput= "HOLA"
cualquiercosa= imput
print("cualquiercosa")
"""
"""
comida_favorita = "Milanesas"
edad= 52
altura=1.62
mascota=True
print(comida_favorita)
print(edad)
print(altura)
print(mascota)
"""
"""
variable1 = int(input("Introduzca un numero"))
variable2 = int(input("Introduzca un segundo numero mayor al anterior"))
print("la suma es:", variable1 + variable2)
print("la resta es:",variable2 - variable1)
print("la suma multiplicada por 2 es:",(variable1 + variable2) * 2)
"""
"""
numeros=25 ,13,3
cantidad=len(numeros)
print(cantidad)
"""
"""
nombre =input("Ingrese su nombre")
apellido =input("Ingrese su apellido")
print("Su nombre y apellido es:", nombre + apellido)
"""
"""
variable1 =int(input("Introduce un primer numero:"))
variable2 =int(input("Introduce un segundo numero:"))
variable3 =int(input("Introduce un tercer numero:"))
variable4 =int(input("Intoduce cualquier numero:"))
print( max(variable1, variable2, variable3, variable4))
print(min(variable1, variable2, variable3, variable4))

print("Tu numero de la suerte es {}".format(5))
print("Las variables ingresadas son:{} {} {} {} El max es: {} El min es: {}".format(variable1, variable2, variable3, variable4, max(variable1,variable2, variable3, variable4), min(variable1, variable2, variable3, variable4)))
""" 
"""   
variable1 = int(input("Ingrese un primer numero:"))
variable2 = int(input("Ingrese un segundo numero:"))
if variable1== variable2:
    print("Son Iguales") 
elif variable1!= variable2:
     print("Son Distintos")
 """
"""
 # Ejemplo la merienda
print("Me voy a la cocina")
print("Abro la heladera")

Hay_Leche= input("Hay Leche?(s/n):")
Hay_Chocolate= input("Hay Chocolate?(s/n):")

if Hay_Leche != "s" or Hay_Chocolate !="s":
    print ("Voy  hasta el super")
    if Hay_Leche !="s":
        print ("Compro leche")
    if Hay_Chocolate != "s":
        print("Compro chocolate")

    print("Ponemos la leche en el vaso")
    print("Ponemos el chocolate en el vaso")
    print("Mezclamos")
    """
print("---BIENVENIDOS A LA MONTAÑA RUSA---")
#Pedimos los datos
edad =int(input("Dime tu edad:"))
altura =int(input("Dime tu altura en centímetros:"))
vip =input("Tienes pase Vip? (s/n):")

#Bloque 1"if" independientes(les sirve para el ejercicio 1)
if altura >170:
    print("Aviso del guardia: Cuidado con la cabeza en los túneles.")

if edad ==80:
    print("Aviso del guardia: ¡Felicidades! Los centenarios entran gratis.")

# Bloque 2: "if /else" compuesto (les sirve para el Ejercicio 2)
if (edad>=12 and altura>=130) or (vip =="s"):
    print("¡Puedes subir a la atracción! Que te diviertas.")
else:
    print("Lo siento, por seguridad no cumples los requisitos para subir.")

     







