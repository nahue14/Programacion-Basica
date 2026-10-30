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
pickachu = 80
