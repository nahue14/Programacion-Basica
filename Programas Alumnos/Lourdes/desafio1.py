print("--- BIENVENIDO AL VIDEOJUEGO LLAMADO CASTILLO DEL DRAGÓN ---")

#Pedir datos
nivel = int(input("Decime tu nivel: "))
puntos_de_vida = int(input("Decime tus puntos de vida: "))
llave_magica_secreta = input ("¿Tenés la llave mágica secreta? (Si/No): ")

if puntos_de_vida < 20:
    print("¡Peligro! Tu salud es muy baja para esta zona.")

if puntos_de_vida == 99:
    print("¡Increíble! Eres un jugador de nivel máximo.")

if (nivel >= 15 and puntos_de_vida > 50) or (llave_magica_secreta == "Si"): 
    print("¡Las puertas del castillo se abren!")

else:
    print("El guardia te prohibe el paso. Vuelve cuando seas más fuerte.")
