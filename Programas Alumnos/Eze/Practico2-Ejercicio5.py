#El test de la personalidad

print("---¡BIENVENIDO!---")

Puntuacion = 0
A = 10
B = 5
C = 0

#Pregunta1

Pregunta1 = input("Que clase de persona te consideras? OPCION A - Sos alegre | OPCION B - Sos apatico | OPCION C - Detesto a la gente: ")
if Pregunta1 == "A":
    Puntuacion = Puntuacion + A
elif Pregunta1 == "B":
    Puntuacion = Puntuacion + B
elif Pregunta1 == "C":
    Puntuacion = Puntuacion + C
else:
    print("Las opciones posibles son A, B o C")
    exit()

Pregunta2 = input("Como sos en una reuinion social? OPCION A - Hablas con todos | OPCION B - Te mantenes al margen | OPCION C - Depende del dia: ")
if Pregunta1 == "A":
    Puntuacion = Puntuacion + A
elif Pregunta1 == "B":
    Puntuacion = Puntuacion + B
elif Pregunta1 == "C":
    Puntuacion = Puntuacion + C
else:
    print("Las opciones posibles son A, B o C")
    exit()

Pregunta3 = input("Como actuas en una discusion? OPCION A - Defendes tu postura | OPCION B - Evitas el conflicto | OPCION C - Buscas un acuerdo: ")
if Pregunta1 == "A":
    Puntuacion = Puntuacion + A
elif Pregunta1 == "B":
    Puntuacion = Puntuacion + B
elif Pregunta1 == "C":
    Puntuacion = Puntuacion + C
else:
    print("Las opciones posibles son A, B o C")
    exit()

print("Puntuacion total: {} puntos".format(Puntuacion))



