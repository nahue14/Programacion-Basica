"""Ejercicio 11: El Validador de Descuentos (Uso de else)
1. Solicítale al usuario que ingrese su edad (como número entero).
2. Solicítale que ingrese su tipo de carnet. Dale las siguientes opciones en el texto de entrada: E para Estudiante, P para Pensionista, 
F para Familia numerosa, o N para Nada.
3. Crea una única condición if utilizando operadores lógicos (and, or) que evalúe si la persona tiene derecho a un descuento. 
El descuento aplica si se cumple al menos una de estas reglas:
○ Tiene entre 25 y 35 años Y su carnet es "E".
○ Tiene 10 años o menos.
○ Tiene 65 años o más Y su carnet es "P".
○ Su carnet es "F" (sin importar la edad).
4. Si la condición masiva se cumple, imprime "Se te aplica el descuento".
5. Utiliza la estructura else (si no) para imprimir "No se te aplica el descuento" en caso de que ninguna de 
las reglas anteriores sea verdadera."""

print("* VALIDADOR DE DESCUENTOS *\n")

edad = int(input("Ingrese su edad: "))
carnet = input("Ingrese su tipo de carnet. Digite:\n'E' para Estudiante\n'P' para Pensionista\n'F' para Familia numerosa\n'N' para Nada\n")
while carnet != 'E' and carnet != 'P'and carnet != 'F'and carnet != 'N':
    carnet = input("\nIngrese una opción válida: ")

if edad >= 25 and edad <= 35 and carnet == 'E':
    print("\nSe aplica descuento")
elif edad <= 10:
    print("\nSe aplica descuento")
elif edad >= 65 and carnet == 'P':
    print("\nSe aplica descuento")
elif carnet == 'F':
    print("\nSe aplica descuento")
else:
    print("\nNo se aplica descuento")