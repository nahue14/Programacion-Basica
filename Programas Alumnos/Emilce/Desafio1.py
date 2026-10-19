print("---Bienvenidos al Castillo del Dragon---")
Nivel = int (input("Ingrese numero de su nivel:"))
Numero_de_vidas= int(input("Ingrese Numero_de_vida:"))
Llave_Magica= input("Tiene Llave_Magica ? (s/n):")

if Numero_de_vidas > 20:
    print("PELIGRO!: Tu salud es muy baja para esta zona")
    if Nivel== 99:
        print("¡INCREIBLE!: Eres un jugador de nivel maximo")

if(Nivel >=15 and Numero_de_vidas <50) or "Tiene: Llave_Magica"==("s"):
    print("¡Las llaves del castillo se abren!")
else:
    print ("El guardia te prohibe el paso. Vuelve cuando seas mas fuerte")
           
