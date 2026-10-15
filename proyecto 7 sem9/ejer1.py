from wsgiref import validate
from cuadrado import cuadrado
from rectangulo import rectangulo

c = cuadrado()

def menu():
    print("BIENVENIDO AL SISTEMA DE CÁLCULO DE ÁREAS Y PERIMETROS\n")
    print("************ Menu de opciones *************")
    print("* 1. Cuadrado                             *")
    print("* 2. Rectángulo                           *")
    print("* 3. Triángulo                            *")
    print("* 4. Trapecio                             *")
    print("* 0. Salir                                *")
    print("*******************************************")
menu()

while True:

    while True:

        try:
            opc = int(input("Ingrese una opcion: "))
        except ValueError:
            opc = -1
        if 0 <= opc <= 4:
            break
        print("Opción invalida, ingresa un número entre 0 y 4\n")
            
    match opc:

        case 0: exit()

        case 1: 

            while True:
            
                try: 
                    l = float(input("\nIngrese el lado del cuadrado: "))
                    
                    if l > 0:
                        break
                    else:
                        print("Error. Ingrese un número positivo")

                except ValueError:
                    print("Error. Ingrese solo números")
            print("\nCuadrado")
            c.area(l)
            c.perimetro(l)

        case 2:
            r = rectangulo()

            print("\nArea: ", r.area())
            print("perimetro: ", r.perimetro())

        
    while True:

        continuar = (input("\n¿Deseas continuar? (si, no): ")).lower().strip()
        if continuar in("si","no"):
            break
        else: 
            print("Invalido, ingrese solo (si o no)")

    if continuar == "no":
        break