import random

num = random.randint(1,20)

for i in range(1,4):
    respuesta = int(input(f"Intento {i}: "))

    if respuesta == num:
        print("\nganaste\n")
        break
    else:
        print("\nfallaste")
        if respuesta < num:
            print("el número es mayor\n")
        else: print("el número es menor\n")
else:
    print(f"perdiste, el número era {num}")