#Conversor de monedas avanzado

Dolar_euro = 0.91
Libra_euro = 1.18

Pregunta1=input("¿Qué desea hacer? A) Convertir de Dólares a Euros B) Convertir de Libras a Euros C) Convertir de Euros a Dólares D) Convertir de Euros a Libras : ")

if Pregunta1 == "A":
    Dolar = float(input("Ingrese la cantidad de Dólares a convertir: "))
    Euro = Dolar * Dolar_euro
    print("{} Dólares son {} Euros".format(Dolar, Euro))

if Pregunta1 == "B":
    Libra = float(input("Ingrese la cantidad de Libras a convertir: "))
    Euro = Libra * Libra_euro
    print("{} Libras son {} Euros".format(Libra, Euro))

if Pregunta1 == "C":
    Euro = float(input("Ingrese la cantidad de Euros a convertir: "))
    Dolar = Euro / Dolar_euro
    print("{} Euros son {} Dólares".format(Euro, Dolar))

if Pregunta1 == "D":
    Euro = float(input("Ingrese la cantidad de Euros a convertir: "))
    Libra = Euro / Libra_euro
    print("{} Euros son {} Libras".format(Euro, Libra))
    
    else:
    print("Opción no válida. Por favor, seleccione A, B, C o D.")
