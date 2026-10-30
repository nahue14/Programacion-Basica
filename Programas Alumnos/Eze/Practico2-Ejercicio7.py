#El Asesor de compras

movil_ideal = "Ninguno"
Usuario = input("Que prefieres? iOs (I) or Android(A): ")
if Usuario == "I":
    Usuario = input("Tienes dinero? (S/N): ")
    if Usuario == "S":
        movil_ideal = "iPhone Ultra Pro Max"
        Usuario = input("Te importa la camara? (S/N): ")
    else:
        movil_ideal = "Te recomiendo un iPhone usado"
if Usuario == "A":
    Usuario = input("Tienes dinero? (S/N): ")
    if Usuario == "S":
        Usuario = input("Te importa la camara? (S/N): ")
        if Usuario == "S":
            movil_ideal = "Te recomiendo un Xiaomi"
        if Usuario == "N":
            movil_ideal = "Te recomiendo un Samsung"
    else:
        movil_ideal = "Te recomiendo TCL"

print("Tu movil ideal es: {}".format(movil_ideal))
