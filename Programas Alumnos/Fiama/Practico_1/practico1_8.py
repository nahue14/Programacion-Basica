"""Ejercicio 8: Conversor de Moneda (Tasa Fija) Escribe un programa que pida al usuario ingresar una cantidad de libras 
esterlinas (como número entero). Luego, calcula y muestra el valor equivalente en euros, asumiendo un tipo de 
cambio fijo donde 1 libra equivale a 1.13 euros."""

print("   * CONVERSOR DE MONEDA *\n")

libras = int(input("Ingrese el valor en libras esterlinas: "))
euros = libras * 1.13
print("\n{} libras esterlinas equivalen a {} euros.".format(libras,euros))