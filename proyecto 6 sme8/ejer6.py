
def suma(num1,num2):

    respuesta = num1 + num2

    return respuesta

def resta(num1,num2):

    respuesta = num1 - num2

    return respuesta

def multiplicacion(num1,num2):

    respuesta = num1 * num2

    return respuesta

def division(num1,num2):

    respuesta = num1 / num2

    return respuesta

def menu():

    print("Bienvenidas al sistema de calculadora basica")
    print("1. suma")
    print("2. resta")
    print("3. multiplicar")
    print("4. dividir")

while True:

    menu()
    opcion = int(input("ingresa una opcion: "))

    if opcion > 0 and opcion < 5:
        num1 = float(input("\nIngresar primer número: "))
        num2 = float(input("Ingresar segundo número: "))
        print()

    match opcion:
        case 1:

            print(f"la suma es {suma(num1,num2)}")
        case 2:

            print(f"la resta es {resta(num1,num2)}")
        case 3:

            print(f"la multiplicacion es {multiplicacion(num1,num2)}")
        case 4:

            if num1 == 0 or num2 == 0:
                print("no puedes dividir entre 0")
            else: 
                print(f"la divison es {division(num1,num2)}")
        case _:
            print("invalido")
            exit

    continuar = input("\n¿deseas continuar?(presiona s): ")
    if continuar != "s": break
    print()