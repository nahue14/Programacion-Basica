print("---SISTEMA DE SEGURIDAD SECRETO---")

#1.Pedimos la contraseña por primera vez
password = input("Ingresa la contraseña para entrar: ")

#2. El guardia 'while' revisa si esta MAL.
#MIENTRAS sea distinta (!=) a "python123", te deja atrapado.
while password != "python123":
    print("¡Acceso denegado! Contraseña incorrecta." )

    #LA LLAVE PARA SALIR: Volver a preguntar dentro del bucle
    #Si nos olvidamos esta linea, es un bucle infinito.
    password = input("Vuleve a intentarlo: ")

#3. Si llegamos a esta linea, significa que logro escapar del while
print("¡Acceso concedido! Bienvenido al sistema.")    


 