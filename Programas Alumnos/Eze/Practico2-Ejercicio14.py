#Combate

import random

Pikachu = 80
Squirtle = 90

#PIKACHU ATACA
while Pikachu > 0 and Squirtle > 0:
    Ataque1 = random.randint(1, 2)
    if Ataque1 == 1:
       Squirtle = Squirtle - 10
       print ("Pikachu ataca con Bola Voltio")
    else:
       Squirtle = Squirtle - 11
       print ("Pikachu ataca con Trueno")

#SQUIRTLE ATACA
    Ataque2 = input("Es tu turno Squirtle! Que ataque deseas realizar?: (P) Pistola Agua, (A) Ataque Rapido o (B) Burbuja: ")
    while Ataque2 != "P" and Ataque2 != "A" and Ataque2 != "B":
        print ("Ataque no valido, ingrese un ataque valido")
        Ataque2 = input("Es tu turno Squirtle! Que ataque deseas realizar?: (P) Pistola Agua, (A) Ataque Rapido o (B) Burbuja: ")
    
    if Ataque2 == "P":
       Pikachu = Pikachu - 10
       print ("Squirtle ataca con Pistola Agua")
    elif Ataque2 == "A":
       Pikachu = Pikachu - 11
       print ("Squirtle ataca con Ataque Rapido")
    elif Ataque2 == "B":
       Pikachu = Pikachu - 8
       print ("Squirtle ataca con Burbuja")
  
    print("La vida de Pikachu es ahora: {}".format(Pikachu))
    print("La vida de Squirtle es ahora: {}".format(Squirtle))

if Pikachu > Squirtle:
     print("¡Pikachu ha ganado el combate!")
else:
     print("¡Squirtle ha ganado el combate!")

