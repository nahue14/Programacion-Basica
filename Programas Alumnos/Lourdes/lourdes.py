"""
nota1=10 
nota2=8 
nota3=9
promedio=(10+8+9)/ 3
print ("promedio final=", promedio)
print("¿aprobo?:", promedio >=6)

#variable=input ("Escribi lo que quieras= ")
#print("Escribiste esto= " + variable)
variable= int(input("Escribi lo que quieras= "))
print(max(variable, 10))
Variable1= int(input("Escriban el primer numero:"))
Variable2= int(input("escriban el segundo numero:"))
Variable3= int(input("escriban el tercer numero:"))
print(min(Variable1,Variable2,Variable3)) 

comida_favorita = "pizza"
print ("Comida favorita= ", comida_favorita) 
edad = "23"
print("Edad= ", edad)
altura = "1.63"
print("Altura=", altura)
mascotas = "true"
print("Mascotas=", mascotas)
#"edad = 23\naltura = 1.63\nmascotas = true")

Variable1 = int(input("Introduce un primer numero:"))
Variable2 = int(input("Introduce un segundo numero:"))
print("Tu resultado es", Variable1+Variable2)
print("Tu resultado es", Variable2-Variable1)
print("Tu resultado es",(Variable1+Variable2)*2)

numeros= 2, 4, 6, 123, 23
cantidad= len(numeros)
print(cantidad)

palabra= 'Lourdes'
cantidad= len(palabra)
print(cantidad)

print("Adivina el numero del 1 al 20")
A= int (input("Inserte el numero: "))
if A == 20:
    print("Excelente")

if A != 10: 
    print("No es correcto")

# ---Ejemplo: LA MERIENDA ---
print("Me voy a la cocina")
print("Abro la nevera")

hay_leche = input ("Hay leche? (s/n): ")
hay_chocolate = input("Hay chocolate (s/n): ")

if hay_leche != "s" or hay_chocolate != "s":
      print("Voy hasta el super")
      if hay_leche != "s":
          print("Compro leche")
if hay_chocolate != "s":
    print("Compro chocolate")


print("Pronemos la leche en el vaso")
print("Ponemos el chocolate en el vaso")
print("Mezclamos")
"""
print("--- BIENVENIDO A LA MONTAÑA RUSA ---")

# Pedimos los datos
edad = int(input("Dime tu edad "))
altura = int(input("Dime tu altura en centimetros: "))
vip = input("¿Tienes pase VIP? (S/N): ")

#Bloquear 1: 'if' independientes (les sirve para el ejercicio 1)
if altura > 170: 
    print("Aviso del guardia: Cuidado con la cabeza en los túneles.")

if edad == 80:
    print("Aviso del guardia: ¡Felicidades! Los centenarios entran gratis.")

#Bloque 2: 'if / else' compuesto (les sirve para el ejercicio 2)
if(edad >= 12 and altura >= 130) or (vip == "S"):
    print("¡Puedes subir a la atracción! Que te diviertas.")
else:
    print("Lo siento, por seguridad no cumples los requisitos para subir.")