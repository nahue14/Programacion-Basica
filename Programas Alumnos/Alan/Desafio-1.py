#     Sistema de Seguridad CASTILLO DEL DRAGÓN
print("Bienvenido al Sistema de Seguridad CASTILLO DEL DRAGÓN")

nombre_héroe = input("Por favor, ingresa tu nombre de héroe: ")
nivel = int(input("Ingresa tu nivel: "))
vida = int(input("Ingresa tu nivel de vida: "))
llave = input("¿Tienes la llave magica secreta? (S/N): ")

if vida <= 20:
    print("¡Peligrooooo! Tu salud es muy baja para esta zona")

if nivel == 99:
    print("¡Increible! Eres un jugador de nivel maximo")

if (nivel >= 15 and vida > 50) or (llave == "S"):
    print("Las puertas del castillo se abren")
else:
    print("El guardia te prohibe el paso. Vuelve cuando seas mas fuerte.")