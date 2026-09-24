while True:
    try:

        num = int(input("Ingrese número: "))
        while num <= 0 or num > 12:
            num = int(input("Error. Ingrese el número de la tabla (1-12): "))

        i = 1

        while i <= 12:
            print(f"{num} x {i} = {num * i}")
            i += 1
        break
    except ValueError:
        print("Solo se permite números enteros")
  