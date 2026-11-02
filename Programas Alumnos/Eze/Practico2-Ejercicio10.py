#Evaluacion de credito

Nombre = input("Ingrese su nombre: ")
Sueldo = int(input("Ingrese su sueldo: "))
Antiguedad = int(input("Ingrese su antiguedad en años: "))
if Sueldo > 15000 and Antiguedad >= 10:
    print("Felicidades {}, su crédito ha sido concedido".format(Nombre))
    else:   
        print("Lo sentimos {}, su crédito no ha sido rechazado".format(Nombre))
        
