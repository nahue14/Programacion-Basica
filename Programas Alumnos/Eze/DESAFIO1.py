print ("---Castillo del dragon---")

nombre_jugador = input("Ingresa tu nombre de jugador: ")
nivel = int(input("Ingresa tu nivel: "))
puntos_de_vida= int(input("Ingresa tus puntos de vida: "))
llave_magica_secreta= input("Tienes llave secreta? S/N: ")

#Bloque 1:
if puntos_de_vida<20:
    print("¡Peligro! Tu salud es muy baja para esta zona.")
if nivel==99:
    print("¡Increible! Eres un jugador de nivel maximo.")

#Bloque 2: 
if (nivel>=15 and puntos_de_vida>50) or (llave_magica_secreta=="S"):
    print("Las puertas del castillo se abren.")
else:
    print("El guardia te prohibe el paso. Vuelve cuando seas mas fuerte.")
