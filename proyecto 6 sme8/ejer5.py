
num1 = float(input("Ingresar primer número: "))
num2 = float(input("Ingresar segundo número: "))

operacion = input("+,-,*,/: ")

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

if operacion == "+":

    print(f"la suma es {suma(num1,num2)}")
elif operacion == "-":

    print(f"la resta es {resta(num1,num2)}")
elif operacion == "*":
    print(f"la multiplicacion es {multiplicacion(num1,num2)}")
elif operacion == "/":
    if num1 == 0 or num2 == 0:
        print("no puedes dividir entre 0")
    else: 
        print(f"la divison es {division(num1,num2)}")



