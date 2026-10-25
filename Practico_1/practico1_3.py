"""Armado de perfiles
1. Pregúntale al usuario su nombre y luego su apellido utilizando input().
2. Muestra un mensaje que diga "Tu nombre completo es [Nombre] [Apellido]" pegando los string con el símbolo + 
3. Ahora, pregúntale cuál es su número de la suerte
4. Muestra un nuevo mensaje que diga "Hola [Nombre] [Apellido], tú número de la suerte es el [Número] utilizando unicamente
la función .format() en un sólo renglón para incluir los 3 datos"""

print("* BIENVENIDO * \n")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("\nTú nombre completo es " + nombre + " " + apellido + "\n")

num_suerte = int(input("¿Cuál es tú número de la suerte? "))

print("\nHola {} {}, tú número de la suerte es el {}".format(nombre, apellido, num_suerte))