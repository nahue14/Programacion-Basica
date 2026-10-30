"""Ejercicio 5: El Test de Personalidad  
1. Imprime un título de bienvenida con un formato prolijo. 
2. Crea una variable llamada puntuación y dale un valor inicial de 0. 
3. Realiza 3 preguntas al usuario, dándole en cada una las opciones "A", "B" o "C". 
4. Utiliza una cadena de if y elif para cada pregunta. Según la letra que elija el usuario, 
súmale puntos a la variable puntuacion (por ejemplo: A suma 10, B suma 5, C suma 0). 
5. Regla de validación: Si el usuario teclea una letra que no existe, usa un else para imprimir 
el mensaje "Las opciones posibles son A, B y C" y utiliza la instrucción exit() para detener 
el programa inmediatamente. 6. Al final de tu código, evalúa la puntuación total 
usando if / elif / else. Muestra un resultado diferente si sacó más de 25 puntos, si sacó más 
de 15, o si sacó menos."""

print("\n_-_ TEST DE PERSONALIDAD _-_\n")

puntuacion = 0

duda1 = input("\n¿Alguna vez viviste alguna experiencia paranormal?\n a. Si\n b. No\n c.No quiero contestar\n")
#while duda1 != 'a' and duda1 != 'b' and duda1 != 'c':
#    duda1 = input("Ingrese una opción válida: Digite 'a', 'b' o 'c': ")
if duda1 == 'a':
    puntuacion = puntuacion + 10
    print("Wow! quiero saber más\n Sumas 1000 de aura")

elif duda1 == 'b':
    puntuacion = puntuacion + 6
    print("Pff! qué aburrido")
    duda1 = input("¿Estás seguro? Responde S/N: ")
    print("Ok")

elif duda1 == 'c':
    puntuacion = puntuacion - 6
    print("Pff! qué aburrido\nNos vemos pronto")
else :
    print("Las opciones posibles son a, b y c")
    exit()

duda2 = input("\n¿Te consideras una persona honesta?\n a. Si\n b. No\n c.A veces\n")
#while duda2 != 'a' and duda2 != 'b' and duda2 != 'c':
#   duda2 = input("Ingrese una opción válida: Digite 'a', 'b' o 'c': ")
if duda2 == 'a':
    puntuacion = puntuacion - 10
    print("\nSNo lo creo")

elif duda2 == 'b':
    puntuacion = puntuacion + 10
    print("Agradecemos la honestidad")

elif duda2 == 'c':
    puntuacion = puntuacion + 10
    print("OK\nNos vemos pronto")

else :
    print("Las opciones posibles son a, b y c")
    exit()
duda3 = input("\n¿Tenés a alguien detras tuyo?\n a. Si\n b. No\n c. Espero que no \n")
#while duda3 != 'a' and duda3 != 'b' and duda3 != 'c':
#    duda3 = input("Ingrese una opción válida: Digite 'a', 'b' o 'c': ")
if duda3 == 'a':
    puntuacion = puntuacion + 10
    print("\n¡Qué bueno que puedas verme")

elif duda3 == 'b':
    puntuacion = puntuacion + 15
    print("¿Seguro?")

elif duda3 == 'c':
    puntuacion = puntuacion + 10
    print("Jaja\n ¡Date la vuelta!")
else :
    print("Las opciones posibles son a, b y c")
    exit()

if puntuacion <= 10:
    print("Tú test de personalidad no dio muy bien. Te recomiendo un especialista")