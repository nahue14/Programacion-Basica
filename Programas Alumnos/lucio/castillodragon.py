print("                          ¡BIENVENIDO AL CASTILLO DEL DRAGON!                          ")

nivel = int(input("tu nivel de personaje: "))
puntos_de_vida = int(input("tu puntos de vida: "))
llave_magica = input("llave magica? (s/n): ")

if puntos_de_vida<20 :
    print("¡peligro! tu salud es baja para esta zona ")
if nivel == 99 :
    print("¡increible! eres un jugador de nivel maximo")
if (nivel>= 15 and puntos_de_vida >= 50) or (llave_magica == "s"):
    print("¡las puertas del castillo se abren!")
else : 
    print("el guardia te prohibe el paso. vuelve cuando seas mas fuerte.")