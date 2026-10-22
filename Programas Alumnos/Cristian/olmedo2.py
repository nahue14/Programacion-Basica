#BIENVENIDOS AL CASTILLO DEL DRAGON:
print("Bienvenido al castillo del dragon")
tu_nombre=input("Escribe tu nombre: ")
tu_nivel=int(input("Cual es tu nivel: "))
tus_puntos_de_vida=int(input("Cuantos puntos de vida tenes: "))
tu_llave_magica=input("Tienes la llave magica: s/n: ")

if tus_puntos_de_vida <= 20:
    print("!peligro¡ tu salud es muy baja para esta zona.")

if tu_nivel == 99 :
    print("!increible¡ eres un jugador de nivel maximo.")

if tu_nivel >= 50 :
    print("!las puertas del castillo se abren¡")

if (tu_nivel >= 15 and tus_puntos_de_vida > 50) or (tu_llave_magica == "s") :
   print("!las puertas del castillo se abren¡")

else :
 print("el guardia te prohibe el paso. Vuelve cuando seas mas fuerte¡")
