#Simulador de tienda online

print("Bienvenido a la tienda online de productos electrónicos")
Iphone = int(input("Ingresa el precio del Iphone 13 pro: "))
Cantidad_Iphone = int(input("Ingresa la cantidad de Iphone 13 pro que deseas comprar: "))
Costo_total = Iphone * Cantidad_Iphone
print("El costo total de tu compra es: {}".format(Costo_total))

#Envio gratis
if Costo_total >= 15000:
    print(True)
else:
    print(False)
    
