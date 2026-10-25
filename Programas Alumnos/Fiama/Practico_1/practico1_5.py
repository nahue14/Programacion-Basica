"""Ejercicio 5: Simulador de Tienda Online (Envío Gratis)
Este ejercicio simula el carrito de compras de cualquier sitio web.Consigna:
1. Solicita al usuario que ingrese el precio de un producto usando input() y conviértelo a número entero.
2. Solicita la cantidad de unidades que va a comprar de ese producto.
3. Calcula el costo total multiplicando (*) el precio por la cantidad.
4. Imprime un mensaje en pantalla indicando el total a pagar utilizando la función .format().
5. La tienda ofrece envío gratuito si la compra total es mayor o igual a $15000.
Utiliza un operador de comparación (>=) para evaluar si al usuario le corresponde el envío gratis y 
muestra el resultado en pantalla (True o False)."""

print("SITIO WEB \n")

precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("\n ¿Qué cantidad de unidades desea comprar? "))

total = precio * cantidad

print("\n El total a pagar es ${}".format(total))

if total >= 15000:
    print("\nComo su compra supera los $15000, el envío es gratis\n")
elif total < 15000:
    print("Como su compra no supera los $15000, debe abonar el envío")