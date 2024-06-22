#CALCULADORA
def sumna(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1,num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        resultado = num1 / num2
    except  Exception as e:
        resultado = None
    return resultado
    
def menu():
    while True:
        try:
            print("*** MENU CALCULADORA ***")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Divifir")
            print("5. Salir")
            op = int(input(">>> OPcion (1-5)? "))
            if op < 1 or op > 5:
                print("Opcion no valida. Esoja del 1 al 5.")
                continue
            return op
        except ValueError:
            print("Error. Opcion no valida.")
            input("Presione cualquier tecla para continuar")

def leerNum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error. Número invalido")
            input("Presione cualquier tecla para continuar...")



##PROGRAMA PRINCIPAL

while True:
    opcion = menu()
    num1 = leerNum("INgrese el primer numero: ")
    num2 = leerNum("INgrese el segundo numero: ")
    if opcion == 1:
        print("1.Sumar")
        print(f"EL resultado de la suma es: {sumna(num1, num2):.3f}")
    elif opcion == 2:
        print("2.Resta")
        print(f"EL resultado de la resta es: {resta(num1, num2):.3f}")
    elif opcion == 3:
        print("3.Multiplicar")
        print(f"EL resultado de la multiplicacion es: {multiplicacion(num1, num2):.3f}")
    elif opcion == 4:
        print("4.Dividir")
        res = division(num1, num2)
        if res != None:
            print(f"EL resultado de la division es: {res:.3f}")
        else:
            print("Division entre CERO inditerminada")
    elif opcion == 5:
        print("\n\nGracias por usar la calculadora")
        print("Adios")
        input()
        break
    input("Presione cualquier tecla para volver al MENU...")





