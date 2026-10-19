#     Sistema de Seguridad CASTILLO DEL DRAGÓN
print("¡Bienvenido!¡Enhorabuena! Este es el sistema de Seguridad CASTLE OF THE DRAGÓN")

nombre_héroe = input("Por favor, ingresa tu Nick: ")
nivel = int(input("Nivel alcanzado: "))
vida = int(input("Pon tu porcentaje de vida: "))
llave = input("¿Tienes la llave magica secreta? (S/N): ")
Armamento = input("¿Cual es tu arma? (Espada, Hacha, Arco, Lanza): ")
Nivel_arma = int(input("Nivel de tu arma: "))

if vida <= 20:
    print("¡Peligrooooo! Tienes poca vida, curate y vuelve a intentarlo")

if nivel == 99:
    print("¡¡Sorprendente!! Tienes el nivel máximo, las puertas del castillo se abren para los mas experimentados.")

if Nivel_arma >= 50:
    print("Tu arma conoce bien la batalla, pero no te confies ¡el dragón es muy fuerte y puede matarte!.")

if nivel >= 50:
    print("Haz batallado lo suficiente, adentrate en el sofocante CASTLE OF THE DRAGÓN y consigue muchas recompensas estupendas.")

if (nivel >= 15 and vida > 50) or (llave == "S"):
    print("Las puertas del castillo se abren para ti {} y todo el terreno se estremece ante el rugido del Dragón del Inframundo .".format(nombre_héroe))

else:
    print("El guardia te prohibe el paso. Vuelve cuando seas mas fuerte.")