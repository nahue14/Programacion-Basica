#Tenemos nuestra caja de herramientas especial para el azar
import random

print("Agitando los dados...")
print("Tirando sobre la mesa...")

#Usamos la herramienta randint() de la librería random
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6) 
print("¡Salieron el {} y el {}!".format(dado1,dado2))
