"""Crea 4 variables distintas para guardar tú información personal, eligiendo el dato correcto para 
cada una (string, Integer, Float, Boolean): 
1. Tú comida favorita 
2. Tú edad 
3. Tú altura en metros (por ejemplo, 1.7) 
4. Una Variable que indique si tienes mascotas (True o False).
Luego de crearlas, usa la función print() para mostrar el contenido de las cuatro cajas (variables) en la consola."""

comida_fav = input("Ingresa tú comida favorita: ")
edad = int(input("ingresa tú edad: "))
altura = float((input("Ingresa tú altura en metros: ")))
mascota = input("¿Tiene mascota? S/N")

print("Tú comida favorita es : {}".format(comida_fav))
print("Tienes {} años".format(edad))
print("Mides: {} m".format(altura))

if mascota == "S":
    print("Tienes mascota")
elif mascota == "N":
    print("No tienes mascota")
else: 
    print("Error de tipeo. No se especifica mascota")
