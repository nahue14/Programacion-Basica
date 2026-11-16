#     Sistema de Seguridad CASTILLO DEL DRAGÓN
print("¡Bienvenido!¡Enhorabuena! Este es el sistema de Seguridad CASTLE OF THE DRAGÓN")

Tipo = input("¿Que raza Osa entrar a Semejante Castillo? (Humano, Elfo, Enano, Orco, Demonio): ")
nombre_héroe = input("Por favor, ingresa tu Nick: ")
nivel = int(input("Nivel alcanzado: "))
vida = int(input("Pon tu porcentaje de vida: "))
llave = input("¿Tienes la llave magica secreta? (S/N): ")
Armamento = input("¿Cual es tu arma? (Espada, Hacha, Arco, Lanza): ")
Nivel_arma = int(input("Nivel de tu arma: "))
Magic = input("¿Utilizas magia? (S/N): ")

if Magic == "S":
    Magia = input("¿Cual es tu magia? (Fuego, Agua, Tierra, Aire, Trueno, Luz, Oscuridad): ")
    if Magia == "Oscuridad":
        print("¡Cuidado! La magia de la Oscuridad es muy poderosa, pero el Dragón del Inframundo es inmune a ella.")
    elif Magia == "Luz":
        print("¡Genial! La magia de la Luz tiene +100% de damage contra el Dragón del Inframundo.")
    elif Magia == "Fuego":
        print("¡Atento! La magia de Fuego tiene -50% de damage contra el Dragón del Inframundo.")
    elif Magia == "Agua":
        print("¡Atento! La magia de Agua tiene +200% de damage contra el Dragón del Inframundo.")
    elif Magia == "Tierra":
             print("¡Atento! La magia de Tierra tiene -10% de damage contra el Dragón del Inframundo.")
    elif Magia == "Aire":
             print("¡Atento! La magia de Aire tiene +25% de damage contra el Dragón del Inframundo.")
    elif Magia == "Trueno":
              print("¡Atento! La magia de Trueno tiene +50% de damage contra el Dragón del Inframundo.")
    else:
         print("Eso no es una Magia... ¡Ten cuidado con lo que dices!")

if vida <= 20:
    print("¡Peligrooooo! Tienes poca vida, curate y vuelve a intentarlo")

if nivel == 99:
    print("¡¡Sorprendente!! Tienes el nivel máximo, las puertas del castillo se abren para los mas experimentados.")

if Nivel_arma >= 50:
    print("Tu arma conoce bien la guerra, pero no te confies ¡el dragón es muy fuerte y puede matarte!.")



if nivel >= 50:
    print("Haz batallado lo suficiente, adentrate en el sofocante CASTLE OF THE DRAGÓN y consigue muchas recompensas estupendas.")

if (nivel >= 15 and vida > 50) or (llave == "S"):
    print("Las puertas del castillo se abren para ti {} y todo el terreno se estremece ante el rugido del Dragón del Inframundo .".format(nombre_héroe))

else:
    print("El GOLEM protector te prohibe el paso. Vuelve cuando seas mas fuerte.")