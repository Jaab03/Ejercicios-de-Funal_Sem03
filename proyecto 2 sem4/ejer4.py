print("Bienenidos al sistema de conversion de dinero")
print("______Convertir de soles a dolar o euro______")
print("______________Menu de opciones_______________")
print("             1. Dolar                        ")
print("             2. Euro                         ")
print("_____________________________________________")

opc = int(input("Escoja una opcion: "))
if opc >= 1 and opc <= 2:
    if opc == 1:
        print("Convertir a dolar")
    if opc == 2:
        print("Convertir a euro")
    cantidad = float(input("\nIngrese la cantidad que quiera cambiar: "))
    
match opc:
    case 1:
        convertir = cantidad / 3.4
        convertir = round(convertir, 2)
        print("El cambio es de",convertir)
    case 2:
        convertir = cantidad / 4
        convertir = round(convertir, 2)
        print("El cambio es de",convertir)
    case _:
        print("Invalido")