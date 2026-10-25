"""Ejercicio 6: Calculadora de Índice de Masa Corporal (IMC)
Este ejercicio es ideal porque los obliga a utilizar el operador de potencia (**) que aparece en la pirámide de prioridades y a mezclar 
variables de tipo float.
Consigna para los alumnos:
1. Solicita al usuario su peso en kilogramos (puede ser un número con decimales, así que conviértelo a float).
2. Solicita su altura en metros (también convertido a float).
3. Calcula el Índice de Masa Corporal (IMC). La fórmula matemática es: el peso dividido por la altura elevada al cuadrado (altura ** 
2). Pista: respeta la prioridad de operadores utilizando paréntesis.
4. Muestra en pantalla el IMC calculado.
5. Para la Organización Mundial de la Salud, un IMC menor a 25 se considera dentro del peso saludable. Utiliza el operador < para 
evaluar si el IMC del usuario es saludable y muestra el resultado booleano en pantalla"""

print("*** CALCULADORA DE IMC ***\n")

peso = float(input("Ingrese su peso: "))
altura = float(input("\nIngrese su altura: "))
imc = peso / (altura ** 2)

print("\n Tú IMC es: {}".format(imc))

if imc <= 25:
    print("\n De acuerdo a los parámetros de la OMS, tienes un peso saludable")
elif imc > 25:
    print("\n De acuerdo a los parámetros de la OMS, No tienes un peso saludable")