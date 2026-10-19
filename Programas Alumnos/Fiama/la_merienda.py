print("Me voy a la cocina")
print("Abro la nevera")

hay_leche = input("¿Hay leche? (s/n): ")
hay_chocolate = input("¿Hay leche? (s/n): ")

if hay_leche != "s" or hay_chocolate != "s":
    print("Voy hasta el súper")
    if hay_leche != "s":
        print("Compro leche")
    if hay_chocolate != "s":
        print("Compro chocolate")

print("Ponemos la leche en el vaso")
print("Ponemos el chocolate en el vaso")
print("Mezclamos")            