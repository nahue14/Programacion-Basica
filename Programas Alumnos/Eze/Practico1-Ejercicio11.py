#El validador de descuentos (Uso del else)

print("Bienvenido")
Edad = int(input("Ingresa tu edad: "))
Carnet = input("Ingresa tu tipo de carnet (E, P, F, N): ")
E = "Estudiante"
P = "Pensionista"
F = "Familia numerosa"
N = "Nada"

if Carnet == "E" and 25 <= Edad <= 35:
    print("Se te aplica descuento por estudiante")
elif Edad <=10:
    print("Se te aplica descuento por edad")
elif Edad >= 65 and Carnet == P:
    print("Se te aplica descuento por pensionista")
elif Carnet == F:
    print("Se te aplica descuento")
else:
    print("No se te aplica descuento")
    


