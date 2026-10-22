#Notas de la universidad

Alumno = int(input("Ingresa un numero del 1 al 100: "))

#Una forma de escribir
if Alumno >= 90:
    print("Excelente, tu nota es un A")
elif Alumno >=80:
    print("Muy bien, tu nota es una B")

#Otra forma de escribir
elif Alumno == 70 or Alumno > 70:
    print("Bien, tu nota es una C")
elif Alumno == 60 or Alumno > 60:
    print("Aprobado rasando, tu nota es una D")
else:
    print("Has reprobado, tu nota es una F")