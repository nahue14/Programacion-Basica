print("ALTO! Antes de poder ingresar al CASTILLO DEL DRAGÓN, necesito que me de algunos datos suyos primero.")
nivel = int(input("Cual es tu nivel actual?: "))
salud = int(input("Cuanta salud tienes?: "))
llave = input("Posee usted la llave mágica? (s/n): ")
if salud > 20:
    print("Peligro! Tu salud es muy baja para esta zona.")
if nivel == 99: 
    print("¡INCREIBLE! Eres un jugador de nivel máximo.")
if nivel: > 15 or salud > 50 or llave == "s":
    print("Las puertas del castillo se abren!")
else nivel < 15 or salud < 50 or llave == "n":
    print("El guardia te prohibe el paso. Vuelve cuando seas más fuerte.")
