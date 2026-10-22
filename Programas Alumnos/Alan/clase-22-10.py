import random

print("¡Un Lujo! Encontraste un cofre antiguo con un tesoro dentro, pero cuidado, puede estar protegido por un guardia o un golem.")

print("Abriendo el cofre viejo y todo oxidado en las visagras...")

print("Revisando el interior...")

monedas_oro = random.randint(50, 500)
diamantes = random.randint(1, 5)

print("¡felicidades! encontraste {} monedas de oro y {} diamantes brillantes".format(monedas_oro, diamantes))

print("Espera... He visto un movimiento extraño detrás de ti, parece que hay un guardia o un golem protegiendo el tesoro.")

decicion = input("¿Qué harás? (¿Luchar, Correr?): ")

if decicion == "Luchar" or "luchar":
    print("¡Que valiente! te deseo mucha suerte...")

elif decicion == "Correr" or "correr":
    print("Ya seras mas fuerte....¡Huye deprisa o te alcanzara! .")







