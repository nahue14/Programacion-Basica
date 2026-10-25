"""Ejercicio 9: Conversor de Moneda (Tasa Dinámica)
Crea un programa que solicite al usuario ingresar primero una cantidad de libras (permitiendo números con decimales)
y luego el tipo de cambio actual de libras a euros. El programa debe multiplicar ambos valores y mostrar cuántos euros representan."""

print("   * CONVERSOR DE MONEDA *\n")

libras = float(input("Ingrese el valor en libras esterlinas: "))
cambio = float(input("\n Ingrese el tipo de cambio en euros: "))
euros = libras * cambio

print("\n{} libras esterlinas a un cambio de {}, equivalen a {} euros.".format(libras, cambio, euros))

