#Practico N° 2

"""Ejercicio 1: Preparando la Merienda  
1.	Imprime dos mensajes en pantalla simulando que vas a la cocina y abres la heladera. 
2.	Pregunta al usuario si hay leche (S/N) y si hay cacao (S/N) utilizando la función input(). 
3.	Crea una condición if para evaluar el faltante: si no hay leche (!= "S") o no hay cacao (!= "S"), imprime el mensaje "Voy hasta el súper". 
4.	Dentro de ese mismo bloque lógico, agrega otros dos if independientes: uno para imprimir "Compro leche" (si la respuesta de la leche fue distinta a "S") y otro para imprimir "Compro cacao". 
5.	Fuera de todas las condiciones (sin sangría), imprime los pasos finales que ocurrirán siempre: "Ponemos la leche en el vaso", "Ponemos el cacao en el vaso" y "Mezclamos". """

"""print("Voy hacia la cocina...")
print("")
print("Abro la Heladera...")
print("")
Leche = input("Hay leche? (s/n): ")

Cacao= input("Hay cacao? (s/n): ")

if Leche !="s" or Cacao != "s":
     print("Voy hasta el super...")
elif Leche!= "s":
    print("Compro leche...")
elif Cacao !="s":
     print("compro Cacao...")


print("Ponemos la leche en el vaso")
print("Ponemos el cacao en el vaso")
print("Mezclamos")
print("A BEBEEEER!")"""

"""Ejercicio 2: Validador de Edad  
1.	Crea un programa que le solicite al usuario ingresar su edad como un número entero. 
2.	Utiliza una condición if para evaluar si la edad es mayor o igual (>=) a 18. 
3.	Si la condición se cumple, imprime el mensaje: 'Puede acceder al permiso'. 
4.	Si la condición no se cumple, utiliza un else para imprimir: 'No puede acceder al permiso'. """

"""edad= int(input("Cuantos años tenes?"))

if edad >= 18:
    print("Puedes acceder al permiso.")
else:
    "No puedes acceder al permiso."

    """
"""Ejercicio 3: El Validador de Descuentos  
1.	Solicita al usuario que ingrese su edad (convertida a número entero). 
2.	Solicita que ingrese su tipo de carnet brindando estas opciones: E (Estudiante), P (Pensionista), F (Familia numerosa) o N (Ninguno). 
3.	Crea una única gran condición if que evalúe si la persona tiene derecho a un descuento. El descuento se aplica si se cumple al menos una de estas reglas: 
○ Tiene entre 25 y 35 años Y su carnet es "E". 
○ Tiene 10 años o menos. 
○ Tiene 65 años o más Y su carnet es "P". ○ Su carnet es "F" (sin importar la edad). 
4.	Si la condición matemática se cumple, imprime "Se te aplica el descuento". 
5.	Utiliza la estructura else para imprimir "No se te aplica el descuento" en caso de que ninguna regla sea verdadera. 
"""
"""
edad= int(input("Cual es tu edad?"))
carnet= input("Que tipo de carnet tenes? \n E (Estudiante) \n P (Pensionista) \n F (familia numerosa) \n N (ninguno) \n")
if 25<= edad and edad <= 35 and carnet == "E" or edad<= 10 or edad<=65 and carnet == "P" and carnet == "F":
    print("Se te aplica el descuento")
else:
    "No se aplica el descuento"
"""
"""Ejercicio 4: Las Trampas del Azar  
1.	Importa la librería random y genera un "número ganador" aleatorio entre el 1 y el 10. 
2.	Solicita al usuario que elija y escriba un número. 
3.	Utiliza condicionales if independientes para evaluar la entrada del usuario y mostrar un mensaje distinto en cada caso: 
○ Si acierta el número exacto, infórmale que ha ganado. 
○ Si ingresa un número mayor a 10, avísale que se ha pasado del límite. ○ Si ingresa un número menor a 1, indícale que se ha quedado corto. 
Trampas secretas: Si el usuario ingresa 666, dile que eligió el número de la bestia. 
Si ingresa -666, dile que es doblemente maligno por ser negativo. 4. Al final del programa, imprime siempre cuál era el número ganador utilizando .format(). """

"""import random

numero_ganador= random.randint(1,10)

usuario=int(input("elije un numero: "))
if usuario == numero_ganador:
    print("Has ganado!")
elif usuario > 10:
    print("Has pasado el limite")
elif usuario<1:
    print("Te has quedado corto.")
if usuario == 666:
    print("Elegiste el numero de la bestia.")
elif usuario == -666:
    print("Es doblemente maligno por ser negativo")
print("El numero ganador fue {} .".format(numero_ganador))
    
"""

"""Ejercicio 5: El Test de Personalidad  
1.	Imprime un título de bienvenida con un formato prolijo. 
2.	Crea una variable llamada puntuación y dale un valor inicial de 0. 
3.	Realiza 3 preguntas al usuario, dándole en cada una las opciones "A", "B" o "C". 
4.	Utiliza una cadena de if y elif para cada pregunta. Según la letra que
elija el usuario, súmale puntos a la variable puntuacion (por ejemplo: A suma 10, B suma 5, C suma 0). 
5.	Regla de validación: Si el usuario teclea una letra que no existe, usa un else para imprimir el mensaje
"Las opciones posibles son A, B y C" y utiliza la instrucción exit() para detener el programa inmediatamente. 
6.	Al final de tu código, evalúa la puntuación total usando if / elif / else. Muestra un resultado diferente 
si sacó más de 25 puntos, si sacó más de 15, o si sacó menos. 
"""
"""
print("       ¡Bienvenido! Esto es un test de personalidad.")

A=10
B=5
C=0
puntuacion= 0
pregunta1=input("Cuan alegre eres? \n A)Muy alegre \n B)Medianamente alegre \n C)Poco alegre \n")
if pregunta1== "A":
    puntuacion=puntuacion+A
elif pregunta1== "B":
    puntuacion=puntuacion+B
elif pregunta1=="C":
    puntuacion=puntuacion+C
else:
    "Las opciones son A, B y C"
    exit()
print("Tu puntuacion por el momento es de: {} puntos.".format(puntuacion))

pregunta2=input("Cuan sociable eres? \n A)Muy sociable \n B)Medianamente sociable \n C)Poco sociable \n")
if pregunta2== "A":
     puntuacion=puntuacion+A
elif pregunta2== "B":
    puntuacion=puntuacion+B
elif pregunta2=="C":
    puntuacion=puntuacion+C
else:
    "Las opciones son A, B y C"
    exit()

print("Tu puntuacion por el momento es de: {} puntos.".format(puntuacion))

pregunta3=input("cuan intrepido eres? \n A)Muy intrepido \n B)Medianamente intrepido \n C)Poco intrepido \n")
if pregunta3== "A":
    puntuacion=puntuacion+A
elif pregunta3== "B":
    puntuacion=puntuacion+B
elif pregunta3=="C":
    puntuacion=puntuacion+C
else:
    "Las opciones son A, B y C"
    exit()
print("Tu puntuacion por el momento es de: {} puntos.".format(puntuacion))
"""
"""Ejercicio 6: Conversor de Monedas Avanzado 
1.	Al principio de tu programa, crea variables para guardar los tipos de cambio exactos (ejemplo: dolar_euro = 0.91, libra_euro = 1.18). 
2.	Imprime un menú preguntando "¿Qué desea hacer?" y ofrece 4 opciones (A, B, C, D) para convertir entre dólares, euros y libras. 
3.	Utiliza condicionales if y elif para detectar qué opción eligió. 
4.	Dentro de cada condicional, solicítale al usuario que introduzca la cantidad de dinero utilizando float(input()). 
(Bonus: intenta guardar el texto de la pregunta en una variable con formato para no repetir tanto código). 
5.	Calcula el resultado e imprímelo utilizando .format(). 
6.	Agrega un else al final para el caso en que el usuario no elija una opción válida. 
"""

"""dolar_euro= 0.91
libra_euro= 1.18

convertir= input("Que desea hacer? \n A) Convertir de Dolares a Euros \n B) Convertir de Euros a Dolares \n C) Convertir de Libras a Euros \n D) Convertir de Euros a Libras \n")
if convertir == "A":
    cantidad= float(input("Ingrese la cantidad de Dolares a convertir: "))
    resultado= cantidad*dolar_euro
    print("El resultado es: {} Euros".format(resultado))
elif convertir == "B":
    cantidad= float(input("Ingrese la cantidad de Euros a convertir: "))
    resultado= cantidad/dolar_euro
    print("El resultado es: {} Dolares".format(resultado))
elif convertir == "C":
    cantidad= float(input("Ingrese la cantidad de Libras a convertir: "))
    resultado= cantidad/libra_euro
    print("El resultado es: {} Euros".format(resultado))
elif convertir == "D":
     cantidad= float(input("Ingrese la cantidad de Euros a convertir: "))
     resultado= cantidad*libra_euro
     print("El resultado es: {} Libras".format(resultado))
else:
    print("La opcion ingresada no es valida. Las opciones son A, B, C o D. Vuelva a intentarlo.")
    """

"""Ejercicio 7: El Asesor de Compras 
1.	Crea una variable llamada movil_ideal y asígnale el valor "Ninguno". 
2.	Pregunta al usuario si prefiere iOS (I) o Android (A). 
3.	Rama iOS: Si elige "I", pregúntale si tiene dinero (S/N). Si tiene, el movil_ideal es un "Iphone Ultra Pro Max". Si no tiene, es un "Iphone usado". 
4.	Rama Android: Si elige "A", pregúntale si tiene dinero. Si NO tiene, recomiéndale un "TCL". 
Si SÍ tiene, hazle una tercera pregunta: "¿Te importa la cámara?". Si responde que sí, recomiéndale un "Xiaomi"; si responde que no, un "Samsung". 
5.	Al final del programa, imprime el mensaje: "Tu móvil ideal es " + movil_ideal. """
"""
movil_ideal= "Ninguno"

pregunta= input("Que sistema operativo prefieres? \n I) iOS \n A) Android \n")

if pregunta == "I":
    dinero= input("Tienes dinero? (S/N): ")
    if dinero == "S":
        movil_ideal= "Iphone Ultra Pro Max"
    else:
        movil_ideal= "Iphone usado"
elif pregunta == "A":
    dinero= input("Tienes dinero? (S/N): ")
    if dinero == "N":
        movil_ideal= "TCL"
    elif dinero == "S":
        camara= input("Te importa la camara? (S/N): ")
        if camara == "S":
            movil_ideal= "Xiaomi"
        else:
            movil_ideal= "Samsung"
print("Tu movil ideal es: {}".format(movil_ideal))
"""

"""Ejercicio 8: Guardando el Resultado  
1.	Solicita al usuario que ingrese dos números enteros por teclado. Guarda el primero en la variable a y el segundo en la variable b. 
2.	Compara ambos números usando un if para ver si a es estrictamente mayor que b (a > b). 
3.	Si es mayor, crea una nueva variable llamada may y asígnale el valor de a. 
4.	Si no es mayor, utiliza un else para asignarle a la variable may el valor de b. 
5.	Fuera de las condiciones, imprime el resultado final mostrando la variable guardada: 'El mayor es:', may. """
"""
v_a= int(input("Ingrese un numero: "))
v_b= int(input("Ingrese otro numero: ")) 

if v_a > v_b:
    may= v_a
else:
    may= v_b
print("El mayor es:", may)
"""

 
"""Ejercicio 9: Opciones Múltiples 
1.	Pídele al usuario que ingrese un número de opción (conviértelo a entero y guárdalo en la variable opción). 
2.	Utiliza el conector lógico or en un único if para evaluar si la opción ingresada es igual a 1, igual a 3, o igual a 5. 
3.	Si se cumple cualquiera de esas tres condiciones, imprime 'Opción correcta'. 
4.	Si ingresa cualquier otro número, utiliza un else para imprimir 'Opción incorrecta'. """
"""
numero= int(input("Ingrese un numero de opcion: "))
if numero == 1 or numero == 3 or numero == 5:
    print("Opcion correcta")
else:
    print("Opcion incorrecta")"""

"""Ejercicio 10: Evaluación de Crédito  
1.	Solicita al usuario dos datos numéricos: su sueldo y su antigüedad laboral. 
2.	Para que el banco otorgue un crédito, se deben cumplir ambas reglas al mismo tiempo. Utiliza el conector 
lógico and en un if para evaluar: si el sueldo es mayor a 15000 Y la antigüedad es mayor o igual a 10. 
3.	Si ambas son verdaderas, imprime 'Crédito concedido'. 
4.	Utiliza un else para imprimir 'Crédito rechazado' en caso de que falle alguna de las dos condiciones. """
"""
sueldo= int(input("Ingrese su sueldo: "))
antiguedad= int(input("Ingrese su antiguedad laboral: "))

if sueldo > 15000 and antiguedad >= 10:
    print("Credito concedido")     
else:
    print("Credito rechazado")
   """

"""Ejercicio 11: ¿El primero es el mayor de todos? 
1.	Muestra un título en pantalla usando print que diga: 'Problema de determinar si el primero es el mayor'. 
2.	Solicita al usuario que ingrese tres números enteros y guárdalos en las variables n1, n2 y n3. 
3.	Utiliza un if con el conector and para evaluar si n1 es mayor a n2 Y además n1 es mayor a n3. 
4.	En lugar de imprimir el resultado directamente, guárdalo en una variable llamada mensaje.
Si la condición anterior se cumple, la variable mensaje debe decir 'El primero es el mayor'. 
5.	Si no se cumple, utiliza un else para que la variable mensaje guarde el texto 'El primero no es el mayor'. 
6.	Al final de todo el programa, imprime: 'Conclusión:', mensaje. 
"""
"""
print("Problema de determinar si el primero es el mayor")
n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese otro numero: "))
n3= int(input("Ingrese otro numero: "))
if n1 > n2 and n1 > n3:
     mensaje= "El primero es el mayor"
else:
    mensaje= "El primero no es el mayor"


print("Conclusión: {}".format(mensaje))"""

"""Ejercicio 12: El calabozo 
1.	Imprime una introducción al juego y dale a elegir entre dos caminos (A o B). 
2.	Utiliza if y elif anidados para desarrollar la historia paso a paso según lo que elija. 
3.	El Inventario: En alguna de las habitaciones, haz que el jugador encuentre un objeto útil (como un palo). 
Crea una variable booleana (True/False) para recordar si lo recogió o no. Más adelante en la historia, crea una ruta de escape que solo funcione 
si el jugador cumple dos condiciones a la vez: elegir el camino correcto and tener el objeto en el inventario. 
4.	El Reto Matemático: En otra ruta, haz que un enemigo le ponga un desafío matemático aleatorio (ejemplo: multiplicar 13 por un número al azar).
 Utiliza la librería random para generar el número. Si el jugador escribe el resultado correcto, sobrevive. Si no, usa un else para narrar su derrota. 
"""
"""print("       BIENVENIDOS AL CALABOZO DE WESTOLD")
import random
agujero= input("Empiezas tu VISITA por el calabozo... \n Te cruzas con un viejo con cara amable y te indica los mejores caminos por donde ir.. \n Cual opcion  elijes?: \n A) Celda Roma. \n B)Celda Montana.  \n")

if agujero == "A":
    guardia=input("Entras en la Celda Roma y te encuentras con un guardia enojado... \n A) Te enfrentas a el? \n B) Prefieres huir.\n")
    if guardia == "A":
        Ganador= print("¡Bien! Ha costado pero has saldido victorioso, sigue adelante..")
    elif guardia == "B":
        print("Huyes! pero te cruzas con otro guardia que te pone un desafio matematico... \n Si lo resuelves, podras salir del calabozo. \n Si no, lamentablemente morirás... \n")
        num_aleatorio= random.randint(1,10)
        print("El guardia te dice: Multiplica 13 por el numero {} y dime el resultado.".format(num_aleatorio))
        resultado= int(input("Ingresa tu resultado: "))
        if resultado == 13*num_aleatorio:
               print("¡Bien! Has resuelto el desafio matematico y has sobrevivido. \n Ahora puedes salir del calabozo.")
        else:
               print("¡Mal! No has resuelto el desafio matematico y lamentablemente has muerto en el calabozo.")
        
    else:
        print("Te Has Equivocado esa NO ES UNA OPCION. ¡VETE DEL CALABOZO!")
if agujero == "B":
    print("Entras a la Celda Montana y ves un objeto tirado lleno de lodo... \n" \
    "¡Enhorabuena! Encontraste un puñal oxidado..")
    recogio= input("¿Deseas recogerlo? (S/N): ")
    if recogio == "S":
            print("¡Bien! Ahora tienes el puñal, y hacia la derecha se vé una salida.")
    else:
     print("¡Mal! No tienes el puñal, y hacia la derecha se vé una salida, pero no podrás abrirla sin el puñal.")"""

"""Ejercicio 13: Calculadora de Tarifas  
Vas a programar el sistema de cobro de una empresa de alquiler de vehículos basándote en los kilómetros recorridos. 
1.	Solicita al usuario que ingrese un número entero y guárdalo en la variable kilometraje. 
2.	Evalúa si el kilometraje es menor o igual a 300. Si es así, la variable monto a cobrar será de 500. 
3.	Si superó los 300 km, abre un bloque else. Adentro de este bloque, primero calcula los kilómetros extra creando la variable excedente = kilometraje - 300. 
4.	Luego, anida un nuevo if (dentro de ese mismo else) para evaluar si el kilometraje total es menor
 o igual a 1000. Si es así, calcula la tarifa: monto = 500 + 3 * excedente. 
5.	Si el kilometraje total superó los 1000 km, agrega un último else (alineado con el if anidado) y 
calcula la tarifa diferenciada: monto = 500 + 1.5 * excedente. 
6.	Finalmente, fuera de todas las condiciones, imprime el total a pagar: 'El importe a pagar es:', monto. 
"""

"""kilometraje = int(input("Ingresa tu kilometraje: "))

if kilometraje <= 300:
    monto=500
else:
    excedente= kilometraje -300
    if kilometraje <= 1000:
        monto= 500+3*excedente
    else:
        monto=500+1.5*excedente

print("El importe a pagar es: {}".format(monto))
"""

"""Ejercicio 14: Combate 
1.	Importa la función randint de la librería random. 
2.	Establece la vida inicial: Pikachu = 80, Squirtle = 90. 
3.	Crea un bucle while principal para que el combate se repita mientras la vida de Pikachu sea mayor a 0 Y la vida de Squirtle sea mayor a 0. 
4.	Turno de Pikachu (Automático): Genera un número al azar (1 o 2). Si sale 1, ataca con Bola Voltio (resta 10 de vida a Squirtle).
Si sale 2, ataca con Trueno (resta 11 de vida). Imprime qué ataque usó. 
5.	Turno de Squirtle (Jugador): Pregúntale al usuario qué ataque desea realizar (P, A o B). 
6.	El Guardia Insistente: Utiliza un SEGUNDO bucle while para validar la respuesta del jugador.
 Si escribe una letra equivocada, el bucle debe dejarlo atrapado y volver a preguntarle el ataque hasta que ingrese una opción válida. 
7.	Aplica el daño del ataque de Squirtle a la vida de Pikachu. 
8.	Fuera del bucle principal, utiliza un if / else para revisar quién de los dos quedó con vida mayor a 0 e imprime al ganador definitivo. """

import random
pikachu= 80
squirtle= 90

while pikachu > 0 and squirtle > 0:
    PIKAPIKA= random.randint(1,2)
    if PIKAPIKA == 1:
        squirtle -= 10
        print("Pikachu ataca con Electrobola y le resta 10 de vida a Squirtle.")
    else:
        squirtle -= 11
        print("Pikachu ataca con Atack Trueno y le resta 11 de vida a Squirtle.")

    SCUARSCUAR= input("Es tu turno, Squirtle. ¿Qué ataque deseas realizar? (P) Pistola Agua, (A) Acua Jet, (B) Burbuja: ")
    while SCUARSCUAR != "P" and SCUARSCUAR != "A" and SCUARSCUAR != "B":
            print("¡Opción inválida! Por favor, elige un ataque válido.")
            SCUARSCUAR= input("¿Qué ataque deseas realizar? (P) Pistola Agua, (A) Acua Jet, (B) Burbuja: ")

    if SCUARSCUAR == "P":
        pikachu -= 9
        print("Squirtle ataca con Pistola Agua y le resta 9 de vida a Pikachu.")
    elif SCUARSCUAR == "A":
        pikachu -= 8
        print("Squirtle ataca con Acua Jet y le resta 8 de vida a Pikachu.")
    else:
        pikachu -= 7
        print("Squirtle ataca con Burbuja y le resta 7 de vida a Pikachu.")
    
    print("La vida de Pikachu es ahora: {}".format(pikachu))
    print("La vida de Squirtle es ahora: {}".format(squirtle))
if pikachu > 0:
     print("¡Pikachu ha ganado el combate!")
else:
     print("¡Squirtle ha ganado el combate!")


     
 





