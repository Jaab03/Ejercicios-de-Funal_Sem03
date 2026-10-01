opc = "n"

while opc != "s":

    i= 1
    suma = 0
    num = int(input("Ingresar número: "))
    
    while i <= num:
        suma += i
        i += 1
    print(f"La suma de {num} es {suma}")

    opc = input("\nDesea salir? (presiones s): ")
    if opc == "s":
        break
print()
