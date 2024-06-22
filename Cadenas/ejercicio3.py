fecha = input("ingrese la fecha de nacimiento [dd/mm/año]")
dato = fecha.split("/")

if len(dato[0])<=2 and len(dato[1])<=2 and len(dato[2]) == 4:

    if dato[0].isdigit() == True and dato[1].isdigit() == True and dato[2].isdigit() == True: 
        print(f"El dia es {dato[0]}, el mes es {dato[1]} y el año es {dato[2]}")
    else:
        print("FORMATO INVALIDO")
else:
    print("FORMATO INVALIDO")