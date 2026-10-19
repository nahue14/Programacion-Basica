nombre = input("Ingrese su nombre: ")
print("hola {}".format(nombre))

t = 13,14,15
print(t)


#Crear un programa que pida dos variables al usuario (numeros enteros) y compararlos con == y !=. crear dos If
#que devuelvan (print) si son iguales o distintos

num1 = int(imput("Ingrese un número: "))
num2 = int(imput("Ingrese un número: "))

if num1 == num2:
    print("Son iguales")
elif num1 != num2:
    print("Son distintos")