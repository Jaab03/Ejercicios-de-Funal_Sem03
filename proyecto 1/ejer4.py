import math

num = float(input("ingrese un numero decimal: "))

r2 = math.sqrt(num)
redo = round(num) #(num,2)
r3 = math.pow(num,3) #num**3
rcu = num**(1/3)

print("\nRaíz cuadrada: ", r2)
print("Redondeado a entero: ", redo)
print("Al cubo: ", r3)
print("Raíz cubica: ", rcu)