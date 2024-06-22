
bandera2 = True
while bandera2 == True: 

    nombre = input("\nINgrese el nombre del usuario")
    estrato = int(input("Ingrese el estrato del usuario[1-5]"))
    
    if estrato == 1:
        tarifaBasica = 10000
        print("\n","="*20)
        print(f"{nombre} debe pagar {tarifaBasica}")
    elif estrato == 2:
        tarifaBasica = 15000
        print("\n","="*20)
        print(f"{nombre} debe pagar {tarifaBasica}")
    elif estrato == 3:
        tarifaBasica = 30000
        print("\n","="*20)
        print(f"{nombre} debe pagar {tarifaBasica}")
    elif estrato == 4:
        tarifaBasica = 50000
        print("\n","="*20)
        print(f"{nombre} debe pagar {tarifaBasica}")
    elif estrato == 5:
        tarifaBasica = 65000
        print("\n","="*20)
        print(f"{nombre} debe pagar {tarifaBasica}")

    bandera = input("Desea continuar? ")

    if bandera == "SI" or bandera == "si":
        bandera2 = True
    else:
        bandera2 = False


