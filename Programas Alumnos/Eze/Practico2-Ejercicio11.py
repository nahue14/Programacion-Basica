#El primero es el mayor de todos?

print("Problema de determinar si el primero es el mayor de todos")
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
if n1 > n2 and n1 > n3:
    Mensaje = "El primer número es el mayor"
    else:
    Mensaje = "El primer número no es el mayor"

print("Conclusion: {}".format(Mensaje))
