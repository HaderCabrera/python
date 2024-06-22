while True:
    try: 
        num1 = int(input("Ingrese un numero"))
        break
    except ValueError:
        print("Error.numero no valido")

    try: 
        num2 = int(input("Ingrese un numero"))
        break
    except ValueError:
        print("Error.numero no valido")

try:
    suma = num1 + num2
    print("la suma es", suma)
except Exception as e:
    print("Error al intentar sumar.\n",e)
     



