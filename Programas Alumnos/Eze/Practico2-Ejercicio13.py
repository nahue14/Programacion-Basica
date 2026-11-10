#Calculadora de tarifas

Kilometraje = int (input("Ingresa el kilometraje del viaje a realizar: "))

if Kilometraje <= 300:
    Monto_a_cobrar = 500
else:
    Excedente = Kilometraje - 300
    if Kilometraje <= 1000:
        Monto_a_cobrar = 500 + (Excedente * 3)
    else:
        Monto_a_cobrar = 500 + (1.5 * Excedente)

print ("El monto a cobrar es de $ {}".format(Monto_a_cobrar))
print ("Gracias por utilizar la calculadora de tarifas. ¡Buen viaje!")
