año = int(input("Ingrese el año: "))

print()
if (año % 4 == 0 and año % 10 != 0) or año % 400 == 0:
    print("El año es bisiesto")
else: 
    print("El año no es bisiesto")

if año % 2 == 0: print("El año es par")
else: print("El año es impar")
print()