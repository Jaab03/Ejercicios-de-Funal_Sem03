print("______________Menu de opciones_______________")
print("             1. Cuadrado                     ")
print("             2. Rectángul                    ")
print("             3. Triángulo                    ")
print("             4. Círculo                      ")
print("_____________________________________________")

opc = int(input("\nIngrese una opvion: "))

match opc:
    case 1:
        l = int(input("Ingrese lado del cuadrado: "))
        ac = l*l
        print(f"\nEl área del cuadrado es: {ac}")
    case 2:
        b = int(input("\nIngrese la base del rectángulo: "))
        h = int(input("\nIngrese la aultura del rectángulo: "))
        ar = b*h
        print(f"\nEl área del rectángulo es: {ar}")
    case 3:
        b = int(input("\nIngrese la base del triángulo: "))
        h = int(input("\nIngrese la aultura del triángulo: "))
        ar = (b*h)/2
        print(f"\nEl área del triángulo es: {ar}")
    case 4:
        import math
        r = int(input("Ingrese el radio del circulo: "))
        ac = math.pi * (r**2)
        print(f"\nEl área del circulo es: {ac}")
    case _: print("\nOpcion invalida")