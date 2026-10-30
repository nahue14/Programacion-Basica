#Practico N° 2

"""1)

Ejercicio 1: Preparando la Merienda  
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

"""2)

Ejercicio 2: Validador de Edad  
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

edad= int(input("Cual es tu edad?"))
carnet= input("Que tipo de carnet tenes? \n E (Estudiante) \n P (Pensionista) \n F (familia numerosa) \n N (ninguno) \n")
if 25<= edad and edad <= 35 and carnet == "E" or edad<= 10 or edad<=65 and carnet == "P" and carnet == "F":
    print("Se te aplica el descuento")
else:
    "No se aplica el descuento"

    




