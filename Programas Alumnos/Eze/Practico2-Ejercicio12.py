#El calabozo

#Imprime una introducción al juego y dale a elegir entre dos caminos (A o B).    
Utiliza if y elif anidados para desarrollar la historia paso a paso según lo que elija. 
El Inventario: En alguna de las habitaciones, haz que el jugador encuentre un objeto útil (como un palo). 
Crea una variable booleana (True/False) para recordar si lo recogió o no. Más adelante en la historia, 
crea una ruta de escape que solo funcione si el jugador cumple dos condiciones a la vez: elegir el camino 
correcto and tener el objeto en el inventario. 4. El Reto Matemático: En otra ruta, haz que un enemigo le 
ponga un desafío matemático aleatorio (ejemplo: multiplicar 13 por un número al azar). Utiliza la librería 
random para generar el número. Si el jugador escribe el resultado correcto, sobrevive. Si no, usa un else 
para narrar su derrota. 

print("Bienvenido al juego del calabozo")
import random
Usuario = input("Ingresa tu nombre: ")
Camino = input("Elige un camino (A o B): ")
if Camino == "A":
    print("Has elegido el camino A: El Inventario.")    
    objeto = input("Encuentras un palo en el camino. ¿Deseas recogerlo? (s/n): ")
    if objeto == "s" and Caminos == "A":
        print("Felicitaciones! Puedes escapar del calabozo.")
        else:
            print("No puedes escapar por aqui del calabozo.")
elif Camino == "B":
    print("Has elegido el camino B: El Reto Matemático.")
    numero_al_azar = random.randint(1, 10)
    resultado_correcto = 13 * numero_al_azar
    UsuarioB = int(input("Adivina cual es el numero clave para sobrevivir, elige un numero del 1 al 10: "))
    if UsuarioB == resultado_correcto:
        print("¡Felicidades! Has sobrevivido al reto matemático.")
    else:
        print("Lo siento, has fallado el reto matemático y has sido derrotado.")

       
    
    
    
