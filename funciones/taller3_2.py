def menu():
    while True:
        try:
            print("=============+ MENU +================")
            print("1. Calcular combinatoria")
            print("2. Convertir texto a solo numero")
            print("3. Calcular IVA de una factura")
            print("4. Salir")
            print("=====================================")
            op = int(input("Opción [1-4]? >>>  "))
            if op < 1 or op > 5:
                print("     Opción no válida. Escoja de 1 a 4.")
                continue
            return op
        except ValueError:
            print("     Opción no válida. Escoja de 1 a 4.")
            input("Presione cualquier tecla para continuar...")

def ingNum(smj):
    while True:
        try:
            num = int(input(smj))
            if num < 0:
                print("     Error. Número negativo")
                continue
            return num
        except ValueError:
            print("     Error. Número inválido")

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        multiplo = i
        factorial = factorial * multiplo
    return factorial

def calCombinatoria():
    n = ingNum("    Number of items to choose from:  ")
    k = ingNum("    Number of items to be chosen:  ")
    if n >= k:
        #combinatoria = (factorial(n)) / ((factorial(k)) * factorial((n - k)) * factorial(n)) NO CALCULA DE FORMA CORRECTA CON ESTA ECUACION
        combinatoria = (factorial(n)) / (factorial((n - k)) * factorial(k))
        result = print(f"       The result of C({n},{k}) = {combinatoria:,.0f}")
        return result
    else:
        result = print("    N cannot be greater than k...")
        return result
    
def cutString(smj):
    newCadena = ""
    cadena = input(smj)
    cadena = cadena.strip()
    for i in cadena:
        if i.isdigit() == True:
            newCadena = newCadena + i
    return newCadena

def calFactura(sinDesc, IVA):
    valor = (1 + IVA / 100) * sinDesc
    return valor

while True:
    opcion = menu()
    if opcion == 1:
        comb = calCombinatoria()
        input("Press any key to continue...")
    elif opcion == 4:
        break
    elif opcion == 2:
        cadena = cutString("Ingrese cadena: ")
        print(f"    La nueva cadena es: {cadena}")
        input("Press any key to continue...")
    elif opcion == 3:
        while True:
            try:
                valorProduct = float(input("Ingrese valor del producto: "))
                if valorProduct <= 0:
                    print("     Ingrese un número mayor a 0.")
                    continue
                break
            except ValueError:
                print("     Número invalido. Ingrese número correcto...")
        porcentDescuento = ingNum("Ingrese porcentaje del IVA: ")
        valFactura = calFactura(valorProduct , porcentDescuento)
        print(f"    El valor del producto aplicando un IVA del {porcentDescuento}% es: ${valFactura:,.0f} COP")
        input("Press any key to continue...")