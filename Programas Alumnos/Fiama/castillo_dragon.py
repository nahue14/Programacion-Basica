"""Vas a programar el sistema de seguridad para entrar al "Castillo del Dragón" en un 
videojuego.
Solicita al usuario que ingrese tres datos: Su nivel (número entero), sus puntos de vida
(número entero) y si tiene la vida llave mágica secreta (S/N).
Programa los siguientes avisos en pantalla usando los condicionales if independientes
(se deben leer siempre, pase lo que pase):
Si la vida del jugador es menor de 20, imprime: "Peligro! Tú salud es muy baja para esta zona"
Si el nivel del jugador es exactamente 99, imprime: "¡Increíble! Eres un jugador de 
nivel máximo"
Ahora programa la decisión del guardia del castillo usando un bloque if/else y paréntesis:
EL jugador sólo puede entrar a pelear si tiene nivel 15 o más y su vida es mayor a 50, o 
tiene la llave mágica, sin importar su nivel ni su vida.
Si cumple la regla, imprime "¡Las puertas del castillo se abren!"
Si no la cumple, imprime "El guardia te prohíbe el paso. Vuelve cuando seas más fuerte"."""

print("-_-_-__ EL CASTILLO DEL DRAGÓN __-_-_-")

nivel = int(input("Ingrese su nivel: "))
vida = int(input("Ingrese su porcentaje de vida (0-100): "))
llave_magica = input("¿Tiene la llave mágica? (S/N): ")

if vida < 20:
    print("¡Peligro! Tú salud es muy baja para esta zona")
    #Agregar línea de pocion para poder pasar a la siguiente pantalla
    pocion_mana = input("Tienes poción de Maná: (S/N)") 
    if pocion_mana == ("S"):
        vida = vida + 20
        print("¡Nivel de vida incrementado! Subes 20 puntos")
        print("Tú nivel de vida es: ", vida)


if nivel == 99:
    print("¡Increíble! Eres un jugador de nivel máximo")

#Decisión del guardia
if (nivel >= 15 and vida > 50) or llave_magica == "S":
    print("¡Las puertas del castillo se abren!")
else:
    print("El guardia te prohíbe el paso. Vuelve cuando seas más fuerte")