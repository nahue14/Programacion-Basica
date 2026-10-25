"""Operaciones matemáticas y Prioridades
1. Escribe un programa que le pida al usuario que introduzca un primer número y luego un segundo número usando la 
función input(). Recuerda convertir estos ingresos a enteros.
2. Muestra en pantalla el resultado de la suma de ambos números.
3. Muestra en pantalla el resultado de restar el segundo número al primero.
4. Crea una operación que sume ambos números y al resultado de esa suma lo multiplique por 2. Imprime el resultado.
Pista: recuerda usar el orden correcto de las operaciones matemáticas"""

print("-_-_ Operaciones matemáticas _-_-")

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
suma = n1 + n2
resta = n2 - n1
operacion = suma * 2 

print("La suma es {}".format(suma))

print("Si restamos {} a {} nos da {}".format(n2,n1,resta))

print("Si sumamos {} a {}, y lo multiplicamos por 2 nos da {}".format(n1,n2,operacion))
