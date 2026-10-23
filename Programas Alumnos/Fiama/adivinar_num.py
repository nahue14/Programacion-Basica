import random
input("___ ADIVINA EL NÚMERO SECRETO ___\n")

num_secreto = random.randint(1,10)
#print (num_secreto)
num_usuario = int(input("Prueba suerte: elige un número del 1 al 10:\n"))

while(num_usuario != num_secreto):
    print("Te equivocaste, intenta de nuevo")
    num_usuario = int(input("Elige un número del 1 al 10\n"))

print("¡Felicidades! Adivinaste, el número era ", num_secreto)
