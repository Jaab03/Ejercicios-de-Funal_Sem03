dolar = 3.78
euro = 4.2
soles = 0

def dolares()->float:

    return soles/dolar

def euros()->float:

    return soles/euro

print("BIENVENIDO A LA CASA DE CAMBIO EN DOLARES Y EUROS")

while True:

    soles = float(input("\nIngrese la cantidad en soles: "))

    print(f"Monto en dolares {dolares():.2f}")
    print("Monto en euros ",round(euros(),2))

    continuar = input("\n¿deseas continuar?(presiona s): ")
    if continuar != "s": break