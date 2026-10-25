"""Ejercicio 7: Conversor de Temperatura Escribe un programa que solicite al usuario ingresar una temperatura en grados Fahrenheit 
(como número entero). El programa debe calcular y mostrar en pantalla la temperatura equivalente en grados Celsius
utilizando la fórmula (F - 32) * (5/9)."""

print("_-_ CONVERSOR DE TEMPERATURA _-_\n")

grados_f = int(input("Ingrese la temperatura en grados Fahrenheit: "))

grados_c = (grados_f - 32) * (5 / 9)

print("\nEl equivalente de {}°F es de {}°C".format(grados_f,grados_c))