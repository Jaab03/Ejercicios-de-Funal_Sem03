password = "hola123"
intentos = 3

while intentos > 0:
    contra = input(f"Intento {intentos}: Ingresar contraseña: ")
    if contra == password:
        print("Acceso concebido.\n")
        break
  
    else: 
        print("Contraseña incorrecta.\n")
        intentos -= 1
else:
    print("Sistema bloqueada.")
    


