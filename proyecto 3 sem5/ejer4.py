n = int(input("Ingresar números: "))

par = impar = ceros = 0
print()

for i in range(1,n+1):
    num = int(input(f"Ingrese número {i}: "))
    
    if num ==0:
        ceros += 1
    elif num %2 == 0:
        par += 1
    else: impar +=1
print(f"\nCantidad de pares: {par}")
print(f"\nCantidad de impares: {impar}")
print(f"\nCantidad de ceros: {ceros}")

    