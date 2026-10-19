"""Crea cuatro variables distintas para guardar tu información personal, eligiendo el tipo de dato correcto
para cada una (Texto/String, Entero/Integer, Racional/Float o Lógico/Boolean)
1. Tú comida favorita
2. Tú edad
3. Tú altura en metros (Por ejemplo: 1.70)
4. Una variable que indique si tenés mascotas (True o False). Consigna: Luego de crearlas, usa la función print 
para mostrar el contenido de las cuatro cajas (Variables) en la consola"""


comida_fav = input("Ingrese su comida favorita: ")
edad = int(input("¿Cuál es su edad?: "))
altura = float(input("Ingrese su altura en metros (con un punto): "))

mascota = input("¿Tiene Mascotas? Responda por SI o NO: ")

print("Su comida favorita es: " + comida_fav)
print("Tiene ", edad, " años")
print("mide ", altura)
if mascota == 'SI':
    print("Tiene mascota")
elif mascota == 'NO':
    print("No tiene mascota")
else : print("Error")


"""if mascota != 'SI' or mascota != 'NO' :
    mascota = input("Ingrese 'SI' o 'NO': ")

elif mascota == 'SI':
    print("Tiene mascotas")

elif mascota == 'NO':
    print("No tiene mascotas")"""
    

"""if (mascota != 'SI' or mascota != 'NO':
    print("Responda por SI o NO: ")
)"""

""" if mascota : True 
print("Tiene mascota")   
else if mascota : False
print("No tiene mascotas")"""

"""while mascota != 'SI' or mascota != 'NO':
    mascota = input("Ingrese 'SI' o 'NO': ")
if mascota == 'SI' :
    mascota = True
elif mascota == 'NO' :
    mascota = False"""