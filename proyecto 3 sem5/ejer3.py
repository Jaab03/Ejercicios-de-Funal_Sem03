n = int(input("Ingresar números: "))

suma = 0

print("lista de números:")
for i in range(1,n+1):
    print(i)
    
    if i%2==0:
    
        suma += i
print(f"\nSuma de pares: {suma}")
    

