"""Ejercicio 14: Combate 
1. Importa la función randint de la librería random. 
2. Establece la vida inicial: Pikachu = 80, Squirtle = 90. 
3. Crea un bucle while principal para que el combate se repita mientras la vida de 
Pikachu sea mayor a 0 Y la vida de Squirtle sea mayor a 0. 
4. Turno de Pikachu (Automático): Genera un número al azar (1 o 2). Si sale 1, ataca 
con Bola Voltio (resta 10 de vida a Squirtle). Si sale 2, ataca con Trueno (resta 11 de 
vida). Imprime qué ataque usó. 
5. Turno de Squirtle (Jugador): Pregúntale al usuario qué ataque desea realizar (P, A o 
B). 
6. El Guardia Insistente: Utiliza un SEGUNDO bucle while para validar la respuesta del 
jugador. Si escribe una letra equivocada, el bucle debe dejarlo atrapado y volver a 
preguntarle el ataque hasta que ingrese una opción válida. 
7. Aplica el daño del ataque de Squirtle a la vida de Pikachu. 
8. Fuera del bucle principal, utiliza un if / else para revisar quién de los dos quedó con 
vida mayor a 0 e imprime al ganador definitivo."""

import random
pikachu = 80
squirtle = 90

while pikachu >= 0 and squirtle >= 0:
    combate_p = random.randint(1,2)
    if combate_p == 1:
        print("¡Pikachu ataca con bola voltio!")
        squirtle = squirtle - 10
    elif combate_p == 2:
        print("Pickachu. ¡Impac Trueno!")
        squirtle = squirtle - 11    

    combate_s = input("Entrenador, ¿Qué ataque va a realizar Squirtle? \nSeleccione \n'A' para 'Acua Cola'\n'B' para 'Burbuja' \n'C' para 'Cabezazo' \n")
    while combate_s != 'A' and combate_s != 'B' and combate_s != 'C':
        combate_s = input("Por favor, ingrese una opción válida. \n Presione 'A', 'B', o 'C'")
    if combate_s == 'A':
        pikachu = pikachu - 10
    elif combate_s == 'B':
        pikachu = pikachu - 11
    elif combate_s == 'C':
        pikachu = pikachu - 12
    
    print("Puntaje final = Pikachu {} - Squirtle {}".format(pikachu,squirtle))
    if pikachu > 0:
        print("¡Pikachu gana!")

    elif squirtle > 0:
        print("¡Squirtle gana!")
    