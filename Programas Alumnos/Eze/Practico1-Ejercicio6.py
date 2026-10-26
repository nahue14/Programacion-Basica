#Calculadora de Indice de Masa Corporal (IMC)

print("Bienvenido a la calculadora de Indice de Masa Corporal (IMC)")
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
IMC = peso / (altura ** 2)
print("Tu indice de masa corporal es: {}".format(IMC))
if IMC < 25:
    print("Tu peso es saludable")
    #print("{}".format(IMC < 25))
else IMC >= 25:
    print("Tu peso no es saludable")
