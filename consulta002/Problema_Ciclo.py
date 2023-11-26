bandera = bool(True)
cadena = ""
while bandera:
    invitados = str(input("Ingrese el nombre completo de un invitado\n"))
    cadena = str(cadena + invitados + "\n")
    opcion = str(input("Ya no desea ingresar mas invitados? pulse ¨n¨\n"))
    if opcion == "n":
        bandera = False
print(f"Lista de invitados\n{cadena}")
