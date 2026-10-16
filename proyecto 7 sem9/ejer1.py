from email.mime import base

from cuadrado import cuadrado
from rectangulo import rectangulo
from triangulo import triangulo
from trapecio import trapecio

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

            print("\nRectangulo")
            print("Área: ", r.area())
            print("perimetro: ", r.perimetro())

        case 3:
            
            t = triangulo()

            print("\nTriángulo")
            print("Área: ", t.area())
            print("perimetro", t.perimetro())

        case 4:


            while True:

                try:

                    base = float(input("\nIngresa la base del trapecio: "))
                    base_superior = float(input("Ingresa la base superior del trapecio: "))
                    altura = float(input("Ingresa la altura del trapecio: "))
                    lado = float(input("Ingresa el lado del trapecio: "))

                    if base > 0 and base_superior > 0 and altura > 0 and lado > 0:


                        break
                    else:
                        print("Ingresa número positivo")
                
                except ValueError:
                    
                    print("invalido")

            tra = trapecio()
            
            print("\nTrapecio")
            print("Área", tra.area(base, base_superior, altura))
            print("perimetro",tra.perimetro(base, base_superior, lado))

    while True:

        continuar = (input("\n¿Deseas continuar? (si, no): ")).lower().strip()
        if continuar in("si","no"):
            break
        else: 
            print("Invalido, ingrese solo (si o no)")

    if continuar == "no":
        break
    print()