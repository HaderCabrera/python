while True:
    try:
        
        name = input("Ingrese el nombre de la persona")
        name = name.strip()
        if len(name) == 0 or name.isalnum() == False:
            print("NOmbre invalido. Vueñlva a digitar")
            continue
        break
    except Exception as e:
        print(f"Error al ingresar el nombre: {e}")
while True:
    try:
        estrato = int(input("INgrese el estrato [1-5]"))
        if estrato < 1 or estrato > 5:
            print("Rango incorrecto")
            continue
        break
    except ValueError:
        print("Error.Estrato invalido")

